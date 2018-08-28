'''
以CSV格式提供的数据需要将行内的 " ' ; ( ) , / \ 转换为中文符号后,将分隔符替换为逗号便于载入计算,最后全部转换为UTF-8保存
鑫磊以{∏}为分隔符,GBK编码
'''

import codecs,os,chardet

def get_charset(filepath):
    with open(filepath, 'rb') as f:
        first_line=f.readline()
        if chardet.detect(first_line)['encoding']=='GB2312':
            return 'gb18030'
        return chardet.detect(first_line)['encoding']

def basic_cleasing(file_dir, filename ,sep=''):
    with codecs.open(file_dir+filename, 'r', encoding=get_charset(file_dir+filename)) as f:
        with open('{}basic_clean_{}'.format(file_dir, filename), 'w', encoding='utf_8_sig') as new:
            content=f.read().replace(',','，').replace('\'','’').replace(';','；').replace('(','（').replace(')','）').replace(r'"','”')
            if sep !='':
                content=content.replace(sep,',')
            content=content.replace(',.00,',',0.00,')
            new.write(content)

def trans():
    #获取文件list
    file_dir=input('请输入需要转换的文件夹地址(只支持一级目录)：')
    while not (os.path.isdir(file_dir) or os.path.exists(file_dir)):
        file_dir=input('请输入文件夹地址：')
    file_dir+='\\'
    postfix=input('请输入需要读取的文件类型：')
    files=[]
    for dirpath,dirnames,filenames in os.walk(file_dir):
        for each in filenames:
            if postfix in each and (not 'basic_clean_' in each):
                files.append(each)    
    sep=input('请输入分隔符(鑫磊为“{∏}”)：')

    #清洗过程
    print (files)
    for each in files:
        print ('{}处理中'.format(each))
        basic_cleasing(file_dir,each,sep)
    
    print ('done')

if __name__=='__main__':
    trans()



