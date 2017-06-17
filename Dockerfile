FROM williamyeh/ansible:centos7
RUN yum install -y vim \
    yum install -y nano
COPY ssh/key /root/id_rsa
