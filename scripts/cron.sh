#!/usr/bin/env bash

set -eu

. ./scripts/fetch-wordpress.sh
. ./scripts/backnumber.sh > ./contents/backnumber.gmi
