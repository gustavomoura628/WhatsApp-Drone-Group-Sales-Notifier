from flask import Flask, request

app = Flask(__name__)

@app.route("/hook", methods=["POST"])
def hook():
    data = request.get_json()
    text = data["text"]
    print(text)
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
