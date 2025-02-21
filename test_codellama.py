from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "codellama/CodeLlama-7b-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

print("CodeLlama Model Loaded Successfully!")
