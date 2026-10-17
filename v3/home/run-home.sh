#!/usr/bin/env bash
cd "$(dirname "$0")"
agy --model gemini-3.8-flash-high --print-timeout 900s -p "$(cat prompt.txt)" > home.agy.txt 2> home.err < /dev/null
