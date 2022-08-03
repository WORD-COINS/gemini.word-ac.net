#!/usr/bin/env bash

set -eu

cat ./scripts/backnumber/header.tpl.gmi
printf "\n"
ls ./word-press-master/data/backnumber/**/*.toml | ./scripts/backnumber/make_link_line.py | sort -nk3 -r
printf "\n"
cat ./scripts/backnumber/footer.tpl.gmi
printf "\n"
echo "最終更新日時: $(date)"
printf "\n"
