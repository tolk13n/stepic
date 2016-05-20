sudo rm /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default

sudo pip install django --upgrade
sudo pip install pymysql

sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE DATABASE db_ask;"
mysql -uroot -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'django';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON db_ask.* TO 'django'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"

rm -rf /home/box/web/ask/qa/migrations/
python manage.py makemigrations qa
python manage.py migrate qa

sudo rm /etc/gunicorn.d/ask.conf
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/ask.conf
sudo /etc/init.d/gunicorn restart
