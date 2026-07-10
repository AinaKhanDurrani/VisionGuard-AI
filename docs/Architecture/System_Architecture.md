# System Architecture

## Overview

VisionGuard-AI follows a modular architecture in which each component is responsible for a specific stage of the monitoring pipeline. Live video streams are processed to detect workers and Personal Protective Equipment (PPE), assign temporary tracking IDs, evaluate workplace safety rules, record worker movements, generate alerts, and update the monitoring dashboard in real time.

---

## Design Goals

The system architecture is designed with the following goals:

- Modular component design
- Real-time video processing
- Easy maintenance and future upgrades
- Scalability for additional cameras and AI modules
- Extensibility for future features such as OCR-based attendance and multi-camera tracking

---

## Architecture Flow

```text
Camera
        │
        ▼
Frame Extraction
        │
        ▼
YOLO Detection
        │
        ▼
ByteTrack
        │
  ┌─────┴───────────┐
  ▼                 ▼
Entry/Exit Logger    Rule Engine
  │                 │
  ▼                 ▼
Entry/Exit Log     Alert Generator
  │                 │
  └──────────┬──────┘
             ▼
      SQLite Database
             │
             ▼
    Streamlit Dashboard
```

---

# System Modules

## 1. Camera Module

Captures live video streams from webcams, IP cameras, or CCTV systems. The captured video serves as the primary input to the monitoring pipeline.

### Responsibilities

- Capture live video streams
- Support webcams, IP cameras, and CCTV cameras
- Continuously stream video frames

---

## 2. Frame Extraction Module

Extracts individual frames from the incoming video stream using OpenCV before passing them to the AI models.

### Responsibilities

- Read video frames
- Convert the video stream into individual frames
- Resize and preprocess frames
- Prepare frames for object detection

---

## 3. Detection Module

Uses the YOLO11 object detection model to detect workers and Personal Protective Equipment (PPE) in each frame.

### Input

- Video frame

### Output

- Bounding Boxes
- Confidence Scores
- Class IDs
- Class Labels

### Detectable Objects

- Person
- Helmet
- Safety Vest

---

## 4. Tracking Module

Tracks detected workers across consecutive video frames using ByteTrack and assigns a temporary tracking ID to each worker.

### Input

- Detection results

### Output

- Track IDs
- Worker trajectories

### Responsibilities

- Assign temporary tracking IDs
- Maintain object identity across consecutive frames
- Maintain object identity during temporary occlusions whenever possible.

---

## 5. Entry & Exit Logger

Monitors worker movement using a virtual entry/exit line. When a tracked worker crosses the line, the system records an entry or exit event.

### Input

- Track IDs
- Worker trajectories

### Output

- Entry records
- Exit records

### Responsibilities

- Detect virtual line crossings
- Record entry timestamps
- Record exit timestamps
- Update worker status

---

## 6. Rule Engine

Evaluates each tracked worker against predefined workplace safety rules to determine PPE compliance.

### Input

- Detection results
- Tracking results

### Output

- Violation events

### Example Rules

- IF Person detected AND Helmet missing THEN Generate Helmet Violation
- IF Person detected AND Saftey Vast missing THEN Generate Saftey Vast Violation

The Rule Engine receives detection and tracking results, evaluates predefined safety rules, and generates a violation event whenever a worker fails to meet the required PPE conditions.

---

## 7. Alert Module

Generates real-time alerts whenever a safety violation is detected.

### Responsibilities

- Display warning notifications
- Capture violation screenshots
- Send violation events to the database

---

## 8. Database Module

Stores all monitoring records for future retrieval and analysis.

### Responsibilities

- Store violation records
- Store entry and exit logs
- Store timestamps
- Store camera IDs
- Store screenshot paths

---

## 9. Live Dashboard

Provides real-time visualization of monitoring results and historical analytics.

### Features

- Live camera feed
- Current worker count
- Today's violations
- Violation log
- Entry and exit log
- Violation analytics

---

# Data Flow

1. The camera captures a live video stream.
2. OpenCV extracts individual video frames.
3. YOLO11 detects workers and PPE.
4. ByteTrack assigns and maintains tracking IDs.
5. The Entry & Exit Logger monitors virtual line crossings.
6. The Rule Engine evaluates PPE compliance.
7. Safety violations trigger real-time alerts and screenshot capture.
8. Entry/exit logs and violation records are stored in the SQLite database.
9. The Streamlit dashboard displays live monitoring information and historical analytics.

---

# Architecture Characteristics

- **Modular:** Each component can be developed, tested, and maintained independently.
- **Scalable:** Supports future integration of multiple cameras and additional AI models.
- **Real-Time:** Designed for continuous live video processing with minimal latency.
- **Maintainable:** Individual modules can be modified without affecting the overall system.
- **Extensible:** Supports future features such as OCR-based attendance, worker re-identification, and multi-camera surveillance.

---

# Technology Stack

| Module | Technology |
|----------|------------|
| Camera | OpenCV |
| Frame Extraction | OpenCV |
| Object Detection | YOLO11 (Ultralytics) |
| Object Tracking | ByteTrack |
| Rule Engine | Python |
| Alert Generation | Python |
| Database | SQLite |
| Dashboard | Streamlit |

---

# Future Enhancements

## Version 2

- OCR-based worker ID card recognition
- Automatic attendance management
- Shift monitoring
- Attendance reports

## Version 3

- Multi-camera surveillance
- Cross-camera worker re-identification (ReID)
- Global worker identity management
- Site-wide worker trajectory tracking