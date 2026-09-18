# Design Diagrams

## System Architecture

```text
+-------------------+
| Command Line User |
+---------+---------+
          |
          v
+-------------------+
| CLI Argument      |
| Parser            |
+---------+---------+
          |
          v
+-------------------+
| Preprocessing     |
| Gray + Gaussian   |
+----+----+----+----+
     |    |    |
     v    v    v
  Canny Hough Contour
     |    |    |
     |    |    +------> Shape measurements
     |    +-----------> Line overlay
     +---------------> Edge map
          |
          v
+-------------------+
| Harris Corners    |
+---------+---------+
          |
          v
+-------------------+
| Reporter          |
| PNG + JSON        |
+-------------------+
```

## Workflow

```text
Start
  |
  v
Read image
  |
  v
Validate image
  |
  v
Convert to grayscale
  |
  v
Gaussian smoothing
  |
  +--> Canny --> Edge map
  |
  +--> Hough --> Lines
  |
  +--> Contours --> Areas / boxes
  |
  +--> Harris --> Corners
  |
  v
Save outputs
  |
  v
End
```

## Use Case Diagram

```text
             +--------------------------------------+
             | Smart Image Analyzer                 |
             |                                      |
User ------> | [Load Image]                         |
             |       |                              |
             |       +--> [Preprocess]              |
             |       +--> [Detect Edges]            |
             |       +--> [Detect Lines]            |
             |       +--> [Analyze Contours]        |
             |       +--> [Detect Corners]          |
             |       +--> [Generate Report]         |
             +--------------------------------------+
```

## Sequence Diagram

```text
User -> CLI: run --input image
CLI -> Preprocessor: load image
Preprocessor -> CLI: image + grayscale
CLI -> Edge Detector: detect edges
Edge Detector -> CLI: edge map
CLI -> Hough Detector: detect lines
Hough Detector -> CLI: line result
CLI -> Contour Analyzer: analyze contours
Contour Analyzer -> CLI: measurements
CLI -> Corner Detector: detect corners
Corner Detector -> CLI: corner result
CLI -> Reporter: save PNG + JSON
Reporter -> User: output files
```

## Class/Component Diagram

```text
+------------------+
| main.py          |
+--------+---------+
         |
         +--> cli.py
         |
         +--> preprocessing.py
         |
         +--> edge_detection.py
         |
         +--> line_detection.py
         |
         +--> contour_analysis.py
         |
         +--> corner_detection.py
         |
         +--> reporter.py
```

## Storage Design

No database is required. The project uses the local filesystem:

```text
Input Image
    |
    +--> PNG result files
    |
    +--> analysis.json
```
