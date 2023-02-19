sudo cp host-status.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl host-status.service
sudo systemctl enable host-status.service
sudo systemctl status host-status.service
mv host-status /usr/bin/