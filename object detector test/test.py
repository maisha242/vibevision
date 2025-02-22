import mediapipe as mp
import numpy as np
import cv2

def main():
    model_path = './efficientdet_lite2.tflite'

    BaseOptions = mp.tasks.BaseOptions
    DetectionResult = mp.tasks.components.containers.DetectionResult
    ObjectDetector = mp.tasks.vision.ObjectDetector
    ObjectDetectorOptions = mp.tasks.vision.ObjectDetectorOptions
    VisionRunningMode = mp.tasks.vision.RunningMode
    
    global CURRCATEGORY 
    CURRCATEGORY = ""
    def print_result(result: DetectionResult, output_image: mp.Image, timestamp_ms: int):
        #Extract the bounding boxes from the detection result
        for detection in result.detections:
            for cat in detection.categories:
                    global CURRCATEGORY
                    if (cat.category_name != "person"):
                        CURRCATEGORY = cat.category_name
            

    options = ObjectDetectorOptions(
        base_options=BaseOptions(model_asset_path=model_path),
        running_mode=VisionRunningMode.LIVE_STREAM,
        max_results=1,
        result_callback=print_result)

    with ObjectDetector.create_from_options(options) as detector:
        cap = cv2.VideoCapture(0)

        # Check if the camera opened successfully
        if not cap.isOpened():
            raise IOError("Cannot open webcam")
        
        desired_fps = 15
        cap.set(cv2.CAP_PROP_FPS, desired_fps)

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
            #detector.detect_async(mp_image, int(timestamp_ms))
            detector.detect_async(mp_image, int(timestamp_ms))

            # Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            print(CURRCATEGORY)

        cap.release()
        cv2.destroyAllWindows()


def get_currentitem():
    global CURRCATEGORY
    main()
    return CURRCATEGORY

        


if __name__ == "__main__":
    main()
