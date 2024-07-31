from PIL import Image, ImageOps
import sys
# shirt = Image.open("shirt.png")
# photo = Image.open("before1.jpg")
# new_photo = ImageOps.fit(photo, shirt.size)
# new_photo.paste(shirt,mask=shirt)
# new_photo.show()

def main():
    if len(sys.argv) != 3:
        if len(sys.argv) < 3:
            sys.exit("Too few command line arguments")
        else:
            sys.exit("Too many command line arguments")
    else:
        if sys.argv[1].endswith(".jpg") and not(sys.argv[2].endswith(".jpg")):
            sys.exit("Input and Output have different extension")
        elif sys.argv[1].endswith(".jpeg") and not(sys.argv[2].endswith(".jpeg")):
            sys.exit("Input and Output have different extension")
        elif sys.argv[1].endswith(".png") and not(sys.argv[2].endswith(".png")):
            sys.exit("Input and Output have different extension")
        else:
            convert(sys.argv[1], sys.argv[2])
def convert(input_one, output_two):
    try:
        with Image.open(input_one) as input:
            shirt = Image.open("shirt.png")
            photo = Image.open("before1.jpg")
            new_photo = ImageOps.fit(photo, shirt.size)
            new_photo.paste(shirt,mask=shirt)
            new_photo.show()
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
