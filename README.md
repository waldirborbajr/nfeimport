## config.ini
Create a file called config.ini with the folowing content

`[mysql]

`#

`# DEV

`#

`host = database.ip.address

`database = database.password

## Virtual Environment

1. easy_install pip
2. pip install virtualenv

3. virtualenv --python=python3 venv // python3 -m venv venv/
4. source venv/bin/activate
5. deactivate

6. pip freeze --local > requirements.txt
7. pip install -r requirements.txt
