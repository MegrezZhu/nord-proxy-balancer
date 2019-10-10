SCRIPT_PATH=$(dirname `which $0`)
source $SCRIPT_PATH/env.sh

docker run \
    --name $CONTAINER_NAME \
    -p 1080:1080 \
    -p 1081:1081 \
    -p 1081:1081/udp \
    -v $(pwd)/nginx/nginx.conf:/etc/nginx/nginx.conf:ro \
    -v $(pwd)/nginx/upstream/http:/etc/nginx/upstream/http:ro \
    -v $(pwd)/nginx/upstream/p2p:/etc/nginx/upstream/p2p:ro \
    -d nginx
