#!/bin/bash

function docker_run_com_interface(){
  sudo docker run --gpus all -ti --net=host --ipc=host -e DISPLAY=$DISPLAY -v $2:$3 -v /tmp/.X11-unix:/tmp/.X11-unix -v $XAUTHORITY:/tmp/.XAuthority -e XAUTHORITY=/tmp/.XAuthority --env="QT_X11_NO_MITSHM=1" $1 /bin/bash
}

# Usage: ./run_container.sh <docker_image_name> <host_path> <container_path>
docker_run_com_interface dope_training_image $1 $2