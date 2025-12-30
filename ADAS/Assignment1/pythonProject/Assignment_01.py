import cv2
import numpy as np

# Define the path for the uploaded image
IMAGE_FILE = "D:\BITS\Assignments\ADAS\Assignment1\pythonProject\Sample1.jpg"


# --- I. Lane Detection (Hough Transform Simulation) ---

def detect_and_draw_lanes(image, output_image):
    """Detects and draws green lane lines using a simplified pipeline."""

    # 1. Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Apply Gaussian blur to smooth edges
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # 3. Apply Canny Edge Detection
    # Thresholds are set to pick up high contrast edges (like white lines)
    edges = cv2.Canny(blur, 50, 150)

    # 4. Define Region of Interest (ROI) to focus detection on the road
    height, width = image.shape[:2]

    # Define vertices for a trapezoidal ROI (Focus on the lower half of the road)
    roi_vertices = [
        (0, height),  # Bottom Left
        (width // 2 - 50, height // 2 + 50),  # Top Left (Narrow point near horizon)
        (width // 2 + 50, height // 2 + 50),  # Top Right (Narrow point near horizon)
        (width, height)  # Bottom Right
    ]

    # Create a mask for the ROI
    mask = np.zeros_like(edges)
    cv2.fillPoly(mask, np.array([roi_vertices], np.int32), 255)
    masked_edges = cv2.bitwise_and(edges, mask)

    # 5. Apply Hough Line Transform
    # Parameters: rho, theta, threshold, minLineLength, maxLineGap
    lines = cv2.HoughLinesP(masked_edges,
                            rho=2,
                            theta=np.pi / 180,
                            threshold=150,
                            minLineLength=30,
                            maxLineGap=60)

    # 6. Draw lines
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            # Draw straight Lane lines with Green color
            cv2.line(output_image, (x1, y1), (x2, y2), (0, 255, 0), 5)  # (B, G, R) Green, thickness 5

    return output_image


# --- II. Object Detection Simulation (YOLO/SSD Output) ---

def draw_vehicles_and_labels(image):
    """Simulates bounding box output from an object detection model."""

    # Simulated model output: [Class_ID, Label, BBOX_X, BBOX_Y, BBOX_W, BBOX_H]
    # NOTE: Coordinates are estimated for the provided image
    detections = [
        {'label': "Red Suv", 'color': (0, 0, 255), 'bbox': (60, 390, 160, 100)},  # Red SUV (Left)
        {'label': "White Car", 'color': (0, 0, 255), 'bbox': (550, 400, 80, 50)},  # White Car (Center)
    ]

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.6
    font_thickness = 2
    label_color = (255, 0, 0)  # Blue color for text (B, G, R)

    for det in detections:
        x, y, w, h = det['bbox']
        label = det['label']

        # I. Draw Red color Rectangle Boxes
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red (B, G, R), thickness 2

        # II. Write label text upon Rectangular Boxes as "Red Suv" and "White Car" with Blue Color
        text_x = x
        text_y = y - 10

        # Ensure text is not drawn off the top edge
        if text_y < 15:
            text_y = y + h + 20  # Move text below the box if too high

        cv2.putText(image, label, (text_x, text_y),
                    font, font_scale, label_color, font_thickness, cv2.LINE_AA)

    return image


# --- Main Processing Function ---

def main_process(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image from {image_path}. Check file name and path.")
        return

    # 1. Vehicle Detection and Labeling (Simulation)
    processed_vehicles = draw_vehicles_and_labels(image.copy())

    # 2. Lane Line Detection (Hough Transform)
    final_output = detect_and_draw_lanes(image.copy(), processed_vehicles.copy())

    # Display the final result
    cv2.imshow("Advanced Detection: YOLO Simulation & Hough Lanes", final_output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the image
    cv2.imwrite("final_detection_output.jpg", final_output)


if __name__ == "__main__":
    # Ensure your image file is named 'image_7d4c60.jpg' or update the variable above
    main_process(IMAGE_FILE)