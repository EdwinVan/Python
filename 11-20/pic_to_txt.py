# 构造图片的字符画
# fyj
# 2020-11-18

from PIL import Image
ascii_char = list("$%_&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-/+@")
def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = 256 / len(ascii_char)
    return ascii_char[int(gray/unit)]

def main():
    size = 100,100
    im = Image.open("小新.png")
    '''im.thumbnail(size,Image.ANTIALIAS)'''
    WIDTH , HEIGHT = 220, 220
    im = im.resize((WIDTH, HEIGHT))

    txt = ""
    for i in range(WIDTH):
        for j in range(HEIGHT):
            txt += get_char(*im.getpixel((j,i)))
        txt += "\n"
    fo = open('H:/Edwin/Desktop/Python/11-20/小新.txt', 'w')
    fo.write(txt)
    fo.close()

main()
