import cv2
import json
import numpy as np
import re
from pathlib import Path
from tqdm import tqdm

# ========== YOUR PATHS ==========
yolo_train_folder = Path(r"C:\Users\thesk\Music\digantra project\-Digantara company  Assessment-.v1i.yolov8  new\train")
yolo_labels_folder = yolo_train_folder / "labels"
yolo_images_folder = yolo_train_folder / "images"
tiling_metadata_folder = Path(r"C:\Users\thesk\Music\digantra project\Tiling_Metadata")
output_masks_folder = Path(r"C:\Users\thesk\Music\digantra project\Repatched_Masks")
# ================================

output_masks_folder.mkdir(parents=True, exist_ok=True)

def yolo_polygon_to_mask(normalized_points, tile_size=1024):
    """Convert YOLO normalized polygon to binary mask."""
    mask = np.zeros((tile_size, tile_size), dtype=np.uint8)
    
    if len(normalized_points) < 3:
        return mask
    
    points = np.array(normalized_points).reshape(-1, 2)
    points[:, 0] *= tile_size
    points[:, 1] *= tile_size
    points = points.astype(np.int32)
    
    cv2.fillPoly(mask, [points], 255)
    return mask

def extract_tile_coords(filename):
    """Extract tile row and col from filename like 'xxx_tile_00_00.png'"""
    match = re.search(r'_tile_(\d{2})_(\d{2})', filename)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None, None

def repatch_all_images():
    """Reconstruct full-size masks from tiled YOLO annotations."""
    
    metadata_files = list(tiling_metadata_folder.glob("*_metadata.json"))
    label_files = list(yolo_labels_folder.glob("*.txt"))
    
    print(f"Found {len(metadata_files)} metadata files")
    print(f"Found {len(label_files)} YOLO label files")
    
    # Create mapping from image filename to label filename
    image_to_label = {}
    for label_file in label_files:
        # label_file.stem is the filename without extension
        # Find corresponding image
        image_candidates = list(yolo_images_folder.glob(label_file.stem + "*"))
        if image_candidates:
            image_to_label[label_file.stem] = label_file
    
    print(f"Matched {len(image_to_label)} images to labels")
    
    for metadata_file in tqdm(metadata_files, desc="Repatching images"):
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
        
        image_name = metadata_file.stem.replace("_metadata", "")
        original_h, original_w = metadata['original_shape']
        padded_h, padded_w = metadata['padded_shape']
        tile_positions = metadata['tile_positions']
        tiles_per_row = metadata['tiles_per_row']
        tiles_per_col = metadata['tiles_per_col']
        tile_size = metadata['tile_size']
        
        # Create full-size masks
        full_mask_blob = np.zeros((padded_h, padded_w), dtype=np.uint8)
        full_mask_streak = np.zeros((padded_h, padded_w), dtype=np.uint8)
        
        # Process each tile
        for row in range(tiles_per_col):
            for col in range(tiles_per_row):
                tile_idx = row * tiles_per_row + col
                y, x = tile_positions[tile_idx]
                
                # Find label file for this tile
                label_file = None
                for lf in label_files:
                    tile_row, tile_col = extract_tile_coords(lf.stem)
                    if tile_row == row and tile_col == col:
                        label_file = lf
                        break
                
                if label_file:
                    try:
                        with open(label_file, 'r') as f:
                            lines = f.readlines()
                        
                        for line in lines:
                            parts = line.strip().split()
                            if len(parts) < 7:
                                continue
                            
                            class_id = int(parts[0])
                            normalized_points = [float(p) for p in parts[1:]]
                            
                            tile_mask = yolo_polygon_to_mask(normalized_points, tile_size)
                            
                            # Place in full mask
                            y_end = min(y + tile_size, padded_h)
                            x_end = min(x + tile_size, padded_w)
                            tile_h = y_end - y
                            tile_w = x_end - x
                            
                            if class_id == 0:  # blob
                                full_mask_blob[y:y_end, x:x_end] = np.maximum(
                                    full_mask_blob[y:y_end, x:x_end],
                                    tile_mask[:tile_h, :tile_w]
                                )
                            elif class_id == 1:  # streak
                                full_mask_streak[y:y_end, x:x_end] = np.maximum(
                                    full_mask_streak[y:y_end, x:x_end],
                                    tile_mask[:tile_h, :tile_w]
                                )
                    except Exception as e:
                        print(f"Error reading {label_file}: {e}")
                        continue
        
        # Remove padding to get original size
        full_mask_blob = full_mask_blob[:original_h, :original_w]
        full_mask_streak = full_mask_streak[:original_h, :original_w]
        
        # Save individual masks
        blob_output = output_masks_folder / f"{image_name}_mask_blob.png"
        streak_output = output_masks_folder / f"{image_name}_mask_streak.png"
        
        cv2.imwrite(str(blob_output), full_mask_blob)
        cv2.imwrite(str(streak_output), full_mask_streak)
        
        # Save combined visualization (RGB)
        combined = np.zeros((original_h, original_w, 3), dtype=np.uint8)
        combined[full_mask_blob > 0] = [0, 255, 0]  # Green = blob
        combined[full_mask_streak > 0] = [0, 0, 255]  # Red = streak
        overlap = (full_mask_blob > 0) & (full_mask_streak > 0)
        combined[overlap] = [255, 255, 0]  # Yellow = overlap
        
        combined_output = output_masks_folder / f"{image_name}_mask_combined.png"
        cv2.imwrite(str(combined_output), combined)

try:
    repatch_all_images()
    print(f"\n✅ Repatching complete!")
    print(f"Masks saved to: {output_masks_folder}")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()