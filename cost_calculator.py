import tiktoken

def embedding_cost_calculator(chunks):
    model_cost = 0.0004 / 1000
    total_tokens = 0

    encoding = tiktoken.encoding_for_model("text-embedding-ada-002")

    for chunk in chunks:
        total_tokens += len(encoding.encode(chunk.page_content))

    cost = total_tokens * model_cost
    return f'{cost:.7f}'




