import mediapipe as mp
import cv2
import numpy as np

model_path = './vibevision/efficientdet_lite2.tflite'  # Model file path.

# Initialize the webcam (0 for the default webcam).
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Initialize Mediapipe ObjectDetector.
BaseOptions = mp.tasks.BaseOptions
ObjectDetector = mp.tasks.vision.ObjectDetector
ObjectDetectorOptions = mp.tasks.vision.ObjectDetectorOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Set up the options for ObjectDetector in image mode.
options = ObjectDetectorOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    max_results=5,
    running_mode=VisionRunningMode.IMAGE,
    score_threshold=0.5,
    category_denylist = ["Person", "person"]
)

# Create the object detector.
detector = ObjectDetector.create_from_options(options)

print("Object detector created successfully.")

while True:
    # Capture frame-by-frame.
    ret, numpy_image = cap.read()

    if not ret:
        print("Failed to capture image")
        break

    # Convert the frame from BGR (OpenCV default) to RGB.
    mp_image_frame = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(numpy_image, cv2.COLOR_BGR2RGB))

    # Perform detection on the current frame.
    detection_result = detector.detect(mp_image_frame)

    # Process detection results.
    if detection_result.detections:
        print(f"Detected {len(detection_result.detections)} objects.")

        # Draw bounding boxes for each detected object.
        for detection in detection_result.detections:
            #cat = detection.categories
            bbox = detection.bounding_box
            x = int(bbox.origin_x)
            y = int(bbox.origin_y)
            w = int(bbox.width)
            h = int(bbox.height)
            print(f"Bounding box: x={x}, y={y}, w={w}, h={h}")

            height, width, _ = numpy_image.shape
            print(f"Bounding box: x={x}, y={y}, w={w}, h={h}, height={height}, width={width}")

            if w + x > width or y + h > height:
                pass
            else:
                try:
                    # Draw a rectangle around the detected object.
                    cv2.rectangle(numpy_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    # add text
                    for cat in detection.categories:
                        cv2.putText(numpy_image, cat.category_name, (x + w, y + h), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                except Exception as e:
                    print(f"An error occurred: {e}")

    # Display the resulting frame with bounding boxes.
    cv2.imshow('Object Detection - Press Q to Exit', numpy_image)

    # Break the loop if 'Q' is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close any OpenCV windows.
cap.release()
cv2.destroyAllWindows()
print("Webcam released and windows closed.")