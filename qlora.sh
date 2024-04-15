#! /bin/bash

if [ ! -d "qlora" ]; then
	git clone https://github.com/artidoro/qlora
	cp ./_qlora.py qlora/_qlora.py
fi
cd qlora
python3 _qlora.py --model_name_or_path microsoft/phi-2 --dataset i../data.jsonl --trust_remote_code True 
