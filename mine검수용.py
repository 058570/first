import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import shutil

name="real_sunny_PM_20221007_125320_sedan_Saha-gu_image_3"
#name="real_sunny_AM_20220913_103032_truck_Dongnae-gu_image_2"#
#name에 폴더이름 입력

aria="검수/"

os.mkdir("C:/Users/kst/Desktop/"+aria+name+"_use")
os.mkdir("C:/Users/kst/Desktop/"+aria+name+"_fail")
# 내가 정제작업한 경로를 name에 입력을 하면 aria(지역) 폴더 내에
# _exam, _del, _issue폴더와 issue내부의 세개의 폴더를 생성

def all_file(path):
    output = os.listdir(path)
    file_list=[]

    for i in output:
        if os.path.isdir(path+"/"+i):
            file_list.extend(all_file(path+"/"+i))
        elif os.path.isfile(path+"/"+i):
            file_list.append(path+"/"+i)
    return file_list
# 폴더의 모든 파일을 리스트화 시키는 함수
# 정제프로그램 1번폴더의 이미지들을 리스트화

def move_file(file_list, new_path):
    for src_path in file_list:
        file = src_path.split("/")[-1]
        shutil.move(src_path, new_path+"/"+file)
# 모든 하위 폴더들을 새로운 경로로 이동시키는 함수
# 이동시킬 폴더는 src_path 목표폴더는 new_path 

# 정제프로그램 1번폴더의 하위파일을 새로만든 _exam폴더로 이동


src_path_1 = "c:/KST_refine/number1"
src_path_2 = "c:/KST_refine/number2"

new_path_1 = "C:/Users/kst/Desktop/"+aria+name+"_use"
new_path_2 = "C:/Users/kst/Desktop/"+aria+name+"_fail"

file_list_1=all_file(src_path_1)
file_list_2=all_file(src_path_2)

move_file(file_list_1,new_path_1)
move_file(file_list_2,new_path_2)


scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

json_key_path="my json key"

credential=ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)
gc=gspread.authorize(credential)



spreadsheet_key = "구글 시트 키 "
doc=gc.open_by_key(spreadsheet_key)
sheet = doc.worksheet("10/12")

'''
sheet.update(input("USE 좌표를 입력하세요 : "),int(len(file_list_1)))
sheet.update(input("FAIL 좌표를 입력하세요 : "),int(len(file_list_2)))
'''

sheet.update("H25",int(len(file_list_1)))
sheet.update("I25",int(len(file_list_2)))