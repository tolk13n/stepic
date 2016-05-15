sudo rm /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo rm /etc/gunicorn.d/ask.conf
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/ask.conf
sudo /etc/init.d/gunicorn restart
