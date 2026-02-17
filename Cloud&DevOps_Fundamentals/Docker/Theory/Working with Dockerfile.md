# Index

# Running containers

As you already know, Dockerfile is a specific file used to create a Docker image. This file represents a text document with all commands necessary for building an image. With its help, the images can be built automatically.

_Find more details in the [official documentation](https://docs.docker.com/engine/reference/builder/)._

At the picture below, you can see a simple example of a Dockerfile to build and run a flask lightweight web framework.

![[pic1_Working_with_Dockerfile2.svg]]

There are some useful commands when working with Dockerfile. It will also be useful to see a list of links to the official Docker documentation.

## Commands

- **FROM** sets the base image for subsequent instructions.
- **RUN** allows you to execute any commands in a new layer on top of the current image and commit the results.
- **CMD** provides defaults for a container that is being executed.
- **EXPOSE** informs Docker that the container connects to the specified network ports at runtime. Please note that the command does not make any ports accessible.
- **ENV** sets the environment variable.
- **ADD** copies new files, directories or a remote file to the container. It invalidates caches.
- **COPY** copies new files or directories to the container.
- **ENTRYPOINT** configures a container that will run as an executable.
- **VOLUME** creates a mount point for externally mounted volumes or other containers.
- **USER** sets the username for the following RUN / CMD / ENTRYPOINT commands.
- **WORKDIR** sets the working directory.
- **ARG** defines a build-time variable.
- **ONBUILD** adds a trigger instruction when the image is used as the base for another build.
- **STOPSIGNAL** sets the system call signal that will be sent to the container to exit
- **LABEL** applies key/value metadata to your images, containers or daemons.

The difference between **COPY** and **ADD** is that **ADD** can work with archieve files, it can copy tarball files inside container and extract the content. The ADD directive also can copy directories or remote file URLs.

## Links and examples

Below you can see the list of the useful links to the official Docker documentation:

- _[Docker Command Line](https://docs.docker.com/engine/reference/commandline/cli/)_
- _[Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)_
- _[Samples](https://docs.docker.com/samples/)_
- _[Examples](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)_
- _[Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)_
- _[Awesome Docker](https://github.com/veggiemonk/awesome-docker)_
- _[Docker FAQs](https://docs.docker.com/engine/faq/)_

## Image creation with Dockerfile

Let’s consider an example of an httpd image creation from CentOS.

```Dockerfile
FROM centos
LABEL maintainer="Sammy-ulfh"
RUN yum install -y https && \
yum clean all
RUN echo "My httpd container" > /var/www/html/index.html
EXPOSE 80
ENTRYPOINT ["httpd"]
CMD ["-DFOREGROUND"]
```

Build image: `docker build -t my_http -f ./Dockerfile .`

With "-f" tag we assign the Dockerfile and with the final dot the entire resources of the current directory.

Start the container: `docker run -d -p 8080:80 myhttp`

## ENTRYPOINT and CMD commands

The **ENTRYPOINT** command allows you to configure a container that will run as executable, and the main purpose of the **CMD** command is to provide defaults for a container that is being executed. To make the container run the same executable each time, use the combination of these two commands.

**ENTRYPOINT** and **CMD** have two forms.

__EXEC FORM__: **exec form** (e.g. [“echo”]) is the preferred one

__SHELL FORM__: **shell form** (e.g., echo) supports ENV VARS resolving.

Using the combination of these two commands, ensure to utilize them in a similar form. Otherwise, they won't work correctly. The **ENTRYPOINT** command is utilized as an exact binary file or a script for running by default when you do not provide any command. The purpose of the **ENTRYPOINT** and **CMD** combination is to use CMD as the default argument to the **ENTRYPOINT** script.

Accordingly, you can execute the image specified in the slide with the **help** option. The **help** option is replaced with what is specified in **CMD** and will be provided to **ENTRYPOINT**. Therefore, you can create an image from the Dockerfile. By default, the ping command should send 1 ICMP to epam.com. **--help** will print help output from the ping command. Ping google.com will ping google.com unless interrupted. The "google.com" and **--help** are replacements for what is specified in **CMD**. To send one package, you can create a shortcut of the command and use it as an alias in the system.

EXAMPLE

![[pic5_Example.svg]]

## Best practice for using RUN instruction

The **RUN** instruction will execute any commands in a new layer on top of the current image and commit the results. The resulting committed image will be used for the next step in the Dockerfile. Layering **RUN** instructions and generating commits conforms to the core concepts of Docker where commits are cheap and containers can be created from any point in an image’s history, much like source control.

### Example 1

Usually, you can see something like in the example below (a custom image for JMeter, a widely used tool for load testing purposes). It doesn't make sense to split commands into multiple **RUN** commands, as each **RUN** is another layer. However, If you are unsure whether the command is full or something else, you can move it to another layer. Each command in **RUN** starts from scratch. This means that if you execute **RUN** cd in one folder and then **RUN** ls, it will execute ls in the default folder, not in the one you specified in **RUN cd**.

```
    FROM openshift/jenkins-slave-base-centos7
    ARG JMETER_VERSION=5.0

    USER root

    RUN yum -y install epel-release
    RUN sed -i 's/^enabled=1/enabled=0/g' /etc/yum.repos.d/epel.repo
    RUN yum -y install --enablerepo=epel jq
    RUN iputils-ping
    RUN telnet
    RUN unzip
    RUN wget
    RUN yum clean all
```

### Example 2

Here you can see the better approach to the usage of commands and instructions in the Dockerfile (RUN, ADD etc.).

```
    RUN mkdir /jmeter \
    && cd /jmeter/ \
    && wget https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-$JMETER_VERSION.tgz \
    && tar -xzf apache-jmeter-$JMETER_VERSION.tgz \
    && rm apache-jmeter-$JMETER_VERSION.tgz \
    && cd apache-jmeter-${JMETER_VERSION}/lib/ext \
    && wget
    https://github.com/NovaTecConsulting/JMeter-InfluxDB-Writer/releases/download/v-1.2/JMeter-InfluxDB-Writer-plugin-1.2.jar 

    WORKDIR /jmeter

    USER 1001
    ENV JMETER_HOME /jmeter/apache-jmeter-$JMETER_VERSION/
    ENV PATH $JMETER_HOME/bin:$PATH
```

## Tagging images

An image name is made up of slash-separated name components, optionally prefixed by a registry hostname. The hostname must comply with standard DNS rules but may not contain underscores. If a hostname is present, it may optionally be followed by a port number in the format :8080. If not present, the command uses Docker's public registry located at registry-1.docker.io by default. Name components may contain lowercase letters, digits, and separators. A separator is defined as a period, one or two underscores, or one or more dashes. A name component may not start or end with a separator. A tag name must be valid ASCII and may contain lowercase and uppercase letters, digits, underscores, periods and dashes. A tag name may not start with a period or dash and may contain a maximum of 128 characters. You can group your images together using names and tags and then upload them to Share images on Docker Hub.

When you build an image, you can tag it. If there is no exact Dockerfile in the folder, you need to provide an argument with the proper name of the Dockerfile. Do not forget to put a dot at the end. The dot means that all content of this folder will be provided to the Docker daemon. After the build, tag and build it again with this tag if you want. You can also use different tags for different builds.

The command format is as follow:

`docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]`

Let’s have a closer look at some examples.

### Tag an image referenced by ID

To tag a local image with ID “0e5574283393” into the “fedora” repository with “version1.0”:

```
    $ docker tag 0e5574283393 fedora/httpd:version1.0
```

### Tag an image referenced by Name

To tag a local image with name “httpd” into the “fedora” repository with “version1.0”:

```
    $ docker tag httpd fedora/httpd:version1.0
```

Note that since the tag name is not specified, the alias is created for an existing local version httpd:latest.

### Tag an image referenced by Name and Tag

To tag a local image with the "httpd" name and tag "test" into the fedora repository with "version1.0.test":

```
    $ docker tag httpd:test fedora/httpd:version1.0.test
```

### Tag an image for a pruvate repository

To push an image to a private registry and not the central Docker registry, you must tag it with the registry hostname and port (if needed).

```
    $ docker tag 0e5574283393 myregistryhost:5000/fedora/httpd:version1.0
```

## Docker base images

When an image is created from the Dockerfile, you can find its parent image there. A base image is created from scratch, having no parent image in the related Dockerfile. _See the details in the [official documentation](https://docs.docker.com/develop/develop-images/baseimages/)._

Let’s consider an example of the Docker base image building.

EXAMPLE

![[pic8_Docker_Base_Images2.svg]]

Building a base image, use the following.

![[pic9_Building_a_base_image1.svg]]

- __scratch__: **Scratch** is the ultimate base image with 0 files and 0 size.
- **Busybox** - is a minimal Unix weighing in at 2.5 MB and around 10000 files.
- **Debian:jessie** - the latest Debian is 122 MB and around 18000 files.
- **Alpine:latest** - Alpine Linux, only 8 MB in size and has access to a package repository.

The first step of building an image from scratch will be adding the tar file into the root directory. The **ADD** command will unpack it. Then **RUN** commands, add labels and execute the default command **/bin/bash** with the help of **CMD**.

EXAMPLE

![[SM_7_L3_Picture1code.png]]

## Building an image with arguments and multiusage build

Let’s have a look at Building an Image with Arguments and Multistage Build.

### Building an image with arguments

As an option, you can insert arguments to your Dockerfile. Dockerfile is considered as static. However, sometimes you need to provide some settings.

![[pic10_Building_an_Image_with_Arguments.svg]]

### Multiusage build

The fact that JDK and JRE are necessary to work with Java and run doesn't mean you need to provide all JDK libraries in a resulted image. To separate the processes for building and running, you do not have to create two Dockerfiles. Just create one with multiple stages.

![[pic11_Multistage_Build.svg]]

The first stage is based on maven: creating the build directory, moving there (using **WORKDIR**), and installing maven with **RUN**. The first image is marked as a builder. In another stage, you copy from the builder image. Therefore, you can build it, and the resulted image can only contain JDK. There is no limit to the number of stages, and you can create as many as you need.

## Running containers

The main command necessary for running the containers is docker run. It can be used with the following parameters. And also, let's consider an example of running the container.

### Parameters

docker run can be used with the following parameters:

- **-d runs** a container in the background and prints container ID
- **-P -** use it to publish all exposed ports to random ports
- **-p -** use it to publish a container's port(s) to the host
- **--restart** - use it to restart policy to apply when a container exits (default 'no')
- **-i -** use it to keep STDIN open even if not attached
- **-t -** use it to allocate a pseudo -TTY
- **--rm** - use it to automatically remove the container when it exits
- **-v -** use it to bind mount a volume
- **-e -** use it to set environment variables
- **--label** - use it to set metadata on a container
- **--log**-driver - use it to log driver for the container
- **-u -** use it to set a username or UID (<name|uid>[:<group|gid>])
- **-w -** use it to set the working directory inside the container
- **--entrypoint** - use it to overwrite the default ENTRYPOINT of the image

### Example

Let’s consider an example of running the container.

![[SM7_L3_Picture3.png]]

## Restart policy

You can execute a process, but it can be unstable for some reason. Let’s consider an example.

