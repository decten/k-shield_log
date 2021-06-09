def get_log_data(filename):
    log_dict = dict()

    with open(filename, encoding='cp949') as f:
        for line in f:
            _, _, _, log_date, log_time, log_ip, *message = line.replace('"', '').split()

            if (log_ip not in log_dict):
                log_dict[log_ip] = {'count': 1, 'date': [log_date], 'time' : [log_time]}
            else:
                log_dict[log_ip]['count'] += 1
                log_dict[log_ip]['date'].append(log_date)
                log_dict[log_ip]['time'].append(log_time)

    return log_dict

def get_protocol_data(filename):
    protocol_dict = dict()

    with open(filename, encoding='cp949') as f:
        for line in f:
            log_protocol, _, _,log_date, log_time, log_ip, *log_message = line.replace('"', '').split()
            log_message = ''.join(log_message)
            if (log_protocol not in protocol_dict):
                protocol_dict[log_protocol] = {'date': [log_date], 'time': [log_time], 'ip': [log_ip], 'message': [log_message]}
            else:
                protocol_dict[log_protocol]['date'].append(log_date)
                protocol_dict[log_protocol]['time'].append(log_time)
                protocol_dict[log_protocol]['ip'].append(log_ip)
                protocol_dict[log_protocol]['message'].append(log_message)

    return protocol_dict
