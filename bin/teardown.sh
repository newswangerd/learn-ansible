echo "Removing Servers ########################################################"
for i in 1 2 3
do
  docker rm -f centos-server-$i
done

echo ""

echo "Remove Control Node #####################################################"
docker rm -f ansible-control

echo ""

echo "Remove Network ##########################################################"
docker network rm ansible
