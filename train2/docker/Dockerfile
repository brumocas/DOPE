# Use the official PyTorch image with CUDA
FROM pytorch/pytorch:1.7.0-cuda11.0-cudnn8-devel

# Add the Missing Public Key
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC

# Install necessary libraries and dependencies
RUN apt-get update && \
    apt-get install -y \
    libglib2.0-0 \
    git

# Clone the repository
RUN git clone https://github.com/brumocas/DOPE.git /workspace/DOPE

# Set the working directory
WORKDIR /workspace/DOPE/train2

# Install Python dependencies if there is a requirements.txt or setup.py
# Uncomment and modify the following lines if you have a requirements.txt or setup.py
RUN pip install -r requirements.txt

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install numpy==1.24.4 scipy albumentations==1.4.13 albucore==0.0.13 scikit-image opencv-python-headless==4.10.0.84

