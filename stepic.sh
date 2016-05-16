sudo pip install django --update
sudo pip install pymysql
rm -rf /home/box/web/ask/qa/migrations/
python manage.py makemigrations qa
python manage.py migrate qa

