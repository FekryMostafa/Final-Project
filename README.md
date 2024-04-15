# Finetuning microsoft/phi-2 with QLoRA on WLU custom dataset

---

### Getting Started

Make sure you have cuda installed, as well as `transformers`, `accelerate`, `peft` and `bitsandbytes`

### Fine-Tuning

1. READ THE SCRIPT `qlora.sh` before running it. See what it does. For gods sake, don't just run random BASH scripts you find online!
2. Make sure to set the right priviledges on `qlora.sh`
```
chmod u+x qlora.sh
```
3. Run that sucker
```
./qlora.sh
```
