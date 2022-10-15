## Launching the project
- ```git clone https://github.com/navik86/test_task.git```
- ```cd web_app/lab_app```
- ```mv .env.example .env```
- ```cd ..```
- ```docker-compose up -d --build```
- ```docker-compose exec lab_app python manage.py migrate --noinput```

## Get endpoints 
```http://127.0.0.1:8000/swagger/```

![Alt text](endpoints.jpg?raw=true "Optional Title")