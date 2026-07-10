# VisionGuard-AI Learning Journal

# Day 1 – OpenCV Fundamentals

## Objective

Establish a foundation in OpenCV by learning basic image processing, video capture, drawing functions, and image manipulation techniques that will be required throughout the VisionGuard-AI project.

---

## Work Completed

### Key APIs Explored

- `cv2.imread()`
- `cv2.imshow()`
- `cv2.imwrite()`
- `cv2.VideoCapture()`
- `cv2.rectangle()`
- `cv2.circle()`
- `cv2.line()`
- `cv2.putText()`
- `cv2.resize()`

### Concepts Learned

#### Image Operations

- Loaded images using `cv2.imread()`.
- Displayed images using `cv2.imshow()`.
- Saved processed images using `cv2.imwrite()`.

#### Video Processing

- Captured video from a webcam using `cv2.VideoCapture()`.
- Learned that a video is a sequence of individual image frames.
- Understood how OpenCV reads and processes one frame at a time.

#### Drawing Functions

- Drew straight lines using `cv2.line()`.
- Drew rectangles using `cv2.rectangle()`.
- Drew circles using `cv2.circle()`.
- Added labels using `cv2.putText()`.

#### Image Manipulation

- Explored image properties such as height, width, channels, and shape.
- Resized images using `cv2.resize()`.
- Cropped images using NumPy array slicing.

---

## Knowledge Gained

Today I learned that OpenCV represents images as NumPy arrays, making image manipulation intuitive using existing NumPy knowledge.

I also understood that OpenCV serves as the interface between the camera and computer vision models by capturing, processing, and preparing video frames before they are analyzed by AI models such as YOLO.

---

## Application to VisionGuard-AI

The concepts learned today will be used throughout the project to:

- Capture live CCTV camera streams.
- Process video frames before object detection.
- Resize frames for efficient inference.
- Draw bounding boxes around detected workers.
- Display class labels, confidence scores, and tracking IDs.
- Draw virtual entry and exit lines on the video feed.

---

## Engineering Decision

OpenCV will be used as the primary video processing library throughout VisionGuard-AI because it provides efficient image processing, video capture, frame manipulation, and visualization capabilities while integrating seamlessly with YOLO11.

---

## Challenges Encountered

No significant technical challenges were encountered during today's learning.

Existing experience with NumPy made understanding OpenCV image operations straightforward.

---

## Reflection

Today's session established the foundation for the entire VisionGuard-AI pipeline. I now understand that OpenCV is responsible for acquiring and processing video frames, while the AI model focuses on analyzing those frames to detect objects. This separation of responsibilities will make the system architecture cleaner and easier to maintain.

---

## Next Steps

- Learn OpenCV color spaces (BGR, RGB, Grayscale, HSV).
- Explore mouse event handling.
- Understand how these concepts can be used to configure interactive safety zones.

---

# Day 2 – Color Spaces and Mouse Events

## Objective

Learn how OpenCV handles color space conversions and mouse events, and understand how these features can be used to build interactive computer vision applications.

---

## Work Completed

### Key APIs Explored

- `cv2.cvtColor()`
- `cv2.setMouseCallback()`

### Mouse Event Constants

- `cv2.EVENT_MOUSEMOVE`
- `cv2.EVENT_LBUTTONDOWN`
- `cv2.EVENT_RBUTTONDOWN`
- `cv2.EVENT_LBUTTONUP`
- `cv2.EVENT_LBUTTONDBLCLK`
- `cv2.EVENT_MOUSEWHEEL`

### Concepts Learned

#### Color Space Conversion

- Converted images from BGR to Grayscale using `cv2.cvtColor()`.
- Converted images from BGR to RGB.
- Converted images from BGR to HSV.
- Learned when different color spaces are useful for computer vision tasks.

#### Mouse Events

- Registered mouse events using `cv2.setMouseCallback()`.
- Implemented a callback function that receives the mouse event type and the `(x, y)` cursor coordinates.
- Used `cv2.EVENT_LBUTTONDBLCLK` to draw a circle at the location where the user double-clicks.
- Learned that mouse callbacks enable interactive image annotation and configuration.

---

## Knowledge Gained

Today I learned that OpenCV supports multiple color spaces, each designed for different computer vision tasks. Although images are loaded in the BGR format by default, converting them to RGB, Grayscale, or HSV enables different types of image analysis.

I also learned that OpenCV provides an event-driven mechanism through mouse callbacks, allowing users to interact directly with images by capturing cursor coordinates and mouse actions. This makes it possible to build configurable interfaces without modifying application code.

---

## Application to VisionGuard-AI

The concepts learned today will be used to:

- Allow the site manager to interactively draw virtual entry and exit lines.
- Enable future support for defining restricted zones directly on the camera feed.
- Store selected coordinates as configuration for the rule engine.

---

## Engineering Decision

Interactive configuration using mouse events will be preferred over hardcoded coordinates. This approach allows safety zones and virtual entry/exit lines to be defined visually and stored as configuration, making the system easier to adapt to different camera layouts.

---

## Challenges Encountered

No significant technical challenges were encountered during today's learning. The concepts were straightforward to understand through experimentation with OpenCV examples.

---

## Reflection

Today's session demonstrated that OpenCV is not limited to image processing. It also provides mechanisms for human-computer interaction through mouse events. This capability will allow VisionGuard-AI to support configurable safety zones and virtual entry/exit lines without requiring code modifications.

---

## Next Steps

- Learn how YOLO11 performs object detection.
- Understand the YOLO inference pipeline.
- Explore the `Results` object returned by YOLO11.
- Learn how bounding boxes, class IDs, and confidence scores are represented.
- Run inference on images, videos, and webcam streams.

---

# Day 3 – YOLO11 Inference Basics

## Objective

Learn how to run inference using YOLO11, understand how video frames are processed, and explore the structure of the detection results returned by the model.

---

## Work Completed

### Key APIs Explored

- `cv2.VideoCapture()`
- `cap.read()`
- `YOLO("yolo11n.pt")`
- `model(frame)`
- `results[0].plot()`

### Concepts Learned

#### Video Frame Processing

- Used `cv2.VideoCapture()` to read a video.
- Learned that a video is processed frame by frame.
- Used `cap.read()` to retrieve one frame at a time for processing.

#### YOLO11 Inference

- Imported the YOLO model from the Ultralytics library.
- Loaded the pretrained `yolo11n.pt` model.
- Passed an image or video frame to `model()` for object detection.
- Learned that `model()` performs inference and returns a `Results` object.
- Used `results[0].plot()` to visualize detections, including:
  - Bounding boxes
  - Class labels
  - Confidence scores
  - Segmentation masks (when applicable)
  - Pose keypoints (when using pose models)

---

## Knowledge Gained

Today I learned how the YOLO inference pipeline works. Each frame captured using OpenCV can be passed directly to the YOLO model, which returns detection results in a structured format.

I also learned that the `Results` object contains all prediction information and provides convenient methods such as `plot()` for visualization.

---

## Application to VisionGuard-AI

The concepts learned today will be used to:

- Run real-time object detection on CCTV video streams.
- Detect workers and safety equipment in each frame.
- Visualize detection results during development.
- Integrate YOLO inference into the VisionGuard-AI processing pipeline.

Additionally, I plan to fine-tune the pretrained YOLO11 model on a custom PPE dataset instead of training from scratch. Transfer learning will provide better accuracy while requiring significantly less training data and computational resources.

---

## Engineering Decision

YOLO11 will be used as the object detection engine for VisionGuard-AI. OpenCV will handle video capture and frame preprocessing, while YOLO11 will perform inference on each frame. Separating these responsibilities will make the overall system more modular and easier to maintain.

---

## Challenges Encountered

No significant technical challenges were encountered during today's learning.

One observation was that the default YOLO workflow stores prediction outputs in its own directory structure. For VisionGuard-AI, custom output management will be implemented using OpenCV together with YOLO so that processed images and videos can be saved within the project's predefined folder structure.

---

## Reflection

Today's session helped me understand how OpenCV and YOLO work together in a computer vision pipeline. OpenCV is responsible for reading and preparing video frames, while YOLO analyzes each frame and returns structured detection results. This clear separation of responsibilities aligns well with the architecture planned for VisionGuard-AI.

---

## Next Steps

- Explore the `Results` object in more detail.
- Extract bounding box coordinates, class IDs, and confidence scores.
- Learn object tracking using ByteTrack.
- Integrate tracking with YOLO11 for persistent object IDs.