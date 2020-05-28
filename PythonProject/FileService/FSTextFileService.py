#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from _ast import Str
import codecs
import json

class FSTextFileService(object):
    
    def open_write_file(self,filePath):
        return codecs.open(filePath, 'a', encoding='utf-8');
    
    def close_file(self,fileHandle):
        fileHandle.close();   
        
    def write_file(self,fileHandle,content:Str):
        fileHandle.write(content);
        
    def write_content(self, content:Str,filePath):
        fileHandle = codecs.open(filePath, 'a', encoding='utf-8');
        fileHandle.write(content); 
        fileHandle.close();
        
    def read_content(self,filePath):
        file = codecs.open(filePath, 'r+', encoding='utf-8');
        return file.read();
        
    #将list文件写到本地
    def write_list_toTxt(self,listData:list, filePath:Str):
        if os.path.exists(filePath):
            os.remove(filePath);
            
        fileHandle = self.open_write_file(filePath);
        for item in listData:
            #if type(item) == 
            item += '\n';
            self.write_file(fileHandle, item);

        self.close_file(fileHandle);
        
        
    #读取list文件
    def read_list_fromTxt(self,filePath:Str)->list:
        if os.path.exists(filePath):
            fileHandle = codecs.open(filePath,'r','utf-8');
            lines = [line.strip() for line in fileHandle];
            self.close_file(fileHandle);
            return lines;
    
    #读取json文件
    def read_json(self,filePath):
        newJson = '';
        if os.path.exists(filePath):
            file = codecs.open(filePath,'r','utf-8');
            newJson = json.load(file);
            file.close();
        return newJson;
    
    #将json写成文件
    def write_json(self,filePath,content):
        f1 = codecs.open(filePath, 'a', encoding='utf-8');
        f1.write(json.dumps(content));
        f1.close();