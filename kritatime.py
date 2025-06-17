from krita import *
import os
import time
import base64
import urllib.request
import urllib.error
import json
import psutil
from datetime import datetime

WAKATIME_API_KEY = 'YOUR_WAKATIME_API_KEY'
WATCH_FOLDER = "ADD_YOUR_FOLDER"
HEARTBEAT_INTERVAL = 120
CHECK_INTERVAL = 60

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

class myExtension(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        pass

Krita.instance().addExtension(myExtension)