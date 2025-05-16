#!/bin/bash
sudo apt update
sudo apt install -y ffmpeg python3 python3-pip asterisk unzip
pip3 install -r requirements.txt
echo "Installation complete. Add your SMTP app password in config/settings.json."
