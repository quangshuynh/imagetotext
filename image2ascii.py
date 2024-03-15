"""
Image to Text
03/15/2024
author: Quang Huynh
"""

from PIL import Image
def convertToAscii(img, type, saveas, scale):
    scale = int(scale)  # convert scale to integer

    image_file = Image.open(img)  # open image file
    w, h = image_file.size  # image file size (width & height)

    image_file.resize((w//scale, h//scale).save("resized.%s" % type))

    image_file = Image.open("resized.%s" % type)  # open new image
    w, h = image_file.size  # new width & height

    grid = []
    for i in range(h):
        grid.append(["X"] * w)

    px_coord = image_file.load()

    for y in range(h):  # iterate over height
        for x in range(w):  # iterate over x
            # pixel brightness to char
            if sum(px_coord[x, y]) == 0:
                grid[y][x] = "#"
            elif sum(px_coord[x, y]) in range (1, 100):
                grid[y][x] = "X"
            elif sum(px_coord[x, y]) in range(100, 200):
                grid[y][x] = "%"
            elif sum(px_coord[x,y]) in range(200, 300):
                grid[y][x] = "&"
            elif sum(px_coord[x][y]) in range(300, 400):
                grid[y][x] = "*"
            elif sum(px_coord[x][y]) in range(400, 500):
                grid[y][x] = "+"
            elif sum(px_coord[x][y]) in range(500, 600):
                grid[y][x] = "/"
            elif sum(px_coord[x][y]) in range(600, 700):
                grid[y][x] = "("
            elif sum(px_coord[x][y]) in range(700, 750):
                grid[y][x] = "'"
            else:
                grid[y][x] = " "

    with open(saveas, "w") as f:
        for row in grid:
            f.write("".join(row) + "\n")

def main():
    print("Welcome to Quang's Image to Text program!")
    image = input("\tInput image path: ")
    type = input("\tInput image type: ")
    saveas = input("\tWhere do you want your text file to be saved?: ")
    scale = input("Scale of image: ")
    convertToAscii(image, type, saveas, scale)
    print("Done!")

if __name__ == "__main__":
    main()


