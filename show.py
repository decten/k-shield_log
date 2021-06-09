from tkinter import *
from tkinter.ttk import *
import get
import save
import get
from tkinter import filedialog

def get_log_file():
    root.filename = filedialog.askopenfilename(parent=root, title='Open Log files',
                                               filetypes=(('log files', '*.log'), ('all files', '*.*')))
    if (root.filename != ''):
        root.protocol_dict = get.get_protocol_data(root.filename)
        root.log_dict = get.get_log_data(root.filename)
        show_log(root.log_dict)

def show_protocol():
    protocol_treeview.delete(*protocol_treeview.get_children())
    protocol_dict = root.protocol_dict

    for p, v in protocol_dict.items():
        for i in range(1, len(v['date'])):
            if value1.get() & (p == 'POP3D'):
                protocol_treeview.insert('', 'end', text=p,
                                         values=(v['date'][i], v['time'][i], v['ip'][i], v['message'][i]))
            if value2.get() & (p == 'SMTPC'):
                protocol_treeview.insert('', 'end', text=p,
                                         values=(v['date'][i], v['time'][i], v['ip'][i], v['message'][i]))
            if value3.get() & (p == 'SMTPD'):
                protocol_treeview.insert('', 'end', text=p,
                                         values=(v['date'][i], v['time'][i], v['ip'][i], v['message'][i]))


def show_log(log_dict):
    for k, v in log_dict.items():
        ip_treeview.insert('', 'end', text=k, values=(v['count'], v['date'][0], v['time'][0]))

        for i in range(1, len(v['date'])):
            if v['date'][i - 1] == v['date'][i]:
                date = ' '
            else:
                date = v['date'][i]

            if v['time'][i - 1] == v['time'][i]:
                time = ' '
            else:
                time = v['time'][i]

                if (time != ' '):
                    ip_treeview.insert('', 'end', text='', values=(' ', date, time))

def reset():
    protocol_treeview.delete(*protocol_treeview.get_children())
    ip_treeview.delete(*ip_treeview.get_children())

def show_result():
    global root, protocol_treeview, value1, value2, value3, ip_treeview
    root = Tk()
    root.title('로그 파일 확인')

    root.filename = ''
    root.log_dict = None

    # 프로토콜
    frame = Frame(root)
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side = 'right', fill = 'y')
    protocol_treeview = Treeview(frame, columns = ['1', '2', '3', '4'], displaycolumns = ['1', '2', '3', '4'])
    protocol_treeview.pack(fill ='both')
    scrollbar['command'] = protocol_treeview.yview

    frame.grid(row = 1, column = 0, columnspan = 3, sticky = 'we')
    protocol_treeview.configure(yscrollcommand=scrollbar.set)
    protocol_treeview.column('#0', width = 100, anchor ='center')
    protocol_treeview.heading('#0', text='프로토콜')
    protocol_treeview.column('1', width = 100, anchor ='center')
    protocol_treeview.heading('1', text ='날짜')
    protocol_treeview.column('2', width = 120, anchor ='center')
    protocol_treeview.heading('2', text ='시간')
    protocol_treeview.column('3', width = 120, anchor ='center')
    protocol_treeview.heading('3', text ='IP')
    protocol_treeview.column('4', width = 120, anchor ='center')
    protocol_treeview.heading('4', text ='메시지')

    Button(root, text='파일 불러오기', command=get_log_file).grid(row=0, column = 0, pady = 5)
    Button(root, text='프로토콜 저장하기(json)', command=save.save_protocol_json).grid(row=0, column = 1, pady = 5)
    Button(root, text='RESET', command=reset).grid(row=0, column=2, pady=5)

    value1 = IntVar()
    value2 = IntVar()
    value3 = IntVar()
    Checkbutton(root, text='POP3D', variable=value1, command=show_protocol).grid(row = 3, column = 0)
    Checkbutton(root, text='SMTPC', variable=value2, command=show_protocol).grid(row = 3, column = 1)
    Checkbutton(root, text='SMTPD', variable=value3, command=show_protocol).grid(row = 3, column = 2)

    # IP
    frame = Frame(root)
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side = 'right', fill = 'y')
    ip_treeview = Treeview(frame, columns = ['1', '2', '3'], displaycolumns = ['1', '2', '3'])
    ip_treeview.pack(fill ='both')
    scrollbar['command'] = ip_treeview.yview
    frame.grid(row = 5, column = 0, columnspan = 4, sticky = 'we')

    ip_treeview.configure(yscrollcommand=scrollbar.set)
    ip_treeview.column('#0', width = 120, anchor ='center')
    ip_treeview.heading('#0', text='IP')
    ip_treeview.column('1', width = 100, anchor ='e')
    ip_treeview.heading('1', text ='IP 횟수')
    ip_treeview.column('2', width = 100, anchor ='center')
    ip_treeview.heading('2', text ='IP 날짜')
    ip_treeview.column('3', width = 100, anchor ='center')
    ip_treeview.heading('3', text ='IP 시간')

    Label(root, text = '').grid(row = 6, column = 0)
    Button(root, text = 'IP 저장하기(json)', command = save.save_log_json).grid(row = 4, column = 0, pady = 5, columnspan = 4, sticky = 'we')

    root.mainloop()
