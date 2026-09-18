import argparse
from pathlib import Path
import cv2
import numpy as np

def generate(path):
    canvas = np.full((500, 800, 3), 245, dtype=np.uint8)

    cv2.rectangle(canvas, (80, 80), (300, 300), (40, 40, 40), -1)
    cv2.rectangle(canvas, (420, 100), (700, 240), (80, 80, 80), -1)
    cv2.circle(canvas, (250, 400), 70, (120, 120, 120), -1)
    cv2.line(canvas, (430, 330), (700, 430), (20, 20, 20), 8)
    cv2.polylines(
        canvas,
        [np.array([[480, 300], [580, 270], [650, 330], [560, 370]], dtype=np.int32)],
        True,
        (160, 160, 160),
        6,
    )

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(path), canvas)
    print(f"Sample image written to {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="data/sample_scene.png")
    args = parser.parse_args()
    generate(args.output)
