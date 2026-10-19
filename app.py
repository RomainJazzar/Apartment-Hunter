from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# On charge le modèle une seule fois, au démarrage de l'application
model = joblib.load("model.pkl")

# Les 8 variables choisies dans le notebook, dans le même ordre que pendant l'entraînement
variables = ["bedrooms", "sqft_living", "sqft_lot", "waterfront", "grade", "yr_renovated", "lat", "long"]


@app.route("/", methods=["GET", "POST"])
def index():
    prix = None

    # Quand l'utilisateur clique sur "Estimer", le formulaire est envoyé en POST
    if request.method == "POST":
        valeurs = {}
        for nom in variables:
            valeurs[nom] = float(request.form[nom])

        # Le modèle attend un tableau avec une ligne (la maison) et les 8 colonnes
        maison = pd.DataFrame([valeurs], columns=variables)
        prix_estime = model.predict(maison)[0]

        # Affichage du prix avec des espaces entre les milliers : 450 000
        prix = "{:,.0f}".format(prix_estime).replace(",", " ")

    # request.form permet de réafficher les valeurs tapées dans le formulaire
    return render_template("index.html", prix=prix, valeurs=request.form)


if __name__ == "__main__":
    # host="0.0.0.0" pour que l'application soit accessible depuis Docker
    app.run(host="0.0.0.0", port=5000)
