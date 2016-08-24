#!/bin/sh

# dir donde esta almacenado este script
DIR="$(dirname $0)"
$DIR/retrieveNewlinks.py
$DIR/getNewVideoIDs.py
$DIR/addVideo.py
