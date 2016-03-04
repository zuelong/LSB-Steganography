from PIL import Image

def unobiterator(data):
    for pix in data:
        for byte in pix:
            yield byte & 1


def desteg(img):
    img_data = list(img.getdata())
    bitstream = unobiterator(img_data)
    msg = ""

    while True:

        c = next(bitstream)
        for i in range(7):
            c <<= 1
            c += next(bitstream)

        if c == 0:
            break

        msg += chr(c)

    print(msg)


if __name__ == "__main__":
    desteg(Image.open("out.png"))