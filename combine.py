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
    files=[]
    for dirpath,dirnames,filenames in os.walk(file_dir):
        print (dirpath,dirnames,filenames)
    #     for each in filenames:
    #         if postfix in each and (not 'basic_clean_' in each):
    #             files.append(each)    


    # #清洗过程
    # print (files)
    # for each in files:
    #     print ('{}处理中'.format(each))
    #     basic_cleasing(file_dir,each,sep)
    
    # print ('done')

if __name__=='__main__':
    combine()



