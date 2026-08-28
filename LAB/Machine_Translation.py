from transformers import pipeline

print("Initializing local Hugging Face translation pipeline...")
try:
    # Uses the small t5 configuration to cleanly perform translation
    translator = pipeline("translation_en_to_fr", model="t5-small")
    translation = translator("Hello, how are you?")
    print("\nFrench Translation Output:")
    print(translation[0]['translation_text'])
except Exception as e:
    print("Pipeline loading skipped or error occurred:", e)