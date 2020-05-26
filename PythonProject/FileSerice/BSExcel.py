#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FileName : Excel.py
# Author   : Adil
# DateTime : 2017/12/10 13:08
# SoftWare : PyCharm

import xlrd
import xlwt
from array import array

class BSExcel(object):
    '''定义一个excel类'''

    def __init__(self):
        return;
    
    def createWorkbook(self):
        self.book = xlwt.Workbook()#新建一个excel
        
    def createSheet(self,SheetName):
        self.sheet = self.book.add_sheet(SheetName)#添加一个sheet页
        
    def write(self,name,columnData:array,columnIndex):
        row = 0#控制行
        self.sheet.write(row,columnIndex,name)
        row+=1;
        for stu in columnData:
            self.sheet.write(row,columnIndex,stu)
            row+=1
            print(row)
            
    def append(self,data,rowIndex,columnIndex):
        self.sheet.write(rowIndex,columnIndex,data)
            
    def readWorkbookCol(self,path,sheetIndex,colIndex):
        book = xlrd.open_workbook(path)#打开一个excel
        sheet = book.sheet_by_index(sheetIndex)#根据顺序获取sheet
        return sheet.col_values(colIndex);

    def close(self,excelName):
        self.book.save(excelName)#保存到当前目录下

excelHelper = BSExcel();