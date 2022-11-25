## Configuration

A list of all environment variables required to run application is stored in '.env.dev_example',
After filing in correct values, environment variables can be loaded by updating environment with values from file with:
`set -o allexport; . .env; set +o allexport'

# Not implementet yet
## Production

### 1. Running db migrations
If necessary, run migrations:
```bash
shovel migrate_db
```
## 2. Loading seed data
If necessary, load seed data:
```bash
shovel load_data
```


### Docker-compose based
#### Building

```bash
docker-compose build
```

#### Runnig

```bash
docker-compose up
```

### Bare metal based
#### 1. Launch database
```bash
docker run -p 5432:5432 -e POSTGRES_USER=blog -e POSTGRES_PASSWORD=blog -e POSTGRES_DB=blog postgres:12
```

#### 2. Configuration
```bash
set -o allexport; . .env; set +o allexport
```

#### 3. Launch api
```
shovel run_api_dev
```
