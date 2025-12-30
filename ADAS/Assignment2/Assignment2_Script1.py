import cv2
import numpy as np

# Define the path for the target image (Sample_02.jpg - the tunnel image)
IMAGE_FILE = "D:\BITS\Assignments\ADAS\Assignment2\pythonProject1\Sample_02.jpg"


# --- 1. Helper Functions (Line Averaging and Drawing) ---

def make_coordinates(image, line_parameters):
    """Calculates coordinates for a single, long line based on slope and intercept."""
    if line_parameters is None or np.isnan(line_parameters).any() or abs(line_parameters[0]) < 0.001:
        return None

    slope, intercept = line_parameters
    y1 = int(image.shape[0])
    y2 = int(y1 * 0.7)

    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])


def average_slope_intercept(image, lines):
    """Averages line segments into left and right lane lines."""
    left_fit = []
    right_fit = []

    if lines is None:
        return [None, None]

    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        if x2 == x1: continue

        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]

        if slope < -0.3:
            left_fit.append((slope, intercept))
        elif slope > 0.3:
            right_fit.append((slope, intercept))

    left_line = None
    if left_fit:
        left_line = make_coordinates(image, np.average(left_fit, axis=0))

    right_line = None
    if right_fit:
        right_line = make_coordinates(image, np.average(right_fit, axis=0))

    return [left_line, right_line]


def draw_lines(img, lines, color=(0, 255, 0), thickness=10):
    """Draws lines onto a blank image and blends."""
    line_image = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            if line is not None:
                x1, y1, x2, y2 = line.reshape(4)
                cv2.line(line_image, (x1, y1), (x2, y2), color, thickness)
    return cv2.addWeighted(img, 0.8, line_image, 1, 1)


def region_of_interest(image, edges):
    """Creates a masked image for the road (The 'Segment' stage)."""
    height, width = image.shape[:2]

    roi_vertices = np.array([
        [(0, height),
         (width * 0.40, height * 0.65),
         (width * 0.60, height * 0.65),
         (width, height)]
    ], dtype=np.int32)

    mask = np.zeros_like(edges)
    cv2.fillPoly(mask, roi_vertices, 255)
    masked_edges = cv2.bitwise_and(edges, mask)
    return masked_edges


# --- 2. Core Pipeline Function (Capturing all stages) ---

def ego_lane_detection_pipeline_full(image):
    """Runs the full pipeline and returns all intermediate images."""

    # a) Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # b) Gaussian Blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # c) Canny Edge Detection
    canny_edges = cv2.Canny(blur, 100, 250)

    # d) Segment/Masked Canny (ROI)
    masked_edges = region_of_interest(image, canny_edges)

    # e) Hough Line Transform (Raw Hough Output)
    raw_hough_lines = cv2.HoughLinesP(masked_edges,
                                      rho=2, theta=np.pi / 180,
                                      threshold=40, minLineLength=10,
                                      maxLineGap=20)

    # Create the Hough visualization frame (Red raw segments)
    hough_frame_raw = np.zeros_like(image)
    if raw_hough_lines is not None:
        for line in raw_hough_lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(hough_frame_raw, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Red Segments
    blended_hough_frame = cv2.addWeighted(image.copy(), 0.8, hough_frame_raw, 1, 1)

    # f) Final Output Processing
    averaged_lines = average_slope_intercept(image, raw_hough_lines)
    final_output_frame = draw_lines(image.copy(), averaged_lines, color=(0, 255, 0), thickness=10)

    return {
        'a) Grayscale': gray,
        'b) Gaussian Blur': blur,
        'c) Canny': canny_edges,
        'd) Segment (ROI Mask)': masked_edges,
        'e) Hough (Raw Segments)': blended_hough_frame,
        'f) Output Frame (Final)': final_output_frame
    }


# --- 3. OpenCV Display Function ---

def visualize_stages_opencv(image_path):
    """Loads image, runs pipeline, and displays all stages using cv2.imshow()."""

    original_image = cv2.imread(image_path)
    if original_image is None:
        print(f"Error: Could not load image from {image_path}. Check file name.")
        return

    # Get all intermediate stages
    stages = ego_lane_detection_pipeline_full(original_image.copy())

    # Use cv2.imshow() for all stages
    print("Displaying all pipeline stages via cv2.imshow(). Press any key to close windows...")
    for title, img in stages.items():
        # Grayscale stages need to be converted to 3-channel BGR to avoid imshow errors
        if len(img.shape) == 2:
            img_display = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        else:
            img_display = img

        cv2.imshow(title, img_display)

    # Wait indefinitely until a key is pressed to close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# --- Execute Script ---
if __name__ == "__main__":
    visualize_stages_opencv(IMAGE_FILE)