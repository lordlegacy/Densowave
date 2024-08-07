import requests
import base64
from datetime import datetime
from OAuth import generate_oauth_token
from config import consumer_key,consumer_secret

def get_password(shortcode, passkey, timestamp):
    data_to_encode = shortcode + passkey + timestamp
    encoded_string = base64.b64encode(data_to_encode.encode())
    return encoded_string.decode('utf-8')

def send_stk_push():
    access_token = generate_oauth_token(consumer_key,consumer_secret)
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # Replace these with your actual values
    shortcode = "174379"
    passkey = "Yourpasskey"
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = get_password(shortcode, passkey, timestamp)

    payload = {
        "BusinessShortCode": shortcode,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": "254743532766",
        "PartyB": shortcode,
        "PhoneNumber": "254743532766",
        "CallBackURL": "https://mydomain.com/pat",
        "AccountReference": "Test",
        "TransactionDesc": "Test"
    }
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    response = requests.post(url, json=payload, headers=headers)

    print(response.json())

send_stk_push()
