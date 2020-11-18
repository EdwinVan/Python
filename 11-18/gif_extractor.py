# 提取GIF图片中的每一帧的图片,并保存
# fyj
# 2020-11-18

from PIL import Image
url = input("请输入图片路径: ")
im = Image.open(url)  # 读入一个文件
print(im.format)
try:
    im.save("picframe{:02d}.png".format(im.tell()))
    while True:
        im.seek(im.tell()+1)
        im.save("picframe{:02d}.png".format(im.tell()))
except:
    print("处理结束")