from PIL import Image, ImageEnhance
import os

def resize_image(img_path, output_path, new_size=(12668, 9000), enhance=False):
    try:
        # Open the image
        image = Image.open(img_path)
        
        # Resize with high-quality resampling
        resized_image = image.resize(new_size, Image.LANCZOS)

        # Enhance image (optional)
        if enhance:
            enhancer = ImageEnhance.Sharpness(resized_image)
            resized_image = enhancer.enhance(1.5)  # Increase sharpness
            enhancer = ImageEnhance.Contrast(resized_image)
            resized_image = enhancer.enhance(1.2)  # Improve contrast
            enhancer = ImageEnhance.Brightness(resized_image)
            resized_image = enhancer.enhance(1.1)  # Slightly increase brightness

        # Preserve the original format
        output_format = image.format if image.format else "PNG"
        
        # Save the resized image
        resized_image.save(output_path, format=output_format)
        print(f"Resized image saved at: {output_path}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
img_path = "image_file.png"
output_path = "resized_image.png"
resize_image(img_path, output_path, enhance=True)
