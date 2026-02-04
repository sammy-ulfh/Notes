# Index

# Docker essentials

## Docker: context of usage

Docker Inc. was founded by Solomon Hykes and Sebastien Pahl during the Y Combinator Summer 2010 startup incubator group and launched in 2011. Docker was released as open source in March 2013.

### Solomon Hykes

- Founder of docker
- Former chief Technology Officer and Chief architec
- Creator of the Docker open source initiative

Solomon Hykes focused on building a platform for developers and system administrators to build, ship, run and orchestrate distributed applications.

### Sebastien Pahl

- Co-founder of Docker
- Worked at cloudflare, Mesosphere and Red Hat

Sebastien Pahl workedon building teams and projects. He is also fond of large-scale platforms, developer tools, automation, open source, and distributed systems.
## Docker

Docker helps facilitate application development, testing and deployment. They can be run separately in containers without configuring the environment and scale and manage then via the containers orchestration system.

## Example

You need to install Apache Tomcat on a server. It includes installing Java and many different dependencies. The problem is that with all these modules, libraries and many files created over the filesystem, your virtual machine becomes unique. If any problems occur to a library upgrade, unpredictable issues may occur. For example, some library versions will be replaced with other ones, which will lead to the Java and Tomcat breakage. In this case, Docker can help. 

### Managing at the application level

You can see a simple command __docker run -d -p 8080:8080 tomcat:\<tomcat_version>__. It will get an image from the library, spin out the server, and you will be able to reach it at port 8080. In this case, there is no need to install Java or Tomcat on your server. All dependencies are installed on the image. Thus, the first Docker advantage is that all dependencies are installed in one package, and you don't have to manage them separately on the server. You can manage everything at the application level.

### Running the right version of application

Let's say you need to run a different version of Tomcat. The previous installation required a different version of Java, and most likely, you had to install all the components versions so that they do not replace each other. You should keep different Java versions to different Tomcat versions. Here, Docker can be of use again. Run the same command  __docker run -d -p \<port_id> tomcat:\<tomcat_version>__ with the necessary version of Java and Tomcat instead of installing the whole package each time you need it and working with dependencies on your server. Thus, Docker allows you to run the right version of the application and avoid errors and manual management of the whole package. No need to install and configure the server by yourself.

## Docker Architecture Overview

Docker architecture is a client-server architecture:

1. Docker commands are run via the CLI Docker Tool.
2. The Docker client communicates with the daemon using the REST API over a UNIX socket or network interface.
3. The Docker daemon does the work on building, running and distributing containers outside the Docker client.
4. The daemon goes to the Docker registry to get the need image.

The client and daemon goes to the Docker registry to get the needed image. Otherwise, you can connect a client to a remote daemon. Find more details in the _[official documentation](https://docs.docker.com/engine/docker-overview/#docker-architecture)._

Let's have a close look at the main elements: the Docker client, the Docker daemon, the Docker registry.

## Docker workflow

Let's have a closer look at the Docker workflow.

## Docker Components. Docker infraestructure

When you ask the Docker daemon to start a new service, it accepts all options:

1. The Docker daemon provide details to containerd (currently, a part of the cloud-native framework, an open-source product).
2. Containerd communicates with container-shim.
3. Containerd-shim starts executing runC.
4. RunC starts a container and goes away.
5. Containerd-shim just look for a container to check whether it is working or not.

Docker infraestructure comprises the following components.

### Docker client

### Docker daemon

It is the Docker daemon itself. The highest-level component and the only Docker product listed. Provides all UX features of Docker.

### Containerd

It is a daemon listening on a UNIX socket, exposes GRPC endpoints. It handles all the low-level container management tasks, storage, image distribution, network attachments, etc.

### docker containerd shim

After runC runs the container, it exists (allowing you not to have any long-running processes responsible for the containers). The shim is the component sitting between containerd and runC to facilitate the process.

### docker runc

It is a lightweight binary for running containers. It deals with the low-level interfacing with Linux capabilities like cgroups, namespaces, etc.

### docker proxy

It is a tool responsible for proxying container ports to the host interface.

![[05_hot_spots_Docker_Components.svg]]

## Docker components: container

A container is something like a virtual machine. It can be used to contain and execute all the software required for running a program. The container includes:

- Filesystem (typically some flavor of Linux)
- Any software installed on top of this fiesystem
- Additional runtime things like external volumes or exposed ports.

It can be run as a self-contained virtual environment. This feature makes it a lot easier to reproduce the same analysis on any infrastructure that supports running the container, from your laptop to a cloud platform, without having to go through the pain of identifying and installing all the software dependencies involved. You can even have multiple switches between different environments if you need to run programs with incompatible system requirements.

![[06_Docker_Components_Container.svg]]

A container is usually a runnable instance of an image. Container detains all dependencies to execute the application. For Tomcat from the example above, there are Debian Tomcat and Java, etc. Tomcat running inside a container is absolutely the same as the Tomcat that you can install on a virtual machine. To do that on a virtual machine, you need Java, libraries, and so on. In a container, prerequisites are the same, but you do not need the entire operating system like on a virtual machine. First, you do not need a kernel inside a container. Docker container will use the host kernel. All containers running on the host will utilize it.

A container is isolated from other containers ans the host machine by default. It is possible to control the level of isolation. The container image with other configuration options defines the container itself. If you don't save the container state's changes in persistent storage, they will disappear after the container removal.

## Virtual machines vs Containers

A container is a new method for launching an application. A lot of specialists compare VMs to containers, but such an analogy is not proper:

- VMs have virtual CPU, OS, Kernel, but container only has binaries and dependencies to run a certain application.
- Docker is responsible for providing the host kernel inside a container.

It's more appropriate to equal a container to a standalone process running in the system.

![[07_Virtual_Machines_vs_Containers.svg]]
## Isolation technologies: functional requirements

As the main container idea is creating an isolated space for running certain applications, containerization requires a technology to organize well-separated spaces within the same machine. It is also required to build an isolation layers not only between the application and host, but also between the applications themselves. This approach rises the level of the default security and reduced the host surface area. So, the host and all containers located on it are well protected.

Below is the list of different kinds of isolation and the reason Docker provides it to container:

- 