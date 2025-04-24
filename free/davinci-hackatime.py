import os
import time
import base64
import urllib.request
import urllib.error
import json
from datetime import datetime

WAKATIME_API_KEY = 'YOUR_WAKATIME_API_KEY'
WATCH_FOLDER = "ADD_YOUR_FOLDER"
HEARTBEAT_INTERVAL = 120
CHECK_INTERVAL = 30

def send_heartbeat(file_path, project_name):
    encoded_key = base64.b64encode(WAKATIME_API_KEY.encode()).decode()
    headers = {
        "Authorization": f"Basic {encoded_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "time": datetime.utcnow().timestamp(),
        "entity": file_path,
        "type": "file",
        "category": "coding",
        "is_write": True,
        "project": project_name,
        "language": "video editing",
        "plugin": "davinci-resolve-wakatime"
    }
    req = urllib.request.Request(
        url='https://hackatime.hackclub.com/api/hackatime/v1/users/current/heartbeats',
        data=json.dumps(payload).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    try:
        with urllib.request.urlopen(req) as response:
            print(f"[{datetime.now()}] Sent heartbeat: {response.status}")
    except urllib.error.HTTPError as e:
        print(f"[{datetime.now()}] Error sending heartbeat: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print("[{}] Network error: {}".format(datetime.now(), e.reason))

def main():
    last_sent = 0

    while True:
        most_recent_file = None 
        most_recent_time = 0

        for root, _, files in os.walk(WATCH_FOLDER):
            for files in files:
                if file.endswith(".db"):
                    full_path = os.path.join(root, file)
                    mod_time = os.path.getmtime(full_path)
                    if mod_time > most_recent_time:
                        most_recent_time = mod_time
                        most_recent_file = full_path

        now = time.time()
        if most_recent_file and now - last_sent > HEARTBEAT_INTERVAL:
            project_name = os.path.basename(os.path.dirname(most_recent_file))
            send_heartbeat(most_recent_file, project_name)
            last_sent = now

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()