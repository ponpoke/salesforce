import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta
import requests

from convert_jks_to_pem import process_keystore

# .env ファイルから環境変数を読み込む
load_dotenv()

# 環境変数から値を取得する
consumer_id = os.getenv("CONSUMER_ID")
username = os.getenv("USERNAME")
private_key_path = os.getenv("PRIVATE_KEY_PATH")  # 秘密鍵のパス
keystore_pass = os.getenv("KEY_STORE_PASSWORD")  # KeyStoreのパスワード
key_alias = os.getenv("KEY_ALIAS")  # KeyStoreのエイリアス名

def generate_jwt_token():
    # JWTヘッダー
    header = {"alg": "RS256", "typ": "JWT"}

    # JWTペイロード
    payload = {
        "iss": consumer_id,
        "sub": username,
        "aud": "https://login.salesforce.com",
        "exp": datetime.now().timestamp() + (3 * 60)  # 3分間
    }

    # 秘密鍵の読み込み
    private_key = process_keystore(private_key_path, keystore_pass, key_alias)

    # JWT生成
    jwt_token = jwt.encode(payload, private_key, algorithm="RS256", headers=header)

    return jwt_token

def get_access_token(jwt_token):
    url = "https://login.salesforce.com/services/oauth2/token"
    
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    payload = {
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": jwt_token
    }

    response = requests.post(url, headers=headers, data=payload)

    return response.json()

if __name__ == "__main__":
    # JWTトークン生成
    jwt_token = generate_jwt_token()

    # Salesforceアクセストークン取得
    access_token_response = get_access_token(jwt_token)

    print(access_token_response)