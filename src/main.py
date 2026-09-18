from pathlib import Path
from .cli import build_parser
from .preprocessing import load_and_preprocess
from .edge_detection import detect_edges
from .line_detection import detect_lines
from .contour_analysis import analyze_contours
from .corner_detection import detect_corners
from .reporter import save_results

def run(args):
    image, gray, blurred = load_and_preprocess(args.input)

    edges = detect_edges(blurred, args.canny_low, args.canny_high)
    line_image, line_count = detect_lines(image, edges, args.hough_threshold)
    contour_image, objects = analyze_contours(image, edges)
    corner_image, corner_count = detect_corners(image, gray)

    summary = {
        "input": str(Path(args.input)),
        "image_size": {"width": int(image.shape[1]), "height": int(image.shape[0])},
        "parameters": {
            "canny_low": args.canny_low,
            "canny_high": args.canny_high,
            "hough_threshold": args.hough_threshold,
        },
        "detected_lines": line_count,
        "detected_corners": corner_count,
        "detected_contours": len(objects),
        "objects": objects,
    }

    save_results(
        args.output,
        edges,
        line_image,
        contour_image,
        corner_image,
        summary,
    )

    print("Analysis complete.")
    print(f"Lines: {line_count}")
    print(f"Contours: {len(objects)}")
    print(f"Corners: {corner_count}")
    print(f"Results saved to: {args.output}")

if __name__ == "__main__":
    parser = build_parser()
    run(parser.parse_args())
