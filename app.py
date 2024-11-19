from flask import Flask, render_template

app = Flask(__name__, template_folder = "siteciencia/templates", static_folder= "siteciencia/static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analise", defaults={"usuario":"visitante"})
@app.route("/analise/<usuario>")
def analise(usuario):
    return render_template("analise.html", usuario=usuario)


if __name__ == "__main__":
    app.run(debug=True)
    