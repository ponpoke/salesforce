import os
import base64
import textwrap
import jks

def print_pem(der_bytes, pem_type):
    print(f"-----BEGIN {pem_type}-----")
    print("\r\n".join(textwrap.wrap(base64.b64encode(der_bytes).decode('ascii'), 64)))
    print(f"-----END {pem_type}-----")

# ...
path_key = "./key/ファイル名,jks" # keyのパスを指定する
keystore_pass = "" # jks をに設定したパスワードを設定する
key_alias = '' # エイリアス名を指定する

keystore_path = os.path.abspath("key/00D5j00000BRFre.jks")
keystore = jks.KeyStore.load(keystore_path, keystore_pass)

private_key_entry = keystore.private_keys[key_alias]

print_pem(private_key_entry.pkey_pkcs8, "PRIVATE KEY")
