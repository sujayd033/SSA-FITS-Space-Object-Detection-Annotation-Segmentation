# 🤝 Contributing to SSA-FITS Space Object Detection

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing.

## 🚀 How to Contribute

### Reporting Bugs
- Check existing issues to avoid duplicates
- Use a clear and descriptive title
- Provide detailed information about the bug
- Include steps to reproduce the issue
- Add relevant screenshots and logs

### Suggesting Enhancements
- Use a clear and descriptive title
- Provide a detailed description of the enhancement
- Explain why this enhancement would be useful
- Provide examples of how the enhancement would be used

### Pull Request Process
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Development Setup

### Prerequisites
- Python 3.8 or higher
- Git
- Virtual environment (recommended)

### Installation Steps
```bash
# Clone the repository
git clone https://github.com/sujayd033/SSA-FITS-Space-Object-Detection-Annotation-Segmentation.git
cd SSA-FITS-Space-Object-Detection-Annotation-Segmentation

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🧪 Testing

Run the preprocessing pipeline:
```bash
python 06_Code/preprocess.py
```

Run the tiling process:
```bash
python 06_Code/tile_images.py
```

Run the repatching process:
```bash
python 06_Code/repatch.py
```

## 📝 Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular
- Add comments for complex logic

## 🎯 Project Structure

- `06_Code/` - Main Python scripts
- `02_Preprocessed_Full_Images/` - Preprocessed images
- `03_Tiles_1024x1024/` - Tiled images
- `04_Annotations_YOLO_Seg/` - YOLO annotations
- `05_Repatched_Masks/` - Reconstructed masks

## 📧 Contact

For questions about contributing:
- Email: sujaydharmavar@gmail.com
- GitHub: [@sujayd033](https://github.com/sujayd033)

## 🙏 Acknowledgments

Thank you for considering contributing to this project! Your contributions help make this project better for everyone.
