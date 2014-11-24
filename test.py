#!/usr/bin/env python
#coding=utf-8
'''
an Simple example for lib https://github.com/hustcc/object2json

@author: hzwangzhiwei
@contact: http://50vip.com/
Created on 2014年11月12日
'''

from object2json import ObjToJson

class Msg(object):
    id = 0 #id生成必须全局唯一
    '''
    resq:请求消息
    resp:返回消息
    '''
    type = 'resq'
    
    cmd = ''
    data = '' 
    sender = ''
    recipient = ''
    range = 0
    ext = ''
    ext2 = ''
    
    #默认构造方法，构造一个空的消息
    def __init__(self):
        '''
        Constructor
        '''
        self.id = 5201314 #int
        self.type = 124.0 #float
        self.cmd = (1, '2', [3,4], {'a':1, 'b':'2'}) #tuple, list, dict
        self.data = {'pos':{'x': 100, 'y':50}} #dict
        self.sender = '50vip' #string
        self.recipient = u'我是中国人' #unicode
        self.range = ['a', 1, 1.0]
        self.ext = None #null
    
    
if __name__ == '__main__':
    msg = Msg()
    msg.ext2 = Msg() #object
    print(ObjToJson(msg).toJson())
    print '----'
    print(ObjToJson("abc").toJson())
