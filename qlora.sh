#! /bin/bash

git clone https://github.com/artidoro/qlora
cd qlora
python3 qlora.py --dataset i../data.jsonl --trust_remote_code True 
