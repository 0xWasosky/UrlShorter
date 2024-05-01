from database import Database
from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


db = Database("./database")
app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app)



@app.route("/add-url", methods=["POST"])
@limiter.limit("10/m")
def add_url():
    url = request.get_json()["url"]

    data = db.add_url(url)

    return {"url": f"/{data}"}



@app.route("/<path>", methods=["GET"])
@limiter.limit("30/m")
def get_url(path):
    try:
        url = db.get_url(path)

        return {"url": url}
    except:
        return {"url": "invalid data"}, 400

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8080

    app.run(host=HOST, port=PORT)
