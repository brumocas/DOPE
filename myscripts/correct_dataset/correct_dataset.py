import json
import os

def reorder_projected_cuboid(projected_cuboid):
    """
    Reorder the first 8 projected cuboid vertices based on a specified mapping,
    keeping the 9th (centroid) point in the same position.
    """
    if len(projected_cuboid) != 9:
        raise ValueError("Expected exactly 9 points in the projected cuboid.")
    
    # Mapping for the first 8 vertices, leaving the 9th (centroid) intact
    new_order = [3, 0, 4, 7, 2, 1, 5, 6]
    reordered_cuboid = [projected_cuboid[i] for i in new_order] + [projected_cuboid[8]]
    return reordered_cuboid

def process_json_file(file_path):
    """
    Process a single JSON file, reordering projected cuboids' positions and saving the changes.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    for obj in data.get("objects", []):
        if 'projected_cuboid' in obj:
            original_cuboid = obj['projected_cuboid']
            obj['projected_cuboid'] = reorder_projected_cuboid(original_cuboid)

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def process_directory(directory):
    """
    Process all JSON files in the specified directory and its subdirectories,
    and count the number of files processed.
    """
    file_count = 0
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.json'):
                file_path = os.path.join(root, filename)
                process_json_file(file_path)
                file_count += 1
                print(f'Processed: {file_path}')
    print(f'Total JSON files processed: {file_count}')

# Example usage
directory_path = '/home/titan/BrunoCosta/DOPE/data/dataset/coffee_box/train_1_rand'  # Change this to your directory path
process_directory(directory_path)