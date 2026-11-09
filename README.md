# TP1Docker

ReadMe 


PS C:\Windows\system32> docker --version
Docker version 29.9.2, build a82e528
PS C:\Windows\system32> docker images
                                                                                                    i Info →   U  In Use
IMAGE   ID             DISK USAGE   CONTENT SIZE   EXTRA
PS C:\Windows\system32> docker pull hello-world
Using default tag: latest
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete
d5e71e642bf5: Download complete
Digest: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest
PS C:\Windows\system32> docker images
                                                                                                    i Info →   U  In Use
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest   c567b231f656       25.9kB         9.49kB
PS C:\Windows\system32> docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

PS C:\Windows\system32> docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
PS C:\Windows\system32> docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      PORTS     NAMES
f5b37b32e7ff   hello-world   "/hello"   43 seconds ago   Exited (0) 43 seconds ago             competent_hofstadter
PS C:\Windows\system32> docker pull nginx
Using default tag: latest
latest: Pulling from library/nginx
37fb86c2a767: Pull complete
1962e1ff75b4: Pull complete
bbb080c71d50: Pull complete
6d2e43921e9e: Pull complete
512ac5e7ce8e: Pull complete
1724c05f72c6: Pull complete
7cb4701ce7cd: Pull complete
4582dace95e2: Download complete
d2c7e31f04a3: Download complete
Digest: sha256:165ddde8751e75a1c907d24ef10d9f6deb08b57e0fe56caf67512486aff76d82
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
PS C:\Windows\system32> docker run -d -p 8080:80 --name mon_nginx nginx
5faec4691a699a11d8da0332fd70c3974c6aeaab320f6c7c71f78f457d6dfc38
PS C:\Windows\system32> docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                     NAMES
5faec4691a69   nginx     "/docker-entrypoint.…"   23 seconds ago   Up 21 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   mon_nginx
PS C:\Windows\system32> docker stop mon_nginx
mon_nginx
PS C:\Windows\system32> docker rm mon_nginx
mon_nginx
PS C:\Windows\system32> docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
PS C:\Windows\system32>
