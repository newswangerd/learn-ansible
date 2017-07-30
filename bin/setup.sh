DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $DIR

echo "Creating Network ########################################################"
docker network create --subnet=192.168.27.1/28 ansible

# docker build -t newswangerd/centos-ssh $DIR/../centos-server

echo ""

echo "Creating Servers ########################################################"
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
  newswangerd/centos-ssh
done

echo ""

echo "Creating Control Node ###################################################"
# docker build -t ansible-control-node .

docker run -dt \
  --name ansible-control \
  --net ansible \
  --ip 192.168.27.2 \
  -v $DIR/../etc/ansible:/etc/ansible \
  --add-host=centos1:192.168.27.3 \
  --add-host=centos2:192.168.27.4 \
  --add-host=centos3:192.168.27.5 \
  newswangerd/ansible-control bash
