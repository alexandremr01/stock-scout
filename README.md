# Stock Scout

# Running in development

Run in 3 different terminals.

```bash
docker-compose up db
docker-compose up front
docker-compose up back
```

Now you can view the django admin site at `0.0.0.0:8000/admin`, and the vue application at `localhost:8080`. 

# Deploy

Deploy is automatic with pushes to main. Production uses `Dockerfile.prod`.

To view in production, access `https://stock-scout.herokuapp.com/`

