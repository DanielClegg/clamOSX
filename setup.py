#!/usr/bin/env python
from __future__ import print_function

import shutil
from os import path, getenv
from subprocess import call

def copy_conf(name, dest):
    print("Copying {}... ".format(name), end="")
    shutil.copy2("./{}".format(name), dest)
    print("done")

print("Installing clamAV for launchd")

if path.exists('/usr/local/bin/freshclam') and path.exists('/usr/local/bin/clamscan'):
    print("ClamAV installed")
else:
    print("Can't find freshclam or clamscan")
    if path.exists('/usr/local/bin/brew'):
        ans = raw_input("Homebrew is installed, do you want me to install ClamAV? (y/n) ")
        if str(ans).lower().startswith('y'):
            call(["brew", "install", "clamav"])

if path.exists('/usr/local/etc/clamav/freshclam.conf'):
    ans = raw_input("freshclam.conf already exists, do you want to overwrite with the repos version? (y/n) ")
    if str(ans).lower().startswith('y'):
        copy_conf("freshclam.conf", "/usr/local/etc/clamav/")
else:
    copy_conf("freshclam.conf","/usr/local/etc/clamav/")

home_dir = getenv("HOME")

launchagents_dest_dir = home_dir + "/Library/LaunchAgents/"

copy_conf("freshclam.plist", launchagents_dest_dir)
copy_conf("clamscan.plist", launchagents_dest_dir)

