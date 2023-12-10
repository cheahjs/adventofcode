#!/usr/bin/env bash

set -ex

YEAR=2023
DAY=$1

mkdir "$DAY"

set +x
echo "Fetching input for day ${DAY}"
curl "https://adventofcode.com/${YEAR}/day/${DAY}/input" \
  -H "cookie: session=$(cat ~/.secrets/aoc_session)" \
  -o "${DAY}/input.txt"
set -x
touch "${DAY}/test.txt"
cp template.py "${DAY}/code-1.py"
