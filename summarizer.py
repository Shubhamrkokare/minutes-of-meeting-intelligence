import torch
from transformers import BartTokenizer, BartForConditionalGeneration
from peft import PeftModel

# -------------------------------
# Model paths (DO NOT CHANGE)
# -------------------------------
BASE_MODEL = "facebook/bart-large-cnn"
LORA_PATH = "models/bart_dialogsum_lora"

def generate_summary(conversation_text: str) -> str:
    tokenizer = BartTokenizer.from_pretrained(LORA_PATH)

    model = BartForConditionalGeneration.from_pretrained(
        BASE_MODEL,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto"
    )

    # 🔑 THIS loads your trained LoRA weights
    model = PeftModel.from_pretrained(model, LORA_PATH)
    model.eval()

    inputs = tokenizer(
        conversation_text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    ).to(model.device)

    summary_ids = model.generate(
        **inputs,
        max_length=180,
        num_beams=6,
        repetition_penalty=2.0,
        no_repeat_ngram_size=3,
        early_stopping=True
    )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
