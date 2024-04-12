from transformers import AutoModelForCausalLM, AutoTokenizer

peft_model_path="checkpoint-500/adapter_model.bin"
model_id = "microsoft/phi-2"

model = AutoModelForCausalLM.from_pretrained(model_id, load_in_8bit=True)
model.load_adapter(peft_model_path)

tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2")
model_inputs = tokenizer(["A list of colors: red, blue"], return_tensors="pt").to("cuda")

generated_ids = model.generate(**model_inputs)

print(tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0])
