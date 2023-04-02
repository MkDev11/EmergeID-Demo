from flask import Flask, jsonify, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import User, db
from utils import upload_to_s3, mint_token
from pydid import DID
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
load_dotenv()



app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return redirect('/authorize')

@app.route('/register', methods=['POST'])
def register():
    idme_id = request.form.get('idme_id')
    did = request.form.get('did')
    image_file = request.files.get('image')

    if not idme_id or not did or not image_file:
        return jsonify({'error': 'Invalid input'}), 400

    image_filename = f"{idme_id}-{image_file.filename}"
    image_url = upload_to_s3(image_file, image_filename)

    user = User(idme_id=idme_id, did=did, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered', 'user_id': user.id})

@app.route('/authorize')
def idme_authorize():
    query_params = {
        'client_id': Config.IDME_CLIENT_ID,
        'redirect_uri': Config.IDME_REDIRECT_URI,
        'response_type': 'code',
        'scope': 'openid'
    }
    url = f"{Config.IDME_AUTH_URL}?{urlencode(query_params)}"
    return redirect(url)

@app.route('/callback')
def idme_callback():
    code = request.args.get('code')
    if not code:
        return jsonify({'error': 'Authorization code missing'}), 400

    token_data = idme_exchange_code(code)
    access_token = token_data['access_token']

    user_info = idme_get_userinfo(access_token)
    idme_id = user_info['id']

    # Generate a DID for the user
    did = DID().to_string()

    # Render the registration form with the Id.me ID and DID
    return render_template('register.html', idme_id=idme_id, did=did)

def idme_exchange_code(code):
    data = {
        'code': code,
        'client_id': Config.IDME_CLIENT_ID,
        'client_secret': Config.IDME_CLIENT_SECRET,
        'redirect_uri': Config.IDME_REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    response = requests.post(Config.IDME_TOKEN_URL, data=data)
    if response.status_code != 200:
        raise ValueError('Error exchanging authorization code for access token')

    return response.json()

def idme_get_userinfo(access_token):
    headers = {'Authorization': f"Bearer {access_token}"}
    response = requests.get(Config.IDME_USERINFO_URL, headers=headers)
    if response.status_code != 200:
        raise ValueError('Error retrieving user information')
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
