pip install -r requirements.txt
apt-get -y update
apt-get install -y wget
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install -y ./google-chrome-stable_current_amd64.deb
gunicorn --bind :8000 --workers 1 --threads 8 --timeout 0 app:app