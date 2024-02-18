#!/bin/bash

# Delete existing data/files and create new folder
sudo rm -rf /var/www/
sudo mkdir -p /var/www/langchain-app 

# Move all files and hidden files
# The '2>/dev/null' part is to suppress error messages for when 'mv' tries to move non-existent hidden files
mv env .env
sudo sh -c 'mv /home/ubuntu/* /home/ubuntu/.* /var/www/langchain-app/ 2>/dev/null'

# Install application dependencies from requirements.txt 
# cd /var/www/langchain-app/
# sudo apt-get install -y python3 python3-pip
# sudo pip3 install -r /var/www/langchain-app/requirements.txt

# echo "starting gunicorn"
# sudo pkill gunicorn
# gunicorn --workers 3 --bind unix:myapp.sock  server:app &

# # Update and install Nginx if not already installed
# if ! command -v nginx > /dev/null; then
#     echo "Installing Nginx"
#     sudo apt-get update
#     sudo apt-get install -y nginx
# fi

# # Configure Nginx to act as a reverse proxy if not already configured
# if [ ! -f /etc/nginx/sites-available/myapp ]; then
#     sudo rm -f /etc/nginx/sites-enabled/default
#     sudo bash -c 'cat > /etc/nginx/sites-available/myapp <<EOF
# server {
#     listen 80;
#     server_name _;

#     location / {
#         include proxy_params;
#         proxy_pass http://unix:/var/www/langchain-app/myapp.sock;
#     }
# }
# EOF'

#     sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled
#     sudo systemctl restart nginx
# else
#     echo "Nginx reverse proxy configuration already exists."
# fi

# Start Gunicorn with the Flask application
# Replace 'server:app' with 'yourfile:app' if your Flask instance is named differently.
#sudo mv env .env  # Env file
# gunicorn --workers 3 --bind 0.0.0.0:8000 server:app &


