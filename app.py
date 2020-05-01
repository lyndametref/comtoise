from flask import Flask, render_template
import datetime
import time
import math

app = Flask(__name__)


@app.route('/')
def comtoise():
    now = datetime.datetime.now()
    return render_template('comtoise.html',
                           now_epoch=math.floor(time.time()),
                           now_english=now.ctime(),
                           now_iso=now.isoformat())


if __name__ == "__main__":
    app.run()
