import json
import cv2
import numpy as np
import os
import argparse

# Argument parser setup
parser = argparse.ArgumentParser(description="Annotate an image with cuboid data from a JSON file.")
parser.add_argument('--json', required=True, help='Path to the input JSON file.')
parser.add_argument('--numbers', action='store_true', help='Enable vertices numbers for cuboid.')
parser.add_argument('--vertices', action='store_true', help='Enable debug markers for cuboid corners.')
parser.add_argument('--ref', action='store_true', help='Enable referencial assignment in the centroid.')
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
bottom_face = [4, 5, 6, 7]  # Vertices for the bottom face
top_face = [0, 1, 2, 3]     # Vertices for the top face
vertical_edges = [(0, 4), (1, 5), (2, 6), (3, 7)]  # Edges connecting the top to the bottom

# Define colors
colors = {
    'bottom_face': (0, 255, 0),   # Green for bottom face edges
    'top_face': (0, 255, 0),      # Green for top face edges
    'vertical_edges': (0, 255, 0), # Green for vertical edges
    'debug': {
        '0': (0, 255, 0),    # Green
        '1': (0, 255, 0),    # Green
        '2': (0, 255, 0),    # Green
        '3': (0, 255, 0),    # Green
        '4': (0, 255, 0),    # Green
        '5': (0, 255, 0),    # Green
        '6': (0, 255, 0),    # Green
        '7': (0, 255, 0),    # Green
    },
    'centroid': (255, 255, 255),  # White
    'x_axis': (0, 0, 255),  # Red for X axis
    'y_axis': (0, 255, 0),  # Green for Y axis
    'z_axis': (255, 0, 0)   # Blue for Z axis
}

# Function to draw a cuboid given the image and cuboid coordinates
def draw_cuboid(image, cuboid_coords, name, vertices=False, numbers=False, ref=False):
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

    # Draw the vertex numbers
    if numbers:
        for i, (x, y) in enumerate(image_coords):
            cv2.putText(image, str(i), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Draw debug markers for cuboid corners
    if vertices:
        for i, color in colors['debug'].items():
            cv2.circle(image, image_coords[int(i)], 5, color, -1)

    # Calculate the centroid in 2D image space
    centroid_2d = np.mean(image_coords, axis=0).astype(int)

    # Calculate directions for axes using specific vertices
    # Z axis (from vertex 4 to vertex 0)
    z_direction = np.array(image_coords[0]) - np.array(image_coords[4])
    z_direction = z_direction / np.linalg.norm(z_direction) * 50  # Normalize and scale for visibility

    # X axis (from vertex 4 to vertex 5)
    x_direction = np.array(image_coords[5]) - np.array(image_coords[4])
    x_direction = x_direction / np.linalg.norm(x_direction) * 50  # Normalize and scale for visibility

    # Y axis (from vertex 4 to vertex 7)
    y_direction = np.array(image_coords[7]) - np.array(image_coords[4])
    y_direction = y_direction / np.linalg.norm(y_direction) * 50  # Normalize and scale for visibility

    if ref:
        # Draw X axis (red)
        cv2.arrowedLine(image, tuple(centroid_2d), 
                        tuple((centroid_2d + x_direction).astype(int)), 
                        colors['x_axis'], 2)

        # Draw Y axis (green)
        cv2.arrowedLine(image, tuple(centroid_2d), 
                        tuple((centroid_2d + y_direction).astype(int)), 
                        colors['y_axis'], 2)

        # Draw Z axis (blue)
        cv2.arrowedLine(image, tuple(centroid_2d), 
                        tuple((centroid_2d + z_direction).astype(int)), 
                        colors['z_axis'], 2)

    # Draw the centroid
    cv2.circle(image, tuple(centroid_2d), 5, colors['centroid'], -1)
    cv2.putText(image, name, (centroid_2d[0], centroid_2d[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# Process each object in the JSON data
objects = json_data.get("objects", [])
for obj in objects:
    name = obj.get("name", obj.get("class", "Unknown"))
    projected_cuboid = obj.get("projected_cuboid", [])
    if len(projected_cuboid) >= 8:  # Ensure there are enough points to draw a cuboid
        draw_cuboid(image, projected_cuboid, name, vertices=args.vertices, numbers=args.numbers, ref=args.ref)

# Save the annotated image
output_path = os.path.join(output_dir, os.path.basename(image_path))
cv2.imwrite(output_path, image)

print(f"Annotated image saved to {output_path}")