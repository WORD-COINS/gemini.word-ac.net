#!/usr/bin/env python3
from urllib.parse import urljoin
from collections import namedtuple
from datetime import date, datetime, timezone, timedelta

import glob
import toml

BACKNUMBER_BASE_URL = "https://bitbucket.org/word-coins/backnumber/raw/master/"
toml_file_lst = glob.glob("word-press-master/data/backnumber/**/*.toml")
BACKNUMBER_GMI = "./contents/backnumber.gmi"

backnumbers_array = []
BackNumber = namedtuple("BackNumber", ["url", "published_at", "title"])
for toml_file in toml_file_lst:
    with open(toml_file, encoding="utf-8") as f:
        toml_dict = toml.load(f)
        backnumbers_array.append(BackNumber(
            urljoin(BACKNUMBER_BASE_URL, toml_dict["pdfpath"]),
            date.fromisoformat(toml_dict["published_at"]),
            toml_dict["title"],
        ))

with open(BACKNUMBER_GMI, "w", encoding="utf-8") as f:
    f.write("# バックナンバー\n")
    f.write("\n")
    for backnumber in sorted(backnumbers_array, key=lambda x: x.published_at, reverse=True):
        f.write(f"=> {backnumber.url} {backnumber.published_at} - {backnumber.title}\n")

    f.write("\n")
    f.write("=> ./index.gmi ホームに戻る\n")
    f.write("\n")
    f.write("(c) 1979-2022 WORD編集部\n")
    f.write(f"最終更新日時: {datetime.now(timezone(timedelta(hours=9))).isoformat()}\n")
