from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PtX Pre-Screening</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background: #f4f6f8;
        }

        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
        }

        h1 {
            color: #1f2937;
        }

        label {
            display: block;
            margin-top: 15px;
            font-weight: bold;
        }

        input, select {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            box-sizing: border-box;
        }

        button {
            margin-top: 25px;
            padding: 12px 20px;
            background: #2563eb;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background: #1d4ed8;
        }

        .result {
            margin-top: 25px;
            padding: 20px;
            background: #eef6ff;
            border-radius: 8px;
        }
    </style>
</head>

<body>
<div class="container">

    <h1>PtX Pre-Screening Application</h1>

    <p>
        Enter basic project information to perform an initial
        Power-to-X project screening.
    </p>

    <form method="POST">

        <label>Project name</label>
        <input type="text" name="project_name" required>

        <label>Country</label>
        <input type="text" name="country" required>

        <label>Electrolyzer capacity (MW)</label>
        <input type="number" name="capacity" min="0" step="0.1" required>

        <label>Electricity price (EUR/MWh)</label>
        <input type="number" name="electricity_price" min="0" step="0.01" required>

        <label>Annual operating hours</label>
        <input type="number" name="operating_hours"
               min="0" max="8760" step="1" required>

        <label>PtX product</label>
        <select name="product">
            <option value="hydrogen">Green Hydrogen</option>
            <option value="ammonia">Green Ammonia</option>
            <option value="methanol">E-Methanol</option>
            <option value="saf">SAF</option>
        </select>

        <button type="submit">Run Pre-Screening</button>

    </form>

    {% if result %}
    <div class="result">
        <h2>Screening Result</h2>

        <p><strong>Project:</strong> {{ result.project_name }}</p>
        <p><strong>Country:</strong> {{ result.country }}</p>
        <p><strong>Product:</strong> {{ result.product }}</p>
        <p><strong>Capacity:</strong> {{ result.capacity }} MW</p>
        <p><strong>Electricity cost:</strong>
           €{{ result.electricity_price }}/MWh</p>

        <hr>

        <p>
            <strong>Estimated annual electricity consumption:</strong>
            {{ result.annual_energy }} GWh
        </p>

        <p>
            <strong>Pre-screening status:</strong>
            {{ result.status }}
        </p>
    </div>
    {% endif %}

</div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        project_name = request.form["project_name"]
        country = request.form["country"]
        capacity = float(request.form["capacity"])
        electricity_price = float(request.form["electricity_price"])
        operating_hours = int(request.form["operating_hours"])
        product = request.form["product"]

        # Simple pre-screening calculation.
        # This is an illustrative estimate, not an engineering model.
        annual_energy = capacity * operating_hours / 1000

        if electricity_price <= 50 and operating_hours >= 4000:
            status = "Potentially attractive"
        elif electricity_price <= 80:
            status = "Requires further analysis"
        else:
            status = "Challenging electricity economics"

        result = {
            "project_name": project_name,
            "country": country,
            "capacity": capacity,
            "electricity_price": electricity_price,
            "operating_hours": operating_hours,
            "product": product,
            "annual_energy": round(annual_energy, 2),
            "status": status
        }

    return render_template_string(
        HTML,
        result=result
    )


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/screen", methods=["POST"])
def api_screen():

    data = request.get_json()

    capacity = float(data["capacity"])
    operating_hours = int(data["operating_hours"])
    electricity_price = float(data["electricity_price"])

    annual_energy = capacity * operating_hours / 1000

    return jsonify({
        "annual_energy_gwh": round(annual_energy, 2),
        "electricity_price_eur_mwh": electricity_price,
        "status": "screening completed"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

