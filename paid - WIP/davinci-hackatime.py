
import os
import time
import base64
import json
import urllib.request
import urllib.error
from datetime import datetime

import sys

script_path = r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules"


if script_path not in sys.path:
    sys.path.append(script_path)

import DaVinciResolveScript as dvr


WAKATIME_API_KEY = 'YOUR_WAKATIME_API_KEY'
PROJECT_NAME = 'DaVinci Resolve Project'
HEARTBEAT_INTERVAL = 120
CHECK_INTERVAL = 60

resolve = dvr.scriptapp("Resolve")
if not resolve:
    print("Can't connect to DaVinci Resolve Script.")
    exit(1)

project_manager = resolve.GetProjectManager()
media_storage = resolve.GetMediaStorage()

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

def main():
    last_sent = 0

    while True:
        project = project_manager.GetCurrentProject()
        if not project:
            print("No project open found.")
            time.sleep(CHECK_INTERVAL)
            continue

        project_name = project.GetName()
        timeline = project.GetCurrentTimeline()

        if timeline:
            timeline_name = timeline.GetName()
        else:
            timeline_name = "NoTimeline"

        file_path = f"{project_name}/{timeline_name}"

        now = time.time()

        if now - last_sent > HEARTBEAT_INTERVAL:
            send_heartbeat(file_path, project_name)
            last_sent = now
        
        time.sleep(HEARTBEAT_INTERVAL)

if __name__ == "__main__":
    main()
