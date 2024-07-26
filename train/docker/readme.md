# DOPE Training Docker Container

This repository contains a Docker setup for training a deep learning model using PyTorch with specific dependencies. The container is based on the NVIDIA optimized PyTorch container and includes necessary libraries and tools.

## Prerequisites

- Docker installed on your machine ([Installation_Guide](https://docs.docker.com/engine/install/ubuntu/))
- NVIDIA GPU and drivers installed
- NVIDIA Container Toolkit ([Installation_Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html))
- Ensure `./get_nvidia_libs.sh` script is executed to obtain necessary NVIDIA libraries before building the Docker image

## Build the Docker Image

Before building the Docker image, make sure to run the `./get_nvidia_libs.sh` script to download the necessary NVIDIA driver libraries. 

```sh
sudo ./get_nvidia_libs.sh
```

Next, build the Docker image using the provided Dockerfile:

```bash
sudo docker build -t dope_training_image .
```

## Run the Docker Container

Run the Docker container with access to all GPUs on your host machine and mount a local directory to persist data:

```bash
sudo docker run --gpus all -it -v /home/bruno/Master/DOPE/train/docker/data:/workspace/dope_training/data dope_training_image
```
In this example, `$(pwd)/data` on the host machine is mounted to `/workspace/dope_training/data` in the container. Any changes in this directory will be saved to the host.


## S3 Configuration (Optional)

If you need to use S3 for storage, you can set up the necessary configuration by filling in your AWS credentials and uncommenting the relevant lines in the Dockerfile. Here are the steps:

1. Uncomment the following lines in the Dockerfile:
    ```dockerfile
    RUN mkdir ~/.aws \
    && echo "[default]" >> ~/.aws/config \
    && echo "aws_access_key_id = <YOUR_USER_NAME>" >> ~/.aws/config \
    && echo "aws_secret_access_key = <YOUR_SECRET_KEY>" >> ~/.aws/config \
    # Setup config files for s3 authentication 
    && echo "[default]" >> ~/.s3cfg \
    && echo "use_https = True" >> ~/.s3cfg \
    && echo "access_key = <YOUR_USER_NAME>" >> ~/.s3cfg \
    && echo "secret_key = <YOUR_SECRET_KEY>" >> ~/.s3cfg \
    && echo "bucket_location = us-east-1" >> ~/.s3cfg \
    && echo "host_base = <YOUR_ENDPOINT>" >> ~/.s3cfg \
    && echo "host_bucket = bucket-name" >> ~/.s3cfg
    ```
2. Replace `<YOUR_USER_NAME>`, `<YOUR_SECRET_KEY>`, `<YOUR_ENDPOINT>`, and bucket-name with your actual AWS credentials and S3 bucket details.

3. Rebuild the Docker image:
    ```bash
    docker build -t dope_training_image .
    ```