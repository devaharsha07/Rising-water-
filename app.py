from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)
model_path = "flood_model/floods.save" if os.path.exists("flood_model/floods.save") else "floods.save"
model = joblib.load(model_path)

columns = {
    "MonsoonIntensity": "🌧 Monsoon Intensity",
    "TopographyDrainage": "🏔 Terrain & Drainage",
    "RiverManagement": "🌊 River Management",
    "Deforestation": "🌳 Deforestation",
    "Urbanization": "🏙 Urbanization",
    "ClimateChange": "🌍 Climate Change",
    "DamsQuality": "🏗 Dam Quality",
    "Siltation": "🪨 Siltation",
    "AgriculturalPractices": "🌾 Agricultural Practices",
    "Encroachments": "🏠 Encroachments",
    "IneffectiveDisasterPreparedness": "🚨 Disaster Preparedness",
    "DrainageSystems": "🚰 Drainage Systems",
    "CoastalVulnerability": "🌊 Coastal Vulnerability",
    "Landslides": "⛰ Landslide Risk",
    "Watersheds": "💧 Watersheds",
    "DeterioratingInfrastructure": "🏢 Infrastructure",
    "PopulationScore": "👥 Population Density",
    "WetlandLoss": "🌿 Wetland Loss",
    "InadequatePlanning": "📋 Urban Planning",
    "PoliticalFactors": "🏛 Administrative Factors"
}

@app.route("/")
def home():
    return render_template("index.html", columns=columns.items())
@app.route("/predict", methods=["POST"])
def predict():
    values = [float(request.form[col]) for col, label in columns.items()]
    final_input = np.array([values])

    prediction = float(model.predict(final_input)[0])
    percentage = round(prediction * 100, 2)

    if prediction >= 0.75:
        result = "High Flood Risk"
        status = "danger"
        recommendation = [
            "Issue early flood warning immediately.",
            "Prepare evacuation plans for low-lying areas.",
            "Deploy emergency response teams.",
            "Monitor rainfall, drainage, and river levels continuously."
        ]
    elif prediction >= 0.5:
        result = "Moderate Flood Risk"
        status = "warning"
        recommendation = [
            "Keep disaster response teams alert.",
            "Monitor vulnerable regions closely.",
            "Inspect dams, drainage systems, and river flow.",
            "Prepare public advisories if rainfall increases."
        ]
    else:
        result = "Low Flood Risk"
        status = "safe"
        recommendation = [
            "Flood risk is currently low.",
            "Continue regular weather monitoring.",
            "Maintain drainage systems.",
            "Stay prepared during monsoon season."
        ]

    return render_template(
        "result.html",
        result=result,
        prediction=round(prediction, 3),
        percentage=percentage,
        status=status,
        recommendation=recommendation
    )

if __name__ == "__main__":
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    