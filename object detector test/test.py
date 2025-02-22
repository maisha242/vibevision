import mediapipe as mp
import numpy as np
import cv2

model_path = './vibevision/efficientdet_lite2.tflite'

BaseOptions = mp.tasks.BaseOptions
DetectionResult = mp.tasks.components.containers.DetectionResult
ObjectDetector = mp.tasks.vision.ObjectDetector
ObjectDetectorOptions = mp.tasks.vision.ObjectDetectorOptions
VisionRunningMode = mp.tasks.vision.RunningMode

def print_result(result: DetectionResult, output_image: mp.Image, timestamp_ms: int):
    # Extract the bounding boxes from the detection result
    for detection in result.detections:
        # Get the bounding box coordinates (normalized to [0, 1])
        bounding_box = detection.bounding_box
        ymin, xmin, ymax, xmax = bounding_box  # Normalized coordinates

        # Convert normalized coordinates to pixel values
        h, w, _ = output_image.data.shape  # Get the image dimensions
        ymin, xmin, ymax, xmax = (
            int(ymin * h),
            int(xmin * w),
            int(ymax * h),
            int(xmax * w),
        )

        # Draw the bounding box on the output image
        cv2.rectangle(output_image.data, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

        # Optionally, add a label (e.g., object class)
        cv2.putText(output_image.data, f'Object', (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Show the image with bounding boxes
    cv2.imshow("Detection", output_image.data)

options = ObjectDetectorOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    max_results=5,
    result_callback=print_result)

with ObjectDetector.create_from_options(options) as detector:
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while(True):
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            break
        timestamp_ms = cap.get(cv2.CAP_PROP_POS_MSEC)

        # Convert frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the resulting frame
        cv2.imshow('Webcam', frame)
        
        # Create MediaPipe Image from frame
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

        # Perform detection asynchronously with the timestamp
        detector.detect_async(mp_image, int(timestamp_ms))

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
