from PIL import Image

# 載入兩張影像
img1 = Image.open("R19.png")
img2 = Image.open("R17.png")

# 檢查兩張影像大小是否一致
print(img1.size)
print(img2.size)

blendImg = Image.blend(img1, img2, alpha = 0.5)
blendImg.save("GA50.png","png")
blendImg.show()