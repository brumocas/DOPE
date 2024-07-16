import json
import cv2
import numpy as np
import os
import argparse

# Argument parser setup
parser = argparse.ArgumentParser(description="Annotate an image with cuboid data from a JSON file.")
parser.add_argument('--image', required=True, help='Path to the input image file.')
parser.add_argument('--json', required=True, help='Path to the input JSON file.')
args = parser.parse_args()

# Ensure the annotated directory exists
output_dir = "./annotated/"
os.makedirs(output_dir, exist_ok=True)

# Paths to the input image and JSON file
image_path = args.image
json_path = args.json

# Load the image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    raise FileNotFoundError(f"Cannot load image from path: {image_path}")

# Load JSON data from the file
with open(json_path, 'r') as f:
    json_data = json.load(f)

# Define the order of vertices based on the provided indices
# Indices in the order: 0, 1, 2, 3, 4, 5, 6, 7 as per the diagram
# Top face: 0, 1, 5, 4
# Bottom face: 3, 2, 6, 7
# Vertical lines: 0-3, 1-2, 4-7, 5-6
bottom_face = [3, 2, 6, 7]
top_face = [0, 1, 5, 4]
vertical_edges = [(0, 3), (1, 2), (4, 7), (5, 6)]

# Function to draw a cuboid given the image and cuboid coordinates
def draw_cuboid(image, cuboid_coords, name):
    # Convert to integer coordinates (assuming projected_cuboid values are in float)
    image_coords = [(int(u), int(v)) for u, v in cuboid_coords]

    # Draw the bottom face
    for i in range(4):
        cv2.line(image, image_coords[bottom_face[i]], image_coords[bottom_face[(i + 1) % 4]], (255, 0, 255), 2)

    # Draw the top face
    for i in range(4):
        cv2.line(image, image_coords[top_face[i]], image_coords[top_face[(i + 1) % 4]], (0, 255, 0), 2)

    # Draw the vertical edges
    for start, end in vertical_edges:
        cv2.line(image, image_coords[start], image_coords[end], (255, 255, 255), 2)

    # Draw the model name near the cuboid
    centroid = np.mean(image_coords, axis=0).astype(int)
    cv2.putText(image, name, (centroid[0], centroid[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

# Process each object in the JSON data
objects = json_data.get("objects", [])
for obj in objects:
    name = obj.get("name", obj.get("class", "Unknown"))
    projected_cuboid = obj.get("projected_cuboid", [])
    if len(projected_cuboid) >= 8:  # Ensure there are enough points to draw a cuboid
        draw_cuboid(image, projected_cuboid, name)

# Save the annotated image
output_path = os.path.join(output_dir, os.path.basename(image_path))
cv2.imwrite(output_path, image)

print(f"Annotated image saved to {output_path}")