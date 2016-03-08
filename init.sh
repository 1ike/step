sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gun.conf   /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/ask.conf   /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql restart

#  rm -rf /home/box
#  git clone https://github.com/discodanser/step.git /home/box
#  bash /home/box/web/init.sh

#  sudo /etc/init.d/nginx restart
#  nano web/etc/nginx.conf
#  wget localhost/uploads/trest.js

#  gunicorn -b 0.0.0.0:8000 ask.wsgi
#  curl '127.0.0.1:8080/?x=1&y=2&z=3'


#  mysql -uroot -e "create database stepic"

#  GRANT ALL ON stepic.* TO 'admin'@'localhost' IDENTIFIED BY '123';
#  python manage.py syncdb