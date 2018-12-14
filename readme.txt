#################################################
#                                               #
#                     README                    #
#                                               #
#################################################


run
    sudo apt install postgresql
    sudo -i -u postgres
    psql
    CREATE DATABASE updfdb;
    \q    

clone repository
https://github.com/JonathanFarinloye/minipdfsite.git

install virtual environment

run
    virtualenv myvenv
    source myvenv/bin/activate
    pip install django
    pip install psycopg2-binary
    pip install Pillow

move into repository directory

run
    python manage.py runserver
    if any_errors:
        dm me
    else:
        continue
    

Open browser
    localhost:8000
