# Flatbond_rest

Flask application for flatbond REST API.

## Getting Started

These instructions will cover usage information and for the docker container 

### Prerequisities


In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

```shell
docker build -t flatbond_rest_docker:latest .
docker run -d -p 5000:5000 flatbond_rest_docker:latest
```
