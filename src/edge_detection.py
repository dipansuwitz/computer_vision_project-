import cv2

def detect_edges(blurred, low_threshold=50, high_threshold=150):
    if low_threshold < 0 or high_threshold <= low_threshold:
        raise ValueError("Canny thresholds must satisfy 0 <= low < high.")
    return cv2.Canny(blurred, low_threshold, high_threshold)
