def get_dialog_act(utterance):
    cleaned = utterance.lower().strip()
    if "?" in cleaned: 
        return "Question"
    if any(greet in cleaned for greet in ["hello", "hi", "hey"]): 
        return "Greeting"
    return "Statement"

print("Utterance Acts Classification:")
print(f"Can you help me? -> Act: {get_dialog_act('Can you help me?')}")
print(f"Hello there!    -> Act: {get_dialog_act('Hello there!')}")
print(f"I am coding now. -> Act: {get_dialog_act('I am coding now.')}")