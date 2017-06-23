FROM williamyeh/ansible:centos7
RUN yum install -y vim \
    yum install -y nano
COPY ssh/key /root/.ssh/id_rsa
COPY tutorial/ /opt/tutorial
RUN ln -s /opt/tutorial/tutorial.py /usr/local/bin/tutorial
