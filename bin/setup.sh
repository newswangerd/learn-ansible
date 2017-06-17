echo "creating network"
docker network create --subnet=192.168.27.1/28 ansible

echo "creating servers"
for i in 1 2 3
do
docker run -d \
  --name centos-server-$i \
  --net ansible \
  --ip 192.168.27.$((i+2)) \
  --expose=22 \
  --env "SSH_USER_PASSWORD=pass" \
  --env "SSH_SUDO=ALL=(ALL) NOPASSWD:ALL" \
  --env "SSH_AUTHORIZED_KEYS=ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDcyxRmXtpXX/ToxT3uV3KHwVdEOw+TkPiUA2Z1XczD5p/RrGI9NLDRNhp0Y2E+JcRxuWE1UF6psvOcAj905kfCJhqmtxV9tEwEoWzrmXG/QILl7ry7NfPwhojAmXeer6rYVakuuuWj+t5NNVOQ79GsYGNFpHbmzcWhIaN4bGlXAkV8e/d8ysJuS/spiAVbcKt3ZGt4HFzHih2fcRnZbXGD2PDMW1tTuaHNDl5rY7PriY2Ay5gKXbiF+JpAeHQwVIPprHuDBVxS+LpjtIjajSNhzqG+9cMExvNjk9271MLoFVZKqwcFlZzVe/l/XjBYZjht+IiWEN9LRJVtFwbBfqVj dnewswan@dnewswan-OSX.local" \
  jdeathe/centos-ssh:centos-7
done

echo "creating control node"
docker build -t ansible-control-node .

docker run -dt \
  --name ansible-control \
  --net ansible \
  --ip 192.168.27.2 \
  -v $(pwd)/etc/ansible:/etc/ansible \
  ansible-control-node bash
