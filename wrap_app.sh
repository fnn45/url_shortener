#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
docker build -t url_shortener $DIR
docker run -p 80:8000 -d url_shortener