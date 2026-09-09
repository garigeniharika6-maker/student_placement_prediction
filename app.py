from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

data = {
    "cgpa": [6.2, 7.1, 8.5, 9.0, 6.8, 8.0, 7.5, 9.2, 6.0, 8.7, 7.8, 5.9],
    "internships": [0, 1, 2, 3, 1, 2, 1, 3, 0, 2, 2, 0],
    "projects": [1, 2, 3, 4, 2, 3, 2, 4, 1, 3, 3, 1],
    "aptitude": [55, 65, 80, 90, 60, 78, 70, 92, 50, 85, 75, 45],
    "communication": [55, 65, 80, 90, 62, 75, 70, 95, 48, 85, 78, 45],
    "placed": [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

X = df[["cgpa", "internships", "projects", "aptitude", "communication"]]
y = df["placed"]

model = LogisticRegression()
model.fit(X, y)


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    probability = None

    if request.method == "POST":

        cgpa = float(request.form["cgpa"])
        internships = int(request.form["internships"])
        projects = int(request.form["projects"])
        aptitude = float(request.form["aptitude"])
        communication = float(request.form["communication"])

        student = [[
            cgpa,
            internships,
            projects,
            aptitude,
            communication
        ]]

        result = model.predict(student)[0]
        probability = model.predict_proba(student)[0][1] * 100

        if result == 1:
            prediction = "PLACED"
        else:
            prediction = "NOT PLACED"

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability
    )


if __name__ == "__main__":
    app.run(debug=True)