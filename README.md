# user_profile


## setup virtualenv

```sh
pip install virtualenv
virtualenv .venv
```

## install requirements

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## running django management commands & usage

```sh
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```