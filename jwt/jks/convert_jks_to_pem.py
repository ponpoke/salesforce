import os
import base64
import textwrap
import jks


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

    return output_pem(private_key_entry.pkey_pkcs8, "PRIVATE KEY")
