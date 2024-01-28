#!/bin/bash 
 
SSID=$(/sbin/iwgetid --raw) 

if [ -z "$SSID" ] 
then 
    echo "`date -Is` WiFi interface is down, trying to reconnect" >> /home/pi/wifi-log.txt
    sudo ifdown wlan1
    sleep 10
    sudo ifup wlan1
fi 

echo 'WiFi check finished'
