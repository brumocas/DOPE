# Cuboid Annotation with OpenCV and JSON

This script annotates cuboids in images based on JSON data using OpenCV (cv2) in Python. It reads JSON files containing cuboid coordinates projected onto the image plane and draws the corresponding cuboid edges on the image.

## Prerequisites

- Python 3.x
- OpenCV (`cv2`) installed (`pip install opencv-python`)
- NumPy (`pip install numpy`)

## Usage

```bash
python check_data_gen.py --image path_to_image --json path_to_json
```

### Example

```bash
python check_data_gen.py --image ./sample_data/000000.png --json ./sample_data/000000.json
```

    