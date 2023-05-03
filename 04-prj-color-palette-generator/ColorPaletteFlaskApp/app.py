from flask import Flask, render_template, request
import openai
from dotenv import dotenv_values

config = dotenv_values("../.env")
openai.api_key = config["OPENAI_API_KEY"]


app = Flask(
    __name__,
    template_folder='templates',
)


@app.route('/palette', methods=['POST'])
def prompt_to_palette():
    # OPEN AI COMPLETION CALL

    # RETURN LIST OF COLORS
    print("test")


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
