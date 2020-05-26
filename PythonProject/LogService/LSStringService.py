#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

class LSStringService(object):
    def dict_to_str(self,dictData)->str:
        strResult = '{ ';
        keyList = list(dictData.keys());
        count = len(keyList);
        nIndex = 0;
        for key in keyList:
            data = dictData[key].replace('\n','');
            if nIndex < count - 1:
                strResult = strResult + '"' +key + '":"' + data + '",';
                nIndex = nIndex + 1;
            else:
                strResult = strResult + '"' +key + '":"' + data + '"}';
        return strResult;
    
    def timestamp_to_str(self,timestamp:int):
        dateArray = datetime.datetime.fromtimestamp(timestamp)
        return dateArray.strftime("%Y-%m-%d %H:%M:%S")
        