from pyautocad import Autocad, APoint

# Create an instance of AutoCAD
acad = Autocad(create_if_not_exists=True)

# Print a message in the AutoCAD command line
acad.prompt("Drawing shapes...\n")

# Define the center point for the circle
circle_center = APoint(-50, 0)
circle_radius = 25

# Draw the circle
acad.model.AddCircle(circle_center, circle_radius)

# Define the points for the polygon
polygon_points = [(0, 0), (-25, 25), (0, 50), (25, 25), (0, 0)]  # Note: Coordinates as tuples

# Draw the sides of the polygon
for i in range(len(polygon_points) - 1):
    start_point = APoint(polygon_points[i][0], polygon_points[i][1])
    end_point = APoint(polygon_points[i + 1][0], polygon_points[i + 1][1])
    acad.model.AddLine(start_point, end_point)

# Close the polygon by connecting the last point to the first point
start_point = APoint(polygon_points[-1][0], polygon_points[-1][1])
end_point = APoint(polygon_points[0][0], polygon_points[0][1])
acad.model.AddLine(start_point, end_point)

# Define the points for the square
square_points = [(50, 0), (75, 0), (75, 25), (50, 25), (50, 0)]  # Note: Coordinates as tuples

# Draw the sides of the square
for i in range(len(square_points) - 1):
    start_point = APoint(square_points[i][0], square_points[i][1])
    end_point = APoint(square_points[i + 1][0], square_points[i + 1][1])
    acad.model.AddLine(start_point, end_point)

# Check if all shapes were added successfully
if acad.doc:
    print("Shapes added successfully.")
else:
    print("Failed to add shapes.")
