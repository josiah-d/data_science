# Docker
Courtesy Moses Marsh, Lead DSI Instructor  

[Docker](https://en.wikipedia.org/wiki/Docker_(software)) software lets you run programs in a controlled, portable environment. You can think of it kind of like a virtual machine, but in fact it is more lightweight. 

What problem does Docker solve? Portability. Take the PostgresSQL Server software, for example. The developers of Postgres had to develop separate versions of this software for Mac, Windows, and Linux. Setting up the software on each machine has its own set of possible problems due to the nature of each operating system. 

Docker handles this problem by allowing users to create *images* that define a piece of code, its dependencies, runtime environment, etc., and sending those images to anyone where they can be run *on any machine* in their own *containers*. Of course, the one caveat is that Docker must be installed first in order to run these containers.

Still, we have reduced the problem of "troubleshooting various installation issues for postgres, mongodb, flask, spark, and many others" into "troubleshooting the installation of Docker".

## Installing Docker

### Mac instructions

Start [here](https://docs.docker.com/docker-for-mac/install/). This page tells you to go to [Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-mac), the grand repository of official and unofficial Docker images accessible to all. Sign up for a free account and remember your username and password. 

The rest of the instructions tell you what to drag and drop. Once you're done, open a terminal and type
```bash
$ docker --version
```
If that worked, it looks like you have a successful installation.

Test out your ability to download a container from Docker Hub and run it locally with the following command:
```bash
$ docker run hello-world
```
It should tell you that you don't have the `hello-world` image locally, and it will automatically download it for you, then, hopefully, tell you that Docker is working correctly.

#### Possible issues
- If downloading images from Docker Hub is failing due to "authentication errors", try logging in again with `docker login`. If Docker is still telling you `user name or password not correct` even though you're SURE you're typing your login correctly, clear your old credentials with `rm /usr/local/bin/docker-credential-osxkeychain` and try again. (tip from [here](https://github.com/docker/for-mac/issues/2295))
- If your system tells you Docker is installed  but `docker --version` says `command docker not found`, make sure the docker service is running by opening searchlight (the magnifying glass icon in the upper right of your screen), typing `Docker`, and pressing `enter` when the whale icon shows up. Once the whale icon is displayed in the upper right of your screen, the terminal commands should work.


### Ubuntu Linux instructions

(if you are using Linux Mint, follow [these](https://www.hiroom2.com/2018/08/06/linuxmint-19-docker-en/) instructions instead, noting that the last step reboots your computer)

[The instructions are here](https://docs.docker.com/install/linux/docker-ce/ubuntu/), but a condensed version follows:

```bash
$ sudo apt-get update
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
$ sudo apt-get update
$ sudo apt-get install docker-ce
$ sudo groupadd docker
$ sudo usermod -aG $USER
```
Once you log out & back in (or reboot), you should be able to run `docker run hello-world` without issue. If prompted, create a free account at [Docker Hub](https://hub.docker.com/) and store your credentials with `docker login`.

### Windows

[Follow these instructions](https://docs.docker.com/docker-for-windows/install/) and good luck!


## Using Docker

Typical docker usage looks like `docker run --name cool_name image` or `docker run --name cool_name image command` where `cool_name` is the unique name you are giving to the container, `image` is the name of the image with the relevant software & environment (to be downloaded from docker hub or found locally) and `command` is the terminal command to run inside the container environment. The nature of the command and the various options depend on the image and the task at hand. 

For example,
```docker run --name my_pgserv -d postgres```
where `-d` means `run in the background (detached state)`. See the [documentation](https://docs.docker.com/engine/reference/run/) for so much more.

To execute commands on a container that's already running, use [`docker exec`](https://docs.docker.com/engine/reference/commandline/exec/). If the command requires further interaction with the terminal inside the container, you must add the `-it` options to run the command in interactive mode. For example,
```
docker exec -it pgserv psql -U postgres
```
This runs the command `psql -U postgres` in the container, then puts you in the resulting terminal (the postgres SQL terminal, where you can run SQL commands).

You can see what containers you've created with `docker container ls -a` and what's running with `docker ps`. You can start, stop, and delete containers with `docker container start container-name`, `docker container stop container-name`, and `docker container rm container-name`. 

The whole world is open to you now. See what you can do:
- [PostgresSQL in Docker](docker_postgres.md)
- [mongoDB in Docker](docker_mongodb.md)
- [Spark in Docker](docker_spark.md) 
- whatever you can find on [Docker Hub](https://hub.docker.com)


### docker command reference
| command | description |
|:--|:--|
|`docker container ls`| # List all running containers|
|`docker ps` | # List all running containers|
|`docker container ls -a` |  # List all containers, even those not running|
|`docker container stop CONTAINER_ID_OR_NAME` | # Gracefully stop the specified container|
|`docker container kill CONTAINER_ID_OR_NAME` | # Force shutdown of the specified container|
|`docker container rm CONTAINER_ID_OR_NAME`  |   # Remove specified container from this machine|
|`docker container rm $(docker container ls -a -q)` | # Remove all containers|
|`docker image ls -a`  | # List all images on this machine|
|`docker image rm IMAGE_ID_OR_NAME` | # Remove specified image from this machine|
|`docker image rm $(docker image ls -a -q)`   |# Remove all images from this machine|
|`docker login` |# Log in this CLI session using your Docker credentials|
