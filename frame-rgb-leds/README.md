# Do a fresh RPi Image

# Install PyEvn

https://github.com/pyenv/pyenv/wiki#suggested-build-environment

# Set up WiFi AP

nmcli con add con-name WiFiAP type wifi ifname wlan0 mode ap ssid "wolf-bike-leds" -- 802-11-wireless.band bg wifi-sec.key-mgmt wpa-psk wifi-sec.psk "xxxxxx" ipv4.method shared ipv4.address 192.168.1.1/24 ipv4.gateway 192.168.1.1
nmcli con up WiFiAP

# Set up Music Strip LED Control

https://github.com/TobKra96/music_led_strip_control/wiki/Installation-Guide#configure-music-led-strip-control

You will need to set up a virualenv in the /share/music_led_strip_control/server directory and copy run.sh there

# Modify the nodemcu file here and set up an IP Address for each device and the SSID/WiFi password
