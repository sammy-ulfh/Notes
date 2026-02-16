# Index

- [[#Docker essentials]]
	- [[#Docker context of usage]]
	- [[#Solomon Hykes]]
	- [[#Sebastien Pahl]]
	- [[#Docker]]
	- [[#Example]]
	- [[#Managing at the application level]]
	- [[#Running the right version of application]]
	- [[#Docker Architecture Overview]]
	- [[#Docker workflow]]
	- [[#Docker Components. Docker infraestructure]]
	- [[#Docker client]]
	- [[#Docker daemon]]
	- [[#Containerd]]
	- [[#docker containerd shim]]
	- [[#docker runc]]
	- [[#docker proxy]]
	- [[#Docker components container]]
	- [[#Virtual machines vs Containers]]
	- [[#Isolation technologies functional requirements]]
	- [[#Docker Image]]
		- [[#Creation]]
		- [[#Storing]]
		- [[#Sending]]
	- [[#Docker storage (Graph) Drivers]]
		- [[#Disadvantages]]
		- [[#Docker Graph Drivers]]
	- [[#VFS]]
	- [[#AUFS]]
	- [[#Overlay2]]
	- [[#DeviceMapper]]
	- [[#Btrfs]]
	- [[#Docker installation and configuration]]
	- [[#MacOS]]
	- [[#Windows]]
	- [[#Microsoft include two types of containers]]
	- [[#Next Notes]]
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

- __Namespaces__: A process in the container shouldn't see other processes running in the system and should feel itself as the only process in the system.
- __Control Groups__: A facility is needed to manage system resources, for instances, to provide the necessary amount of RAM, CPU, shares, and so on the container.
- __Chroot__: A process in the container should see/use only that part of the filesystems required by it.
- __Process capabilities__: A process in the container should have enough permissions to manage/use kernel.
- __Virtual eth__: A process in the container should have access to an ethernet device.
- __Port Binding__: A few containers can expose the same ports, and it shouldn't cause any problem.
- __Volumes__: A service should have the facility to keep data, even if it goes down.
- __Docker Network__: Service should be able to communicate with other services by IP/names.

The most often used technologies are Namespaces, Control Groups and Chroot.

### Namespaces

If you compare a Docker container to a simple process, you will see that this process running in your system requires isolation. This isolation presents a namespace. When you run a container, Docker creates a set of namespaces for it. This provides a layer of isolation: each aspect of a container runs in its own namespace and does not have access outside.

There are 6 Linux kernel namespaces used by Docker Engine:

- The __MNT__ namespaces: Managing mount-points, filesystems.
- The __UTS__ namespace: Isolating kernel and version identifiers. (UTS: Unix Timesharing System).
- The __IPC__ namespace: Managing access to IPC resources (IPC: Inter Process Communication).
- The __PID__ namespace: Process isolation.
- The __NET__ namespace: Managing network interfaces.
- The __USER__ namespace.

![[09_Dropdown_1_Namespaces_fixed.svg]]

### Control Groups

A key to running applications in isolation is to make them only use the resources you want. This ensures that containers are good multi-tenant citizens on a host. Control Groups is an isolation technology that allows Docker Engine to share available hardware resources to containers and, if required, set up limits and constraints—for example, limiting the memory available to a specific container.

![[10_Dropdown_2_Control_Groups.svg]]

### Chroot

Chroot presents the idea that a process running inside your container sees only a piece of a filesystem. This piece is located somewhere in the root filesystem.

![[11_Dropdown_3_Chroot.svg]]

## Isolation Technology Example

Let's say you need to run Tomcat. It should be able to load certain libraries which will be located inside the container filesystem. Tomcat is developed to run at a certain VM port, and therefore, it requires a network interface. At the same time, the container needs isolation from everything. That is why Docker does not provide an Ethernet interface directly to this container. Instead, it provides a virtual Ethernet interface. To make the container available from outside, you need to use port binding or port forwarding. That is the reason why a port from the host is mapped to a port inside a container.

## Docker Image

A Docker image is an inert, immutable file essentially presenting a snapshot of a container.

### Creation

Images are generated using the build command that runs the script described in a Dockerfile. Images will create a container when run.

### Storing

Images are stored in a Docker Registry such as [https://hub.docker.com](https://hub.docker.com).

### Sending

As images can become quite large, they are designed to be composed of layers of other images, allowing a minimal amount of data to be sent when transferring images over the network.

Let's see an example. You need to run five instances of Tomcat of the same version. For all five instances, Docker will create five containers, but it will use only one image for all five containers as a base (since you need the same Tomcat version on all five). The interesting point is that a Docker image is not a kind of a .tar.gz package; it is several layers. A piece of a filesystem is packaged and linked to another layer. When you run the command as in the slide, it will execute layers. You do not need to care about exact layers, but you should know that if some layers already exist on your host, Docker will not download them. The same idea is when you built your container, and you need to push it to the registry. If the Docker registry has most of the layers already, it will only upload the new layers you created.

![[Code-ex_l1_1910Picture1.png]]

## Docker storage (Graph) Drivers

**Union filesystem (Union FS)** allows files and directories of separate files known as branches to be transparently overlaid, forming a single coherent filesystem. Contents of directories with the same path within the merged branches will be seen together in a single merged directory within the new virtual system.

**The copy-on-write (CoW) strategy** is a strategy of sharing and copying files for maximum efficiency. If a file or a directory exists in a lower layer within the image, and another layer (including the writable one) needs a read access to it, it just uses the existing file. The first time another layer needs to modify the file (when building the image or running the container), the file is copied into that layer and modified. This approach minimizes I/O and the size of each of the subsequent layers.  
In the following figure, you can see the layer with a system, updates, Java, and Tomcat. Where does container come into all of this? All layers in the image become read-only. Docker generates a container layer for storing just delta, a difference between the data in the image and in the container. When you start a container from an image, it can start the process, and then it can create certain files. All the files, new and updated, will go to this thin r/w layer. However, if your process needs to get some data from the Centos base, it will go to the read-only layer.

![[14_Docker_Storage.svg]]

There are certain disadvantages in this approach.

### Disadvantages

First of all, it is performance, but at the same time, your image can be used to spin up a new container. Still, if you have a big file in the layer, for example, a database, and you need to update just one byte in a 5 GB file, Docker will copy this 5 GB database file to the r/w layer, update it, and the file will stay there. When you need to create an image from the container, and you add to commit your changes, these 5 GB will join a chain of layers, and you will have an extra 5 GB. This is a major disadvantage of Docker.

The best implementation for Docker is to use a lightweight application with an image size of only about 100 MB. The only thing that you should pay attention to is the operations that it does on this level.

## Docker Graph Drivers

Since the image graph of the layer content represents the relationships between various layers, the driver handling these layers is called a **graph driver**.

### VFS

- VFS does not use a Union FS or CoW.
- It is suitable for simple validation and testing of the Docker Engine parts.
- VFS is valuable for situations where a copy-on-write filesystem cannot be utilized.
- It is not recommended for production use due to poor performance.

### AUFS

- Using Ubuntu or Debian, this graph driver is going to be the default.
- It enables shared memory pages for different containers loading the same shared libraries from the same layer.
- There is no quota support for AUFS.

### Overlay2

- Overlay2 is the preferred storage driver for all currently supported Linux distributions.
- It requires no extra configuration.
- Overlay2 resolves the inode exhaustion problem and a few other bugs that were inherent to the old design of the original driver.
- It enables shared memory between disparate containers through the same on-disk shared libraries.

### DeviceMapper

- Device mapper works on block devices.
- There is no way to get the default "out of the box" performance with device mapper.
- Some of the features rely on specific versions of libdevmapper, and it requires an above-average skill to validate all these settings on a system.

### Btrfs

- A disk formatted as a btrfs filesystem is required as the graph driver root (by default, /var/lib/docker).
- It's not supported by RedHat.
- Quota support was added directly to the Docker daemon for btrfs in PR #19651, which was included in the Docker 1.12 release.

Let's consider an example. When Tomcat creates a Catalina log file, it knows nothing about layers, reads in one place, saves to another, etc. It doesn't manage this process at all. Instead, you have a filesystem driver that works to achieve the mentioned above. There are different filesystem drivers or graph drivers because your dependencies between layers can be represented as a sophisticated graph. Graph drivers give you the best performance if you choose a graph driver correctly. On your machine where you practice your Docker command, you will use overlay2, which is the default. AUFS is only supported on Ubuntu and Debian and may require extra packages to be installed. VFS does not apply UnionFS and copy-on-write strategy; it looks fancy but low on performance. Device Mapper and btrfs are what you should look at when you prepare your environment for production. The difference between them is that Device Mapper works perfectly when you have prepared an underlying filesystem of the device. Btrfs requires the btrfs filesystem on the piece of your filesystem, where Docker will keep all files. There is no correct answer to which driver will give you best performance. Device Mapper requires a lot of tuning, btrfs is simple but requires a specific filesystem, especially here if you leave this folder by default, and unfortunately not supported by RedHat, unlike Device Mapper.

## Docker installation and configuration

If you decided to utilize Docker, you have to install it on your computer. If it has already been installed, please make sure to use the latest available version. Use the instructions below for macOS or Windows.  
If you need to install Docker on Ubuntu, follow the [link](https://docs.docker.com/engine/install/ubuntu/)_

### MacOS

The Docker Desktop installation includes Docker Engine, Docker CLI client, Docker Compose, Notary, Kubernetes, and Credential Helper.

- Double-click **Docker.dmg** to open the installer, then drag the Docker icon to the Applications folder.
- Double-click **Docker.app** in the **Applications** folder to start Docker. The Docker menu in the top status bar indicates that Docker Desktop is running, and accessible from a terminal. If you’ve just installed the app, Docker Desktop launches the onboarding tutorial. The tutorial includes a simple exercise to build an example Docker image, run it as a container, push and save the image to Docker Hub.
- Click the **Docker** menu to see **Preferences** and other options.
- Select **About Docker** to verify that you have the latest version.

### Windows

How to install Docker on  [Windows](https://docs.docker.com/desktop/setup/install/windows-install/).

There are two types of containers: HyperV and containers based on Windows Server Core images.

### Microsoft include two types of containers

![[15_Tab_2_Windows.svg]]

# Next Notes

[[Working with Docker]]