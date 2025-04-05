# Raspberry Pi Smart Traffic Management System Using YOLOv5 and Real-Time Vehicle Detection

## 📸 Project Overview
A real-time smart traffic management system using Raspberry Pi, YOLOv4 and YOLOv3, and 4 webcams to detect vehicles, monitor congestion, and dynamically control traffic lights at intersections. Designed for efficient urban traffic flow using low-cost, AI-powered edge computing.

📍 **Deployment Location:** Curry Avenue and Arteche Boulevard Intersection, Catbalogan City, Philippines

---

## 🧠 Features
- Real-time vehicle detection using YOLOv5
- Congestion monitoring per lane
- Adaptive traffic light control logic
- Edge computing on Raspberry Pi
- Scalable for future smart city intersections

---

## ⚙️ Hardware Components
- Raspberry Pi 4 (Raspbian OS)
- 4 USB Webcams
- 4 Traffic Light Modules (LEDs)
- Relay Modules
- Breadboard, Jumper Wires, Power Supply

---

## 🧰 Software Stack
| Component        | Description                    |
|------------------|--------------------------------|
| Python 4/3       | Programming Language           |
| OpenCV           | Video & Image Processing       |
| YOLOv5 (PyTorch) | Real-Time Object Detection     |
| RPi.GPIO         | GPIO Control for LEDs/Relays   |

---

## 🔄 System Architecture
```
[4 Webcams] ---> [YOLOv5 Detection] ---> [Traffic Analysis] ---> [Signal Controller]
                                     ↑                          ↓
                              [Raspberry Pi] <--- [Timing Logic & Control]
```

---

## 📂 Project Structure
```
microprocessor/
├── camera_stream.py       # Multi-camera video feed
├── detect.py              # YOLOv5-based detection and bounding box logic
├── traffic_logic.py       # Traffic light timing optimization
├── gpio_control.py        # GPIO traffic light control
├── yolov5/                # YOLOv5 model and weights
├── data/
│   ├── images/            # Sample training images
│   └── labels/            # Annotated YOLO format labels
└── README.md              # Documentation
```

---

## 🔁 How It Works
1. **Data Collection**: Webcams collect traffic footage
2. **Detection**: YOLOv5 detects vehicles from video frames
3. **Analysis**: Count and analyze vehicles in each lane
4. **Decision**: Identify congestion and determine timing
5. **Control**: Raspberry Pi controls traffic lights accordingly

---

## ⚡ Traffic Light Logic
- Each direction evaluated based on real-time vehicle count
- More congested lanes receive longer green signal duration
- Prevents starvation by using a fair cycle reset logic

---

## 📈 Model Training Pipeline
1. Data Gathering using cameras/drones
2. Annotation with bounding boxes
3. Training with YOLOv5s model
4. Validation with test set
5. Deployment to Raspberry Pi

---

## 🧪 Testing
- Simulated and real-world intersection testing
- Measured detection latency and system response
- Performed optimizations for Raspberry Pi compatibility

---

## 🔧 Future Improvements
- Add vehicle type classification (motorcycle, car, bus)
- Cloud-based dashboard for remote monitoring
- GPS and routing integration
- Model Enhancement and RPi 4 compatibility

---

## 👨‍💻 Authors
- **Nathaniel C. Llano**

---

## 📜 References
- YOLOv5: https://docs.ultralytics.com/
- OpenCV: https://opencv.org/
- Raspberry Pi GPIO: https://gpiozero.readthedocs.io/en/stable/

---

> Built as a final project for a Microprocessor System course, showcasing real-time AI in smart city infrastructure.

