import cv2
import json
import numpy as np
from pathlib import Path
from tqdm import tqdm

# ========== YOUR PATHS ==========
input_folder = Path(r"C:\Users\thesk\Music\digantra project\Preprocessed_Images")
tiles_output_folder = Path(r"C:\Users\thesk\Music\digantra project\Tiles_1024x1024")
metadata_output_folder = Path(r"C:\Users\thesk\Music\digantra project\Tiling_Metadata")
# ================================

tiles_output_folder.mkdir(parents=True, exist_ok=True)
metadata_output_folder.mkdir(parents=True, exist_ok=True)

TILE_SIZE = 1024

def tile_image(image_path, tile_size=1024, pad_value=0):
    """
    Tile an image to tile_size x tile_size with zero-padding.
    Returns: tiles (list), positions (list of (y, x) tuples), padding info, original shape
    """
    img = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Could not read {image_path}")
    
    h, w = img.shape[:2]
    original_shape = (h, w)
    
    # Calculate padding needed to make dimensions multiples of tile_size
    pad_h = (tile_size - h % tile_size) % tile_size
    pad_w = (tile_size - w % tile_size) % tile_size
    
    # Apply padding
    if pad_h > 0 or pad_w > 0:
        img_padded = cv2.copyMakeBorder(
            img, 0, pad_h, 0, pad_w, 
            cv2.BORDER_CONSTANT, value=pad_value
        )
    else:
        img_padded = img.copy()
    
    padded_shape = img_padded.shape[:2]
    
    # Extract tiles
    tiles = []
    positions = []  # (y, x) of top-left corner of each tile
    
    for y in range(0, img_padded.shape[0], tile_size):
        for x in range(0, img_padded.shape[1], tile_size):
            tile = img_padded[y:y+tile_size, x:x+tile_size]
            tiles.append(tile)
            positions.append((int(y), int(x)))
    
    return tiles, positions, (pad_h, pad_w), original_shape, padded_shape


# Process all preprocessed PNG files
png_files = list(input_folder.glob("*_preprocessed.png"))
print(f"\n{'='*60}")
print(f"Found {len(png_files)} preprocessed PNG files")
print(f"{'='*60}\n")

if len(png_files) == 0:
    print("ERROR: No *_preprocessed.png files found in:")
    print(input_folder)
    print("\nMake sure your preprocessing script ran successfully.")
else:
    for png_path in tqdm(png_files, desc="Tiling all images"):
        try:
            # Tile the image
            tiles, positions, (pad_h, pad_w), orig_shape, padded_shape = tile_image(
                png_path, tile_size=TILE_SIZE
            )
            
            # Create a subfolder for this image's tiles
            image_name = png_path.stem.replace("_preprocessed", "")
            image_tiles_folder = tiles_output_folder / image_name
            image_tiles_folder.mkdir(parents=True, exist_ok=True)
            
            # Save each tile
            for idx, (tile, (y, x)) in enumerate(zip(tiles, positions)):
                # Tile naming: image_name_tile_00_00.png (row_col format)
                row = y // TILE_SIZE
                col = x // TILE_SIZE
                tile_filename = f"{image_name}_tile_{row:02d}_{col:02d}.png"
                tile_path = image_tiles_folder / tile_filename
                cv2.imwrite(str(tile_path), tile)
            
            # Save metadata for this image (needed for repatching)
            metadata = {
                "original_image": png_path.name,
                "original_shape": orig_shape,  # (h, w)
                "padded_shape": padded_shape,
                "padding": {
                    "pad_h": pad_h,
                    "pad_w": pad_w
                },
                "tile_size": TILE_SIZE,
                "tile_positions": positions,  # List of (y, x) tuples
                "num_tiles": len(tiles),
                "tiles_per_row": padded_shape[1] // TILE_SIZE,
                "tiles_per_col": padded_shape[0] // TILE_SIZE
            }
            
            metadata_file = metadata_output_folder / f"{image_name}_metadata.json"
            with open(metadata_file, 'w') as f:
                json.dump(metadata, f, indent=2)
            
        except Exception as e:
            print(f"\nERROR processing {png_path.name}: {e}")
            continue

print(f"\n{'='*60}")
print(f"Tiling complete!")
print(f"{'='*60}")
print(f"Tiles saved to:     {tiles_output_folder}")
print(f"Metadata saved to:  {metadata_output_folder}")
print(f"\nNext step: Upload tiles to CVAT or Roboflow for annotation.")