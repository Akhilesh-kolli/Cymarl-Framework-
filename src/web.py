from flask import Flask, render_template, request
from marlon.simulate import SimulationCache, simulate
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

SIMULATION = SimulationCache()


@app.route('/')
def home():
    return render_template(
        "index.html",
        logs=SIMULATION.value
    )


@app.route('/simulate', methods=['POST'])
def run_simulation():
    SIMULATION.value = simulate(
        timesteps=20,
        attacker_option="ppo",
        defender_option="ppo"
    )
    return render_template("index.html", logs=SIMULATION.value)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
