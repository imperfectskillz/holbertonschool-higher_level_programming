#!/bin/bash
# curls and displays size of body
curl -sI "$1" | grep Content-Length | cut -d' ' -f2
