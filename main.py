from tkinter import *
from tkinter.ttk import *
import get
import show
import save

if __name__ == '__main__':

    root = Tk()
    root.title('로그 파일 확인')

    root.filename = ''
    root.log_dict = None

    # 프로토콜
    frame = Frame(root)
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side = 'right', fill = 'y')
    log_treeview = Treeview(frame, columns = ['1', '2', '3', '4'], displaycolumns = ['1', '2', '3', '4'])
    log_treeview.pack(fill = 'both')
    scrollbar['command'] = log_treeview.yview

    frame.grid(row = 1, column = 0, columnspan = 3, sticky = 'we')
    log_treeview.configure(yscrollcommand=scrollbar.set)
    log_treeview.column('#0', width = 100, anchor = 'center')
    log_treeview.heading('#0', text='프로토콜')
    log_treeview.column('1', width = 100, anchor = 'center')
    log_treeview.heading('1', text = '날짜')
    log_treeview.column('2', width = 120, anchor = 'center')
    log_treeview.heading('2', text = '시간')
    log_treeview.column('3', width = 120, anchor = 'center')
    log_treeview.heading('3', text = 'IP')
    log_treeview.column('4', width = 120, anchor = 'center')
    log_treeview.heading('4', text = '메시지')

    # 위치를 이쁘게 하고 싶은데 포기
    Button(root, text='파일 불러오기', command=get.get_log_file).grid(row=0, column = 0, pady = 5)
    Button(root, text='프로토콜 저장하기(json)', command=save.save_protocol_json).grid(row=0, column = 1, pady = 5)

    value1 = IntVar()
    value2 = IntVar()
    value3 = IntVar()
    Checkbutton(root, text='POP3D', variable=value1, command=show.show_protocol).grid(row = 3, column = 0)
    Checkbutton(root, text='SMTPC', variable=value2, command=show.show_protocol).grid(row = 3, column = 1)
    Checkbutton(root, text='SMTPD', variable=value3, command=show.show_protocol).grid(row = 3, column = 2)

    # IP

    frame = Frame(root)
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side = 'right', fill = 'y')
    log_treeview = Treeview(frame, columns = ['1', '2', '3'], displaycolumns = ['1', '2', '3'])
    log_treeview.pack(fill = 'both')
    scrollbar['command'] = log_treeview.yview
    frame.grid(row = 5, column = 0, columnspan = 4, sticky = 'we')

    log_treeview.configure(yscrollcommand=scrollbar.set)
    log_treeview.column('#0', width = 120, anchor = 'center')
    log_treeview.heading('#0', text='IP')
    log_treeview.column('1', width = 100, anchor = 'e')
    log_treeview.heading('1', text = 'IP 횟수')
    log_treeview.column('2', width = 100, anchor = 'center')
    log_treeview.heading('2', text = 'IP 날짜')
    log_treeview.column('3', width = 100, anchor = 'center')
    log_treeview.heading('3', text = 'IP 시간')

    Label(root, text = '').grid(row = 6, column = 0)
    Button(root, text = 'IP 저장하기(json)', command = save.save_log_json).grid(row = 4, column = 0, pady = 5, columnspan = 4, sticky = 'we')

    root.mainloop()