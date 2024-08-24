import json
import cv2
import numpy as np
import os
import argparse

# Argument parser setup
parser = argparse.ArgumentParser(description="Annotate an image with cuboid data from a JSON file.")
parser.add_argument('--json', required=True, help='Path to the input JSON file.')
parser.add_argument('--debug', action='store_true', help='Enable debug markers for cuboid corners.')
args = parser.parse_args()

# Ensure the annotated directory exists
output_dir = "./annotated/"
os.makedirs(output_dir, exist_ok=True)

# Paths to the input image and JSON file
json_path = args.json
image_path = os.path.splitext(json_path)[0] + ".png"

# Load the image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    raise FileNotFoundError(f"Cannot load image from path: {image_path}")

# Load JSON data from the file
with open(json_path, 'r') as f:
    json_data = json.load(f)

# Define the order of vertices based on the provided indices
bottom_face = [4, 5, 6, 7]  # Magenta face
top_face = [0, 1, 2, 3]     # Green face
vertical_edges = [(0, 4), (1, 5), (2, 6), (3, 7)]  # Connect top to bottom

# Define colors
colors = {
    'bottom_face': (255, 0, 255),  # Magenta
    'top_face': (0, 255, 0),       # Green
    'vertical_edges': (255, 255, 255),  # White
    'debug': {
        '0': (0, 255, 0),    # Green (g)
        '1': (0, 255, 0),    # Green (g)
        '2': (255, 0, 255),  # Magenta (m)
        '3': (255, 0, 255),  # Magenta (m)
        '4': (0, 255, 0),    # Green (g)
        '5': (0, 255, 0),    # Green (g)
        '6': (255, 0, 255),  # Magenta
        '7': (255, 0, 255),  # Magenta
    },
    'centroid': (255, 255, 255)  # White
}

# Function to draw a cuboid given the image and cuboid coordinates
def draw_cuboid(image, cuboid_coords, name, debug=False):
    # Convert to integer coordinates
    image_coords = [(int(u), int(v)) for u, v in cuboid_coords]

    # Draw the bottom face
    for i in range(4):
        cv2.line(image, image_coords[bottom_face[i]], image_coords[bottom_face[(i + 1) % 4]], colors['bottom_face'], 2)

    # Draw the top face
    for i in range(4):
        cv2.line(image, image_coords[top_face[i]], image_coords[top_face[(i + 1) % 4]], colors['top_face'], 2)

    # Draw the vertical edges
    for start, end in vertical_edges:
        cv2.line(image, image_coords[start], image_coords[end], colors['vertical_edges'], 2)

    # Draw debug markers for cuboid corners
    if debug:
        for i, color in colors['debug'].items():
            cv2.circle(image, image_coords[int(i)], 5, color, -1)

    # Draw the centroid
    centroid = np.mean(image_coords, axis=0).astype(int)
    cv2.circle(image, tuple(centroid), 5, colors['centroid'], -1)
    cv2.putText(image, name, (centroid[0], centroid[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

# Process each object in the JSON data
objects = json_data.get("objects", [])
for obj in objects:
    name = obj.get("name", obj.get("class", "Unknown"))
    projected_cuboid = obj.get("projected_cuboid", [])
    if len(projected_cuboid) >= 8:  # Ensure there are enough points to draw a cuboid
        draw_cuboid(image, projected_cuboid, name, debug=args.debug)

# Save the annotated image
output_path = os.path.join(output_dir, os.path.basename(image_path))
cv2.imwrite(output_path, image)

print(f"Annotated image saved to {output_path}")


