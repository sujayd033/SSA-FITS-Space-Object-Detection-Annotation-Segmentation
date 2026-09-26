from astropy.io import fits
import numpy as np
import cv2
from pathlib import Path
from tqdm import tqdm

# ========== YOUR PATHS ==========
input_folder = Path(r"C:\Users\thesk\Downloads\Telegram Desktop\images project\Datasets_Assessment")
output_folder = Path(r"C:\Users\thesk\Music\digantra project\Preprocessed_Images")
# ================================

output_folder.mkdir(parents=True, exist_ok=True)

fits_files = list(input_folder.rglob("*.fits")) + list(input_folder.rglob("*.FITS"))
print(f"Found {len(fits_files)} FITS files")

if len(fits_files) == 0:
    print("ERROR: No FITS files found. Check the path!")
else:
    for fits_path in tqdm(fits_files, desc="Preprocessing"):
        with fits.open(fits_path) as hdul:
            data = hdul[0].data.astype(np.float32)

        # Percentile stretch (makes faint stars + streaks visible)
        low, high = np.percentile(data, (0.5, 99.8))
        data_stretched = np.clip((data - low) / (high - low + 1e-8), 0, 1)

        # Convert to 8-bit
        image_8bit = (data_stretched * 255).astype(np.uint8)

        # Light noise reduction
        image_8bit = cv2.medianBlur(image_8bit, 3)

        # Save
        output_name = fits_path.stem + "_preprocessed.png"
        output_path = output_folder / output_name
        cv2.imwrite(str(output_path), image_8bit)

    print("\nDone! Check the folder:")
    print(output_folder)