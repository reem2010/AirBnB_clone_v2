#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
apt-get -y update
apt-get -y install nginx
service nginx start
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
if [ -e "/data/web_static/releases/test/index.html" ]
then
	touch /data/web_static/releases/test/index.html
fi
echo "for test" > /data/web_static/releases/test/index.html
if [ -L "/data/web_static/current" ]
then
	rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i 's/server_name _;/&\n	location \hbnb_static {\n		alias /data/web_static/current/;\n	}/' /etc/nginx/sites-available/default
service nginx restart
