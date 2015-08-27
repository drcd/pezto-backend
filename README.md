# Pezto

A pastebin clone, running Django as backend and Angular as frontend.

# Credits

Oliver Stenkilde (@stenkilde) - Concept, Frontend

Younes Zakaria (@drcd) - Backend

# Requirements

- Python 3
- virtualenv

# How to run dev-server

It should be noted that this is *not* the recommended way to run the server on production environments.
Please refer to the *How to run production server* section for more info. (coming soon)

Go to the root of the GIT repo, and run `virtualenv env` to start a virtual environment.

Next, activate the virtual environment:

Windows: `env/scripts/activate` or `env\scripts\activate`
OS X / Linux / UNIX: `env/bin/activate`

When that's done, you should see an `(env)` prefix on your terminal.

Next, run `pip install -r requirements.txt`.

*If this fails*, please refer to the *PIP Troubleshooting* section, as there has been known problems to this step regarding bcrypt.

After the PIP requirements has been installed, change the directory to /pezto: `cd pezto`

By default, the dev server uses SQLite as a development database, so no further configuration is needed for the database.

Run the following commands:
```
./manage.py makemigrations
./manage.py migrate
```

If you're running on Windows, you might replace `./manage.py` with `python manage.py` or `python3 manage.py`, if the first doesn't work.

Now you can run the development server by running `./manage.py runserver`. :)

When you're finished, you can disable the virtual environment by running `deactivate`. Remember to reactivate your virtualenv to run the server again! Otherwise, the program will not recognize the required packages.

# PIP Troubleshooting

If the PIP requirements.txt installation fails, try to install the requirements "manually" (sequentially).
Make sure that your virtualenv is activated!
```
pip install bcrypt
pip install django
pip install hashids
pip install mysqlclient
```

# Frontend

All static files (JS, CSS, etc), are stored in the /static directory in /pezto. The index.html file is stored in /templates.

TODO: Explain more about frontend, blah
