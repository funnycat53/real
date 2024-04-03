from flask import Flask, render_template
from dati import dabut_rindinas

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/text")
def text():
    return render_template("text.html")

@app.route("/saraksts")
def saraksts():
    saraksts = ["Messi", "Ronaldo", "Neymar"]
    bildes = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnVRQUiLZMMBawmw2483gS0iCOUXhvrvzYWg&s",
               "data:image/jpeg;base64,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",
                 "data:image/jpeg;base64,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"]
    kopejais_saraksts = []
    faila_rindas = dabut_rindinas()
    for rinda in faila_rindas:
        elements = rinda.split(", ")
        kopejais_saraksts.append(elements)

    return render_template("saraksts.html", vardi = saraksts, bildes = bildes, garums = len(saraksts), visi = kopejais_saraksts)


if __name__ == "__main__":
        app.run(port = 5000)