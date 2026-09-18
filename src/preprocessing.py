import cv2

def load_and_preprocess(path):
    image = cv2.imread(path)
    if image is None:
        raise ValueError(f"Could not read image: {path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return image, gray, blurred
