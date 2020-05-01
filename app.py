from flask import Flask, render_template, request
import datetime
import time
import math

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def comtoise():
    [now_epoch, now_iso, now_iso_utc, now_prose] = convert_datetime(datetime.datetime.now())

    if request.method == 'POST':
        if "convert_from_epoch" in request.form:

            from_time = datetime.datetime.fromtimestamp(int(request.form['from_epoch']))
        elif "convert_from_iso" in request.form:
            from_time = datetime.datetime.fromisoformat(request.form['from_iso'])
        elif "convert_from_picker" in request.form:
            from_time = datetime.datetime.fromtimestamp(request.form['from_picker'])
        else:
            raise AttributeError("Wrong form used")
    else:
        from_time = datetime.datetime.now()

    [converted_epoch, converted_iso, converted_iso_utc, converted_prose] = convert_datetime(from_time)

    return render_template('comtoise.html',
                           now_epoch=now_epoch,
                           now_prose=now_prose,
                           now_iso=now_iso,
                           now_iso_utc=now_iso_utc,
                           converted_prose=converted_prose,
                           converted_iso=converted_iso,
                           converted_iso_utc=converted_iso_utc,
                           converted_epoch=converted_epoch)


def convert_datetime(from_time) -> [str, str, str, str]:
    converted_prose = str(from_time.ctime())
    converted_iso = from_time.isoformat(timespec='seconds')
    converted_iso_utc = from_time.astimezone(tz=datetime.timezone.utc).isoformat()
    converted_epoch = math.floor(from_time.timestamp())
    return [converted_epoch, converted_iso, converted_iso_utc, converted_prose]


if __name__ == "__main__":
    app.run()
