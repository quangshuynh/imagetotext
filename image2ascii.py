"""
Image to Text
03/15/2024
author: Quang Huynh
"""

from PIL import Image
def convertToAscii(img, saveas, scale):
    scale = int(scale)  # Ensure scale is an integer

    # Open the image and convert to grayscale
    image_file = Image.open(img).convert('L')  # 'L' mode converts image to grayscale
    w, h = image_file.size

    # Resize image according to the scale factor
    image_file = image_file.resize((w // scale, h // scale))
    px_coord = image_file.load()

    ascii_chars = "@%#*+=-:. "  # Define a string of ASCII characters from dark to light
    ascii_len = len(ascii_chars)

    # Create ASCII art
    ascii_art = []
    for y in range(h // scale):
        line = []
        for x in range(w // scale):
            brightness = px_coord[x, y]  # Brightness value in 'L' mode is an integer
            # Map the brightness value to an ASCII char
            char_index = brightness * (ascii_len - 1) // 255
            line.append(ascii_chars[char_index])
        ascii_art.append("".join(line))

    # Write the ASCII art to the specified file
    with open(saveas, "w") as f:
        for line in ascii_art:
            f.write(line + "\n")

def main():
    print("Welcome to Quang's Image to Text program!")
    image = input("\tInput image path: ")
    saveas = input("\tWhere do you want your text file to be saved?: ")
    scale = input("\tScale of image: ")
    convertToAscii(image, saveas, scale)
    print("\tDone! Text file saved in " + saveas)

if __name__ == "__main__":
    main()


