#pip install pillow
from PIL import Image

def main():
    bmp = Image.open("sample.bmp")
    width, height = bmp.size

    rgb = bmp.convert("RGB")

    print("width:{0}, height:{1}".format(width, height))

    for y in range(height):
        for x in range(width):
            r, g, b = rgb.getpixel((x,y))
            print("r:{0}, g:{1}, b:{2}".format(hex(r), hex(g), hex(b)))

if __name__ == "__main__":
    main()

