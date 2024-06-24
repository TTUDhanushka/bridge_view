import subprocess

from flask import Flask

app = Flask(__name__)


@app.route('/start_recording', methods=['POST'])
def start_recording():
    try:
        # Start rosbag recording
        subprocess.Popen(['rosbag', 'record', '-a'])
        return '', 200
    except Exception as e:
        print(f" Error start recording {e}")
        return '', 500


@app.route('/stop_recording', methods=['POST'])
def stop_recording():
    try:
        # Stop rosbag recording
        subprocess.Popen(['pkill', 'rosbag'])
        return '', 200
    except Exception as e:
        print(f" Error occured at stopping {e}")
        return '', 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
