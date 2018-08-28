'''
以CSV格式提供的数据需要将行内的 " ' ; ( ) , / \ 转换为中文符号后,将分隔符替换为逗号便于载入计算,最后全部转换为UTF-8保存
鑫磊以{∏}为分隔符,GBK编码
'''

import os

def combine():
    #获取文件list
    file_dir=input('请输入需要合并的文件夹地址(只支持一级目录)：')
    while not (os.path.isdir(file_dir) or os.path.exists(file_dir)):
        file_dir=input('请输入文件夹地址：')
    file_dir+='\\'
    postfix=input('请输入需要合并的文件类型：')
    files={}
    for each in os.walk(file_dir):
        file_paths=each[1]
        break
    for each in file_paths:
        for every in os.walk(file_dir+each+'\\'):
            for eachone in every[2]:
                if eachone not in files.keys():
                    files[eachone]=[]
                files[eachone].append(file_dir+each+'\\'+eachone)
    # print (files)

    for each in files.keys():
        i=0
        with open(file_dir+each,'w',encoding='utf_8_sig') as new:
            for every in files[each]:
                with open(every,'r',encoding='utf-8') as old:
                    if i!=0:
                        old.readline()
                    new.write(old.read())
                    i+=1
                    print (every)





    print ('done')

if __name__=='__main__':
    combine()



