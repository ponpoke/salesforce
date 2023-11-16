## 概要
Salesforceの接続アプリケーションを使用したJWT認証をPythonで行う

## スクリプト概要
### jks
Salesforce組織の[証明書と鍵の管理]画面より作成した自己署名証明書および、対応する非公開鍵をキーストアからエクスポートした
 jksファイルを使用してJWTを生成する

- 使用手順

jksディレクトリに移動
```
cd jks
```
.envファイルを編集
```
CONSUMER_ID="接続アプリケーションから取得したコンシューマID"
USERNAME="実行する Salesforce ユーザ名"
PRIVATE_KEY_PATH="jksファイルのパス"
KEY_STORE_PASSWORD ="jksに設定したパスワード"
KEY_ALIAS="jksのエイリアス名"
```

スクリプトを実行
```
python main.py
```

### pem
OpenSSLコマンドなどSalesforce組織外で作成したpemを使用してJWTを生成する

- 使用手順

pemディレクトリに移動
```
cd pem
```
.envファイルを編集
```
CONSUMER_ID="接続アプリケーションから取得したコンシューマID"
USERNAME="実行する Salesforce ユーザ名"
PRIVATE_KEY_PATH="jksファイルのパス"
```

スクリプトを実行
```
python main.py
```

