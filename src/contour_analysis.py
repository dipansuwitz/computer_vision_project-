import cv2

def analyze_contours(image, edges, min_area=100):
    result = image.copy()
    contours, _ = cv2.findContours(
        edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    objects = []
    for contour in contours:
        area = float(cv2.contourArea(contour))
        if area < min_area:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        perimeter = float(cv2.arcLength(contour, True))
        objects.append({
            "area": round(area, 2),
            "perimeter": round(perimeter, 2),
            "bounding_box": [int(x), int(y), int(w), int(h)]
        })

        cv2.drawContours(result, [contour], -1, (255, 0, 0), 2)
        cv2.rectangle(result, (x, y), (x+w, y+h), (0, 0, 255), 1)

    return result, objects
