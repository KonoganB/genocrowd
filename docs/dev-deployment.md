In development mode, Genocrowd dependencies can be deployed with docker-compose, but Genocrowd have to be running locally, on your dev machine.

# Prerequisites

Install dev dependencies


```bash
# Debian/Ubuntu
sudo apt install -y git python3 python3-venv python3-dev make gcc zlib1g-dev libbz2-dev liblzma-dev g++ npm
# Fedora
sudo dnf install -y git make gcc zlib-devel bzip2-devel xz-devel python3-devel gcc-c++ npm
```


Install `docker`:

- [Debian](https://docs.docker.com/install/linux/docker-ce/debian/)
- [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- [Fedora](https://docs.docker.com/install/linux/docker-ce/fedora/)

Install `docker-compose`:

```bash
# Debian/Ubuntu
apt install -y docker-compose
# Fedora
dnf install -y docker-compose
```

# Deploy dependencies

We provide a `docker-compose` template to run external services used by Genocrowd. Clone the [genocrowd-docker-compose](https://github.com/annotons/genocrowd-docker-compose) repository to use it.

```bash
git clone https://github.com/annotons/genocrowd-docker-compose.git
```

Use the `dev` directory

```bash
cd genocrowd-docker-compose/dev
```

Deploy dockers

```bash
docker-compose up -d
```

# Fork and clone Genocrowd repository


[Fork](https://help.github.com/articles/fork-a-repo/) the Genocrowd repository

then, clone your fork locally

```bash
git clone https://github.com/USERNAME/genocrowd.git # replace USERNAME with your github username
```

# Install Genocrowd

Use the `install.sh` script to setup the python virtual environment and to download python and node modules needed.

```bash
./install.sh
```

# Run

Run in dev mode

```bash
./run_all.sh -d dev
```
