import cv2

IMG_PATH = "D:\BITS\Assignments\ADAS\Assignment2\pythonProject1\IMG_20251101_223026.jpg"


def run_edge_pipeline(img_path):
    """
    Runs Canny edge detection pipeline and shows the output of each step
    using standard OpenCV display windows.
    """

    # 1. Grab the frame
    frame = cv2.imread(img_path)

    if frame is None:
        print(f"Bummer. Couldn't load the image at {img_path}.")
        return

    # 2. Go Grayscale (a)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 3. Blur it out (c)
    # 5x5 blur is a good default to clean up noisy details
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 4. Find the Edges (d)
    # Thresholds are set to find the strong, high-contrast edges of the plant against the wall.
    low_thresh = 50
    high_thresh = 150
    edges = cv2.Canny(blurred, low_thresh, high_thresh)

    # --- Show the Steps (cv2.imshow) ---

    print("Opening 4 OpenCV windows. Press any key to close them all.")

    # a) Input frame
    cv2.imshow("a) 1. INPUT FRAME", frame)

    # b) Grayscale
    cv2.imshow("b) 2. GRAYSCALE", gray)

    # c) Gaussian Blur
    cv2.imshow("c) 3. GAUSSIAN BLUR", blurred)

    # d) Canny
    cv2.imshow("d) 4. CANNY EDGES", edges)

    # Wait for a key press and clean up
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_edge_pipeline(IMG_PATH)