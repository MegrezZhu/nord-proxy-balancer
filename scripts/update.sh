SCRIPT_PATH=$(dirname `which $0`)
source $SCRIPT_PATH/env.sh

python3 nordapi/nordtoy.py -d | ./filter.js --type p2p  --port 1080 > nginx/upstream/p2p;
python3 nordapi/nordtoy.py -d | ./filter.js --type http --port 1081 > nginx/upstream/http;
docker container exec $CONTAINER_NAME nginx -s reload
