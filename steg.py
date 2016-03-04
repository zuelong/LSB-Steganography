from PIL import Image
import random


def obiterator(msg):
    for c in msg:
        byte = ord(c)
        for i in range(8):
            yield (byte & 128) >> 7
            byte <<= 1
    for i in range(8):
        yield 0
    while True:
        yield random.randrange(2)


def set_bit(old_byte, new_bit):
    if new_bit:
        return old_byte | new_bit
    else:
        return old_byte & 254


def steg(img, msg):
    bitstream = obiterator(msg)
    data = list(img.getdata())

    for i, pix in enumerate(data):
        r = pix[0]
        g = pix[1]
        b = pix[2]

        msg_bit = next(bitstream)
        r = set_bit(r, msg_bit)
        msg_bit = next(bitstream)
        g = set_bit(g, msg_bit)
        msg_bit = next(bitstream)
        b = set_bit(b, msg_bit)

        data[i] = (r, g, b)

    img.putdata(data)
    img.save("out.png")

if __name__ == '__main__':
    image = Image.open("rand.png")
    image = image.convert("RGB")
    steg(image, "hello!")
