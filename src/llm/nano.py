class NanoLLM:
    
    def generate(self, text: str):
        if not text.strip():
            raise ValueError("Empty text for LLM")

        return {
            "answer": f"Mock GPT-5-Nano response: {text[:200].replace("\n","")}"
        }
