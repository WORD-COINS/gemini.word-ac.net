# gemini.word-ac.net
contents of gemini.word-ac.net

`contents/`以下に掲載するファイルを入れてください

## backnumber ページの作成

依存パッケージ: [toml](https://github.com/uiri/toml)

### cred ファイルの作成

まず、cred を以下のように、作成します。
適宜、GitHub で生成した Personal Access Token と自分の userid を入力します。
この作業は 1 回のみ行えば大丈夫です。
```shell
export GITHUB_TOKEN=hogehoge
export GITHUB_USER=eniehack
```

``` sh
sudo chmod 700 cred
```

## backnumber ページの生成

この README.md のある Directory で、以下のように実行してください

``` sh
./scripts/backnumber.sh > ./contents/backnumber.gmi
```

