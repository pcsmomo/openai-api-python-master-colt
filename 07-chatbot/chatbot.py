import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


def main():
    parser = argparse.ArgumentParser(
        description="Simple command line chatbot with GPT")

    parser.add_argument("--personality",
                        type=str,
                        help="A brief summary of the chatbot's personality",
                        default="friendly and helpful")

    args = parser.parse_args()
    # python chatbot.py --personality "silly and goofy"
    # python chatbot.py --personality "rude and sarcastic"
    # python chatbot.py --personality "chlidish and toddler-like 3 years old"
    # You: What should I eat for dinner?
    # print(args)
    # Namespace(personality='silly and goofy')

    initial_prompt = f"You are a conversational chatbot. Your personality is {args.personality}"
    messages = [{"role": "system", "content": initial_prompt}]

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
            print("\n")

        except KeyboardInterrupt:
            print("Exiting...")
            break

    # print(res)


if __name__ == "__main__":
    main()
