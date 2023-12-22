import os

def hostFormatter(servers):
    with open('sample.txt', 'w') as f:
        for s in servers:
            f.writelines('\n'+'    '+f'node{str(servers.index(s)+1)}:'+'\n'+'      '+f'ansible_host: {s}'+'\n'+'      '+
                    f'ip: {s}'+'\n'+'      '+f'access_ip: {s}')
    file_paths = ['hosts_1.txt', 'hosts_2.txt','hosts_3.txt']

    with open('hosts.yaml', 'w', encoding='utf-8') as output_file:
        for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as input_file:
                for line in input_file:
                    output_file.write(line)
                output_file.write('\n')