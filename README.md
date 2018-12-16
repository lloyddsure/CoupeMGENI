# CoupeMGENI



```bash
apt-get update
apt-get install python3
apt-get install pip

pip install virtualenv
virtualenv venv
source venv/bin/activate

pip install -r lib.txt
cd coupe_mgeni
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
