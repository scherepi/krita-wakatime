# DaVinci Resolve WakaTime

2 scripts to send WakaTime heartbeats, the free version of DaVinci Resolve does not allow you to use the `DaVinciResolveScript` API, BUT we can watch changes in AppData folder.

However, I haven't tested the paid version, I don't have the money for that. If you have paid version, you can also use free version.

Pull Requests and Issues are welcome!

## Setup

Clone the repo (or download [DaVinci Resolve WakaTime](/free/davinci-hackatime.py)):

```
git clone https://github.com/LucasHT22/davinci-resolve-wakatime.git
```

In `davinci-hackatime.py`, change `WAKATIME_API_KEY` to your WakaTime API Key and change `WATCH_FOLDER`.


Your file path should look like something like this:

### Windows
```
C:\\Users\\{USER}\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Resolve Project Library\\Resolve Projects\\Users\\guest\\Projects\\{PROJECT_NAME}
```

### Mac
```
\\Users\\{USER}\\Library\\Application Support\\Blackmagic Design\\DaVinci Resolve\\Support\\Resolve Disk Database\\Resolve Projects\\\Users\\guest\\Projects\\{PROJECT_NAME}
```

Make sure there is a `Project.db` inside, if you just created the project in DaVinci Resolve, it may not appear, add something to the timeline and it should work.

> Don't forget to use `\\` for file path! \ or / won't work.

## Compatibility

I (Lucas) have a Windows machine, tests are welcome!

| OS | Tested |
| -- | ------ |
| Windows | ✅ |
| Mac | |

## How It Works?

1. Script look for changes in `WATCH_FOLDER` every 30 seconds
2. If change is detected, a WakaTime heartbeat is sent
3. Done!

<video src="assets/davinci-wakatime.mov" width="320" height="240" controls></video>

## Main References

- [WakaTime Developers](https://wakatime.com/developers)
- [Resolve Scripting Documentation - Blackmagic Design Forum](https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=78611)
- [Python3 DaVinci Resolve 19 Console Not Found - alexthecreative](https://alexthecreative.com/python3-davinci-resolve-19-console-not-found/)
- [Scripting in the free version? - Blackmagic Design Forum](https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=113252)
- [Where Does Davinci Resolve Save Projects and Project Files? - contentcreatortemplates](https://www.contentcreatortemplates.com/learn/where-does-davinci-resolve-save-projects)
- [Scripting: DaVinciResolveScript module not found - Blackmagic Design Forum](https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=137340)
