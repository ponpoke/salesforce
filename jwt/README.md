## 概要
Salesforce の 接続アプリケーションを使用した JWT 認証を Python で行う

## スクリプト概要
### jks
Salesforce 組織の [証明書と鍵の管理] 画面より作成した自己署名証明書および、対応する非公開鍵をキーストアからエクスポートした
 jks ファイルを使用して JWT を生成する

- 使用手順

jks ディレクトリに移動
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
python generate_jwt.py
```

### pem
OpenSSL コマンドなど Salesforce 組織外で作成した pem を使用して JWT を生成する

- 使用手順

pem ディレクトリに移動
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
python generate_jwt.py
```

