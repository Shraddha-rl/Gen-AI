import tiktoken
encoding = tiktoken.get_encoding('cl100k_base')
text = "Generative AI helps software developer."

tokens = encoding.encode(text)

print("Original text:", text)
print("Token IDs:", tokens)
print("Number of token", len(tokens))
print("Decoded text:",encoding.decode(tokens))