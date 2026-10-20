from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open("Salary_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("job_encoder.pkl", "rb") as file:
    job_encoder = pickle.load(file)

with open("education_encoder.pkl", "rb") as file:
    education_encoder = pickle.load(file)

with open("industry_encoder.pkl", "rb") as file:
    industry_encoder = pickle.load(file)

with open("company_encoder.pkl", "rb") as file:
    company_encoder = pickle.load(file)

with open("location_encoder.pkl", "rb") as file:
    location_encoder = pickle.load(file)

with open("remote_encoder.pkl", "rb") as file:
    remote_encoder = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        job_title = request.form["job_title"]
        education = request.form["education_level"]
        skills=request.form['skills_count']
        industry = request.form["industry"]
        company_size = request.form["company_size"]
        location = request.form["location"]
        remote_work = request.form["remote_work"]

        certifications = int(request.form["certifications_count"])
        years_experience = float(request.form["years_experience"])
        job_title = job_encoder.transform([job_title])[0]
        education = education_encoder.transform([education])[0]
        industry = industry_encoder.transform([industry])[0]
        company_size = company_encoder.transform([company_size])[0]
        location = location_encoder.transform([location])[0]
        remote_work = remote_encoder.transform([remote_work])[0]
        input_data = np.array([[
            job_title,
            years_experience,
            education,
            skills,
            industry,
            company_size,
            location,
            remote_work,
            certifications
            
        ]])

        prediction = model.predict(input_data)[0]

        prediction = round(float(prediction), 2)

        return render_template(
            "index.html",
            prediction=f"₹{prediction:,.2f}"
        )

    except Exception as e:

        return render_template(
            "index.html",
            error=str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)