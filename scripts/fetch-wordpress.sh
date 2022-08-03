#!/usr/bin/env bash

set -eu

. cred

curl -sSL -u "$GITHUB_USER:$GITHUB_TOKEN" \
    -o "latest-http.tar.gz" \
    "https://github.com/WORD-COINS/word-press/archive/refs/heads/master.tar.gz"

sha512sum "latest-http.tar.gz" > latest

diff current latest
if [ $? -eq 0 ]; then
    rm latest
    rm latest-http.tar.gz
else
    mv -f latest current
    rm -r word-press-master
    tar -xzf latest-http.tar.gz
    mv -f latest-http.tar.gz current-http.tar.gz
fi
