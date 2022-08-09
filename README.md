# gemini.word-ac.net


contents of gemini.word-ac.net

`contents/`以下に掲載するファイルを入れてください

## Dependencies

- python3 <= 3.6
- [python3-toml](https://github.com/uiri/toml)

## Install

### cred ファイルの作成

まず、cred を以下のように作成します。

適宜、GitHub で生成した Personal Access Token と自分の userid を入力します。
また、この作業は 1 回のみ行えば大丈夫です。

例:
```shell
export GITHUB_TOKEN=hogehoge
export GITHUB_USER=eniehack
```

``` sh
sudo chmod 700 cred
```

### 定期実行環境の作成

下のsectionのうち1つを実行してください。

#### cron jobの作成

Debianでは`/etc/cron.d/`以下にファイルを作成し、下のように書き込み、保存してください。

```cron
0 * * * * gmid cd {{Git repo directory}} && ./scripts/cron.sh
```

#### systemd-timer unitの作成

(2022-08-09現在、systemd-timerを使って動かしていないので、動作は未確認です)

これをsystemdが認識する場所に置き、`gemini-word-ac-net.service`などと保存する:
```conf
[Service]
Description=generates gemtext from WORDPress' contents
After=network.target

[Unit]
Type=oneshot
User=gmid
Group=gmid
ExecStart=./scripts/cron.sh
WorkingDirectory={{Git repo directory}}

[Install]
WantedBy=multi-user.target
```

次に、これをsystemd-timerが認識する場所に置き、`gemini-word-ac-net.timer`などと保存する:
```conf
[Service]
Description=gemini.word-ac.net periodic executor

[Timer]
OnCalendar=hourly
Persistent=true

[Install]
WantedBy=timers.target
```
