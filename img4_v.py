#遍历访问图片每个像素点，并修改相应的RGB
import cv2 as cv
import numpy as np

#从左往右4色块：白 红 绿 蓝
#画布大小 1920*1080
def creat_image():
    img = np.zeros([1080, 1920, 3], np.uint8)   #创建纯黑色图片，将所有像素点的各通道数值赋0
    channels = img.shape[2]


    for col in range(1920):
        count = 1               #每列开始前，初始化
        lenth = 4
        delta = 0


        for row in range(1080):

            #判断填充颜色  [B,G,R]
            if col < 480:
                for c in range(channels):
                    img[row, col, c] += delta      #白色：每个通道值+delta值
                pass
            elif col < 960:
                img[row , col, 2] += delta    #红色 [0,0,1]
                pass
            elif col < 1440:
                img[row , col, 1] += delta  #绿色 [0,1,0]
                pass
            elif col < 1920:
                img[row , col, 0] += delta  #蓝色 [0,1,0]

            #判断纵列阶梯
            count += 1               #判断下一个像素
            if count > lenth:
                if lenth == 4:
                    lenth = 5
                    pass

                elif lenth == 5:
                    lenth = 4

                delta += 1        #决定下一个阶梯的涂色色值
                count = 1      #开启新阶梯，重新计数



    print(img.shape)
    return img




img = creat_image()
cv.namedWindow("new_image")
cv.imshow("new_image",img)    #全部涂完，预览效果

# cv.imwrite('test.jpg',img,[int(cv.IMWRITE_JPEG_QUALITY),100])
cv.imwrite('test4_v.png',img,[int(cv.IMWRITE_PNG_COMPRESSION),0])
cv.imwrite('test4_v.jpg',img,[int(cv.IMWRITE_JPEG_QUALITY),100])

cv.waitKey(0)
cv.destroyAllWindows()

