from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        text_to_translate = request.form["text_to_translate"]
        target_lang = request.form["target_lang"]
        
        # Translate the text
        translated_text = translator.translate(text_to_translate, dest=target_lang).text
        
    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
