## 概要
Salesforce 組織のキーストアからエクスポートとり取得した jks ファイルを pem に変換する

- 使用手順

.envファイルを編集
```
PRIVATE_KEY_PATH="jksファイルのパス"
KEY_STORE_PASSWORD ="jksに設定したパスワード"
KEY_ALIAS="jksのエイリアス名"
```

スクリプトを実行
```
python jks_to_pem.py
```
