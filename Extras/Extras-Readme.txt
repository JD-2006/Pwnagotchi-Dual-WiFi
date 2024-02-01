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


wifi-reconnect.sh -
If your internet wifi adapter keeps disconnecting from your AP.
$ sudo chmod +x /usr/local/bin/wifi-reconnect.sh

$ sudo su

Edit crontab to let it check WiFi connection every minute:
# echo '* * * * * root bash wifi-reconnect.sh' >> /etc/crontabcrontab'

This would check every 5 minutes:
# echo '*/5 * * * * root bash wifi-reconnect.sh' >> /etc/crontabcrontab'

After a an hour or so check /var/mail/mail. If you see errors like:
/usr/local/bin/wifi-reconnect.sh: line 2: $'\r': command not found
/usr/local/bin/wifi-reconnect.sh: line 5: $'\r': command not found
/usr/local/bin/wifi-reconnect.sh: wifi-reconnect.sh: line 7: syntax error near unexpected token `$'{\r''
/usr/local/bin/wifi-reconnect.sh: wifi-reconnect.sh: line 7: `log() 

$ sudo apt-get install dos2unix

$ sudo dos2unix /usr/local/bin/wifi-reconnect.sh

Edited from: https://github.com/carry0987/Raspberry-Pi-Repo/blob/master/Auto-WiFi-Reconnect/wifi-reconnect.sh
