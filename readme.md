# Ubuntu Fresh Build Instructions
The following should contain all the instructions neccesary to build an Ubuntu docker image with MySQL, Postgres and Timescale


## Building
in the `/ubuntu-docker-build` folder run

`docker build . --tag benchmark_main`


## Running
Run with docker-compose:
`docker-compose up -d`

Run manually
`docker run -dit benchmark_main:latest`

Always quit with ctrl+c, ctrl+z will leave hanging containers

## Running with Docker Compose
The application will typically be run with docker-compose

## Managing Running Containers
List running containers:  `docker ps`

## Connecting to Containers SSH
`docker exec -it`
To get BASH shell: `/bin/bash`

## Troubleshooting
* Delete parent images, then rebuild them


# Database Administration
Login to postgres console: `psql -U postgres -h localhost`


# Benchmarkdb Repository


## MySQL
[localhost:8081](http://localhost:8080)
server(adminer): `mysql`
server(from host): `localhost:3307`
username: `root`
password: `edward`

## Postgres
host: `localhost:5432`
user: `postgres`

## Timescale
host: ``
user: ``