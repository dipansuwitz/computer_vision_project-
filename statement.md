# Project Statement

## Project Title
Smart Image Edge & Shape Analyzer

## Problem Statement
Images contain useful structural information such as object boundaries, straight lines, contours, and corners. Manually identifying these structures is slow and subjective. The proposed system automatically analyzes an input image and extracts important geometric features using classical Computer Vision techniques.

## Scope
The project focuses on classical image-processing and feature-extraction methods. It accepts a normal image from the command line and generates edge, line, contour, and corner analysis results.

The project does not attempt full object recognition or deep-learning-based classification.

## Target Users
- Computer Vision students
- Beginners learning OpenCV
- Students demonstrating image-processing concepts
- Developers needing a small command-line image-analysis utility

## High-Level Features
1. Image preprocessing
2. Canny edge detection
3. Hough line detection
4. Contour and shape analysis
5. Harris corner detection
6. JSON result generation
7. Command-line execution
8. Automated tests

## Functional Requirements

### FR1 — Input
The system shall accept a valid image path through a command-line argument.

### FR2 — Preprocessing
The system shall convert the image to grayscale and apply Gaussian smoothing.

### FR3 — Edge Detection
The system shall produce an edge map using Canny edge detection.

### FR4 — Line Detection
The system shall detect prominent straight lines using the Hough Transform.

### FR5 — Contour Analysis
The system shall identify contours and calculate basic measurements such as area and bounding boxes.

### FR6 — Corner Detection
The system shall identify corner-like points using the Harris corner detector.

### FR7 — Reporting
The system shall save visual outputs and a JSON summary.

## Non-Functional Requirements

- Performance: should complete a normal academic-size image in a short command-line run.
- Usability: commands and arguments should be simple and clearly documented.
- Reliability: invalid image paths and malformed inputs should produce clear errors.
- Maintainability: each CV operation should be implemented in a separate module.
- Resource efficiency: images should be processed in memory without requiring a database.
- Testability: core processing functions should have automated tests.

## Inputs
- Image file path
- Optional Canny thresholds
- Optional Hough threshold
- Output directory

## Outputs
- Edge image
- Line-detection image
- Contour image
- Corner image
- JSON analysis report
