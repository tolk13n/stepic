mysql -uroot -e "CREATE DATABASE db_ask;"
mysql -uroot -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'django';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON db_ask.* TO 'django'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
