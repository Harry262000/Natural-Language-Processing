from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load tokenizer and model
def load_models():
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
    return tokenizer, model
