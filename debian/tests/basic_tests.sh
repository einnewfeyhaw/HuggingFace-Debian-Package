#!/bin/sh
set -e

if ! command -v huggingface-cli >/dev/null 2>&1;then
   echo "hugging face cli not installed"
   exit 1
fi
#test -f /usr/bin/huggingface-cli || {echo "huggingface cli not found";exit 1;}
huggingface-cli --version || {echo "hugging face cli failed to run"; exit 1;}
