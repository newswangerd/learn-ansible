# What does this project do?
The idea behind this project is to provide an easy way to quickly boostrap an Ansible environment without having to worry about installing Ansible or provisioning servers. This can be used for learning Ansible with an interactive tutorial or just for building and prototyping playbooks. This project accomplishes all of this by creating four Docker containers: one to server as a control server and three server as nodes.

This repo has two primary use cases as:
- a tutorial to teach beginners how to use Ansible
- a development environment which provides the user with a set of simulated CentOS servers to test playbooks on.

## Requirements
- Docker (version 17.03 or greater)
- Bash

## Setup
0. Ensure that you have a version of Docker which supports the `docker network` command. Version 17 and up should work. You can check this with `docker --version`.
1. Clone or download this repo onto your local machine
2. Run the setup script with `./bin/setup.sh`
3. Connect to the ansible-control container using `docker exec -it ansible-control bash`
4. If you want to use the interactive tutorial enter the `tutorial` command

## Ansible Tutorial
Once you are connected to the ansible-control container, start the interactive tutorial by using the `t` or `tutorial` command.

## Dev Environment
The `ansible/` directory in this project will get mounted into `/etc/ansible` on the ansible-control container. You can develop your playbooks in `ansible/` using the pre-configured hosts.

## Teardown
Once you are done using the containers you can remove them by running `./bin/teardown.sh`.
