# Testing

The project uses Python's built-in `unittest` framework.

## Test Coverage

1. Edge detection returns an image with the expected dimensions.
2. Hough line detection returns a valid output image and non-negative count.
3. Contour analysis returns a valid image and a list of detected objects.

Run:

```bash
python -m unittest discover -s tests -v
```

The sample image generator also provides a deterministic input for manual verification.
