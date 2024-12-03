from transformers import AutoTokenizer, AutoModelForCausalLM

def generate_suggestions(event_description, prompt, model_name="gpt2", token=None):
    """
    Generates suggestions based on an event description and prompt using GPT-2 or another model.

    Args:
        event_description (str): Description of the event.
        prompt (str): Additional prompt for generating suggestions.
        model_name (str): Name of the Hugging Face model.
        token (str): Hugging Face authentication token (if needed).

    Returns:
        list: Generated suggestions as a list of strings.
    """
    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=token)
    model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=token)
    
    # Add a padding token if not present
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token  # Use the end-of-sequence token as the padding token

    # Prepare the input text
    input_text = f"Event Description: {event_description}\nPrompt: {prompt}\nSuggestions:"
    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=512
    )
    
    # Pass `attention_mask` explicitly
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]
    
    # Generate output
    outputs = model.generate(
        input_ids,
        attention_mask=attention_mask,  # Explicitly pass the attention mask
        max_length=200,
        num_return_sequences=3,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        do_sample=True,
        pad_token_id=tokenizer.pad_token_id
    )
    
    # Decode and format suggestions
    suggestions = [tokenizer.decode(output, skip_special_tokens=True).split("Suggestions:")[1].strip() for output in outputs]
    return suggestions

# Example usage
if __name__ == "__main__":
    event_description = "A community fundraiser to support local schools."
    prompt = "What activities and ideas could make this event more engaging?"
    
    # Replace 'gpt2' with the actual model name or path
    suggestions = generate_suggestions(event_description, prompt, model_name="gpt2")  # Testing with GPT-2
    for idx, suggestion in enumerate(suggestions, 1):
        print(f"Suggestion {idx}: {suggestion}")
