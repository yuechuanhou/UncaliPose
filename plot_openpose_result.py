import json
import matplotlib.pyplot as plt

# Load the JSON data from the file
file_path = 'data/isaacsim/openpose_label/BODY_25/Camera2/rgb_0040_keypoints.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Set up the plot
fig, ax = plt.subplots()

# Extract and plot keypoints for each detected person
for person in data['people']:
    keypoints = person['pose_keypoints_2d']
    x = keypoints[0::3]
    y = keypoints[1::3]
    confidence = keypoints[2::3]

    # Plot only keypoints with a confidence greater than a threshold (e.g., 0.1)
    threshold = 0.0
    x_plot = [xi for xi, ci in zip(x, confidence) if ci > threshold]
    y_plot = [-yi for yi, ci in zip(y, confidence) if ci > threshold]  # Negate y for visual consistency with image coordinates

    ax.scatter(x_plot, y_plot)  # Plot keypoints

    # Optionally, you can add line connections between keypoints based on the BODY_25 model skeleton structure.
    # This would require defining the connections between keypoints and iterating through them to draw lines.

# Set axis labels and show the plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.invert_yaxis()  # Invert the y-axis to match the image coordinate system
plt.show()
