### News Feeder
#### Collect news from [newsapi](https://newsapi.org/)

---

### Setup

---

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/russell310/news_feeder.git .
$ cd news_feeder
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies copy `.env` and change with your settings:
```sh
(venv)$ cp .env.example .env
```

After adding `.env` migrate to database
```sh
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
```

Import source list from newsapi
```sh
(venv)$ python manage.py load_sources
```

Now start the development server
```sh
(venv)$ python manage.py runserver
```

Alongwith `runserver` open separate two terminal for celery and celery beat
```sh
(venv)$ celery -A news_feeder worker --pool=solo -l info
(venv)$ celery -A news_feeder beat -l INFO
```

Now navigate to [http://localhost:8000/](http://localhost:8000/)
