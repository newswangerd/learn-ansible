# Quickstart Ansible Tutorial
The idea behind this project is to provide an easy way to learn the basics of Ansible without having to worry about provisioning your own servers to run Ansible on. Quickstart Ansible Tutorial does this by creating a set of Docker containers which mimic the way that Ansible would run on a real server.

## Requirements
- Docker (version 17.03 or greater)
- Bash

## Setup
0. Ensure that you have a version of Docker which supports the `docker network` command. Version 17 and up should work. You can check this with `docker --version`.
1. Clone or download this repo onto your local machine
2. Run the setup script with `./bin/setup.sh`
3. Connect to the ansible control node using `docker exec -it ansible-control bash`
4. Once you are connected to the control container, start the interactive tutorial by using the `tutorial` command.

## Teardown
Once you are done using the containers you can remove them by running `./bin/teardown.sh`.
