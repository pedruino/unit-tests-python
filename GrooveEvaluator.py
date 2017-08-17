from Geometry import Vector, Line


class GrooveEvaluator:
    def __init__(self):
        pass

    @staticmethod
    def calculate_groove_passes(groove_area, is_horizontal, tool_thickness, tool_interlock):

        top_left = groove_area[0]
        top_right = groove_area[1]
        bottom_left = groove_area[2]
        bottom_right = groove_area[3]

        distance = Vector.distance(bottom_left, Vector(0, 0))
        if distance > Vector.distance(bottom_right, Vector(0, 0)):
            aux = bottom_right
            bottom_right = bottom_left
            bottom_left = aux

        distance = Vector.distance(top_left, Vector(0, 0))
        if distance > Vector.distance(top_right, Vector(0, 0)):
            aux = top_right
            top_right = top_left
            top_left = aux

        pass_offset = Vector(0, tool_thickness / 2.0)
        pass_offset_interlock = Vector(0, tool_interlock)
        material_to_remove = top_left.y - bottom_left.y

        if not is_horizontal:
            pass_offset = Vector(tool_thickness / 2.0, 0)
            pass_offset_interlock = Vector(tool_interlock, 0)
            material_to_remove = top_left.x - bottom_left.x

        return GrooveEvaluator.__calculate_passes(material_to_remove, tool_thickness, top_left, top_right, bottom_left,
                                                  bottom_right,
                                                  is_horizontal, pass_offset, pass_offset_interlock)

    @staticmethod
    def __calculate_passes(material_to_remove, tool_thickness, top_left, top_right, bottom_left, bottom_right,
                           is_horizontal,
                           pass_offset, pass_offset_interlock):
        lines = []

        if material_to_remove == 0:
            return lines

        top_left -= pass_offset
        top_right -= pass_offset
        bottom_left += pass_offset
        bottom_right += pass_offset

        lines.append(Line(bottom_left, bottom_right))

        if is_horizontal:
            tool_interlock = pass_offset_interlock.y
            material_to_remove = (top_left.y - bottom_left.y)
        else:
            tool_interlock = pass_offset_interlock.x
            material_to_remove = (top_left.X - bottom_left.X)

        if material_to_remove < 0:
            material_to_remove = 0

        if material_to_remove == 0:
            return lines

        lines.append(Line(top_left, top_right))
        material_to_remove -= (tool_thickness - tool_interlock)

        if material_to_remove <= 0:
            return lines
        else:
            material_to_remove += tool_interlock

        top_left -= pass_offset
        top_right -= pass_offset
        bottom_left += pass_offset
        bottom_right += pass_offset

        top_left += pass_offset_interlock
        top_right += pass_offset_interlock
        bottom_left -= pass_offset_interlock
        bottom_right -= pass_offset_interlock

        lines.extend(GrooveEvaluator.__calculate_passes(material_to_remove, tool_thickness,
                                                        top_left, top_right, bottom_left, bottom_right,
                                                        is_horizontal, pass_offset, pass_offset_interlock))

        return lines
