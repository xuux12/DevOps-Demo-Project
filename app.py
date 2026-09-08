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
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #f1f8f4;
            color: #173b2b;
        }

        /* NAVBAR */
        .navbar {
            background: linear-gradient(135deg, #064e3b, #087f5b);
            color: white;
            padding: 18px 7%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 25px;
            font-weight: bold;
        }

        .logo span {
            color: #86efac;
        }

        .nav-links {
            display: flex;
            gap: 25px;
            font-size: 14px;
        }

        /* HERO */
        .hero {
            min-height: 410px;
            padding: 60px 7%;
            background:
                linear-gradient(
                    90deg,
                    rgba(4, 78, 59, 0.96),
                    rgba(4, 78, 59, 0.72),
                    rgba(255,255,255,0.05)
                ),
                linear-gradient(#8ed8ff, #dff7ff);

            position: relative;
            overflow: hidden;
            color: white;
        }

        .hero-content {
            max-width: 700px;
            position: relative;
            z-index: 2;
        }

        .hero h1 {
            font-size: 52px;
            margin-bottom: 20px;
            line-height: 1.05;
        }

        .hero h1 span {
            color: #86efac;
        }

        .hero p {
            font-size: 19px;
            line-height: 1.6;
            max-width: 650px;
        }

        .hero-icons {
            margin-top: 30px;
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }

        .eco-badge {
            background: rgba(255,255,255,0.14);
            border: 1px solid rgba(255,255,255,0.3);
            padding: 12px 18px;
            border-radius: 30px;
            backdrop-filter: blur(5px);
        }

        /* SCENE */
        .scene {
            position: absolute;
            right: 4%;
            bottom: 0;
            width: 480px;
            height: 300px;
        }

        .sun {
            position: absolute;
            right: 100px;
            top: 10px;
            width: 90px;
            height: 90px;
            background: #facc15;
            border-radius: 50%;
            box-shadow: 0 0 50px #fde68a;
        }

        .mountain {
            position: absolute;
            bottom: 0;
            width: 0;
            height: 0;
            border-left: 180px solid transparent;
            border-right: 180px solid transparent;
            border-bottom: 230px solid #75b798;
        }

        .mountain.two {
            right: 0;
            border-left-width: 150px;
            border-right-width: 150px;
            border-bottom-color: #4d9877;
            border-bottom-width: 190px;
        }

        .water {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 70px;
            background: #38bdf8;
            opacity: .8;
            border-radius: 50% 50% 0 0;
        }

        .house {
            position: absolute;
            bottom: 45px;
            left: 120px;
            width: 115px;
            height: 80px;
            background: #f8fafc;
            border-radius: 4px;
        }

        .roof {
            position: absolute;
            top: -55px;
            left: -15px;
            width: 0;
            height: 0;
            border-left: 72px solid transparent;
            border-right: 72px solid transparent;
            border-bottom: 60px solid #166534;
        }

        .window {
            position: absolute;
            width: 25px;
            height: 25px;
            background: #7dd3fc;
            top: 20px;
            left: 20px;
        }

        .solar-panel {
            position: absolute;
            bottom: 50px;
            left: 260px;
            width: 110px;
            height: 55px;
            background: #064e3b;
            border: 4px solid #d1fae5;
            transform: skew(-15deg);
        }

        /* MAIN */
        .main {
            max-width: 1200px;
            margin: -45px auto 60px;
            padding: 0 20px;
            position: relative;
            z-index: 5;
        }

        .card {
            background: white;
            border-radius: 18px;
            padding: 35px;
            margin-bottom: 25px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.08);
        }

        .section-title {
            color: #065f46;
            font-size: 25px;
            margin-bottom: 25px;
        }

        .section-title span {
            color: #16a34a;
        }

        /* FORM */
        .form-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 22px;
        }

        .form-group label {
            display: block;
            font-weight: bold;
            margin-bottom: 8px;
            color: #24543e;
        }

        input,
        select {
            width: 100%;
            padding: 14px;
            border: 1px solid #cbded3;
            border-radius: 10px;
            font-size: 15px;
            background: #fbfffc;
        }

        input:focus,
        select:focus {
            outline: none;
            border-color: #16a34a;
            box-shadow: 0 0 0 3px rgba(22,163,74,.1);
        }

        .button-container {
            margin-top: 25px;
        }

        button {
            background: linear-gradient(135deg, #15803d, #16a34a);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 10px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: .2s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(22,163,74,.3);
        }

        /* INFO CARDS */
        .eco-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
        }

        .eco-card {
            padding: 25px;
            border-radius: 14px;
            background: #ecfdf5;
            text-align: center;
        }

        .eco-icon {
            font-size: 38px;
            margin-bottom: 10px;
        }

        .eco-card h3 {
            color: #065f46;
            margin-bottom: 8px;
        }

        .eco-card p {
            color: #527064;
            font-size: 14px;
            line-height: 1.5;
        }

        /* RESULTS */
        .result-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
        }

        .result-box {
            background: #f0fdf4;
            border: 1px solid #bbf7d0;
            padding: 25px;
            border-radius: 14px;
        }

        .result-row {
            display: flex;
            justify-content: space-between;
            padding: 13px 0;
            border-bottom: 1px solid #dcfce7;
        }

        .result-row:last-child {
            border-bottom: none;
        }

        .result-label {
            color: #527064;
        }

        .result-value {
            font-weight: bold;
            color: #14532d;
        }

        .energy-number {
            font-size: 38px;
            color: #15803d;
            font-weight: bold;
            margin: 15px 0;
        }

        .status {
            margin-top: 20px;
            padding: 16px;
            border-radius: 10px;
            font-weight: bold;
        }

        .status.good {
            background: #dcfce7;
            color: #166534;
        }

        .status.warning {
            background: #fef3c7;
            color: #92400e;
        }

        .status.bad {
            background: #fee2e2;
            color: #991b1b;
        }

        /* FOOTER */
        footer {
            background: #064e3b;
            color: white;
            text-align: center;
            padding: 25px;
            font-size: 14px;
        }

        footer span {
            color: #86efac;
        }

        /* MOBILE */
        @media (max-width: 800px) {

            .hero h1 {
                font-size: 38px;
            }

            .scene {
                opacity: .25;
                right: -150px;
            }

            .form-grid,
            .result-grid {
                grid-template-columns: 1fr;
            }

            .eco-grid {
                grid-template-columns: 1fr 1fr;
            }

            .nav-links {
                display: none;
            }
        }

        @media (max-width: 500px) {

            .eco-grid {
                grid-template-columns: 1fr;
            }

            .card {
                padding: 22px;
            }
        }
    </style>
</head>

<body>

<!-- NAVBAR -->
<nav class="navbar">
    <div class="logo">
        🌱 PtX <span>Pre-Screening</span>
    </div>

    <div class="nav-links">
        <span>Home</span>
        <span>API</span>
        <span>Health</span>
        <span>🌍 Green Future</span>
    </div>
</nav>


<!-- HERO -->
<section class="hero">

    <div class="hero-content">

        <h1>
            Power-to-X<br>
            <span>for a Greener Future</span>
        </h1>

        <p>
            Perform an initial screening of renewable Power-to-X
            projects and evaluate electricity requirements,
            operating conditions and project potential.
        </p>

        <div class="hero-icons">
            <div class="eco-badge">💧 Green Hydrogen</div>
            <div class="eco-badge">☀️ Solar Energy</div>
            <div class="eco-badge">🌊 Clean Water</div>
            <div class="eco-badge">🏡 Sustainable Energy</div>
        </div>

    </div>


    <!-- Renewable energy illustration -->
    <div class="scene">

        <div class="sun"></div>

        <div class="mountain"></div>
        <div class="mountain two"></div>

        <div class="house">
            <div class="roof"></div>
            <div class="window"></div>
        </div>

        <div class="solar-panel"></div>

        <div class="water"></div>

    </div>

</section>


<!-- MAIN -->
<main class="main">


    <!-- PROJECT FORM -->
    <section class="card">

        <h2 class="section-title">
            🌱 Project Information
        </h2>

        <form method="POST">

            <div class="form-grid">

                <div class="form-group">
                    <label>Project Name</label>
                    <input
                        type="text"
                        name="project_name"
                        placeholder="e.g. Green Hydrogen Denmark"
                        required>
                </div>


                <div class="form-group">
                    <label>Country</label>
                    <input
                        type="text"
                        name="country"
                        placeholder="e.g. Denmark"
                        required>
                </div>


                <div class="form-group">
                    <label>Electrolyzer Capacity (MW)</label>
                    <input
                        type="number"
                        name="capacity"
                        min="0"
                        step="0.1"
                        placeholder="e.g. 50"
                        required>
                </div>


                <div class="form-group">
                    <label>Electricity Price (EUR/MWh)</label>
                    <input
                        type="number"
                        name="electricity_price"
                        min="0"
                        step="0.01"
                        placeholder="e.g. 50"
                        required>
                </div>


                <div class="form-group">
                    <label>Annual Operating Hours</label>
                    <input
                        type="number"
                        name="operating_hours"
                        min="0"
                        max="8760"
                        placeholder="e.g. 4000"
                        required>
                </div>


                <div class="form-group">
                    <label>PtX Product</label>

                    <select name="product">

                        <option value="Green Hydrogen">
                            Green Hydrogen
                        </option>

                        <option value="Green Ammonia">
                            Green Ammonia
                        </option>

                        <option value="E-Methanol">
                            E-Methanol
                        </option>

                        <option value="SAF">
                            Sustainable Aviation Fuel
                        </option>

                    </select>

                </div>

            </div>


            <div class="button-container">

                <button type="submit">
                    🌿 Run PtX Pre-Screening
                </button>

            </div>

        </form>

    </section>


    <!-- ECO CARDS -->
    <section class="card">

        <h2 class="section-title">
            ☀️ Renewable <span>Power-to-X</span>
        </h2>

        <div class="eco-grid">

            <div class="eco-card">
                <div class="eco-icon">💧</div>
                <h3>Green H₂</h3>
                <p>
                    Produce hydrogen using renewable electricity
                    and water.
                </p>
            </div>

            <div class="eco-card">
                <div class="eco-icon">☀️</div>
                <h3>Solar Power</h3>
                <p>
                    Use clean renewable electricity to power
                    PtX production.
                </p>
            </div>

            <div class="eco-card">
                <div class="eco-icon">🌊</div>
                <h3>Clean Water</h3>
                <p>
                    Water is an important input for
                    hydrogen production.
                </p>
            </div>

            <div class="eco-card">
                <div class="eco-icon">🏡</div>
                <h3>Green Future</h3>
                <p>
                    Support cleaner energy systems and
                    sustainable industries.
                </p>
            </div>

        </div>

    </section>


    {% if result %}

    <!-- RESULTS -->
    <section class="card">

        <h2 class="section-title">
            📊 Screening <span>Result</span>
        </h2>


        <div class="result-grid">


            <!-- PROJECT DETAILS -->
            <div class="result-box">

                <div class="result-row">
                    <span class="result-label">
                        Project
                    </span>

                    <span class="result-value">
                        {{ result.project_name }}
                    </span>
                </div>


                <div class="result-row">
                    <span class="result-label">
                        Country
                    </span>

                    <span class="result-value">
                        {{ result.country }}
                    </span>
                </div>


                <div class="result-row">
                    <span class="result-label">
                        Product
                    </span>

                    <span class="result-value">
                        {{ result.product }}
                    </span>
                </div>


                <div class="result-row">
                    <span class="result-label">
                        Capacity
                    </span>

                    <span class="result-value">
                        {{ result.capacity }} MW
                    </span>
                </div>


                <div class="result-row">
                    <span class="result-label">
                        Electricity Price
                    </span>

                    <span class="result-value">
                        €{{ result.electricity_price }}/MWh
                    </span>
                </div>

            </div>


            <!-- ENERGY RESULT -->
            <div class="result-box">

                <div>
                    Estimated Annual Electricity
                </div>

                <div class="energy-number">
                    {{ result.annual_energy }} GWh
                </div>

                <div>
                    Based on {{ result.operating_hours }}
                    operating hours per year.
                </div>


                <div class="status {{ result.status_class }}">
                    {{ result.status }}
                </div>

            </div>

        </div>

    </section>

    {% endif %}

</main>


<footer>

    🌱 PtX Pre-Screening Application
    &nbsp; | &nbsp;
    Built with <span>Flask</span>
    &nbsp; | &nbsp;
    <span>Docker Ready</span>
    &nbsp; | &nbsp;
    Renewable Energy

</footer>

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

        electricity_price = float(
            request.form["electricity_price"]
        )

        operating_hours = int(
            request.form["operating_hours"]
        )

        product = request.form["product"]


        # Simple electricity consumption estimate
        annual_energy = (
            capacity * operating_hours / 1000
        )


        # Simple screening logic
        if electricity_price <= 50 and operating_hours >= 4000:

            status = "Potentially attractive"
            status_class = "good"

        elif electricity_price <= 80:

            status = "Requires further analysis"
            status_class = "warning"

        else:

            status = "Challenging electricity economics"
            status_class = "bad"


        result = {

            "project_name": project_name,
            "country": country,
            "capacity": capacity,
            "electricity_price": electricity_price,
            "operating_hours": operating_hours,
            "product": product,
            "annual_energy": round(annual_energy, 2),
            "status": status,
            "status_class": status_class

        }


    return render_template_string(
        HTML,
        result=result
    )


# Health endpoint for Docker/Kubernetes
@app.route("/health")
def health():

    return jsonify({
        "status": "healthy",
        "application": "PtX Pre-Screening"
    })


# API endpoint
@app.route("/api/screen", methods=["POST"])
def api_screen():

    data = request.get_json()

    capacity = float(data["capacity"])
    operating_hours = int(data["operating_hours"])
    electricity_price = float(data["electricity_price"])

    annual_energy = (
        capacity * operating_hours / 1000
    )

    return jsonify({

        "capacity_mw": capacity,

        "operating_hours": operating_hours,

        "annual_energy_gwh": round(
            annual_energy,
            2
        ),

        "electricity_price_eur_mwh":
            electricity_price,

        "status":
            "screening completed"

    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )