SQlite is a lightweight serverless relational database management system.

# Connects or creates the db if it doesn't exist
`sqlite.connect(DB_NAME)`


# Create a cursor object to execute SQL commands
`cursor = conn.cursor()`

## Docker, Kubernaties Notes:

## Virtualization 
VIRTUALIZATION: is the process of simulating hardware and software in a virtual (software) environment. The software that creates and runs the virtualization is called the HYPERVISOR. 
It allocates and controls the sharing of a machine's resources (RAM, CPUs, Storage space). They come in type 1 (installed in bare empty metal hardware) and type 2 (runs ontop of an OS like Linux, MacOS, etc.) and sits between OS and APPs.
- type 1 normally for enterprise and type 2 for personal comps

Benefits on virtualization:
- Saves money on hardware and electricity and floorspace 
- Less physical machines so less maintanance
- Portability: Easily transferable to more powerful machines
- Full utilization of computer resources. 

The OS virtualizes Hardware...
Docker virtualizes the OS !
Docker file: Text document blueprint that instructs how docker image will be built:
    - starts with FROM word
    - RUN commands

## Virtual Memory
3 problems virtual memory solves:
1. Not enough memory
2. Memory fragmentation
3. Security

The KEY problem is that programs have access to the same memory space. What if we give each program a set isolated amount called Virtual Memory?
The virtual memory address of a program needs to be mapped to physical memory address (RAM). The mapper can solve problem (1) by locating oldest memory in use and map it to storage. The "additional" memory is called Swap memory. Problem (2) solved by mapping memory to a seemingly continous stream of memory. (3) solved by the map again: If two programs try to write to same memory, the mapper actually writes them to two differnt addresses even if we specify both to write in same address.


# Containers:
Why need Containers?
Solve problem of making software portable
A CONTAINER is a standard unit of software that encapsulates everything that programmers need to build, ship, and run apps. (settings, libraries, etc.)
- No need to pip install everything!
- Isolation and Allocation: No way to define resource boundaries for apps in a physical server
- Server Utilization: Not optimal bc servers tend to be either over or under utilized.
- Performance: Contrained during peak workloads
- Portability: Complex, time consuming and expensive
- Scalibility: limited 

Racap: They are light weight (mem efficient), fast, isolated, portable and secure. A machine can host many containers. They are Platform, Language, IDE independant. They lower deployment time and costs, improve utilization, automate process, and support next gen tech. 

# Docker 
Docker is an open platform used for developing, shipping, and running applications as containers. 


Docker is a robust and most popular container platform. Available since 2013. It is open platform for developing, shipping, and running applications as containers.
Speeds up deployment process across multiple environments.
Supports Agile and CI/CD DevOps practices.
NOT IDEAL FOR USE IN MONOLITHIC ARCHITECTURE OR APPS WITH HIGH PERFORMANCE OR SECURITY 

How to build a container image?
GIST: Docker File > Image > Container
Some Docker commands: docker <...>
* build: Creates containers images from a DockerFile
* images: Lists all images, repositories, tags, and sizes
* run: Creates a container from an image
* push: Stores images in a configured registry
* pull: Retrieves images from a conig registry

i.e.
docker build -t my-app:v1 
builds an image 

Docker Objects:
Dockerfiles, images, network, storage volumes
You can create a docker file with a terminal or any editior
and must always begin with a FROM command and defines base image. The RUN command executes commands. Should have one CMD instruction that defines default command for container execution.

Docker Image
Read-only template with instructions for creating a docker container.
Built using instructions in a Dockerfile. New read-only image layer created for each instruction in dockerfile. A writable container layer is placed ontop of read-only layers. It is needed because containers are not immutable. 
Format:
     hostname/repository:tag
     docker.io/ubuntu:18:04
     docker.io/ubuntu is docker hub registry and 18.04 represents installed ubuntu version.

# Docker Container
A runnable instance of an image
Can be created, stopped, or deleted using the Docker API or CLI
Can connect to multiple networks
Networks are used to isloate container communication. 

# Docker Architecture
Client-server architecture
Docker client, Docker host, and Registry
Docker CLI or REST APIs to Docker host that contains Daemon that listens for docker commands and does heavy lifting to run, build containers.
Docker Host includes and manages: 
- Images, storage, networks, clients

Docker stores and distributes images in a registry (public or private)

More info on Docker: https://tinyurl.com/notaleginger

# CODE
Docker Cheat Sheet: https://tinyurl.com/bdzc8atd

docker images // shows your docker images

docker ps -a // shows your containers (after running docker run <image>)

docker container rm <container_id> // removes container with c_id

docker stop <container_id> // stops container with id

docker stop $(docker ps -q) // stops all docker containers

# Container Orchestration
Overtime we get many containers - too many! How do we manage and scale? We need to automate lifecycle and orchestration to streamline complexity and increase speed, agility, and efficiency.
Features include:
- Define container images and registry
- Improve provision and deployment
- secure network connectivity 
- ensure availability and performance
- Health checks and automate error handling
- YAML or JSON files config containers to find resoureces, establish networks, store logs

Well known Container orchestration tools: Docker Swarm and Kubernetes (Standard for open source) robust feature set and widely supported

They all use automation to increase production, faster deployment, reduce cost, scalability, and faster recovery

# Kubernetes
Open-source system for automating deployment, sccaling, and management for containerized apps.

Portable across clouds and on-premises.

What is it NOT?
- not an all inclusive platform as a service
- Not rigid or opionionated but flexible model
- Does not provide CI/CD pipelines to deploy source code or build apps
- Does not provicde monitoring or logging 
- Not built in Databases

* Pods and Workloads: Pods are smallest deployable computer object in kubernetes
* Services: Exposes apps running on a set of pods
* Storage: Persistent and temporary storage for pods
* Configuration: Resources used for config pods
* Schedule Eviction: Runs and proactively terminates one or more pods on resourece- starved nodes

What can it do?
- Provide roll out changes to apps or configs
- Monitor application health and ensures instances are running
- Roll back changes
-Scales automatically


# What should you learn first before Kubernetes:
1. Containerization and Orchestration. 
2. Cloud basics (AWS, Azure, GCP)
3. YAML (like JSON)
4. Networking basics