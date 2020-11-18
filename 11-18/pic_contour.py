# 输出图片的轮廓图
# fyj
# 2020-11-18

from PIL import Image
from PIL import ImageFilter
url = input("请输入图片路径: ")
im = Image.open(url)
om = im.filter(ImageFilter.CONTOUR)
a = list(url)
b = a.insert((len(a)-4),'2')
saveurl = ''.join(a)    # 将列表a转化成字符串saveurl
om.save(saveurl)
print("图片保存成功，地址:{}".format(saveurl))