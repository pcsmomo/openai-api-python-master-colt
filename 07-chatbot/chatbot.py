import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

messages = []

while True:
    try:
        user_input = input("You: ")
        messages.append({"role": "user", "content": user_input})

        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        res_message = res["choices"][0]["message"]
        messages.append(res_message.to_dict())
        # print(messages)
        print("Assistant: ", res_message["content"])
        print("\n\n")

    except KeyboardInterrupt:
        print("Exiting...")
        break

print(res)
