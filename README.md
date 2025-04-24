> [!WARNING]
> "Paid" version is still a Work In Progress, if you have paid version, you can also use free version.

# DaVinci Resolve Wakatime

2 scripts to send WakaTime heartbeats, the free version of DaVinci Resolve does not allow you to use the `DaVinciResolveScript` API, BUT we can watch changes in AppData folder.

However, I haven't tested the paid version, I don't have the money for that. If you have paid version, you can also use free version.

Pull Requests and Issues are welcome!

## Setup

Clone the repo (or download .zip):

```
git clone https://github.com/LucasHT22/davinci-resolve-wakatime.git
```

In `davinci-resolve.py`, change WAKATIME_API_KEY to your WakaTime API Key and change file path.


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

> Don't forget to use \\ for file path! \ or / won't work.

## Compatibility

I (Lucas) have a Windows machine, tests are welcome!

| OS | Tested | Version |
| -- | ------ | ------- |
| Windows | ✅ | Free |
| Mac | | Free |

## Main References