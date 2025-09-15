from flask import Flask, request

app = Flask(__name__)

@app.route("/whoami")
def whoami():
    client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    client_port = request.environ.get("REMOTE_PORT")  # Flask doesn't expose port directly
    return {"ip": client_ip, "port": client_port}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
