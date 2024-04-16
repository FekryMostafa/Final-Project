# Finetuning or run microsoft/phi-2 with QLoRA on WLU custom dataset

---

## Running the model

### Getting started
If you have a GPU available, you should consider installing CUDA to run this on that device.

### Requirements
Make sure you install the requirements and they are up-to-date. 
Requirements are `transformers`, `accelerate`, `peft` and `bitsandbytes`. 

Install requirements with
```
pip3 install -r requirements.txt
```

### CPU vs. GPU
CUDA isn't completely necessesary so long as you are fine running on the model on your CPU.
On the GPU, however, you can expect the time to generate a response to be about 30x faster.

### Run the model from huggingface.co

Download the model and run it on your machine with our `GenAI-CoolCats/WLU-Phi2` [link](GenAI-CoolCats/WLU-Phi2)
```
python3 load_from_checkpoint.py
```
Or run it as a Gradio App
```
python3 app.py
```

---

# Fine-Tuning

1. READ THE SCRIPT `qlora.sh` before running it. See what it does. For gods sake, don't just run random BASH scripts you find online!
2. Make sure to set the right priviledges on `qlora.sh`
```
chmod u+x qlora.sh
```
3. Run that sucker
```
./qlora.sh
```
