import subprocess
import os
from flask import Flask

app = Flask(__name__)

target_scripts_dir = "home/dhanushka/PycharmProjects/SCC-Tower-Scripts"

@app.route('/start_ros', methods=['POST'])
def start_ros():
    try:
        cwd = os.getcwd()
        print(f"Current working directory {cwd}")

        if cwd != target_scripts_dir: 
            print(f"Changing the working directory.")

            # Change to the scripts directory
            os.chdir(r"../SCC-Tower-Scripts")

            cwd = os.getcwd()
            print(f"Updated working directory to {cwd}")

        # Start roscore
        subprocess.call(['sh', 'ros_start.sh'])
        return '', 200
    except Exception as e:
        print(f" Error starting ROS {e}")
        return '', 500

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
