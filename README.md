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

```bash
python3 -m pip install -r requirements.txt
```

Starting the screen manually:

```bash
python3 main.py
```

## Configure the script to run as a systemd service

Instead of running the code manually, we can let [systemd](https://en.wikipedia.org/wiki/Systemd) manage the process for us. Systemd is the system service manager for a bunch of GNU/Linux systems including Raspbian, Debian and Ubuntu. I have provided a unit-file template with a install(uninstall) script. This adds a user unit file and does not require sudo access.

To install the daemon and start running it in the background

```bash
./install.sh
```

To uninstall the daemon and stop the service

```bash
./install.sh uninstall
```
