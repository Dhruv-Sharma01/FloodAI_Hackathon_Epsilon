# 🌊 FloodAI Hackathon - Epsilon Team

![FloodAI](https://img.shields.io/badge/Hackathon-FloodAI-blue) ![Python](https://img.shields.io/badge/Python-3.9+-yellow.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

A complete end-to-end AI-driven solution developed at the **FloodAI Hackathon 2024** by Team Epsilon. Our system focuses on flood prediction, risk assessment, satellite image analysis, and real-time alert generation for Mumbai using meteorological, topographical, and urban data sources.

---

## 🚀 Features

- 📊 **Rainfall Prediction Model:**  
  Time series model trained on IMD data to forecast rainfall in mm.

- 🗺️ **Flooded Area Segmentation:**  
  Semantic segmentation using satellite images to identify flooded regions.

- 🌧️ **Risk Assessment System:**  
  Combines rainfall, elevation, drainage network, and land use data to compute flood risk across Mumbai.

- 📍 **Interactive Map & Alert System:**  
  Web-based dashboard to visualize risk zones and push alerts to residents.

- 🧠 **Integrated AI Pipeline:**  
  Combines predictive models, geospatial analysis, and real-time user interaction.

---

## 🏆 Achievements

🥉 **Secured 3rd place** at FloodAI Hackathon organized by IIT Gandhinagar and IIT Bombay Climate Studies Department.  
🔬 Developed a research-backed multi-model architecture within 36 hours.  
📍 Mumbai-focused system with real-world applicability.

---


---

## 🧠 Tech Stack

- **Languages:** Python, JavaScript (for dashboard)
- **Libraries:** TensorFlow, Keras, OpenCV, Scikit-learn, XGBoost, Pandas, NumPy, Matplotlib, Rasterio
- **Geospatial Tools:** QGIS, Folium, GeoPandas, Shapely
- **Frontend:** Leaflet.js, Streamlit
- **Other:** Google Earth Engine, SRTM DEM, IMD Rainfall Data

---

## ⚙️ How to Run

1. **Clone the repository**

```bash
git clone https://github.com/DeepMathukiya/FloodAI_Hackathon_Epsilon.git
cd FloodAI_Hackathon_Epsilon
```

2. **Run Backend**

```bash
cd backend
python app.py
```

3. **Run Frontend**
```bash 
cd frontend
yarn run dev --host
```
## Demo
<img src="https://imgur.com/i4aoKu2.gif" alt="demo">

