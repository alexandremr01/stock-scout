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

First, login in heroku with 

```bash
heroku login
```

Then, deploy to the remote with

```bash
git push heroku main
```

Production uses `Dockerfile.prod`.
