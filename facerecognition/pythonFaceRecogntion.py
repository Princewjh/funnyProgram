#python20行实现自动戴帽
#代码来自知乎分享

from PIL import Image
import face_recognition

img_path = "./1.jpg" #用户输入头像图片的路径

image = face_recognition.load_image_file(img_path) #将所指的图像数据读入image中
#调用face_locations处理image中的图像数据，
#对图片中的人脸进行识别定位，定位后的得到的像素坐标数据放在face_locations里
face_locations = face_recognition.face_locations(image)
#输出图片里识别到的人脸的个数
print("Found {} face(s) in this photograph.".format(len(face_locations)))

#把路径所指的图像数据读入human_img中，并转换为四通道RGBA模式
human_img = Image.open(img_path)
human_img = human_img.convert("RGBA")

#读入帽子图像并做相同处理
hat_img = Image.open("./hat.png")
hat_img = hat_img.convert("RGBA")

for face_location in face_locations:
	top,right,bottom,left = face_location #得到人脸的位置信息
	top -= 10
	#print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right)
	head_h = bottom - top#头高度
	head_l = right - left#头宽度

	hat_img = hat_img.resize((head_l,head_h))#根据人脸大小调整帽子位置
	hat_region = hat_img #帽子图像作为顶层图像
	human_region = (left, top - head_h, right, top)
	human_img.paste(hat_region, human_region, mask = hat_img)

human_img.show()




