import json
from src.utils.pdfl import load_pdf
from src.utils.retry import retry
from src.moderation.moderation import ModerationClient
from src.llm.nano import NanoLLM


def pipeline(pdf_path):
    
    text = load_pdf(pdf_path)

    
    mod = ModerationClient()
    mod_result = mod.check(text)

    if not mod_result["allowed"]:
        return mod_result   

    
    llm = NanoLLM()
    llm_output = retry(lambda: llm.generate(text), attempts=2, delay=1)

    return {
        "allowed": True,
        "result": llm_output
    }


if __name__ == "__main__":
    result = pipeline("task1_data.pdf")
    print(json.dumps(result, indent=2))
