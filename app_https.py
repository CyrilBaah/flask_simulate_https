from flask import Flask, request, render_template, make_response

app = Flask(__name__)


@app.before_request
def enforce_https():
    if not request.is_secure:
        return render_template("force_https.html"), 403


@app.route("/")
def home():
    token = request.cookies.get("secure-token")
    resp = make_response(render_template("index.html", cookie=token))
    resp.set_cookie("secure-token", "secure123", secure=True,
                    httponly=True, samesite="None")
    return resp


if __name__ == "__main__":
    app.run(ssl_context=("./srv.crt", "./srv.key"), port=5001, debug=True)
