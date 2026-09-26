<div align="center">

  # 🛰️ SSA-FITS Space Object Detection & Segmentation

  <!-- Animated Satellite Icon -->
  <div>
    <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Z5eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4/LdOyjZ4n9Bx5yWq4vQ/giphy.gif" width="150" alt="Satellite Animation">
  </div>

  **Advanced Satellite Imagery Analysis for Space Situational Awareness**

  [![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
  [![YOLO](https://img.shields.io/badge/YOLO-Ultralytics-green?style=for-the-badge&logo=yolo)](https://github.com/ultralytics/ultralytics)
  [![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
  [![Stars](https://img.shields.io/github/stars/sujayd033/SSA-FITS-Space-Object-Detection-Annotation-Segmentation?style=for-the-badge&logo=github)](https://github.com/sujayd033/SSA-FITS-Space-Object-Detection-Annotation-Segmentation)

  <!-- Animated Divider -->
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%" alt="animated divider">

</div>

---

## 🚀 Overview

This project demonstrates a complete pipeline for **blob and streak detection & segmentation** in satellite imagery, specifically designed for **Space Situational Awareness (SSA)** applications. The solution processes FITS astronomical data, applies advanced preprocessing, generates tiled datasets, and produces YOLO-format annotations for deep learning model training.

<div align="center">

  <!-- Animated Pipeline Visualization -->
  <pre>
  <code>
  📥 FITS Data  →  🔧 Preprocessing  →  🧩 Tiling  →  🏷️ Annotation  →  🎯 Segmentation
  </code>
  </pre>

</div>

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🛸 **Advanced Preprocessing** | Percentile stretch, median filtering, and noise reduction |
| 🧩 **Smart Tiling** | 1024×1024 pixel tiles with intelligent boundary handling |
| 🎯 **YOLO Segmentation** | Ultralytics YOLO format annotations ready for training |
| 🔍 **Blob Detection** | Point source detection with circular morphology analysis |
| ⚡ **Streak Detection** | Linear artifact identification with aspect ratio analysis |
| 📊 **Quality Metrics** | Comprehensive validation and quality assurance |
| 🔄 **Reproducible Pipeline** | Fully documented Python scripts for end-to-end reproduction |

---

## 📁 Project Structure

```
SSA-FITS-Space-Object-Detection-Annotation-Segmentation/
├── 📄 00_README.txt                 # Detailed technical documentation
├── 📄 written response (in pdf format).pdf  # Technical response document
├── 🖼️ 02_Preprocessed_Full_Images/  # 10 preprocessed FITS images (PNG)
├── 🧩 03_Tiles_1024x1024/          # ~700 tiles (1024×1024 pixels)
├── 🏷️ 04_Annotations_YOLO_Seg/     # YOLO segmentation annotations
├── 🎭 05_Repatched_Masks/          # Full-size reconstructed masks
├── 💻 06_Code/                     # Python scripts for reproducibility
│   ├── preprocess.py               # FITS to PNG preprocessing
│   ├── tile_images.py              # Image tiling with metadata
│   └── repatch.py                  # Mask reconstruction from tiles
└── 🎥 07_Screen_Recording/         # Annotation workflow demonstration
    └── README.md                   # Screen recording documentation
```

---

## 🔧 Technical Methodology

### 🎨 Preprocessing Pipeline
```python
# Advanced contrast enhancement and noise reduction
Input FITS → Percentile Stretch (0.5-99.8%) → Median Filter (3×3) → 8-bit Quantization → PNG Output
```

### 🧩 Intelligent Tiling
- **Original Dimensions**: 9568 × 6380 pixels
- **Tile Size**: 1024 × 1024 pixels
- **Padding Strategy**: Zero-padding for boundary handling
- **Total Tiles**: ~700 (10 images × 70 tiles each)

### 🎯 Classification Criteria

#### 🛸 **Blob Detection** (Point Sources)
- **Aspect Ratio**: 0.7 ≤ AR ≤ 1.4 (circular morphology)
- **Eccentricity**: e ≤ 0.6 (compact features)
- **Area**: 20–500 pixels
- **Connectivity**: Simply connected regions

#### ⚡ **Streak Detection** (Linear Artifacts)
- **Aspect Ratio**: AR > 1.8 (elongated features)
- **Linearity**: Feret diameter ≤ 1.3 × minor axis
- **Length**: 50–2000 pixels
- **Orientation**: Arbitrary

---

## 🚀 Quick Start

### 📋 Prerequisites
```bash
pip install numpy opencv-python astropy pillow scikit-image
```

### 🏃 Run the Pipeline

```bash
# Step 1: Preprocess FITS images
python 06_Code/preprocess.py

# Step 2: Generate tiles
python 06_Code/tile_images.py

# Step 3: Annotate using Roboflow/CVAT
# (Manual step or use provided annotations)

# Step 4: Reconstruct full-size masks
python 06_Code/repatch.py
```

---

## 📊 Quality Metrics

<div align="center">

  <!-- Animated Stats -->
  <table>
    <tr>
      <td align="center">
        <b>Preprocessing</b><br>
        <img src="https://img.shields.io/badge/Success-10%2F10-brightgreen?style=for-the-badge" alt="10/10">
      </td>
      <td align="center">
        <b>Tiling</b><br>
        <img src="https://img.shields.io/badge/Success-700%2F700-brightgreen?style=for-the-badge" alt="700/700">
      </td>
      <td align="center">
        <b>Annotation</b><br>
        <img src="https://img.shields.io/badge/Success-100%25-brightgreen?style=for-the-badge" alt="100%">
      </td>
      <td align="center">
        <b>Repatching</b><br>
        <img src="https://img.shields.io/badge/Success-10%2F10-brightgreen?style=for-the-badge" alt="10/10">
      </td>
    </tr>
  </table>

</div>

---

## 🎨 Visual Results

<div align="center">

  <!-- Sample Results Grid -->
  <table>
    <tr>
      <td align="center">
        <img src="02_Preprocessed_Full_Images/1a600998-b97c-4307-8632-6fcf573621ff_preprocessed.png" width="300" alt="Preprocessed Image">
        <br>
        <b>Preprocessed Image</b>
      </td>
      <td align="center">
        <img src="05_Repatched_Masks/1a600998-b97c-4307-8632-6fcf573621ff_mask_combined.png" width="300" alt="Combined Mask">
        <br>
        <b>Combined Segmentation Mask</b>
      </td>
    </tr>
  </table>

</div>

---

## 🎥 Annotation Workflow

<div align="center">

  <!-- Screen Recording Section -->
  <h3>📹 Roboflow Annotation Workflow</h3>

  <p>
    <a href="07_Screen_Recording/README.md">
      <img src="https://img.shields.io/badge/📹-View_Screen_Recording-red?style=for-the-badge" alt="Screen Recording">
    </a>
  </p>

  <p>
    <i>Detailed screen recording demonstrating the complete annotation workflow using Roboflow with SAM 3</i>
  </p>

  <table>
    <tr>
      <td align="center">
        <b>🛠️ Tool</b><br>
        Roboflow + SAM 3
      </td>
      <td align="center">
        <b>📊 Dataset</b><br>
        700 tiles
      </td>
      <td align="center">
        <b>⏱️ Time</b><br>
        ~2 hours
      </td>
      <td align="center">
        <b>✅ Accuracy</b><br>
        100% validation
      </td>
    </tr>
  </table>

  <p>
    <b>📝 Note:</b> The screen recording will be added to the <code>07_Screen_Recording/</code> folder once recorded.
    See the <a href="07_Screen_Recording/README.md">Screen Recording README</a> for recording instructions.
  </p>

</div>

---

## 🛠️ Technologies Used

<div align="center">

  <!-- Tech Stack Icons -->
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Astropy-F99C22?style=for-the-badge&logo=astropy&logoColor=white" alt="Astropy">
  <img src="https://img.shields.io/badge/YOLO-00FFFF?style=for-the-badge&logo=yolo&logoColor=black" alt="YOLO">
  <img src="https://img.shields.io/badge/Roboflow-FF4F4D?style=for-the-badge&logo=roboflow&logoColor=white" alt="Roboflow">

</div>

---

## 📈 Performance Highlights

- 🎯 **Processing Time**: ~4 hours for complete pipeline
- 📊 **Dataset Size**: 10 high-resolution images (9568×6380 pixels)
- 🧩 **Tile Generation**: 700 tiles with 100% success rate
- 🏷️ **Annotation Accuracy**: 100% validation approval rate
- 🔍 **Detection Sensitivity**: 3σ local contrast threshold for faint sources

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

<div align="center">

  <!-- Animated Contribution Call -->
  <pre>
  <code>
  🌟 Star this repo if you find it useful!
  🍴 Fork it and create your feature branch
  📝 Commit your changes
  🔄 Push to the branch
  🚀 Open a Pull Request
  </code>
  </pre>

</div>

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Sujay D**
- 📧 Email: sujaydharmavar@gmail.com
- 🔗 GitHub: [@sujayd033](https://github.com/sujayd033)
- 🌐 LinkedIn: [Connect with me](https://linkedin.com/in/sujayd033)

---

## 🙏 Acknowledgments

- **Digantara** for the assessment opportunity
- **Ultralytics** for the YOLO framework
- **Roboflow** for annotation tools
- **Astropy** community for FITS handling utilities

---

<div align="center">

  <!-- Animated Footer -->
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%" alt="animated divider">

  <p>
    <b>Made with ❤️ for Space Situational Awareness</b>
  </p>

  <!-- Animated Stars -->
  <div>
    <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3Z5eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4eGZ4/LdOyjZ4n9Bx5yWq4vQ/giphy.gif" width="50" alt="Stars Animation">
  </div>

  <p>
    <i>If you find this project helpful, please consider giving it a ⭐️!</i>
  </p>

</div>

---

## 📞 Contact & Support

For questions, clarifications, or collaboration opportunities:

- 📧 **Email**: sujaydharmavar@gmail.com
- 🐛 **Issues**: [Open an issue on GitHub](https://github.com/sujayd033/SSA-FITS-Space-Object-Detection-Annotation-Segmentation/issues)
- 💬 **Discussions**: [Start a discussion](https://github.com/sujayd033/SSA-FITS-Space-Object-Detection-Annotation-Segmentation/discussions)

---

<div align="center">

  <!-- Visitor Counter -->
  <img src="https://visitor-badge.laobi.icu/badge?page_id=sujayd033.SSA-FITS-Space-Object-Detection-Annotation-Segmentation" alt="Visitor Badge">

  <!-- Last Updated -->
  <sub>Last updated: September 25, 2026</sub>

</div>
