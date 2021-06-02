from tkinter import *
from tkinter import filedialog
import json

window = Tk()
window.title('프로토콜 확인')
window.geometry("600x500")

def open_log():
    window.file = filedialog.askopenfilename(title='select file', filetypes=(('log files', '*.log'),('all files','*.*')))
    print(window.file)
open_button = Button(window, text='파일 불러오기', command=open_log)
open_button.grid(row=0)
#Text(window, text=window.file).grid(row=0, column=1)

Label(window, text='확인할 프로토콜을 선택하세요').grid(row=1, sticky=W)
value1 = IntVar()
value2 = IntVar()
value3 = IntVar()
Checkbutton(window, text='POP3D', variable=value1).grid(row=2, sticky=W)
Checkbutton(window, text='SMTPC', variable=value2).grid(row=3, sticky=W)
Checkbutton(window, text='SMTPD', variable=value3).grid(row=4, sticky=W)

def read_log():
    text = Text(window)

    # 로그 파일 읽어오기#
    f = open(window.file, 'r')

    POP3D = list()
    SMTPC = list()
    SMTPD = list()

    while True:
        line = f.readline()
        if not line: break
        line = line.replace(" ", "")
        line.split()
        # for i in line :
        #    if i == '"':
        #       result = result + (i)
        protocol = line[1:6]
        if protocol == "POP3D":
            POP3D.append(line)
        elif protocol == "SMTPC":
            SMTPC.append(line)
        elif protocol == "SMTPD":
            SMTPD.append(line)
    f.close()

    if value1.get() == 1:
        text.insert(END, POP3D)
        with open('./POP3D.json', 'w') as f:
            f.write(json.dumps(POP3D))
    if value2.get() == 1:
        text.insert(END, SMTPC)
        with open('./SMTPC.json','w') as f:
            f.write(json.dumps(SMTPC))
    if value3.get() == 1:
        text.insert(END, SMTPD)
        with open('./SMTPD.json','w') as f:
            f.write(json.dumps(SMTPD))
    text.grid(row=6, sticky=W)


result_button = Button(window, text='결과보기', command= read_log)
result_button.grid(row=5, sticky=W)

window.mainloop()


