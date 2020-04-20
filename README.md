# LCD Covid Tracker with a Raspberry Pi

Components:
* Raspberry Pi (any model)
* LCD1602
* Lots of jumper wires
* 1 or 2 potentiometers (one required for adjusting screen contrast, one optional for adjusting screen brightness)
* Follow [this tutorial](https://www.mbtechworks.com/projects/drive-an-lcd-16x2-display-with-raspberry-pi.html) to setup the LCD1602

Dependencies:
* RPi.GPIO (should come pre-installed in a Raspbian system)
* requests

Starting the screen:

```bash
python3 main.py
```

## Configure the script to run as a systemd service

Instead of running the code manually, we can let [systemd](https://en.wikipedia.org/wiki/Systemd) manage the process for us. Systemd is the system service manager for a bunch of GNU/Linux systems including Raspbian, Debian and Ubuntu. 

Use your favourite text editor to create the systemd unit file with sudo, and lets call the service 'lcd':

```bash
sudo vim /etc/systemd/system/lcd.service
```

Copy the following into the file, make sure to replace <YOUR USERNAME> with your username and <PATH TO WORKING DIRECTORY> with the absolute path to this repo.

```
[Unit]
Description=LCD Display
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=<YOUR USERNAME>
WorkingDirectory=<PATH TO THE WORKING DIRECTORY WHERE main.py IS LOCATED>
ExecStart=python3 main.py

[Install]
WantedBy=multi-user.target
```

Finally, reload the systemd daemon so systemd recognise our new config file:

```bash
sudo systemctl daemon-reload
sudo systemctl enable lcd
sudo systemctl start lcd
```

To stop this process we can run 

```bash
sudo systemctl stop lcd
```

And to disable it from running at startup,

```bash
sudo systemctl disable lcd
```
