import json

def reorder_projected_cuboid(projected_cuboid):
    """
    Reorder the projected cuboid vertices based on a specified mapping.
    The input projected_cuboid is expected to be a list of vertices, each a list of [x, y].
    """
    # Mapping according to the given instruction
    new_order = [3, 0, 4, 7, 2, 1, 5, 6]
    reordered_cuboid = [projected_cuboid[i] for i in new_order]
    return reordered_cuboid

def process_json_file(input_file, output_file):
    """
    Process the JSON file, reordering projected cuboids' positions and saving to a new file.
    """
    with open(input_file, 'r') as f:
        data = json.load(f)

    for obj in data.get("objects", []):
        # Assuming each object has a 'projected_cuboid' property with the cuboid vertices
        if 'projected_cuboid' in obj:
            original_cuboid = obj['projected_cuboid']
            obj['projected_cuboid'] = reorder_projected_cuboid(original_cuboid)

    # Save the modified data to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage
input_file = '/home/bruno/Workspace/Master/BII/DOPE/myscripts/correct_dataset/data/000007.json'  # Change this to your input file
output_file = '/home/bruno/Workspace/Master/BII/DOPE/myscripts/correct_dataset/data/000007_sol.json'  # Output file for modified data
process_json_file(input_file, output_file)
