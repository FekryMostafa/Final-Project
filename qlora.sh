#! /bin/bash

# this literally pulls the whole qlora repo down
if [ ! -d "qlora" ]; then
	git clone https://github.com/artidoro/qlora
	cp ./_qlora.py qlora/_qlora.py # I changed ONE LINE to make things run
fi
cd qlora
git reset --hard 7f4e95a # this is the last version we used
python3 _qlora.py --model_name_or_path GenAI-CoolCats/WLU-Phi2 --dataset ../data.jsonl --trust_remote_code True --do_eval True
