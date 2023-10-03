## Set up and Run the Application

1. Clone the repository and navigate to the project directory:

```
https://github.com/Samandar587/alltrip-task.git with HTTPS
git@github.com:Samandar587/alltrip-task.git with SSH
cd HealthTrackAPI
```

2. Create and activate a Python virtual environment:

```
python3 -m venv env
source env/bin/activate
```

3. Create a .env file in the root directory of the project and add the following environment variables:

```
SECRET_KEY='django-insecure-^e7*rn(^ezdia__8+g17*(kxt!2(x12ib*oc!dx+b6w(kg1(d^'
DB_NAME=database_name
DB_USER=database_user
DB_PASSWORD=database_password
DB_HOST=database_host
DB_PORT=database_port

```


4. Install the required packages:

```
pip install -r requirements.txt
```


5. Run database migrations:

```
python manage.py migrate
```

6. Create a superuser account:

```
python manage.py createsuperuser
```

7. To login, send a POST request to http://localhost:8000/alltrip/api/login with appropriate user credentials


