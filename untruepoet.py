from flask import Flask, render_template, request, jsonify
import openai
import os
from google.cloud import secretmanager

app = Flask(__name__)


# Fetch the OpenAI API key from Google Secret Manager
def get_openai_api_key():
    client = secretmanager.SecretManagerServiceClient()
    project_id = "image-collector-440021"
    secret_id = "OPENAI_API_KEY"
    version_id = "latest"
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(name=name)
    return response.payload.data.decode("UTF-8")

# Set OpenAI API key
openai.api_key = get_openai_api_key()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_poem", methods=["POST"])
def generate_poem():
    data = request.json
    prompt = (
        f"Write a {data['num_lines']} line poem "
        f"with a {data['rhyme_type']} rhyme scheme, "
        f"{data['concreteness']} language, "
        f"{data['erratic_rhythm']} erratic rhythm, "
        f"and a {data['rating']} rating. "
        f"Start with '{data['seed']}'"
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return jsonify({"poem": response.choices[0].text.strip()})

if __name__ == "__main__":
    app.run(debug=True)
