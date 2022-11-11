text = input()

result = [text[i] + text[i+1] for i in range(len(text)) if text[i] == ":"]

print("\n".join(result))