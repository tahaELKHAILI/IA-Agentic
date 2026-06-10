import tiktoken

def num_tokens_from_string(string: str, encoding_name: str = "o200k_base") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(string))


encoding = tiktoken.encoding_for_model("gpt-4o")
print(f"The model used: {encoding.name}")

system_message = """
Perform sentiment analysis of the review presented in the user message.
The result should be positif or negative. Do not justify your response
"""

tokens = encoding.encode(system_message)

print(f"The number of tokens: {len(tokens)}")
print(f"The list of tokens: {tokens}")


for token in tokens:
    print(encoding.decode_single_token_bytes(token), end = "")


print("\n")
print(f"Number of tokens in tiktoken is great!: {num_tokens_from_string("tiktoken is great!")}")