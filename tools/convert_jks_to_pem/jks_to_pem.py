import os
from dotenv import load_dotenv
import base64
import textwrap
import jks

# .env ファイルから環境変数を読み込む
load_dotenv()

# 環境変数から値を取得する
private_key_path = os.getenv("PRIVATE_KEY_PATH") # keyのパスを指定する
keystore_pass = os.getenv("KEY_STORE_PASSWORD")  # jks をに設定したパスワードを設定する
key_alias = os.getenv("KEY_ALIAS")  # jks のエイリアス名を指定する

def print_pem(der_bytes, pem_type):
    print(f"-----BEGIN {pem_type}-----")
    print("\r\n".join(textwrap.wrap(base64.b64encode(der_bytes).decode('ascii'), 64)))
    print(f"-----END {pem_type}-----")

def output_pem(der_bytes, pem_type):
    return "\r\n".join([
        f"-----BEGIN {pem_type}-----",
        "\r\n".join(textwrap.wrap(base64.b64encode(der_bytes).decode('ascii'), 64)),
        f"-----END {pem_type}-----"
    ])

def process_keystore(path_key, keystore_pass, key_alias):
    """
    path_key : jksファイルのpath
    keystore_pass : jksに設定したパスワード 
    key_alias : エイリアス名
    """
    keystore_path = os.path.abspath(path_key)
    keystore = jks.KeyStore.load(keystore_path, keystore_pass)

    # print(print(keystore.private_keys))
    private_key_entry = keystore.private_keys[key_alias]

    print_pem(private_key_entry.pkey_pkcs8, "PRIVATE KEY")
    # return output_pem(private_key_entry.pkey_pkcs8, "PRIVATE KEY")

if __name__ == "__main__":

    process_keystore(private_key_path, keystore_pass, key_alias)