FROM williamyeh/ansible:centos7
RUN yum install -y vim nano
COPY ssh/key /root/.ssh/id_rsa
COPY tutorial/ /opt/tutorial
RUN ln -s /opt/tutorial/tutorial.py /usr/local/bin/tutorial \
    && ln -s /opt/tutorial/tutorial.py /usr/local/bin/t \
    && echo "192.168.27.3 centos1" >> /etc/hosts \
    && chmod 600 /root/.ssh/id_rsa
