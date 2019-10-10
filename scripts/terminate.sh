SCRIPT_PATH=$(dirname `which $0`)
source $SCRIPT_PATH/env.sh

docker rm -f $CONTAINER_NAME
