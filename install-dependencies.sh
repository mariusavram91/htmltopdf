!#/bin/sh
wget http://download.gna.org/wkhtmltopdf/0.12/0.12.2/wkhtmltox-0.12.2_linux-trusty-amd64.deb
dpkg -i wkhtmltox-0.12.2_linux-trusty-amd64.deb
apt-get install xfonts-75dpi
rm wkhtmltox-0.12.2_linux-trusty-amd64.deb
