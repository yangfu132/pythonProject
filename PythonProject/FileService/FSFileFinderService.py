#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import platform
import glob

from FileService.FSTextFileService import FSTextFileService


class FSFileFinderService(object):
    def __init__(self):
        self.allowedExtensions = set(['txt','gpx','ipa','xls','xlsx','csv']);
        self.textService = FSTextFileService();
        
###############################目录函数###############################
    
    #获取当前目录的文件列表，包含文件大小        
    def get_fileInfoDict(self,order_dir)->dict:
        resultDict = {};
        hasOrder = os.path.exists(order_dir);
        if hasOrder and not os.path.isfile(order_dir):
            pattern = '*'
            os.chdir(order_dir)
            for fname in glob.glob(pattern):
                key = fname
                if os.path.isfile(fname):
                    resultDict[key]= os.path.getsize(fname)/1024;
                else:
                    resultDict[key]= '';
        return resultDict;
    
    #获取当前目录的内容   
    def get_content_list(self, order_dir) -> list:
        resultArray = [];
        hasOrder = os.path.exists(order_dir);
        if hasOrder and not os.path.isfile(order_dir):
            pattern = '*'
            os.chdir(order_dir)
            for fname in glob.glob(pattern):
                #if os.path.isfile(fname):
                    resultArray.append(fname);
                #else:
        return resultArray;
    
    #获取当前目录下的文件    
    def get_file_list(self, order_dir) -> list:
        resultArray = [];
        hasOrder = os.path.exists(order_dir);
        if hasOrder and not os.path.isfile(order_dir):
            pattern = '*'
            os.chdir(order_dir)
            for fname in glob.glob(pattern):
                if os.path.isfile(fname):
                    resultArray.append(fname);
                #else:
        return resultArray;
    
    #打开指定目录
    def open_dir(self, path):
            sysstr = platform.system()
            if sysstr == 'Darwin':
                os.system('open ' + path);
            # else if sysstr == 'Windows':
            # else if sysstr == "Linux" 
            
            
###############################路径函数###############################
    #将path于item拼接成newpath
    def appendPath(self,path,item)->(str,str): 
        if len(item) > 0:
            isFile = item.find('.') >= 0;   
            if isFile: 
                newPath = path = path + item;
            else:
                if len(path) > 0:
                    newPath = path + item + '/';
                else:
                    newPath = item;

        return newPath;
    
###############################文件函数###############################
    #获取文件大小
    def getFileSize(self,fname):
        if os.path.isfile(fname):
            sizeFile = os.path.getsize(fname)/1024;
            return sizeFile;
        else:
            return 0;
        
    def read_content(self,filePath):
        return self.textService.read_content(filePath);
    
    def write_content(self,content,filePath):
        self.textService.write_content(content, filePath);
        
    def read_list_fromTxt(self,filePath):
        return self.textService.read_list_fromTxt(filePath);
    
    def write_list_toTxt(self,rows:list, filePath):
        self.textService.write_list_toTxt(rows,filePath);
        
    def read_json(self,filePath)->dict:
        return self.textService.read_json(filePath);
    
    def write_json(self,filePath,content)->dict:
        return self.textService.write_json(filePath,content);
    

sharedFileService = FSFileFinderService();