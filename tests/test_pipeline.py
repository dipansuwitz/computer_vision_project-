import unittest
import numpy as np

from src.edge_detection import detect_edges
from src.line_detection import detect_lines
from src.contour_analysis import analyze_contours

class TestPipeline(unittest.TestCase):

    def setUp(self):
        self.image = np.full((200, 300, 3), 255, dtype=np.uint8)
        self.image[50:150, 70:230] = 0
        self.gray = np.mean(self.image, axis=2).astype(np.uint8)

    def test_edge_detection_returns_image(self):
        edges = detect_edges(self.gray, 50, 150)
        self.assertEqual(edges.shape, self.gray.shape)

    def test_line_detection_returns_count(self):
        edges = detect_edges(self.gray, 50, 150)
        result, count = detect_lines(self.image, edges, 20)
        self.assertEqual(result.shape, self.image.shape)
        self.assertGreaterEqual(count, 0)

    def test_contour_analysis_returns_list(self):
        edges = detect_edges(self.gray, 50, 150)
        result, objects = analyze_contours(self.image, edges, min_area=20)
        self.assertEqual(result.shape, self.image.shape)
        self.assertIsInstance(objects, list)

if __name__ == "__main__":
    unittest.main()
