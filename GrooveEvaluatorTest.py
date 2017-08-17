import unittest

from ddt import ddt

from Geometry import Vector, Line
from GrooveEvaluator import GrooveEvaluator


@ddt
class GroovePassesCalculatorTest(unittest.TestCase):
    # tool_thickness = 10, groove_width = 10
    def test_case_1(self):
        groove_area = [Vector(0, 5), Vector(100, 5), Vector(0, -5), Vector(100, -5)]
        lines = GrooveEvaluator.calculate_groove_passes(groove_area, True, tool_thickness=10, tool_interlock=1)
        expected_lines = [Line(Vector(0, 0), Vector(100, 0))]

        self.assertListEqual(expected_lines, lines)

    # tool_thickness = 8, groove_width = 10
    def test_case_2(self):
        groove_area = [Vector(0, 5), Vector(100, 5), Vector(0, -5), Vector(100, -5)]
        lines = GrooveEvaluator.calculate_groove_passes(groove_area, True, tool_thickness=8, tool_interlock=1)
        expected_lines = [Line(Vector(0, -1), Vector(100, -1)), Line(Vector(0, 1), Vector(100, 1))]

        self.assertListEqual(expected_lines, lines)

    # tool_thickness = 8, groove_width = 16
    def test_case_3(self):
        groove_area = [Vector(0, 8), Vector(100, 8), Vector(0, -8), Vector(100, -8)]
        lines = GrooveEvaluator.calculate_groove_passes(groove_area, True, tool_thickness=8, tool_interlock=1)
        expected_lines = [Line(Vector(0, -4), Vector(100, -4)), Line(Vector(0, 4), Vector(100, 4)),
                          Line(Vector(0, 3), Vector(100, 3))]

        self.assertListEqual(expected_lines, lines)

    # tool_thickness = 8, groove_width = 20
    def test_case_4(self):
        groove_area = [Vector(0, 10), Vector(100, 10), Vector(0, -10), Vector(100, -10)]
        lines = GrooveEvaluator.calculate_groove_passes(groove_area, True, tool_thickness=8, tool_interlock=1)
        expected_lines = [Line(Vector(0, -6), Vector(100, -6)), Line(Vector(0, 6), Vector(100, 6)),
                          Line(Vector(0, 1), Vector(100, 1))]

        self.assertListEqual(expected_lines, lines)

    # tool_thickness = 2.2, groove_width = 10
    def test_case_5(self):
        groove_area = [Vector(-1, 479.1), Vector(1001, 479.1), Vector(-1, 469.1), Vector(1001, 469.1)]
        lines = GrooveEvaluator.calculate_groove_passes(groove_area, True, tool_thickness=2.2, tool_interlock=1)

        expected_lines = [
            Line(Vector(-1, 470.2), Vector(1001, 470.2)),
            Line(Vector(-1, 478.0), Vector(1001, 478.0)),
            Line(Vector(-1, 471.4), Vector(1001, 471.4)),
            Line(Vector(-1, 476.8), Vector(1001, 476.8)),
            Line(Vector(-1, 472.6), Vector(1001, 472.6)),
            Line(Vector(-1, 475.6), Vector(1001, 475.6)),
            Line(Vector(-1, 473.8), Vector(1001, 473.8)),
            Line(Vector(-1, 474.4), Vector(1001, 474.4))
        ]

        self.assertListEqual(expected_lines, lines)

    # tool_thickness = 3.2, groove_width = 10
    def test_case_6(self):
        groove_area = [Vector(-1, 479.1), Vector(451, 479.1), Vector(-1, 469.1), Vector(451, 469.1)]
        lines = GrooveEvaluator.calculate_groove_passes(groove_area, True, tool_thickness=3.2, tool_interlock=1)
        expected_lines = [
            Line(Vector(-1, 470.7), Vector(451, 470.7)),
            Line(Vector(-1, 477.5), Vector(451, 477.5)),
            Line(Vector(-1, 472.9), Vector(451, 472.9)),
            Line(Vector(-1, 475.3), Vector(451, 475.3)),
            Line(Vector(-1, 475.1), Vector(451, 475.1)),
        ]

        self.assertListEqual(expected_lines, lines)

    # tool_thickness = 3, groove_width = 10
    def test_case_7(self):
        groove_area = [Vector(0, 10), Vector(20, 10), Vector(0, 0), Vector(20, 0)]
        lines = GrooveEvaluator.calculate_groove_passes(groove_area, True, tool_thickness=3, tool_interlock=1)
        expected_lines = [
            Line(Vector(0, 1.5), Vector(20, 1.5)),
            Line(Vector(0, 8.5), Vector(20, 8.5)),
            Line(Vector(0, 3.5), Vector(20, 3.5)),
            Line(Vector(0, 6.5), Vector(20, 6.5)),
            Line(Vector(0, 5.5), Vector(20, 5.5)),
        ]

        self.assertListEqual(expected_lines, lines)

    if __name__ == '__main__':
        unittest.main()
