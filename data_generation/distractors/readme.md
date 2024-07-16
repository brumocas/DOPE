# Distractors
We recommend adding "distractor" objects to the scene. These are unrelated objects that serve to enrich the training data, provide occlusion, etc.
Our data generation scripts use the [Google scanned objects dataset](https://app.ignitionrobotics.org/GoogleResearch/fuel/collections/Google%20Scanned%20Objects).
After downloading the files, run the following script to move the files to the desired location. More information about this can be found in the [DOPE](https://github.com/NVlabs/Deep_Object_Pose) git repository.

# Image Copier Script

This Python script copies image files with specified extensions from a source folder (`materials/textures/`) to a destination folder (`meshes/`) within each subdirectory of a specified directory. The script processes directories and files in alphabetical order. This is required in order to the blenderproc_data_gen to work.

## Features

- Recursively iterates through all subdirectories in the specified path.
- Copies image files with specific extensions (e.g., `.png`, `.jpg`) from the source to the destination folder within each subdirectory.
- Ensures the directories and files are processed in alphabetical order.

## Requirements

- Python

## Usage

1. **Clone or Download the Script:**

    Download the script file to your local machine.

2. **Edit the Script:**

    Set the `path` variable in the script to the directory containing your distractors.

    ```python
    path = 'path/to/your/directory'
    ```

3. **Run the Script:**

    Execute the script using Python.

    ```bash
    python copy_images.py
    ```