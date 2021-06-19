from flask import Flask, render_template, url_for, request,redirect
import socket
import hashlib
app = Flask(__name__)

@app.route("/")
def home():
    host_name = socket.gethostname()
    #host_name = str(hash("help"))
    # Hash function from the hostname string
    hash_host = hashlib.md5(host_name.encode())
    print(hash_host.hexdigest()[0:6])
    color = hash_host.hexdigest()[0:6]
    return render_template('index.html.j2', host_name=host_name,color=color)

if __name__ == "__main__":
    app.run(debug=True)