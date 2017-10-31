from flask import Flask
from datetime import datetime

app = Flask(__name__)

time_now = datetime.now()
today_8am = time_now.replace(hour=8, minute=0, second=0, microsecond=0)
today_6pm = time_now.replace(hour=18, minute=0, second=0, microsecond=0)


@app.route("/")
def count_hours():
    # open_hours = "8AM-6PM PST"
    if today_8am <= time_now <= today_6pm:
        result = "Open"
    else:
        result = "Close"
    return result

if __name__ == "__main__":
    app.run()
