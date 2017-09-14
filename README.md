# clamOSX
Launchd plist file for running clamscan anti virus and freshclam automatically on OSX

## Requirements
ClamAV http://www.clamav.net/downloads

### Installation (auto-ish)

just run ```setup.py``` from the terminal, then log out and back in.


### Installation (manual)
Either download directly from http://www.clamav.net/downloads or better use 
```brew install clamav``` see here for [Installing Brew](https://brew.sh)

You can find a minimal ClamAV config in the repo ```freshclam.conf``` just copy that to ```/usr/local/etc/clamav/```
```clamscan``` and ```freshclam``` should in installed in ```/usr/local/bin/```

Copy both ```clamscan.plist``` and ```freshclam.plist``` to ```~/Library/LaunchAgents/```

Now just log out and log back in and both should loaded and ready to run

You can check to see if there are installed by ```launchctl list | grep local``` which should return something like

```
-	0	local.clamscan.job
-	0	local.freshclam.job
```

### Loggging

Both services log to ```/Users/Shared/freshclam.log``` and ```/Users/Shared/clamscan.log```

### Configuration

```clamscan``` is confgiured to do a recursive scan on the users home directory ```~/``` this can be easily changed by editing the ```clamscan.plist``` and changing line 11

```		<string>/usr/local/bin/clamscan -r $HOME</string>``` and replacing the ```$home``` with whatever directory you want to check


```freshclam``` is set to update definitions once an hour but can be easily changed on line 16 

```	<integer>3600</integer>``` the value is in seconds
