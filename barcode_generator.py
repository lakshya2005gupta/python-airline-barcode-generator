
import pdf417gen
from PIL import Image

data = "M1GUPTA/JAHNVI         L2JY9Q IXZCCUIX 2642 056Y000000000 100"
codes = pdf417gen.encode(data, columns=6, security_level=5)
image = pdf417gen.render_image(codes)  # returns a PIL image

# Save the image
image.save("C:/Users/HP/Desktop/barcode_output.png")
print("Barcode generated and saved successfully!")

