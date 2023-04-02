import os

class Config:
    # App Config
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')

    #Polygon config
    POLYGON_RPC_URL = os.environ.get('POLYGON_RPC_URL')


    # Database Config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///emergeid.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AWS Config
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_BUCKET = os.environ.get('AWS_S3_BUCKET')

    # Id.me Config
    IDME_CLIENT_ID = os.environ.get('IDME_CLIENT_ID', '89f30556d12ce873ac781af85cd86ed2')
    IDME_CLIENT_SECRET = os.environ.get('IDME_CLIENT_SECRET', '49b8c3d33ec6bb548059e1a3772ddfd2')
    IDME_REDIRECT_URI = os.environ.get('IDME_REDIRECT_URI', 'https://emergeid.org/')
    IDME_AUTH_URL = 'https://api.id.me/oauth/authorize'
    IDME_TOKEN_URL = 'https://api.id.me/oauth/token'
    IDME_USERINFO_URL = 'https://api.id.me/api/public/v2/attributes.json'