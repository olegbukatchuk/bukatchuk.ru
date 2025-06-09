#!/bin/bash

set -ex

cd ~/git/github.com/bukatchuk.com/hugo && jekyll build && hugo
echo "Copy"
cp -r ~/git/github.com/bukatchuk.com/hugo/public/* ~/git/github.com/bukatchuk.com/
echo "Done"
