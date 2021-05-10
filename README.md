# Stock Scout

# Running in development

Run in 3 different terminals.

```bash
docker-compose up db
docker-compose up front
docker-compose up back
```

Now you can view the production Vue application at `127.0.0.1:8000`, and the development application at `localhost:8080`. 

# Deploy

Deploy is automatic with pushes to main. Production uses `Dockerfile.prod`.
