import os
import shutil


f = open("error.txt","r") # 오류.txt 파일 위치 
line = f.readlines()
path = "./" # 이미지있는 파일 경로
file_list = os.listdir(path)
dir = './save/' # 옮길 폴더 경로 
	img_name = line[i].split("/")[0].split("\\")[2].split(":")[0]
	img_file = [file for file in file_list if file == img_name]
	if img_file : 
		shutil.move(path + img_file[0], dir + img_file[0])
		print(img_file[0]," 파일을 옮겼음.")
