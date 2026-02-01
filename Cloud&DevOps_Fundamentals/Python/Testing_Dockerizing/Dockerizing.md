# Index

# Dockerizing

## Packaging for python application

1. Python’s native packaging (wheel, archive).
2. System Package, RPM or DEB .
3. Conda Packagе.
4. Freezers (PyInstaller, PyOxidize).
5. Container image (Docker)
6. Virtual machines
7. Hardware (drag and plug).

## Dockerizing python application

__Dockerfile__

```docker
# set base image (host OS)
FROM python:3.8
# set the working directory in the container
WORKDIR /code
# copy the dependencies file to the working directory
COPY requirements.txt .
# install dependencies
RUN pip install -r requirements.txt
# copy the content of the local src directory to the working directory
COPY src/ .
# command to run on container start
CMD [ "python", "./server.py" ]
```

__Run application__

```shell
$ docker build -t my-python-app .
$ docker run -it --rm --name my-running-app my-python-app
```

## docker-compose

![[docker-compose.png]]

## Base Python image

- ***-slim**. This image generally only installs the minimal packages needed to run your particular tool. It requires Unix knowledge to configure and extend it according to application needs.
- ***-alpine**. Alpine images are based on the Alpine Linux Project, which is an operating system that was built specifically for use inside containers. For a long time, these were the most popular image variations due to their tiny size.However, some teams are moving away from alpine because these images can cause compatibility issues that are hard to debug. This image is the most highly recommended if space is a concern.
- full official image: **python:x.x.x**. These images are based on the most recent stable Debian operating system release. It is good to use them at the start of the project when trying to get a project up and running quickly and when you are not concerned about the size of the resulting image. The full image is the safest choice.

# Next Notes

