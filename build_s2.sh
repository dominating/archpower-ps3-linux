#!/bin/bash
export IDF_PATH=~/esp/esp-idf
source ~/esp/esp-idf/export.sh
cd entropy-zero-fw
idf.py fullclean
idf.py set-target esp32s2
idf.py build
