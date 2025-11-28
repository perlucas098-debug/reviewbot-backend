from transformers import pipeline

def generate_review(title):
    generator = pipeline('text-generation', model='distilgpt2')
    prompt = f"Escribe una reseña positiva y natural sobre el producto '{title}'. Incluye pros y contras breves."
    result = generator(prompt, max_length=150, num_return_sequences=1)
    text = result[0]['generated_text']
    cleaned = text.replace(prompt, '').strip()
    return cleaned[:600]
