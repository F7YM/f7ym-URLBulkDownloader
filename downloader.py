import requests
import random

UALib = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", 
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36", 
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14", 
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"]
urlFile = input('输入Url文件路径(Win用户请将反斜杠替为两个反斜杠)>>>')
fileLastName = input('下载文件的后缀名>>>').replace('.','')
#duanDian = input('断点续下()')

with open(urlFile,'r') as f:
    lines = f.readlines()
    allTask = len(lines)
    print('共' + str(allTask) + '个任务')
    for i in range(0,allTask):
        task = f'({i + 1}/{allTask})'
        print(f'{task}正在获取来自' + lines[i].strip() + '的文件')
        userAgent = {'User-Agent': random.choice(UALib)}
        print(f'{task}使用随机UA: {userAgent}')
        getFile = requests.get(lines[i],headers = userAgent)
        print(f'{task}状态码: {getFile.status_code},',end='')
        if getFile.status_code == 200:
            print('获取成功')
        else:
            print('获取失败')
        print(f'{task}正在写入{i}.{fileLastName}')
        with open(f'{i}.{fileLastName}','wb') as savedFile:
            savedFile.write(getFile.content)
        print(f'{task}OK...')