# Design Decisions and Rationale

## Why Classical Computer Vision?
The project is intended to demonstrate fundamental Computer Vision concepts directly rather than hiding the processing inside a pretrained deep-learning model.

## Why Canny?
Canny is a standard multi-stage edge detector and clearly demonstrates how object boundaries can be extracted.

## Why Hough Transform?
The Hough Transform is suitable for detecting prominent straight lines and connects directly to geometric feature extraction.

## Why Contours?
Contours provide a simple way to analyze connected object boundaries and calculate area, perimeter, and bounding boxes.

## Why Harris Corners?
Corner detection demonstrates another important local feature-extraction technique.

## Why CLI?
The submission rules require terminal execution. A CLI also makes the project easy to reproduce and test.

## Why Modular Files?
Separate modules make the implementation easier to understand, test, maintain, and extend.
