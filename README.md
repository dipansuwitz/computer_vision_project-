# Smart Image Edge & Shape Analyzer

A command-line Computer Vision project that analyzes an image and detects **edges, straight lines, contours, and corners**. It demonstrates core image-processing concepts such as grayscale conversion, Gaussian smoothing, Canny edge detection, Hough Line Transform, contour analysis, and Harris corner detection.

## 1. Problem

Manual inspection of an image for boundaries, straight structures, object outlines, and corners is time-consuming. This project provides a simple CLI-based pipeline that extracts these visual features and produces annotated result images plus a JSON summary.

## 2. Features

- Image validation and loading
- Grayscale conversion and Gaussian noise reduction
- Canny edge detection
- Hough Transform for straight-line detection
- Contour detection and geometric measurements
- Harris corner detection
- Automatic result report in JSON
- Synthetic sample-image generator
- Command-line execution; no GUI is required
- Unit tests for core processing functions

## 3. Architecture

```text
Input Image
    |
    v
CLI / Argument Parser
    |
    v
Preprocessing
    |
    +------> Canny Edge Detection ------> Edge Map
    |
    +------> Hough Transform ------------> Line Overlay
    |
    +------> Contours -------------------> Object Measurements
    |
    +------> Harris Corners -------------> Corner Overlay
    |
    v
Result Reporter
    |
    +------> PNG result images
    +------> analysis.json
```

## 4. Requirements

- Python 3.10+
- pip

## 5. Setup

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 6. Generate a sample image

```bash
python -m src.generate_sample --output data/sample_scene.png
```

The generated image contains simple geometric objects so the CV pipeline can be tested without downloading a dataset.

## 7. Run the project

```bash
python -m src.main --input data/sample_scene.png --output outputs
```

Optional parameters:

```bash
python -m src.main --input data/sample_scene.png --output outputs --canny-low 50 --canny-high 150 --hough-threshold 80
```

## 8. Output

The `outputs/` directory contains:

- `edges.png` — Canny edge map
- `lines.png` — detected straight lines
- `contours.png` — detected contours and bounding boxes
- `corners.png` — detected Harris corners
- `analysis.json` — numerical summary

## 9. Run tests

```bash
python -m unittest discover -s tests -v
```

## 10. Project Structure

```text
Smart_Image_Analyzer_CV/
├── data/
├── docs/
├── outputs/
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── preprocessing.py
│   ├── edge_detection.py
│   ├── line_detection.py
│   ├── contour_analysis.py
│   ├── corner_detection.py
│   ├── reporter.py
│   ├── generate_sample.py
│   └── main.py
├── tests/
│   └── test_pipeline.py
├── requirements.txt
├── statement.md
├── .gitignore
└── README.md
```

## 11. Course Concepts Demonstrated

- Image representation and preprocessing
- Edge detection
- Canny operator
- Hough Transform
- Contours and shape analysis
- Corner detection
- Feature visualization
- Modular computer-vision pipeline

## 12. Limitations

The project is intentionally designed as a lightweight academic CV system. Results can vary with lighting, image noise, object scale, camera angle, and threshold values.

## 13. Future Enhancements

- Add object classification using a trained model
- Add perspective correction
- Add circle detection
- Add batch-folder processing
- Add precision/recall evaluation using labeled images
- Add a REST API while keeping the CLI as the primary execution mode
