def error():
    input("[INFO] Press enter to exit")
    sys.exit(0)

try:
    import sys
    import requests as rq
    from flask import Flask
except:
    print(f"[ERROR] Import error: programm isn't installed correctly. Please read the documentation (at least the installation part).")
    error()

app = Flask(__name__)

# URL input
try:
    print("[INFO] Loading " + sys.argv[1])
    url = sys.argv[1]
except:
    url = input("[INPUT] URL:\t")

# URL check (is valid?)
if not url.startswith("http"):
    url = "https://" + url

if not url.count("."):
    print(f"[ERROR] Invalid url '{url}': url has to contain at least one '.'.")
    error()

if not url.count("://"):
    print(f"[ERROR] Invalid url '{url}': url has to contain '://'.")
    error()

try:
    got = rq.get(url)
except:
    print("[ERROR] Couldn't load the url: GET-Function from Requests failed.")
    error()

@app.route('/')
def index():
    try:
        return got.text
    except:
        print("[ERROR] Failed getting the html code: .text-Argument from Requests failed.")
        error()

try:
    app.run()
except:
    print("[ERROR] Couldn't run application: Flask app failed run.")
    error()