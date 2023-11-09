import os
import base64
import textwrap
import jks

def print_pem(der_bytes, type):
    print("-----BEGIN %s-----" % type)
    print("\r\n".join(textwrap.wrap(base64.b64encode(der_bytes).decode('ascii'), 64)))
    print("-----END %s-----" % type)

# ...

keystorePath = os.path.abspath("key/00D5j00000BRFre.jks")
keystorePass = "test12345"
keystore = jks.KeyStore.load(keystorePath, keystorePass)

keyAlias = 'case45664050'
private_key_entry = keystore.private_keys[keyAlias]
#private_key_bytes = private_key_entry.pkey
#encoded_data = base64.b64encode(private_key_bytes)

print_pem(private_key_entry.pkey_pkcs8, "PRIVATE KEY")

#print(pem)