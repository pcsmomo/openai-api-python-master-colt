def print_completion_token_usage(response):
    """
    This function prints the token usage of the Complete response.
    It works for Completion and ChatCompletion
    """
    # "·Token usage: 36 = 33 + 3 (prompt + completion)"
    print(f"·Token usage: {response['usage']['total_tokens']} = {response['usage']['prompt_tokens']} + {response['usage']['completion_tokens']} (prompt + completion)")