import requests
import json
from OAuth import generate_oauth_token
from config import consumer_key,consumer_secret

def get_password(shortcode, passkey, timestamp):
    data_to_encode = shortcode + passkey + timestamp
    encoded_string = base64.b64encode(data_to_encode.encode())
    return encoded_string.decode('utf-8')


def generate_dynamic_qr(merchant_name, ref_no, amount, trx_code, cpi, size):
    # API endpoint
    url = "https://sandbox.safaricom.co.ke/mpesa/qrcode/v1/generate"

    # Request payload
    payload = {
        "MerchantName": merchant_name,
        "RefNo": ref_no,
        "Amount": amount,
        "TrxCode": trx_code,
        #"CPI": cpi,
        "Size": size
    }

    # Convert payload to JSON
    json_payload = json.dumps(payload)
    access_token = generate_oauth_token(consumer_key,consumer_secret)
    # Headers
    headers = {
        "Content-Type": "application/json",
        'Authorization': f'Bearer {access_token}'
    }

    try:
        # Make the POST request
        response = requests.post(url, data=json_payload, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            result = response.json()
            return result
        else:
            return f"Error: {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    result = generate_dynamic_qr(
        merchant_name="TEST SUPERMARKET",
        ref_no="Invoice Test",
        amount=1,
        trx_code="BG",
        cpi="373132",
        size="300"
    )
    print(json.dumps(result, indent=2))
