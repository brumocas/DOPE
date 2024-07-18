#!/bin/bash

# Ensure we are in the correct directory where `drivers/` exists
cd "$(dirname "$0")"  # This ensures we change to the script's directory

# Create `drivers/` directory if it doesn't exist
mkdir -p drivers

# Copy necessary NVIDIA driver files
cd drivers/
cp -r /usr/lib/x86_64-linux-gnu/libnvoptix.so.1 .
cp -r /usr/lib/x86_64-linux-gnu/*nvidia* .

# Optionally, you might want to print a message indicating success
echo "NVIDIA driver files copied successfully to ./drivers/"
