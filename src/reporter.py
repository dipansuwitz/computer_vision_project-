import json
from pathlib import Path
import cv2

def save_results(output_dir, edges, lines, contours, corners, summary):
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    cv2.imwrite(str(out / "edges.png"), edges)
    cv2.imwrite(str(out / "lines.png"), lines)
    cv2.imwrite(str(out / "contours.png"), contours)
    cv2.imwrite(str(out / "corners.png"), corners)

    with open(out / "analysis.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)

    return out
