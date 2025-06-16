# DaVinci Resolve WakaTime

A script to send Wakatime heartbeats from Krita, the free and open source illustration software. Forked from LucasHT22's wonderful DaVinci Resolve script that does the same thing, watching a folder for changes.

Pull Requests and Issues are welcome!

## Setup

Clone the repo (or download [Krita WakaTime](/free/krita-wakatime.py)):

```
git clone https://github.com/scherepi/krita-wakatime.git
```

In `krita-hackatime.py`, change `WAKATIME_API_KEY` to your WakaTime API Key and change `WATCH_FOLDER`.


Your file path should look like something like this:

### Windows
```
TBD
```

### Mac
```
TBD
```

> Don't forget to use `\\` for file path! \ or / won't work.

## Compatibility

Tests incoming!

| OS | Tested |
| -- | ------ |
| Windows |  |
| Mac | |

## How Does It Work?

1. The script looks for changes in `WATCH_FOLDER` every 30 seconds
2. If a change is detected, a WakaTime heartbeat is sent
3. Done!

<video src="assets/davinci-wakatime.mov" width="320" height="240" controls></video>

## Main References

- [WakaTime Developers](https://wakatime.com/developers)
