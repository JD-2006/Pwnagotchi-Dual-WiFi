#!/bin/bash

# Check if WiFi interface is already up
if ifconfig wlan1 | grep -q "UP"; then
    SSID=$(/sbin/iwgetid --raw)
    if [ -z "$SSID" ]; then
        echo "`date -Is` WiFi interface is already up, but not connected to a network. Trying to reconnect." >> /home/pi/wifi-log.txt
        sudo ifdown wlan1
        sleep 20
        sudo ifup wlan1
    else
        echo "`date -Is` WiFi interface is already up and connected to SSID: $SSID. No action needed." >> /home/pi/wifi-log.txt
    fi
else
    echo "`date -Is` WiFi interface is down, trying to reconnect" >> /home/pi/wifi-log.txt
    sudo ifdown wlan1
    sleep 10
    sudo ifup wlan1
fi

echo 'WiFi check finished'
