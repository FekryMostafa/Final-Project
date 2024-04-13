from transformers import AutoModelForCausalLM, AutoTokenizer

save_dir = "model_save/checkpoint-1750"

print("Loading model from checkpoint...")
model = AutoModelForCausalLM.from_pretrained(save_dir, load_in_8bit=True)
print("Attaching adapter...")
model.load_adapter(save_dir, adapter_name="Adapter1")
print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(save_dir)

while True:
	text = input(">>> ")
	if text == "exit":
		break
	
	model_inputs = tokenizer([text], return_tensors="pt", max_length=256).to("cuda")

	generated_ids = model.generate(**model_inputs, 
									max_length=1024,
									#truncation=True,
									temperature=0.1,
									do_sample=True,
									pad_token_id=tokenizer.eos_token_id)

	response=tokenizer.batch_decode(generated_ids, 
									skip_special_tokens=True)[0]

	print(f"\n\t<<< {response} >>>\n")