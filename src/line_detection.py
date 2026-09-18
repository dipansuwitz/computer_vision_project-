import cv2
import numpy as np

def detect_lines(image, edges, threshold=80):
    if threshold <= 0:
        raise ValueError("Hough threshold must be positive.")

    result = image.copy()
    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi / 180,
        threshold=threshold,
        minLineLength=40,
        maxLineGap=10,
    )

    count = 0
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(result, (x1, y1), (x2, y2), (0, 255, 0), 2)
            count += 1

    return result, count
