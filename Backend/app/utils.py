import boto3
import os
from config import Config
from web3 import Web3

# Amazon S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY
)

# Initialize Web3 instance
w3 = Web3(Web3.HTTPProvider(Config.POLYGON_RPC_URL))

# Load the ABI and bytecode for the SoulboundToken contract
soulbound_token_abi = None  # Replace None with the ABI JSON for SoulboundToken
soulbound_token_bytecode = None  # Replace None with the bytecode for SoulboundToken

def upload_to_s3(image_file, image_filename):
    s3.upload_fileobj(
        image_file,
        Config.AWS_S3_BUCKET,
        image_filename,
        ExtraArgs={'ACL': 'public-read', 'ContentType': image_file.content_type}
    )
    image_url = f"https://{Config.AWS_S3_BUCKET}.s3.amazonaws.com/{image_filename}"
    return image_url

def mint_token(did, image_url):
    # Load the SoulboundToken contract
    soulbound_token_contract = w3.eth.contract(
        address=Config.SOULBOUND_TOKEN_ADDRESS,
        abi=soulbound_token_abi
    )

    # Build the transaction for minting the token
    transaction = soulbound_token_contract.functions.mint(did, image_url).buildTransaction({
        'chainId': Config.POLYGON_CHAIN_ID,
        'gas': 3000000,  # You may need to adjust the gas limit
        'gasPrice': w3.eth.gasPrice,
        'from': Config.DEPLOYER_ADDRESS,
        'nonce': w3.eth.getTransactionCount(Config.DEPLOYER_ADDRESS),
    })

    # Sign the transaction
    signed_transaction = w3.eth.account.signTransaction(
        transaction, Config.DEPLOYER_PRIVATE_KEY
    )

    # Send the signed transaction
    transaction_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

    # Wait for the transaction receipt
    transaction_receipt = w3.eth.waitForTransactionReceipt(transaction_hash)

    # Get the tokenId from the transaction receipt
    token_id = transaction_receipt['logs'][0]['topics'][2]

    return int(token_id, 16)