!#/bin/sh
apt-get update
apt-get -y install xvfb
apt-get -y install xfonts-75dpi
wget http://download.gna.org/wkhtmltopdf/0.12/0.12.2/wkhtmltox-0.12.2_linux-trusty-amd64.deb
dpkg -i wkhtmltox-0.12.2_linux-trusty-amd64.deb
rm wkhtmltox-0.12.2_linux-trusty-amd64.deb
