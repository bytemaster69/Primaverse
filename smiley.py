from pyautocad import Autocad, APoint

# Create an instance of AutoCAD
acad = Autocad(create_if_not_exists=True)

# Print a message in the AutoCAD command line
acad.prompt("Drawing a smiley face...\n")

# Define the center point for the smiley face
center_point = APoint(0, 0)

# Draw the face (circle)
face_radius = 50
acad.model.AddCircle(center_point, face_radius)

# Define the points for the eyes
left_eye_center = APoint(-20, 15)
right_eye_center = APoint(20, 15)
eye_radius = 5

# Draw the eyes (circles)
acad.model.AddCircle(left_eye_center, eye_radius)
acad.model.AddCircle(right_eye_center, eye_radius)

# Define the center point for the mouth
mouth_center = APoint(0, -10)

# Draw the mouth (arc)
start_angle = 30
end_angle = 150
acad.model.AddArc(mouth_center, 20, start_angle, end_angle)

# Check if all elements were added successfully
if acad.doc:
    print("Smiley face added successfully.")
else:
    print("Failed to add smiley face.")
