# README to publish

📖 [Pythonスクリプトってどうやってパブリッシュするんだぜ（＾～＾）？](https://crieit.net/drafts/61a3496b73b42)  

👇 ソースは、 `src` ディレクトリーを作って、その中に入れてほしい  

```plaintext
👉  └── 📂 src
        └── 📂 パッケージ名
            └── 📄 __init__.py
```

👇 pipを更新  

```shell
python -m pip install --upgrade pip
```

👇 以下のファイルを新規作成  

```plaintext
    ├── 📂 src
    │   └── 📂 パッケージ名
    │       └── 📄 __init__.py
👉  ├── 📄 setup.cfg  
👉  └── 📄 setup.py  
```

２回目以降のアップロードでは、バージョン番号を上げてほしい  

（必要ないかもしれないが build をする前に） Git Hub などのリポジトリ―を利用しているなら、コミットしていないファイルがあればコミットしておくといいかもしれない  

👇 （していなければ）buildパッケージをインストール  

```shell
python.exe -m pip install --upgrade build
```

👇 buildを実行  

```shell
python.exe -m build
```

👇 dist ディレクトリーが自動生成される  

```plaintext
    ├── 📂 dist
👉  │       ├── 📄 パッケージ名-バージョン-py3-none-any.whl
👉  │       └── 📄 パッケージ名-バージョン.tar.gz
    ├── 📂 src
    │   └── 📂 パッケージ名
    │       └── 📄 __init__.py
    ├── 📄 setup.cfg  
    └── 📄 setup.py  
```

👇 まず、テスト環境へのアップロードを試します  
PyPi へログインするためのユーザー名とパスワードの入力が求められます  

```shell
python.exe -m twine upload --repository testpypi dist/* --verbose
```

ログインに成功すると、アップロードが行われ、 URL が出てくるのでアクセスしてください  

👇 本番です  

```shell
python.exe -m twine upload dist/*
```

ログインに成功すると、アップロードが行われ、 URL が出てくるのでアクセスしてください  
