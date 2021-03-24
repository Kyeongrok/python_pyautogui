from PIL import Image

def compare_images(input_image, output_image):
  # compare image dimensions (assumption 1)
  if input_image.size != output_image.size:
    return False

  rows, cols = input_image.size

  # compare image pixels (assumption 2 and 3)
  for row in range(rows):
    for col in range(cols):
      input_pixel = input_image.getpixel((row, col))
      output_pixel = output_image.getpixel((row, col))
      if input_pixel != output_pixel:
        return False

  return True

original = Image.open("departure1.png")
possible_duplicate = Image.open("../screen_shot/departure2.png")

print(compare_images(original, possible_duplicate))

