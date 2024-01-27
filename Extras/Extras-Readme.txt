auto-connect.py -
This script reads your cracked wifi potfile and adds the AP's to your wpa_supplicant.conf
file so you will automatically connect. Need wpa-sec plugin enabled. Change potfile location to yours.
I have this run once after reboot with:
Make the script executable (if not already) by running:
chmod +x monitor_file.py

Open the crontab configuration:
crontab -e

@reboot sudo /usr/bin/python3 /root/auto-connect.py

inky.py - 
Here is my version of /usr/local/lib/python3.9/dist-packages/pwnagotchi/ui/hw/inky.py
that shows all of the ui on a 16:9 tv. Change display in config.toml.
