from rembg import remove
from PIL import Image

input_path = 'download.jpg'
output_path = 'download.png'

# Open the input image
inp = Image.open(input_path)

# Remove the background
output = remove(inp)

# Save the result
output.save(output_path)

# Open the saved image
Image.open(output_path).show()
