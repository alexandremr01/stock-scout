# Stock Scout

This project was an assignment for CES-22 course (OOP) at Aeronautics Institute of Technology, São Paulo, Brazil.

# Running in development

Run in 3 different terminals.

```bash
docker-compose up db
docker-compose up front
docker-compose up back
```

Now you can view the django admin site at `0.0.0.0:8000/admin/`, and the vue application at `localhost:8080`. 

# Running migrations

```bash
docker-compose exec back bash
python manage.py migrate
```

# Deploy

Deploy is automatic with pushes to main. Production uses `Dockerfile.prod`.

To view in production, access `https://stock-scout.herokuapp.com/`
