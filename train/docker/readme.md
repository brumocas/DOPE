# DOPE Training Docker Container

This repository provides a Docker setup for training a deep learning model using PyTorch with specific dependencies. The Docker container is based on an NVIDIA-optimized PyTorch image and includes the necessary libraries and tools for model training.

## Prerequisites

Before using this Docker container, ensure you have the following installed:

- **Docker**: Follow the [Installation Guide](https://docs.docker.com/engine/install/ubuntu/) for installation instructions.
- **NVIDIA GPU and Drivers**: Ensure your system has a compatible NVIDIA GPU and the appropriate drivers installed.
- **NVIDIA Container Toolkit**: Install the toolkit by following the [Installation Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).

## Build the Docker Image

1. Navigate to the root of the DOPE repository:
   ```bash
   cd YOUR_PATH_TO/DOPE
   ```

2. Build the Docker image using the provided Dockerfile:
   ```bash
   sudo docker build -t dope_training_image -f train/docker/Dockerfile .
   ```

   This command creates a Docker image named `dope_training_image` from the Dockerfile located at `train/docker/Dockerfile`.

## Run the Docker Container

1. **Prepare the Data Directory**: Ensure you have a directory on your host machine to store and manage data. Create a directory named `data` in the host machine if it does not exist:
   ```bash
   mkdir -p YOUR_PATH_TO/DOPE/data
   ```
   Place your datasets and pretrained weights into this `data` directory.

2. **Use the Shell Script to Run the Docker Container**

   Make the script executable:

   ```bash
   chmod +x run_container.sh
   ```

3. **Run the Docker Container with GPU Support**

   Run the container with GPU support enabled by executing the shell script:

   ```bash
   ./run_container.sh <host_path> <container_path>
   ```

   - `dope_training_image`: Docker image name.
   - `host_path`: Host directory to mount inside the container.
   - `container_path`: Container path to mount.

   Example:
   ```bash
   ./run_container.sh home/bruno/Workspace/Master/DOPE/data /workspace/DOPE/data
   ```

   This shell script provides access to all GPUs on the host machine and mounts the host directory `home/bruno/Workspace/Master/DOPE/data` to `/workspace/DOPE/data` in the container. Any modifications to the mounted directory will be reflected on the host.

## Notes

- Ensure that you have placed all necessary files, such as datasets and pretrained weights, into the `data` directory before running the Docker container.
- The `--gpus all` flag allows the container to use all available GPUs. If you want to limit the GPUs used, you can modify this flag accordingly.
- For more information on Docker and GPU support, refer to the [Docker documentation](https://docs.docker.com/) and [NVIDIA Container Toolkit documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/).


## Acknowledgments

- [PyTorch](https://pytorch.org/)
- [CUDA](https://developer.nvidia.com/cuda-zone)
- [cuDNN](https://developer.nvidia.com/cudnn)