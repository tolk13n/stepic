sudo rm /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default 
sudo /etc/init.d/nginx restart
gunicorn --config /home/box/web/etc/test.py hello -D
