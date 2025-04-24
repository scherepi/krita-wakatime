# davinci-resolve-wakatime

2 scripts to send WakaTime heartbeats, the free version of DaVinci Resolve does not allow you to use the `DaVinciResolveScript` API, BUT we can watch changes in AppData folder.

However, I haven't tested the paid version, I don't have the money for that. Issues and Pull Requests are welcome.

## Setup

Clone the repo (or download .zip):

```
git clone https://github.com/LucasHT22/davinci-resolve-wakatime.git
```

In `davinci-resolve.py`, change WAKATIME_API_KEY to your WakaTime API Key, and, if necessary, change file paths.

For the paid version, you need to add this script to `C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Comp` folder.

## Main References