import os
import shutil

def copy_images(source_folder, destination_folder, image_extensions=None):
    """
    Copies image files from source_folder to destination_folder.
    
    Parameters:
    - source_folder (str): The path of the folder to copy images from.
    - destination_folder (str): The path of the folder to copy images to.
    - image_extensions (list): List of image file extensions to copy. Defaults to common image formats.
    """
    if image_extensions is None:
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Check if source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder does not exist: {source_folder}")
        return

    # List and sort all files in the source folder
    files = sorted(os.listdir(source_folder))
    
    # Filter and copy image files
    for file_name in files:
        # Get the file extension
        _, extension = os.path.splitext(file_name)
        
        if extension.lower() in image_extensions:
            # Construct full file path
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)
            
            # Copy the file
            shutil.copy2(source_path, destination_path)
            print(f"Copied: {file_name}")

def iter_folders(path):
    for entry in sorted(os.listdir(path)):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            print(f"Directory: {full_path}")
            source_folder = os.path.join(full_path, 'materials', 'textures')
            destination_folder = os.path.join(full_path, 'meshes')
            print(f"Source Directory: {source_folder}")
            print(f"Destination Directory: {destination_folder}")
            copy_images(source_folder, destination_folder, image_extensions=['.png'])

# Path to root directory where distractors are saved
path = '../../Deep_Object_Pose/data_generation/distractors/'
iter_folders(path)

