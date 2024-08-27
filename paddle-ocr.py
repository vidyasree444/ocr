from paddleocr import PaddleOCR
from PIL import Image, ImageFont, ImageDraw
from pdf2image import convert_from_path
import numpy as np

# Convert PDF to images
pdf_path = 'Pegasus1.pdf'
images = convert_from_path(pdf_path)

ocr = PaddleOCR(
    det_db_thresh=0.3,
    det_db_box_thresh=0.3,
    det_db_unclip_ratio=1.3,
    max_batch_size=10
)

# Process each image
for i, image in enumerate(images):
    # Convert PIL image to numpy array
    image_np = np.array(image)

    # Apply OCR to each image
    results = ocr.ocr(image_np, cls=True)
    print(results)
    text = "\n".join([line[1][0] if line[1][0] is not None else "\n" for line in results[0]])


    # Convert numpy array back to PIL image for drawing
    image = Image.fromarray(image_np)

    # Draw OCR results on the image
    draw = ImageDraw.Draw(image)
    font_path = "/usr/share/fonts/truetype/liberation2/LiberationSerif-Regular.ttf"
    font = ImageFont.truetype(font_path, 12)

    for res in results:
        for line in res:
            box = [tuple(point) for point in line[0]]
            box = [(min(point[0] for point in box), min(point[1] for point in box)),
                   (max(point[0] for point in box), max(point[1] for point in box))]
            txt = line[1][0]
            draw.rectangle(box, outline="red", width=3)
            draw.text((box[0][0], box[0][1] - 25), txt, fill="blue", font=font)

    # Save the result image
    image.save(f"result_page_{i + 1}.pdf")

# Optionally, merge all pages into a single PDF
from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()
for i in range(len(images)):
    merger.append(f"result_page_{i + 1}.pdf")
merger.write("final_result.pdf")
merger.close()
