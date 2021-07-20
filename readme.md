# How to start Article Service

PLEASE DOWNLOAD AND INSTALL DOCKER AND DOCKER-COMPOSE BEFORE USING THE APP


## Step 1
Create environment file i.e. `.env` in root folder and add values in following fields
```
POSTGRES_USER=<add-whatever-username-you-like>
POSTGRES_PASSWORD=<add-whatever-password-you-like>
POSTGRES_DB=<add-whatever-database-name-you-like>
```

## Step 2
Create another environment file i.e. `api.env` in root folder and add value in following field
```
DATABASE_URL=postgresql://POSTGRES_USER:POSTGRES_PASSWORD@db/POSTGRES_DB
```
NOTE: Remember this username and password is same you used in step 1


## Step 3
Run following command to download and build image for API

- Build images ```docker-compose build```
- Start docker and put the process in back ```docker-compose up -d```
- Check database log ```docker-compose logs db ```
- Check API log ```docker-compose logs service```
- Check test log ```docker-compose logs test-service```

( Both DB and Service should be running )


## Step 4
Now go to http://localhost:5000/docs to see API doc


Once All image build you can run following command to run the test again
```
docker-compose run test-service python -m pytest
```
