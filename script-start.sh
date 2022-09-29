sudo apt-get update -y
sudo apt-get install -y wget
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
sudo apt install python3-pip -y
sudo pip3 install -r requirements.txt
sudo apt-get install nginx -y
sudo apt-get install gunicorn -y
sudo cp flaskapp.conf /etc/nginx/sites-enabled
sudo service nginx restart
gunicorn app:app

# sudo apt-get -y update
# sudo curl -O https://bootstrap.pypa.io/get-pip.py
# sudo python3 get-pip.py
# sudo apt install -y gunicorn
# sudo pip install -r requirements.txt
# sudo apt-get install -y wget
# wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
# gunicorn --bind :8000 --workers 1 --threads 8 --timeout 0 app:app