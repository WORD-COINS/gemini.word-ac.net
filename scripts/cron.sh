#!/usr/bin/env bash

set -eu

. ./scripts/fetch-wordpress.sh && ./scripts/backnumber.py
