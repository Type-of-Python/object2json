#!/usr/bin/env python
#coding=utf-8
'''
object2json.py Convent OBJECT to JSON

将对象结构转化成一个json字符串，使用递归思路，项目地址；https://github.com/hustcc/object2json
python json库，对于对象嵌套的类型无能为力


@author: hzwangzhiwei
@contact: http://50vip.com/
Created on 2014年11月19日
'''

class DictToJson(object):
    '''
    convent dict to json str
    '''
    __dict = None

    def __init__(self, __dict):
        '''
        Constructor DictToJson
        '''
        self.__dict = __dict
    
    def toJson(self):
        if self.__dict == None:
            return '{}'
        
        json_str = '{'
        for (k, v) in self.__dict .items(): 
            if isinstance(v, int):
                json_str = json_str + ('"%s":%d,' % (k, v))
            elif isinstance(v, float):
                json_str = json_str + ('"%s":%f,' % (k, v))
            elif isinstance(v, long):
                json_str = json_str + ('"%s":%f,' % (k, v))
            elif isinstance(v, str):
                json_str = json_str + ('"%s":"%s",' % (k, v))
            elif isinstance(v, unicode):
                json_str = json_str + ('"%s":"%s",' % (k, v))
            elif isinstance(v, list):
                json_str = json_str + ('"%s":%s,' % (k, ListToJson(v).toJson()))
            elif isinstance(v, dict):
                json_str = json_str + ('"%s":%s,' % (k, DictToJson(v).toJson()))
            elif isinstance(v, object):
                json_str = json_str + ('"%s":%s,' % (k, ObjToJson(v).toJson()))
        #如果json_str以','结尾，则去掉','
        if json_str.endswith(','):
            json_str = json_str[0 : -1] #去掉最后一个','
            
        json_str = json_str + '}'
        return json_str
        
class ListToJson(object):
    '''
    convent list to json str
    '''
    __list = None

    def __init__(self, __list):
        '''
        Constructor ListToJson
        '''
        self.__list = __list
    
    def toJson(self):
        if self.__list == None:
            return '[]'
        
        json_str = '['
        for v in self.__list:
            if isinstance(v, int):
                json_str = json_str + ('%d,' % v)
            elif isinstance(v, float):
                json_str = json_str + ('%f,' % v)
            elif isinstance(v, str):
                json_str = json_str + ('"%s",' % v)
            elif isinstance(v, unicode):
                json_str = json_str + ('"%s",' % v)
            elif isinstance(v, list):
                json_str = json_str + ('"%s",' % ListToJson(v).toJson())
            elif isinstance(v, dict):
                json_str = json_str + ('"%s",' % DictToJson(v).toJson())
            elif isinstance(v, object):
                json_str = json_str + ('"%s",' % ObjToJson(v).toJson())
        
        #如果json_str以','结尾，则去掉','
        if json_str.endswith(','):
            json_str = json_str[0 : -1] #去掉最后一个','
            
        json_str = json_str + ']'
        return json_str


class ObjToJson(object):
    '''
    convent object to json str
    '''
    __object = None

    def __init__(self, __object):
        '''
        Constructor ObjToJson
        '''
        self.__object = __object
    
    def toJson(self):
        if self.__object == None:
            return '{}'
        return DictToJson(self.__object.__dict__).toJson()
        