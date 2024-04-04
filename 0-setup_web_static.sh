#!/usr/bin/env bash

# Script to set up web servers for deployment of web_static

# Install Nginx if not already installed
if ! dpkg -l nginx &> /dev/null; then
    apt-get -y update
    apt-get -y install nginx
fi

# Create necessary directories if they don't exist
mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create symbolic link, remove if already exists
rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership of /data/ to ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sed -i "/server_name _;/a $config" /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart

exit 0
