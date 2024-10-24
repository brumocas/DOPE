import json
import os

def reorder_projected_cuboid(projected_cuboid):
    """
    Reorder the projected cuboid vertices based on a specified mapping.
    The input projected_cuboid is expected to be a list of vertices, each a list of [x, y].
    """
    # Mapping according to the provided instruction
    new_order = [3, 0, 4, 7, 2, 1, 5, 6]
    reordered_cuboid = [projected_cuboid[i] for i in new_order]
    return reordered_cuboid

def process_json_file(file_path):
    """
    Process a single JSON file, reordering projected cuboids' positions and saving the changes.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    for obj in data.get("objects", []):
        # Assuming each object has a 'projected_cuboid' property with the cuboid vertices
        if 'projected_cuboid' in obj:
            original_cuboid = obj['projected_cuboid']
            obj['projected_cuboid'] = reorder_projected_cuboid(original_cuboid)

    # Save the modified data back to the same file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def process_directory(directory):
    """
    Process all JSON files in the specified directory and its subdirectories.
    """
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.json'):
                file_path = os.path.join(root, filename)
                process_json_file(file_path)
                print(f'Processed: {file_path}')

# Example usage
directory_path = '/home/bruno/Workspace/Master/BII/DOPE/data/dataset/blenderproc_data_gen/coffee_box/train1/coffee_box/'  # Change this to your directory path
process_directory(directory_path)
