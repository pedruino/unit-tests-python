import unittest
from ddt import ddt, data, unpack
from GrooveEvaluator import Magic
from Geometry import Vector, Line


@ddt
class GroovePassesCalculatorTest(unittest.TestCase):
    # tool_thickness = 10, groove_width = 10
    def test_case_1(self):
        groove_area = [Vector(0, 5), Vector(100, 5), Vector(0, -5), Vector(100, -5)]
        lines = Magic.calculate_groove_passes(groove_area, True, tool_thickness=10, tool_interlock=1)
        expected_lines = [Line(Vector(0, 0), Vector(100, 0))]

        self.assertEquals(expected_lines, lines)

    # tool_thickness = 8, groove_width = 10
    def test_case_2(self):
        groove_area = [Vector(0, 5), Vector(100, 5), Vector(0, -5), Vector(100, -5)]
        lines = Magic.calculate_groove_passes(groove_area, True, tool_thickness=8, tool_interlock=1)
        expected_lines = [Line(Vector(0, -1), Vector(100, -1)), Line(Vector(0, 1), Vector(100, 1))]

        self.assertEquals(expected_lines, lines)

    # tool_thickness = 8, groove_width = 16
    def test_case_3(self):
        groove_area = [Vector(0, 8), Vector(100, 8), Vector(0, -8), Vector(100, -8)]
        lines = Magic.calculate_groove_passes(groove_area, True, tool_thickness=8, tool_interlock=1)
        expected_lines = [Line(Vector(0, -4), Vector(100, -4)), Line(Vector(0, 4), Vector(100, 4)),
                          Line(Vector(0, 3), Vector(100, 3))]

        self.assertEquals(expected_lines, lines)

    # tool_thickness = 8, groove_width = 20
    def test_case_4(self):
        groove_area = [Vector(0, 10), Vector(100, 10), Vector(0, -10), Vector(100, -10)]
        lines = Magic.calculate_groove_passes(groove_area, True, tool_thickness=8, tool_interlock=1)
        expected_lines = [Line(Vector(0, -6), Vector(100, -6)), Line(Vector(0, 6), Vector(100, 6)),
                          Line(Vector(0, 1), Vector(100, 1))]

        self.assertEquals(expected_lines, lines)

    # tool_thickness = 2.2, groove_width = 10
    def test_case_5(self):
        groove_area = [Vector(-1, 479.1), Vector(10001, 479.1), Vector(-1, 469.1), Vector(1001, 469.1)]
        lines = Magic.calculate_groove_passes(groove_area, True, tool_thickness=2.2, tool_interlock=1)
        expected_lines = [
            Line(Vector(-1, 470.2), Vector(1001, 470.2)),
            Line(Vector(-1, 478.0), Vector(1001, 478.0)),
            Line(Vector(-1, 471.4), Vector(1001, 471.4)),
            Line(Vector(-1, 476.8), Vector(1001, 476.8)),
            Line(Vector(-1, 472.6), Vector(1001, 472.6)),
            Line(Vector(-1, 475.6), Vector(1001, 475.6)),
            Line(Vector(-1, 473.8), Vector(1001, 473.8)),
        ]

        self.assertEquals(expected_lines, lines)

    if __name__ == '__main__':
        unittest.main()
