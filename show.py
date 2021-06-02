from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import main

def show_protocol():
    main.log_treeview.delete(*main.log_treeview.get_children())
    protocol_dict = main.root.protocol_dict

    for k, v in protocol_dict.items():
        for i in range(1, len(v['date'])):
            # if를 반복문에서 뺄 수 없나. 비효율적이네
            if main.value1.get() & (k == 'POP3D'):
                main.log_treeview.insert('', 'end', text=k, values=(v['date'][i], v['time'][i], v['ip'][i], v['message'][i]))
            if main.value2.get() & (k == 'SMTPC'):
                main.log_treeview.insert('', 'end', text=k, values=(v['date'][i], v['time'][i], v['ip'][i], v['message'][i]))
            if main.value3.get() & (k == 'SMTPD'):
                main.log_treeview.insert('', 'end', text=k, values=(v['date'][i], v['time'][i], v['ip'][i], v['message'][i]))


def show_log(log_dict):
    for k, v in log_dict.items():
        main.log_treeview.insert('', 'end', text=k, values=(v['count'], v['date'][0], v['time'][0]))

        # 날짜가 둘 이상인 경우
        for i in range(1, len(v['date'])):
            if v['date'][i - 1] == v['date'][i]:
                date = ' '
            else:
                date = v['date'][i]

            if v['time'][i - 1] == v['time'][i]:
                time = ' '
            else:
                time = v['time'][i]
                # 시간이 같지 않는 경우(중복 날짜에 대해서 시간만 출력)
                if (time != ' '):
                    main.log_treeview.insert('', 'end', text='', values=(' ', date, time))