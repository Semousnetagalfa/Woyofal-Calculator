from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot WhatsApp en ligne !"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        VERIFY_TOKEN = "mon_token_secret"
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if mode and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Unauthorized", 403
    if request.method == "POST":
        data = request.get_json()
        print("Message reçu :", data)
        return "OK", 200        

