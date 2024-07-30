import requests
import base64

def generate_oauth_token(consumer_key, consumer_secret):
    #Base64 encoding of Consumer Key + ":" + Consumer Secret
    credentials = f"{consumer_key}:{consumer_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    #Create a GET request with the Authorization header
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/json"
    }

    #Send the request to the endpoint
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print("OAuth token generated successfully!")
            token_data = response.json()
            print(f"Access Token: {token_data.get('access_token')}")
            print(f"Expires in: {token_data.get('expires_in')} seconds")
        else:
            print(f"Failed to generate OAuth token. Status code: {response.status_code}")
            print(f"Response: {response.text}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

#consumer keys
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"

# Generate the OAuth token
generate_oauth_token(consumer_key, consumer_secret)
