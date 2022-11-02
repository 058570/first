import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import shutil

name="real_sunny_PM_20221007_125320_sedan_Saha-gu_image_3"
#name="real_sunny_PM_20220920_116609_truck_Gangseo-gu_image_1"#
#name에 폴더이름 입력

os.mkdir("C:/Users/kst/Desktop/정제/"+name+"_exam")
os.mkdir("C:/Users/kst/Desktop/정제/"+name+"_del")
os.mkdir("C:/Users/kst/Desktop/정제/"+name+"_issue")
os.mkdir("C:/Users/kst/Desktop/정제/"+name+"_issue/1. 애매한 파손")
os.mkdir("C:/Users/kst/Desktop/정제/"+name+"_issue/2. 장애물 가림")
os.mkdir("C:/Users/kst/Desktop/정제/"+name+"_issue/3. 화각잘림")
# 내가 정제작업한 경로를 name에 입력을 하면 지역) 폴더 내에
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
src_path_3 = "c:/KST_refine/number3"
src_path_4 = "c:/KST_refine/number4"
src_path_5 = "c:/KST_refine/number5"

new_path_1 = "C:/Users/kst/Desktop/정제/"+name+"_exam"
new_path_2 = "C:/Users/kst/Desktop/정제/"+name+"_del"
new_path_3 = "C:/Users/kst/Desktop/정제/"+name+"_issue/2. 장애물 가림"
new_path_4 = "C:/Users/kst/Desktop/정제/"+name+"_issue/3. 화각잘림" 
new_path_5 = "C:/Users/kst/Desktop/정제/"+name+"_issue/1. 애매한 파손"

#new_path_5 = f"C:/Users/kst/Desktop/정제/{name}_issue/1. 애매한 파손"


file_list_1=all_file(src_path_1)
file_list_2=all_file(src_path_2)
file_list_3=all_file(src_path_3)
file_list_4=all_file(src_path_4)
file_list_5=all_file(src_path_5)

move_file(file_list_1,new_path_1)
move_file(file_list_2,new_path_2)
move_file(file_list_3,new_path_3)
move_file(file_list_4,new_path_4)
move_file(file_list_5,new_path_5)


scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

json_key_path=" "

credential=ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)
gc=gspread.authorize(credential)



spreadsheet_key = "구글 스프레드 키"
doc=gc.open_by_key(spreadsheet_key)
sheet = doc.worksheet("10/12")


sheet.update("F25",int(len(file_list_1)))
sheet.update("J25",int(len(file_list_2)))
sheet.update("S25:U25",[[int(len(file_list_5)),int(len(file_list_3)),int(len(file_list_4))]])