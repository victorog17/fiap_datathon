from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/recommendations", methods=["GET"])
def get_recommendations():
    user_id = request.args.get("userId")
    return jsonify({"userId": user_id, "recommendations": ["news1", "news2", "news3"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
