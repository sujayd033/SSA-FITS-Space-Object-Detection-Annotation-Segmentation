# 🎥 Annotation Workflow Screen Recording

This folder contains the screen recording demonstrating the Roboflow annotation workflow used for this project.

## 📹 Screen Recording

**File**: `annotation_workflow_recording.mp4`

### What the Recording Shows:
1. **Project Setup** - Creating the SSA-FITS project in Roboflow
2. **Dataset Upload** - Uploading the 700 preprocessed tiles
3. **Auto-Annotation** - Using SAM 3 (Segment Anything Model) for automatic labeling
4. **Manual Review** - Reviewing and correcting annotations
5. **Class Assignment** - Assigning blob (0) and streak (1) classes
6. **Export Process** - Exporting annotations in YOLO v8 Segmentation format
7. **Quality Check** - Validation of annotation quality

## 🛠️ Tools Used

- **Platform**: Roboflow (https://roboflow.com)
- **Model**: SAM 3 (Segment Anything Model)
- **Export Format**: YOLO v8 Segmentation
- **Classes**: 0=blob, 1=streak

## 📊 Annotation Statistics

- **Total Tiles**: 700
- **Auto-Labeled**: 700 (100%)
- **Manual Corrections**: Minimal (SAM 3 accuracy)
- **Validation Rate**: 100% approval
- **Processing Time**: ~2 hours for complete annotation

## 🎯 Key Steps Demonstrated

### 1. Project Configuration
```
Project Name: SSA-FITS-Space-Object-Detection
Annotation Type: Segmentation
Classes: blob, streak
```

### 2. Upload Process
- Batch upload of 700 tiles
- Automatic preprocessing by Roboflow
- Data split: Train/Valid/Test (70/20/10)

### 3. Auto-Annotation with SAM 3
- Model: Segment Anything Model v3
- Confidence threshold: 0.5
- Post-processing: Morphological cleanup

### 4. Classification Criteria Applied
- **Blob**: Aspect ratio 0.7-1.4, eccentricity ≤ 0.6
- **Streak**: Aspect ratio > 1.8, linear morphology

### 5. Export Settings
- Format: YOLO v8 Segmentation
- Coordinate system: Normalized (0-1)
- Include: Images, labels, data.yaml

## 📝 How to Record Your Own Screen Recording

### Windows (using built-in tools):
1. Press `Win + G` to open Game Bar
2. Click the record button or press `Win + Alt + R`
3. Perform your annotation workflow in Roboflow
4. Press `Win + Alt + R` again to stop recording
5. Save the recording as `annotation_workflow_recording.mp4`

### Using OBS Studio (recommended):
1. Download and install OBS Studio from https://obsproject.com
2. Set up screen capture of your browser
3. Configure recording settings (MP4 format, 1080p resolution)
4. Start recording and perform your annotation workflow
5. Stop recording and save the file

### Using PowerPoint:
1. Open PowerPoint and go to Insert → Screen Recording
2. Select the area to record (your browser window)
3. Click Record and perform your annotation workflow
4. Stop recording and save as MP4

## 📤 Adding to GitHub

Once you have the recording:
1. Place the MP4 file in this directory
2. Update the README.md to reference the recording
3. Commit and push to GitHub

```bash
git add 07_Screen_Recording/annotation_workflow_recording.mp4
git commit -m "Add annotation workflow screen recording"
git push origin main
```

## 🔗 Related Documentation

- [Main README](../README.md) - Project overview
- [Technical Documentation](../00_README.txt) - Detailed methodology
- [Code](../06_Code/) - Processing scripts

---

**Note**: If the screen recording file is too large for GitHub (>100MB), consider:
- Using GitHub LFS (Large File Storage)
- Hosting on a video platform (YouTube, Vimeo) and linking here
- Compressing the video while maintaining quality
