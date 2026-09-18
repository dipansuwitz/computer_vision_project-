import argparse

def build_parser():
    parser = argparse.ArgumentParser(
        description="Smart Image Edge & Shape Analyzer"
    )
    parser.add_argument("--input", required=True, help="Path to input image")
    parser.add_argument("--output", default="outputs", help="Output directory")
    parser.add_argument("--canny-low", type=int, default=50)
    parser.add_argument("--canny-high", type=int, default=150)
    parser.add_argument("--hough-threshold", type=int, default=80)
    return parser
