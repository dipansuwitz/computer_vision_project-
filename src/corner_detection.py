import cv2
import numpy as np

def detect_corners(image, gray, max_corners=80):
    result = image.copy()
    gray_float = np.float32(gray)

    response = cv2.cornerHarris(gray_float, 2, 3, 0.04)
    response = cv2.dilate(response, None)

    threshold = 0.01 * response.max() if response.size else 0
    ys, xs = np.where(response > threshold)

    points = list(zip(xs.tolist(), ys.tolist()))
    points = points[:max_corners]

    for x, y in points:
        cv2.circle(result, (x, y), 3, (0, 0, 255), -1)

    return result, len(points)
