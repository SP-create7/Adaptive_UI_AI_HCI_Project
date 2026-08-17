from flask import Flask, render_template, jsonify
from adaptive_model import AdaptivePreferenceModel

app = Flask(__name__)

# Create the machine-learning model
model = AdaptivePreferenceModel()

# Store the current user's interaction history
interaction_history = {
    "simple": 0,
    "detailed": 0,
    "dark": 0
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/record/<preference>", methods=["POST"])
def record_preference(preference):

    if preference not in interaction_history:
        return jsonify({
            "success": False,
            "message": "Invalid preference."
        }), 400

    # Record the user's interaction
    interaction_history[preference] += 1

    # Use the machine-learning model to predict
    # the user's preferred interface style
    prediction = model.predict_preference(
        interaction_history["simple"],
        interaction_history["detailed"],
        interaction_history["dark"]
    )

    return jsonify({
        "success": True,
        "selected": preference,
        "prediction": prediction,
        "counts": interaction_history
    })


@app.route("/reset", methods=["POST"])
def reset_session():

    # Clear the current interaction history
    interaction_history["simple"] = 0
    interaction_history["detailed"] = 0
    interaction_history["dark"] = 0

    return jsonify({
        "success": True,
        "message": "The user session has been reset.",
        "counts": interaction_history
    })


if __name__ == "__main__":
    app.run(debug=True)