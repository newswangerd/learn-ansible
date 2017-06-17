# Poor Man's Ansible Tutorial
The idea behind this project is to provide an easy way to learn the basics of Ansible without having to worry about provisioning your own servers to run Ansible on. Poor Man's Ansible Tutorial does this by creating a set of Docker containers which mimic the way that Ansible would run on a real server.

## Requirements
- Docker (version 17.03)
- Bash

## Setup
0. Ensure that you have a version of Docker which supports the `docker network` command. Version 17 and up should work. You can check this with `docker --version`.
1. Clone or download this repo onto your local machine
2. Change to the project's base directory (the one README.md file)
3. Run the setup script with `./bin/setup.sh`
4. Connect to the ansible control node using `docker exec -it ansible-control bash`

## Teardown
Once you are done using the containers you can remove them by running `./bin/teardown.sh`.
