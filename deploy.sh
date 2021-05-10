docker build -f Dockerfile.prod --tag registry.heroku.com/stock-scout/web .
docker push registry.heroku.com/stock-scout/web
heroku container:release web -a stock-scout