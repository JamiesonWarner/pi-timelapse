from flask import Flask, request, send_from_directory
import os

app = Flask(__name__, static_url_path="")

# Define the folder of timelapse images
timelapse_dir = "/media/usbdrive/timelapse"

@app.route('/camera/<path:path>')
def send_js(path):
    return send_from_directory(timelapse_dir, path)

@app.route("/")
def index():
    names = os.listdir(timelapse_dir)
    print(names)
    return "\n".join(names)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
