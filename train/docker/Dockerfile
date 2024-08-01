# Use the base PyTorch image with CUDA and cuDNN support
FROM pytorch/pytorch:2.3.1-cuda12.1-cudnn8-runtime

# Install git and other dependencies
RUN apt-get update && \
    apt-get install -y git libglib2.0-0
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx

# Clone the repository
RUN git clone https://github.com/brumocas/DOPE.git /workspace/DOPE

# Set the working directory to /workspace/DOPE
WORKDIR /workspace/DOPE

# Not required if you use the the shared folder between the host and the container
# Copy dataset and weights required for training to /workspace
# COPY data/ /workspace/DOPE

# Install Python dependencies if there is a requirements.txt or setup.py
# Uncomment and modify the following lines if you have a requirements.txt or setup.py
RUN pip install -r requirements.txt
