# Stock Scout

Next, change into the `frontend` directory, install the Node dependencies, build the Vue.js application, and run the Vue dev server. I use [Yarn](https://yarnpkg.com/en/):

```bash
cd frontend
yarn install
yarn build
yarn serve
```

Finally, run the Django development server in a different terminal:

```bash
./manage.py runserver
```

Now you can view the production Vue application at `127.0.0.1:8000`, and the development application at `localhost:8080`. Both will use the local Django instance as the API.

Thanks for visiting!
