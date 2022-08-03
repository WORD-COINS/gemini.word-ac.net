#!/usr/bin/env python3

from urllib.parse import urljoin

import sys
# import glob
import toml

BACKNUMBER_BASE_URL = "https://bitbucket.org/word-coins/backnumber/raw/master/"
# toml_file_lst = glob.glob("word-press-master/data/backnumber/**/*.toml")

# https://dev.classmethod.jp/articles/python-shell-cli-tool-template/
line = sys.stdin.readline()
while line:
    line = line.strip("\n")
    with open(line, encoding="utf-8") as f:
        toml_dict = toml.load(f)
        print("=> {} {} - {}".format(
            urljoin(BACKNUMBER_BASE_URL, toml_dict["pdfpath"]),
            toml_dict["published_at"],
            toml_dict["title"]
        ))
        line = sys.stdin.readline()
