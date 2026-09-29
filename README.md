# 🚀 AstroGuard AI

## AI-Powered Space Object Risk & Observation Assistant

AstroGuard AI is a space-data prototype developed for the Asteria '26 Open Challenge. It analyzes basic space-object telemetry such as distance from Earth, velocity, and object size, and estimates an observation priority.

## 🌌 Problem

Space-object monitoring involves analyzing multiple characteristics to determine which objects may require closer observation. AstroGuard AI provides a simple interactive dashboard for exploring this concept.

## 💡 Solution

The application allows users to:

- Select a space object from a telemetry dataset
- View its distance, velocity, and size
- Calculate a prototype risk score
- Classify the observation priority as LOW, MEDIUM, or HIGH
- View a telemetry summary
- Visualize the object's telemetry

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- CSV Dataset

## 📁 Project Structure

```text
AstroGuard-AI/
├── app.py
├── app_backup.py
├── ml_model.py
├── requirements.txt
├── README.md
└── data/
    └── sample_objects.csv