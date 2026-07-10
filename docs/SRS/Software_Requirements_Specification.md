# Software Requirements Specification (SRS)

# VisionGuard-AI

**AI-Based PPE Compliance Monitoring, Worker Tracking, and Safety Violation Detection System**

| Document Information | Details |
|----------------------|---------|
| Project | VisionGuard-AI |
| Version | 1.0 |
| Status | Draft |
| Document Type | Software Requirements Specification (SRS) |
| Author |  Aina Khan |
| Last Updated | 07/06/2026 |

---

# Table of Contents

1. Introduction
2. Problem Statement
3. Project Objectives
4. System Overview
5. Functional Requirements
6. Non-Functional Requirements
7. Assumptions
8. Constraints
9. Future Scope

---

# 1. Introduction

## 1.1 Purpose

VisionGuard-AI is an AI-powered workplace safety monitoring system that uses Computer Vision and Deep Learning to detect workers, identify Personal Protective Equipment (PPE), monitor workplace safety compliance, and generate real-time alerts.

The system automates workplace safety monitoring by analyzing live video streams using computer vision and deep learning techniques.

---

## 1.2 Scope

The system is designed for construction sites. The architecture is extensible to other industrial environments.

VisionGuard-AI performs the following operations:

- Detect workers from live CCTV streams
- Detect mandatory PPE equipment
- Track workers using unique track IDs
- Detect workplace safety violations
- Generate real-time alerts
- Store violation evidence
- Maintain worker entry and exit logs
- Display live analytics through a web dashboard

The project follows a modular architecture, allowing additional features to be integrated in future phases.

---

## 1.3 Intended Users

- Site Manager
- Safety Officer
- Site Supervisor
- System Administrator
- Construction Company Management

---

# 2. Problem Statement

Construction sites often rely on manual safety inspections to ensure workers wear mandatory PPE such as helmets and safety vests. Manual monitoring is inefficient, prone to human error, and incapable of providing continuous surveillance.

Organizations require an automated system capable of detecting workers, monitoring PPE compliance, recording entry and exit events, and providing real-time alerts and analytics.

VisionGuard-AI addresses these challenges by combining AI-based object detection, worker tracking, rule-based violation detection, and live dashboard visualization into a unified safety monitoring platform.

---

# 3. Project Objectives

VisionGuard-AI aims to:

- Detect workers from live CCTV feeds.
- Detect mandatory PPE equipment.
- Track workers using temporary tracking IDs within a single camera stream.
- Verify PPE compliance automatically.
- Detect workplace safety violations.
- Generate real-time alerts.
- Capture and store violation evidence.
- Maintain worker entry and exit logs.
- Display real-time analytics through a web dashboard.
- Maintain historical violation records for later analysis.

---

# 4. System Overview

VisionGuard-AI consists of the following major modules.

| Module | Description |
|---------|-------------|
| Detection Module | Detects workers and PPE using YOLO11.|
| Worker Tracking | Assigns unique track IDs and tracks workers across consecutive video frames. |
| Rule Engine | Verifies PPE compliance against predefined workplace safety rules. |
| Alert & Violation Management | Detects violations, captures screenshots, and generates alerts. |
| Entry & Exit Monitoring | Records worker movement using virtual line crossing. |
| Database |Database stores violation records, entry/exit logs, tracking IDs, timestamps, camera IDs, and captured screenshots. |
| Live Dashboard | Displays live monitoring statistics, violation history, charts, and analytics. |

---

# 5. Functional Requirements

| ID | Requirement |
|----|-------------|
| FR-01 | Detect workers from live CCTV video streams. |
| FR-02 | Detect PPE including helmets, and vests. |
| FR-03 | Assign and maintain unique tracking IDs within each camera stream. |
| FR-04 | Verify PPE compliance using predefined safety rules. |
| FR-05 | Detect workplace safety violations in real time. |
| FR-06 | The system shall generate visual alerts within 2 seconds after detecting a violation. |
| FR-07 | Capture and store screenshots of violations. |
| FR-08 | Store violation records including tracking ID, camera ID, timestamp, and violation type. |
| FR-09 | Update the dashboard automatically in real time. |
| FR-10 | Display total violations, today's violations and worker-count. |
| FR-11 | Detect worker entry and exit using virtual line crossing. |
| FR-12 | Maintain complete entry and exit logs. |
| FR-13 | Allow filtering by date, camera, and violation type.|
| FR-14 | The system shall display the camera ID associated with each violation. |
| FR-15 | The system shall maintain worker count for each camera stream. |
| FR-16 | The system shall allow configurable virtual entry and exit lines.|

---

# 6. Non-Functional Requirements

| Category | Requirement |
|-----------|-------------|
| Performance | Process live video streams in real time with dashboard updates under 2 seconds. |
| Reliability | The system should process continuous video streams without interruption during normal operation.|
| Accuracy | Minimize false detections and false alerts while maintaining reliable worker tracking. |
| Scalability | The architecture should support future integration of multiple cameras and additional PPE classes. |
| Availability | The system should operate continuously while running. |
| Maintainability | Use a modular architecture for easier maintenance and future upgrades. |
| Usability | Provide a responsive and user-friendly dashboard with minimal training required. |

---

# 7. Assumptions

The following assumptions are made during development:

- CCTV cameras provide sufficient image quality.
- Cameras remain fixed during operation.
- Adequate lighting conditions are available.
- Workers remain visible within the camera's field of view.
- Network connectivity is stable.
- AI models are trained before deployment.
- GPU resources are available for real-time inference.
- Database services remain operational.

---

# 8. Constraints

The system may be affected by the following limitations:

- Poor lighting conditions.
- Worker occlusion.
- Fast worker movement.
- Low-resolution camera feeds.
- Camera viewing angle.
- Network latency.
- Hardware limitations affecting AI inference speed.
- Workers may partially leave the camera field of view.

---

# 9. Future Scope

## Version 2.0 – Smart Attendance System

Extend VisionGuard-AI with an AI-based attendance module using worker ID cards.

**Features**

- Automatic attendance
- Check-in / Check-out
- Attendance reports
- Shift monitoring
- Late arrival detection

---

## Version 2.0 – Cross-Camera Worker Re-Identification (ReID)

Enable continuous worker tracking across multiple cameras.

**Features**

- Cross-camera identity matching
- Multi-camera worker tracking
- Continuous worker trajectory
- Reduced identity switching
- Large-area surveillance

---

# Document Summary

| Item | Description |
|------|-------------|
| Project | VisionGuard-AI |
| Document | Software Requirements Specification (SRS) |
| Version | 1.0 |
| Status | Draft |

---

**End of Document**