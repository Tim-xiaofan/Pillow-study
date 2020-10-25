from PIL import Image
import os, sys

gif_path = input("输入要分解的GIF图片文件名：");
gif_dirname, gif_basename = os.path.split(gif_path)#分解路径
print('gif_dirname = ', gif_dirname, 'gif_basename = ', gif_basename)
root, extension = os.path.splitext(gif_basename)#分解扩展名

#检查是不是GIF文件
print("root = ", root, "extension = ", extension)
if gif_basename == '':
	print(gif_path, "不是GIF文件,是一个目录")
	sys.exit()
if extension != '.gif' and extension !='.GIF':
	print(gif_path, "不是GIF文件")
	sys.exit()

try:
	im = Image.open(gif_path)# 将准备好的gif打开
except FileNotFoundError:
	print(gif_path, '文件不存在')
	sys.exit()
except LookupError:
	print('指定了未知的编码!')
	sys.exit()
except UnicodeDecodeError:
	print('读取文件时解码错误!')
	sys.exit()

png_path = os.path.join(os.getcwd(), root)
print("pngdir=", png_path)
if not os.path.exists(png_path):
	'''如果没有重名的文件夹，就生成这个文件夹来存放图片'''
	os.mkdir(png_path)         

try:      
	'''while True 的作用就是不停的遍历gif，取得每一个图片，如果图片访问结束 会报错，所以 try一下'''
	while True:
		current = im.tell() # 获取img对象的 帧图片
		filename = str(current) + '.png'
		fullname = os.path.join(png_path,filename)#win or linux
		print(fullname)
		im.save(fullname)# 保存
		im.seek(current + 1)     # seek的作用就相当于 装饰器的 next，代表下一个
		# current 代表帧图片，+1 就是下一张

except EOFError:
    pass
