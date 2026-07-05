# VisionGuard AI 👷‍♂️🦺

> An AI-powered construction safety monitoring system for real-time PPE compliance, worker occupancy monitoring, and safety analytics.

## 📌 Project Status

🚧 **Current Phase:** Week 1 – Project Setup

This repository is currently under active development. The first phase focuses on setting up the project architecture, development environment, and understanding the core computer vision technologies required for the system.

---

## 🎯 Project Goal

VisionGuard AI aims to build an intelligent safety monitoring platform capable of:

- Detecting workers in real time
- Monitoring PPE compliance (Helmet, Safety Vest, Safety Shoes)
- Tracking workers across video frames
- Logging safety violations
- Monitoring worker occupancy
- Recording worker entry and exit events
- Providing a live analytics dashboard

---

## 🛣️ Development Roadmap

### ✅ Phase 1 (Current)
- [x] Create project architecture
- [x] Create GitHub repository
- [x] Design folder structure
- [x] Prepare documentation
- [ ] Learn OpenCV fundamentals
- [ ] Learn YOLOv8 fundamentals
- [ ] Build first real-time object detection demo

### 🔜 Phase 2
- Fine-tune YOLOv8 on PPE dataset
- Integrate ByteTrack
- Develop Rule Engine
- Build SQLite database
- Create Streamlit dashboard

### 🚀 Future Phases
- OCR-based ID card attendance
- Multi-camera surveillance
- Cross-camera person re-identification
- Edge deployment using ONNX

---

## 🏗️ Project Structure

```text
VisionGuard-AI/
├── app/
├── config/
├── assets/
├── data/
├── docs/
├── experiments/
├── logs/
├── models/
├── notebooks/
├── screenshots/
├── scripts/
├── tests/
├── main.py
├── requirements.txt
└── README.md