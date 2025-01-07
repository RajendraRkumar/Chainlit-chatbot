from transformers import GPTNeoForCausalLM, GPT2Tokenizer

class GrubhubLLM:
    def __init__(self, model_path):
        self.tokenizer = GPT2Tokenizer.from_pretrained(
            model_path,
            local_files_only=True
        )
        self.model = GPTNeoForCausalLM.from_pretrained(
            model_path,
            local_files_only=True
        )

        # Set pad_token if not already defined
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def generate_response(self, input_text):
        inputs = self.tokenizer(input_text, return_tensors="pt", padding=True)
        outputs = self.model.generate(
            inputs["input_ids"],
            max_length=200,
            temperature=0.7,
            do_sample=True,  # Enable sampling for creative responses
            pad_token_id=self.tokenizer.pad_token_id
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
