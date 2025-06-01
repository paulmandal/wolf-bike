# Do a fresh RPi Image

# Install LedFX

https://docs.ledfx.app/en/latest/installing.html#raspberry-pi-installation

# Set up WiFi AP

sudo nmcli con add con-name WiFiAP type wifi mode ap ifname wlan0 ssid "wolf-bike-leds" -- wifi-sec.key-mgmt wpa-psk wifi-sec.psk "xxxxxx" ipv4.method shared ipv4.address 192.168.1.1/24 ipv4.gateway 192.168.1.1
sudo nmcli con up WiFiAP

# Install WLED on Devices

https://kno.wled.ge/basics/install-binary/
