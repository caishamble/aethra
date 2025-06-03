from PIL import Image, ImageDraw

# Load the image
img = Image.open("/mnt/data/image.png")

# Initialize drawing context
draw = ImageDraw.Draw(img)

# Draw circles to mark the nodes for the common ancestors
# These coordinates are estimated based on the provided image and may need adjustment
# Camel and whale common ancestor node
draw.ellipse((88, 318, 108, 338), outline ="red", width=2)
# Camel and deer common ancestor node
draw.ellipse((88, 188, 108, 208), outline ="red", width=2)

# Save the image with nodes highlighted
img_with_nodes = "/mnt/data/image_with_nodes.png"
img.save(img_with_nodes)
img_with_nodes
