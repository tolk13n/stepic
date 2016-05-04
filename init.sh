sudo rm /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default 
sudo ln - s /home/box/web/hello.py /usr/local/lib/python3.4/hello.py 
sudo /etc/init.d/nginx restart
gunicorn -b 0.0.0.0:8080 -D hello

