sudo ln -s /home/mint/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default 
sudo /etc/init.d/nginx restart
