# Index

- [[#Docker Hub and Registry]]
- [[#Docker services]]
	- [[#First step]]
	- [[#Second step]]
	- [[#Third step]]
	- [[#Example]]
	- [[#Example]]
- [[#Docker commands]]
	- [[#Docker stop, Docker start, Docker exec]]
	- [[#Docker exec]]
	- [[#Docker commit]]
- [[#Working with docker daemon, docker hub and registry commands]]
- [[#Getting the docker version and information]]
- [[#Working with docker hub and registry]]
- [[#Configuring the docker daemon]]
	- [[#Example]]
- [[#Creating docker images]]
- [[#Docker commands for working with images]]
- [[#Working with docker images]]
- [[#working with images info]]
	- [[#Example]]
- [[#Working with the image layers]]
- [[#Working with a dockerfile]]
	- [[#Example]]
- [[#Next Notes]]
# Docker Hub and Registry

## Docker services

Let's have a closer look at the Docker Services installation. The Docker daemon binds to a UNIX socker __/var/run/docker.sock__, which is owned by __root:docker__.

### First step

The Docker Engine client is launched using the **docker** tool with the **run** option running a new container. The bare minimum the Docker client needs to tell the Docker daemon to run the container is:

- What Docker image to build/create the container from (e.g., Ubuntu).
- The command you want to run inside the container when it is launched (e.g., /bin/bash).

### Second step

When the command is run, Docker Engine does the following:

- Pulls the Ubuntu image
- Creates a new container
- Allocates a filesystem and mounts a read-write layer
- Allocates a network/bridge interface
- Sets up an IP address

### Third step

After that, you can manage your container, interact with your application, and stop and remove the container when needed.

**"-i -t"** is used precisely to capture and provide allocation output.

	
    `docker run -ti ubuntu bash`

Running the **docker run** command, you need to provide the service that will be run on the image. The following example shows that bash is specified. It is unable to find the Ubuntu image locally, so it searches remotely. To make the command run in interactive mode, provide **TTY (-t key)** and, at the same time, specify interactive mode **(-i key)**.

### Example

```
    bash > docker run ubuntu bash
    Unable to find image 'ubuntu:latest' locally
    latest: Pulling from library/ubuntu
    3ff22d22a855: Pull complete 
    e7cb79d19722: Pull complete 
    323d0d660b6a: Pull complete 
    b7f616834fd0: Pull complete 
    Digest: sha256:5d1d5407f353843ecf8b16524bc5565aa332e9e6a1297c73a92d3e754b8a636d
    Status: Downloaded newer image for ubuntu:latest
    bash > docker run -ti ubuntu bash
    root@0827f1baca7f:/# ps -ef
    UID        PID  PPID  C STIME TTY          TIME CMD
    root         1     0  0 20:48 pts/0    00:00:00 bash
    root         9     1  0 20:48 pts/0    00:00:00 ps -ef
    root@0827f1baca7f:/#
```

Now, you see that there is bash with PID (Process ID) 1. This is a general idea; everything inside the container lives as long as the process does. In addition, if you want to stop everything inside this container, just exit bash.

### Example

```
    bash > docker run -ti ubuntu bash
    root@0827f1baca7f:/# ps -ef
    UID        PID  PPID  C STIME TTY          TIME CMD
    root         1     0  0 20:48 pts/0    00:00:00 bash
    root         9     1  0 20:48 pts/0    00:00:00 ps -ef
    root@0827f1baca7f:/# exit
    bash > docker info
    Client:
    Debug Mode: false
    Server:
    Containers: 2
    Running: 0 
    Paused: 0
    Stopped: 2 
    Images: 47
    Server Version: 19.03.8
    Storage Driver: overlay2
    Backing Filesystem: 
    Supports d_type: true
    Native Overlay Diff: true
```

## Docker commands

Let's learn the basic Docker commands. The **docker info** command provides a lot of important information: how many containers in the system now, information about running, paused and stopped containers, and images and server configuration. The **docker ps** command shows the container status. To stop the container, use the **docker stop** command.

### Docker stop, Docker start, Docker exec

Use **docker stop** command to stop a running container. The command will send _SIGTERM_ signal to container's main process to gracefully terminate it.

Use **docker start** command to start one or more stopped container.

To execute a command within a running container use **docker exec** command. The command might be useful to run some diagnostic commands alongside the main container's process, or to open a shell to the container.

### Docker exec

For command execution inside a container we can use __docker exec__ in interactive mode:

`docker exec -it [containerID/containerNAME] [COMMAND]`

Example:

```
> docker exec -it my_container /bin/bas
container~username$
```

### Docker commit

We can use `docker commit` command to create an image from a modified container. For example, we can download ubuntu image and run a container. Until we have changes we can create a new image from the modified container.

`docker commit [containerID] [newImageName]`

## Working with docker daemon, docker hub and registry commands

### Getting the docker version and information

The following Docker commands will help you get the necessary information and version for work:

- **docker --version** provides you with the version of your Docker container, Docker service and client.
- **docker version --format' {{ .Server.Version}}'** gives you the server version, which can be applied to adjust the configuration.
- **docker version --format '{{json . }}'** - the command with this parameter is useful when you need to get the specific key.
- **docker info**
- **docker info --format ‘{{json .}}’**

To see the Docker version info, use the **docker version** command:

```
    bash > docker version
    Client: Docker Engine - Community
    Version:           19.03.8
    API version:       1.40
    Go version:        go1.12.17
    Git commit:        afacb8b
    Built:             Wed Mar 11 01:21:11 2020
    OS/Arch:           darwin/amd64
    Experimental:      false
```

```
    Server: Docker Engine - Community
    Engine:
    Version:          19.03.8
    API version:      1.40 (minimum version 1.12)
    Go version:       go1.12.17
    Git commit:       afacb8b
    Built:            Wed Mar 11 01:29:16 2020
    OS/Arch:          linux/amd64
    Experimental:     false
    containerd:
    Version:          v1.2.13
    GitCommit:        7ad184331fa3e55e52b890ea95e65ba581ae3429
    runc:
    Version:          1.0.0-rc10
    GitCommit:        dc9208a3303feef5b3839f4323d9beb36df0a9dd
    docker-init:
    Version:          0.18.0
    GitCommit:        fec3683
```

### Working with docker hub and registry

To work with Docker Hub and Registry, use the following commands:

- **docker login** allows you to log in to a registry. If you have an account in the Docker registry, you can use the **docker login** command with the account ID.
- **docker logout** lets you logout from a registry.
- **docker search** starts the search for an image.
- **docker pull** pulls an image from the registry to a local machine.
- **docker push** pushes an image to the registry from the local machine.

## Configuring the docker daemon

Let's look at the logs to see the system state. As you see, there are Docker daemon and containerd working in the system. Containerd configuration is default. However, the Docker daemon configuration is possible.

There are two ways to configure the Docker daemon.

![[SM7_L2_pic2_Configuring_the_Docker_Daemon.svg]]

You can use these options together as long as you don't specify the same option both as a flag and in the JSON file. If that happens, the Docker daemon won't start and print an error message.

To configure the Docker daemon via a JSON file, create a file at /etc/docker/daemon.json on Linux systems, or C:\ProgramData\docker\config\daemon.json on Windows. On macOS, go to the whale in the taskbar > Preferences > Daemon > Advanced. Here's what the configuration file looks like.

### Example

With this configuration, the Docker daemon runs in debug mode, uses TLS, and listens for the traffic routed to 192.168.59.3 on port 2376. You can learn available configuration options in the _[dockerd reference docs](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file)_

Also, there is a **/var/lib/docker** folder in which Docker has a lot of other folders. You do not need to manage them but remember that the Docker daemon puts here everything it takes.

Also, in the Docker Desktop version (Windows or MAC), you can find the daemon configuration in the docker desktop utility.

![[SM7_L2_image8.png]]

## Creating docker images

### Docker commands for working with images

In Docker, everything is based on Images. An image is a combination of a file system and parameters. Some Docker commands are used for working with Docker images and images info. Let's take a closer look at them.

### Working with docker images

The following Docker commands are used for working with Docker images:

- **docker images** shows all existing images.
- **docker import** creates an image from a tarball.
- **docker build** this command creates an image from a Dockerfile.
- **docker commit** creates an image from a container, pausing it temporarily ifit is running.
- **docker rmi** removes one or more images from the host node.
- **docker load** loads an image from a tar archive as STDIN, including images and tags.
- **docker save** saves an image to a tar archive stream to STDOUT with all parent layers, tags and versions.

You need to know that docker rmi cannot remove an image relied upon by some working container. So, to remove such an image, you need to remove a container, or containers, first.

### working with images info

The following commands allow you to work with images info:

- **docker history** shows the history of an image.
- **docker tag** tags an image to a name (local or a registry one). The most common use of this command is to tag an image to send it to another repository since the repository name is always part of the name of the image in it.

Here's an example of commands, including the **docker history** command. You can see the creation date and other information. Using the **docker commit** command is not the best choice because you cannot see the events' history. You can run **docker history** to check the events of the images created from a Dockerfile. You can also utilize **docker ls**, like **docker container ls** and **docker image ls**.

### Example

![[SM7_L2_image9.png]]

## Working with the image layers

Basically, an image is a number of layers. For example, there is an image sbelakou/centos:latest built long time ago. Based on that single layer, the image owner created image ansible:2.6.1. Then, based on Ansible 2.6.1, the owner generated the ansible:2.6.2 image. Technically 2.6.2 is a chain of all these layers. Then, CentOS was updated, and a new image was created.

You should know that updating the base image had NO impact on ansible 2.6.2. When you create an image based on another one, you only add delta, the difference, which is in a separate layer. The problem is there is a chain of layers, which are obsolete in most cases, inherited from the base image to all its children down by the chain. That is why the management of base images is an important thing, and there are a lot of tricks about it. Frequently, the best way is to build an image from scratch or from a simple base image, but then you lose the benefits of adding just the delta. From the pulling point of view, only the delta layer is pulled; the CentOS node will reuse the already pulled layers.

![[SM7_L2_pic3_working_with_The_Image_Layers.svg]]

## Working with a dockerfile

Dockerfile is a way to create a Docker image. Here you can put what you need to create an image. For example, Python is necessary, so the base image is provided FROM python 3.8. Then, it's needed to run some commands to install dependencies (RUN pip install flask). The next step is to copy everything inside the local folder with the application files uploaded or created to the new root of this file system on this container through the COPY directive. Afterward, you need to create a command that will be started when the container starts via the CMD directive.

### Example

Lets image that you want to create an image for a Python application like this:

![[SM7_L2_image12.png]]

This is application is based on the Flask framework. This application serves on the 80 port simple html page.

```
    from flask import Flask 
    app = Flask(__name__) 
    @app.route("/") 
    def hello(): 
        html = "<H1> Hello world!</H1>"
        return html 
    if __name__=="__main__": 
        app.run(host="0.0.0.0",port=80) 
```

The Dockerfile can be like this:

```
    FROM python:3.8 
    WORKDIR /app 
    RUN pip install flask 
    ADD app.py /app/app.py 
    EXPOSE 80 
    CMD ["python","app.py"] 
```

Each directive creates and runs a container, performs an action, and commits results to the intermediate image.

- The FROM directive defines the base image.
- The WORKDIR directive defines the working directory.
- The RUN directive installs the Flask framework into the image.
- The ADD directive copies the file into the image.
- The EXPOSE directive defines the external exposed port.
- The CMD directive defined command for start container.

Now, you will build a new image. The name for the new image is my_app. Note: Do not forget the point at the end — it indicates that the current directory is a working directory for building.

![[SM7_L2_image13.png]]

Now, you can see the log of the building process and run the container from the new image:

![[SM7_L2_image14.png]]

Next, you will check that the container works:

![[SM7_L2_image15.png]]

# Next Notes

[[Working with Dockerfile]]