A project utilizing the internal wifi to connect to an access point for internet, and an external adapter for pwning.
We can't let Flipper have all the tricks. ;) . There's lots of of options for this like running Wifite, Reaver or EvilTwin...

My goal was to create a pwnagotvhi with two options for command and control. Bluetooth and WiFi since I do not use a screen.
This is basically my setup notes with a few added comments, since I restarted from scrath so many times and I'm down with copy, paste.

My hardware is a Pi Zero W, RTC, A rando GPS module I had laying around from a drone project, A Cable Matters WiFi adapter (Panda),
A shutdown button scavenged from a old computer case and an extra LED. 

I used WinSCP as soon as I could ssh in for file manipulation. Ext2Fsd is a driver for windows to be able to read ext2 etc Linux
volumes so you can plug your sd card into your pc for file transfers also.


*** Caveats Aplenty *** :dragon:

My OS flavor is https://github.com/jayofelony/pwnagotchi-torch but 'should' work on others.

Some plugins have caused issues or have behaviour that changes files needed for this project. Ones that I know of are
fix_services and fix_brcmf_plugin. They should be disabled and a reboot before continuing. Look through any plugins code before enabling
as any that mess with specific adapter names or the internal wifi module may break things.

My GPS module 'just worked' after the steps contained herein. I had problems with GPSD so I do not use it or know how it will afect
your GPS. My module was a four wire version and most others should work the sane. I would reccommend something like a BN-180 or similiar
(the size of a quarter). No need to spend more on Pi specific HATs. I enabled the 'GPS' plugin.

I have tried to add some troubleshooting options but as hardware and software differences are limitless, buyer beware.

Here are some addition repos I have used in this project:

https://github.com/JD-2006/pwnagotchi-Pi-Zero-W-RTC

https://github.com/JD-2006/pwnagotchi-plugins_JD-2006

https://github.com/Howchoo/pi-power-button

Thanks for the inspiration:

https://github.com/unagisan69/pwnagotchi-external-wifi-plugin
