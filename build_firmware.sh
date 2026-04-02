#!/bin/bash
export IDF_PATH=~/esp/esp-idf
source ~/esp/esp-idf/export.sh
cd entropy-zero-fw
idf.py set-target esp32
idf.py build
