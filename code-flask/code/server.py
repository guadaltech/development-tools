from flask import Flask
import random

import ptvsd
ptvsd.enable_attach()
print("Wait for Attach...")
ptvsd.wait_for_attach()
print("Attach!")

app = Flask(__name__)

@app.route("/hello")
def hello():
	return "Hello, World!"

@app.route("/")
def random_flask():
	print("[INFO] Generate...", flush=True)
	return str(random.randrange(100000))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
