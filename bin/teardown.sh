echo "remove servers"
for i in 1 2 3
do
  docker rm -f centos-server-$i
done

echo "remove control node"
docker rm -f ansible-control

echo "remove network"
docker network rm ansible
