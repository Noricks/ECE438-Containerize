# ECE 438 containerized

This is a development environment for ECE 438, replacing virtual machines with containers.

Docker Hub: https://hub.docker.com/repository/docker/metricvoid/ece438

Note: Compatibility not guaranteed. 

Note: this is not a production image and is not optimized for size.

## Features
1. The IP address of each container is displayed in the prompts
    ```
    root@ece438-1[172.17.0.3]:/repo#
    ```
2. The `repo` folder is stored on host machine and shared across all containers. You can write code on the host machine and compile&run them in containers.

3. SSH access between containers. All containers have user `root` with password `root`.

4. Docker provides DNS service for the network bridge. e.g. `ece438-1` will resolve to `172.17.0.3` in the example above.

## Networking
1. All containers have an IP address in CIDR `172.17.0.0/16`.
2. Containers can communicate with each other.
3. Containers can access the host. The host is at `172.17.0.1`.
4. On Linux hosts, the host can access the container with their IPs. On Mac and Windows hosts, the host cannot access the containers.

## Usage of Powershell Scripts
0. Install Docker
1. Clone the repository
2. Clone your ECE 438 repository into the `repo/` folder.
3. Use the scripts.
   - `Start-Container` Start a container. (You may want multiple containers.) Containers are numbered with IDs
   - `Attach-Container` Attach to the console of a container for various operations.
     - Cannot attach to a stopped container.
     - Do not use `exit` or `logout` to detach. Use `Ctrl-P + Ctrl-Q`.
   - `Stop-AllContainers` to stop all ECE438 containers.
   - `Remove-AllContainers` to remove all ECE438 containers.  
4. You will be dropped into `/repo` in the containers. Use `ls` to discover your code.


# ECE 438 containerized (Native Updated by Noricks)

## Info
- This repository is forked from [Metric-Void/ECE438-Containerize](https://github.com/Metric-Void/ECE438-Containerize) for platforms with python to run.
- Provide native python scripts (python >= 3.6), which are re-write from Metric-Void's PowerShell scripts.
- Modified `ubuntu:16.04` to `ubuntu:22.04` to align with this year's requirement and one missing package.
- Provided auto docker image build
- This repo may update as the course/MPs progress.
- Welcome for comments and issues.

## WARNING: these updates are not checked with TAs yet

## Usage of Python Scripts
0. Install Docker and run `python3 command.py --install` to create the image
1. Clone your ECE 438 repository into the `repo/` folder.
2. Use the scripts.
   - `python3 command.py --start ContainerID` Start a container. (You may want multiple containers.) Containers are numbered with IDs
   - `python3 command.py --attach ContainerID` Attach to the console of a container for various operations.
     - Cannot attach to a stopped container.
     - Do not use `exit` or `logout` to detach. Use `Ctrl-P + Ctrl-Q`.
   - `python3 command.py --stop_all` to stop all ECE438 containers.
   - `python3 command.py --remove_all` to remove all ECE438 containers.
3. You will be dropped into `/repo` in the containers. Use `ls` to discover your code.  

## Note
- I personally recommend using [Portainer](https://docs.portainer.io/v/ce-2.9/start/install/server/docker/linux) to manage the containers and images if you do not want to install Docker Desktop.