from transformers import AutoModelForCausalLM, AutoTokenizer
import torch.cuda as cuda


save_dir = "GenAI-CoolCats/WLU-Phi2"
device = "cuda" if cuda.is_available() else 'cpu'
load8bit = device == "cuda"

print("Loading model from checkpoint...")
model = AutoModelForCausalLM.from_pretrained(save_dir, load_in_8bit=load8bit)
print("Attaching adapter...")
model.load_adapter(save_dir, adapter_name="Adapter1")
print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(save_dir)

while True:
	text = input(">>> ")
	if text == "exit":
		break
	
	model_inputs = tokenizer([text], return_tensors="pt", max_length=256).to(device)

	generated_ids = model.generate(**model_inputs, 
									max_length=1024,
									#truncation=True,
									temperature=0.1,
									do_sample=True,
									pad_token_id=tokenizer.eos_token_id)

	response=tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

	# remove repeat of the question
	if '?' in response:
		to_q = response.index('?')
		if len(text)-1 <= to_q and response[:to_q] == text[:to_q]:
			response = response[to_q+1:]
		
	print(f"\n\t<<< {response} >>>\n")
