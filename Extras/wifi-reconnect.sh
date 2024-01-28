#!/bin/bash 
 
SSID=$(/sbin/iwgetid --raw) 

if [ -z "$SSID" ] 
then 
    echo "`date -Is` WiFi interface is down, trying to reconnect" >> /home/pi/wifi-log.txt
    sudo ifconfig wlan1 down
    sleep 10
    sudo ifconfig wlan1 up 
fi 

echo 'WiFi check finished'
