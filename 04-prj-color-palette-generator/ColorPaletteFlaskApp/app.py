from flask import Flask, render_template, request
import openai
from dotenv import dotenv_values
import json

config = dotenv_values("./.env")
openai.api_key = config["OPENAI_API_KEY"]


app = Flask(
    __name__,
    template_folder='templates',
    static_url_path='',
    static_folder='static'
)


def print_completion_token_usage(response):
    """
    This function prints the token usage of the Complete response.
    It works for Completion and ChatCompletion
    """
    # "·Token usage: 36 = 33 + 3 (prompt + completion)"
    print(
        f"·Token usage: {response['usage']['total_tokens']} = {response['usage']['prompt_tokens']} + {response['usage']['completion_tokens']} (prompt + completion)")


def get_colors(msg):
    prompt = f"""
    You are a color palette generating assistant that responds to text prompts for color palettes
    Your should generate color palettes that fit the theme, mood, or instructions in the prompt.
    The palettes should be between 2 and 8 colors.

    Q: Convert the following verbal description of a color palette into a list of colors: The Mediterranean Sea
    A: ["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]

    Q: Convert the following verbal description of a color palette into a list of colors: sage, nature, earth
    A: ["#EDF1D6", "#9DC08B", "#609966", "#40513B"]


    Desired Format: a JSON array of hexadecimal color codes

    Q: Convert the following verbal description of a color palette into a list of colors: {msg} 
    A:
    """

    response = openai.Completion.create(
        prompt=prompt,
        model="text-davinci-003",
        max_tokens=200,
    )

    print_completion_token_usage(response)
    colors = json.loads(response["choices"][0]["text"])
    return colors


@app.route('/palette', methods=['POST'])
def prompt_to_palette():
    query = request.form.get("query")
    app.logger.info(query)

    # OPEN AI COMPLETION CALL
    colors = get_colors(query)

    return {"colors": colors}


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
