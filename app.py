from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'
load8 = True if device == 'cuda' else False
model = AutoModelForCausalLM.from_pretrained("GenAI-CoolCats/WLU-Phi2", load_in_8bit=load8)
model.load_adapter("GenAI-CoolCats/WLU-Phi2", adapter_name="ad1")
tokenizer = AutoTokenizer.from_pretrained("GenAI-CoolCats/WLU-Phi2")


def predict(input_text):
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=256).to(device)
    outputs = model.generate(inputs, max_length=128, 
                            temperature=0.5, 
                            pad_token_id=tokenizer.eos_token_id,
                            do_sample=True)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

	# remove repeat of the question
    if '?' in response:
        to_q = response.index('?')
        #if len(input_text)-1 <= to_q and response[:to_q] == input_text[:to_q]:
        response = response[to_q+1:]
    return response
	
import gradio as gr

iface = gr.Interface(fn=predict, 
                     inputs="text", 
                     outputs="text",
                     title="Fine-Tuned Language Model",
                     description="Type something to interact with the fine-tuned model.")
iface.launch()
