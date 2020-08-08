import json
import os

#file=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','Vcard','result.json') #If your json file not in same directory with python file u can use it
file = 'result.json' #If your json file in same directory with python file u can use it
with open(file, 'r', encoding="utf8") as f:
    file_dict = json.load(f)

my_list = file_dict['contacts']["list"]

s = ''
begin = "BEGIN:VCARD\nVERSION:2.1"

for i, dic in enumerate(my_list):
    d_f_name = dic['first_name']
    d_l_name = dic['last_name']
    d_phone = dic['phone_number']
    f_name = "\nN:" + d_l_name + ";" + d_f_name + ";;;"
    phone = "\nTEL;CELL:" + d_phone
    s += begin + f_name + phone + "\nEND:VCARD\n"
    print('Writing ' + str(i + 1) + '/' + str(len(my_list)))

text_file = open("Exported.vcf", "w" , encoding="utf8")
text_file.write(s)
text_file.close()
print("Completed!")
