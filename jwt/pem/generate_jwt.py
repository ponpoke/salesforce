import jwt
from datetime import datetime, timedelta
import requests

def generate_jwt_token():
    # ヘッダー
    header = {
        "alg": "RS256",
        "typ": "JWT"
    }

    # ペイロード
    payload = {
        "iss": "consumer id",
        "sub": "username",
        "aud": "https://login.salesforce.com",
        "exp": datetime.now().timestamp() + (3 * 60)  # 3分間
    }

    # 秘密鍵の読み込み
    with open("key/_demo.pem", "r") as f:
        private_key = f.read()

    # JWT生成
    jwt_token = jwt.encode(payload, private_key, algorithm="RS256", headers=header)

    return jwt_token

def get_access_token(jwt_token):
    url = "https://login.salesforce.com/services/oauth2/token"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": jwt_token
    }

    response = requests.post(url, headers=headers, data=payload)

    return response.json()

if __name__ == "__main__":
    # JWTトークン生成
    jwt_token = generate_jwt_token()

    # print(jwt_token)

    # Salesforceアクセストークン取得
    access_token_response = get_access_token(jwt_token)

    print(access_token_response)