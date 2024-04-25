# Find Electron Apps on Linux

## Description
A simple Python script to list Electron applications in specific directories on Linux-based systems. <br/>

---

## Note
In summary, this script searches designated directories where applications are commonly installed, such as `/usr/share` or `/opt`, as well as the `/home` directories where users may choose to install apps.  <br/><br/>
Basically, this script adopts a similar approach to the previous PowerShell script by navigating through common directories to locate Electron-related files. While it may not cover all potential paths, at least it can provide an initial step in identifying Electron-based applications within a Linux environment. <br/><br/>
As a note, the determination of the application name (App Name) still relies on the directory name, occasionally resulting in inaccurate output if users utilize a directory name different from the application name.<br/>

---

## How to use

`python3 find-electron-on-linux.py`

Sample output: <br/>

```
____________________________________________________________________________________________________
App Name                       Location
====================================================================================================
AdvancedRestClient             /opt/AdvancedRestClient
WordPress.com                  /opt/WordPress.com
code                           /usr/share/code/resources/app
File-Manager                   /home/yoko/Documents/File-Manager/node_modules/electron/dist/resources
samplehandling                 /home/yoko/Documents/samplehandling/node_modules/electron/dist/resources
super-productivity             /home/yoko/Documents/super-productivity/node_modules/electron/dist/resources
portElectron                   /home/yoko/Documents/portElectron/node_modules/electron/dist/resources
portElectron                   /home/yoko/Documents/portElectron/dist/linux-unpacked
```

---

## Additional Information: 
* No license. <br/>
* Free to use and modify - for good purposes.

