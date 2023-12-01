#!/usr/bin/env bash

set -ex

DAY=$1

mkdir $DAY

touch "${DAY}/input.txt"
touch "${DAY}/test.txt"
cp template.py "${DAY}/code-1.py"
