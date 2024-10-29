from PIL import Image

# Open the image file
img_path = "image_file"
image = Image.open(img_path)

# Resize the image to 12668x9000 pixels
new_size = (12668, 9000)
resized_image = image.resize(new_size)

# Save the resized image
resized_image_path = "path_to_save_resized_image.png"
resized_image.save(resized_image_path)

print("Resized image saved at:", resized_image_path)