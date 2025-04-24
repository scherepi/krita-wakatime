"""
shout out to https://resolvedevdoc.readthedocs.io/en/latest/index.html for documenting almost everything that is here, checked posts on reddit and blackmagicdesign forum and this is by far the best. 
"""

import os
import time
import requests
from datetime import datetime

try:
    import DavinciResolveScript as dvr 
except ImportError:
    print("DaVinci Resolve Scripting not found!")
    exit(1)

WAKATIME_API_KEY = 'YOUR_WAKATIME_API_KEY'
PROJECT_NAME = 'DaVinci Resolve Project'
HEARTBEAT_INTERVAL = 120
CHECK_INTERVAL = 30

resolve = dvr.scriptapp("Resolve")
project_manager = resolve.GetProjectManager()
media_storage = resolve.GetMediaStorage()

def send_heartbeat(file_path, project_name):
    encoded_key = base64.b64encode(WAKATIME_API_KEY.encode()).decode()
    headers = {
        "Authorization": f"Basic {encoded_key}"
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
    response = requests.post('https://api.wakatime.com/api/v1/users/current/heartbeats', headers=headers, json=payload)
    print(f"[{datetime.now()}] Sent heartbeat: {response.status_code}")

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
