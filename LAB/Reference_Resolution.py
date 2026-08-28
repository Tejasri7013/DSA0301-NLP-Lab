def simple_reference_resolution(text):
    # A deterministic rule-based mapping for singular pronoun resolution
    sentences = text.split(".")
    context_noun = "John" # Default target fallback

    print(f"Analyzing Text: {text}\n")
    words = text.split()
    for word in words:
        clean_word = word.lower().strip(",.")
        if clean_word in ["he", "him", "his"]:
            print(f"Resolved Pronoun Reference: '{word}' points back to entity -> '{context_noun}'")

simple_reference_resolution("John said he would arrive.")