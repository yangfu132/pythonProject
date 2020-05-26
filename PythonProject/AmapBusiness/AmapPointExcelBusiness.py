#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from FileSerice.BSExcel import BSExcel
from LogService.LSStringService import LSStringService

class AmapPointExcelBusiness():
    #读取高德点位信息,转化为经度、纬度、时间
    def formatAmapPosition(self,sourcePath,sourceName,nReadCol):
        #pathRead = '/Users/Shared/demo.xls';
        excelHelperRead = BSExcel();
        orderIdAmapCol = excelHelperRead.readWorkbookCol(sourcePath, 0, 0);
        orderIdCol = excelHelperRead.readWorkbookCol(sourcePath, 0, 1);
        dataCol = excelHelperRead.readWorkbookCol(sourcePath, 0, nReadCol);
        dataCol.pop(0);
    
        #点位分析
        excelHelperPointOut = BSExcel();
        excelHelperPointOut.createWorkbook();
        excelHelperPointOut.createSheet('点位分析');
    
        #点位统计
        excelHelperTotal = BSExcel();
        excelHelperTotal.createWorkbook();
        excelHelperTotal.createSheet(sourceName);
        excelHelperTotal.append('高德orderId',0, 0);
        excelHelperTotal.append('神州orderId',0, 1);
        excelHelperTotal.append('有效点位',0, 2);
        excelHelperTotal.append('有效个数',0, 3);
        excelHelperTotal.append('总点位个数',0, 4);
    
        nColPointOut = 0;
        nReadRow = 1;
        nPointOutFileIndex = 0;
        strOutPath = '/Users/Shared/' + sourceName + '_detail' + str(nPointOutFileIndex) + '.xls'
        for itemOrder in dataCol:
            print('开始行' + str(nReadRow) + '列' + str(nColPointOut));
            excelHelperTotal.append(orderIdAmapCol[nReadRow],nReadRow, 0);
            excelHelperTotal.append(orderIdCol[nReadRow],nReadRow, 1);
            if nReadRow % 64 == 0:
                excelHelperPointOut.close(strOutPath);
                nPointOutFileIndex = nPointOutFileIndex + 1;
                strOutPath = '/Users/Shared/' + sourceName + '_detail' + str(nPointOutFileIndex) + '.xls'
                excelHelperPointOut.createWorkbook();
                excelHelperPointOut.createSheet('点位分析');
                nColPointOut = 0;
            #else:
            
            #订单信息
            excelHelperPointOut.append(orderIdCol[nReadRow],0, nColPointOut);
            excelHelperPointOut.append('经度',1, nColPointOut + 0);
            excelHelperPointOut.append('纬度',1, nColPointOut + 1);
            excelHelperPointOut.append('时间',1, nColPointOut + 2);
        
            self.readAmapOrder(excelHelperTotal,excelHelperPointOut,itemOrder,nReadRow,nColPointOut); 
            nColPointOut = nColPointOut + 4;
            nReadRow = nReadRow + 1;
        #endf
    
        excelHelperTotal.close('/Users/Shared/' + sourceName + '_Total.xls');
        excelHelperPointOut.close(strOutPath);
        
    #将点位文件切分为有效数据
    def readAmapOrder(self,excelHelperTotal,excelHelperPointOut,itemOrder,nRow,nCol)->str:
        if len(itemOrder) > 0:
            strSplite="|";
            strSpliteItem=",";
            
            lonArray = [];
            latArray = [];
            pointArray = [];
            numPoint=itemOrder.count(strSplite);
            listPoint = itemOrder.split(strSplite, numPoint);
            index = 2;
            stringService = LSStringService();
            for itemPoint in  listPoint:
                numItem=itemPoint.count(strSpliteItem);
                if numItem > 1:
                    listItem = itemPoint.split(strSpliteItem, numItem); 
                    excelHelperPointOut.append(listItem[0],index, 0 + nCol);
                    excelHelperPointOut.append(listItem[1],index, 1 + nCol);
                    excelHelperPointOut.append(listItem[2],index, 2 + nCol);
                    timeValue = stringService.timestamp_to_str(int(listItem[2]));
                    excelHelperPointOut.append(timeValue,index, 3 + nCol);
                    if not listItem[0] in lonArray or not listItem[1] in latArray:
                        lonArray.append(listItem[0]);
                        latArray.append(listItem[1]);        
                        pointArray.append(itemPoint);       
                    index = index + 1;
                else:
                    break;
            #endf
            
            strPoint = '';
            for validPoint in pointArray:
                if len(strPoint) > 0:
                    strPoint = strPoint + '|' + validPoint;
                else:
                    strPoint = validPoint;
            
            excelHelperTotal.append(strPoint,nRow, 2);
            excelHelperTotal.append(str(len(lonArray)),nRow, 3);
            excelHelperTotal.append(str(len(listPoint)),nRow, 4);
        else:
            excelHelperTotal.append(itemOrder,nRow, 2);
            excelHelperTotal.append('0',nRow, 3);
            excelHelperTotal.append('0',nRow, 4);
        
        return '';
    
    #读取高德link时间信息,转化为时间列
    def formatAmapLinkTime(self,sourcePath,sourceName,nReadCol):
        #pathRead = '/Users/Shared/demo.xls';
        excelHelperRead = BSExcel();
        orderIdAmapCol = excelHelperRead.readWorkbookCol(sourcePath, 0, 0);
        orderIdCol = excelHelperRead.readWorkbookCol(sourcePath, 0, 1);
        dataCol = excelHelperRead.readWorkbookCol(sourcePath, 0, nReadCol);
        dataCol.pop(0);
    
        #点位分析
        excelHelperPointOut = BSExcel();
        excelHelperPointOut.createWorkbook();
        excelHelperPointOut.createSheet('点位分析');
    
        #点位统计
        excelHelperTotal = BSExcel();
        excelHelperTotal.createWorkbook();
        excelHelperTotal.createSheet(sourceName);
        excelHelperTotal.append('高德orderId',0, 0);
        excelHelperTotal.append('神州orderId',0, 1);
        excelHelperTotal.append('有效点位',0, 2);
        excelHelperTotal.append('有效个数',0, 3);
        excelHelperTotal.append('总点位个数',0, 4);
    
        nColPointOut = 0;
        nReadRow = 1;
        nPointOutFileIndex = 0;
        strOutPath = '/Users/Shared/' + sourceName + '_detail' + str(nPointOutFileIndex) + '.xls'
        for itemOrder in dataCol:
            print('开始行' + str(nReadRow) + '列' + str(nColPointOut));
            excelHelperTotal.append(orderIdAmapCol[nReadRow],nReadRow, 0);
            excelHelperTotal.append(orderIdCol[nReadRow],nReadRow, 1);
            if nReadRow % 64 == 0:
                excelHelperPointOut.close(strOutPath);
                nPointOutFileIndex = nPointOutFileIndex + 1;
                strOutPath = '/Users/Shared/' + sourceName + '_detail' + str(nPointOutFileIndex) + '.xls'
                excelHelperPointOut.createWorkbook();
                excelHelperPointOut.createSheet('点位分析');
                nColPointOut = 0;
            #else:
            
            #订单信息
            excelHelperPointOut.append(orderIdCol[nReadRow],0, nColPointOut);
            excelHelperPointOut.append('经度',1, nColPointOut + 0);
            excelHelperPointOut.append('纬度',1, nColPointOut + 1);
            excelHelperPointOut.append('时间',1, nColPointOut + 2);
        
            self.readAmapLinkTime(excelHelperTotal,excelHelperPointOut,itemOrder,nReadRow,nColPointOut); 
            nColPointOut = nColPointOut + 4;
            nReadRow = nReadRow + 1;
        #endf
    
        excelHelperTotal.close('/Users/Shared/' + sourceName + '_Total.xls');
        excelHelperPointOut.close(strOutPath);
        
    #将高德Amap时间切分为有效数据
    def readAmapLinkTime(self,excelHelperTotal,excelHelperPointOut,itemOrder,nRow,nCol)->str:
        if len(itemOrder) > 0:
            strSplite="|";

            pointArray = [];
            numPoint=itemOrder.count(strSplite);
            listPoint = itemOrder.split(strSplite, numPoint);
            index = 2;
            for itemPoint in  listPoint:
                    excelHelperPointOut.append(itemPoint,index, 0 + nCol);
                    pointArray.append(itemPoint);       
                    index = index + 1;
            #endf
            
            strPoint = '';
            for validPoint in pointArray:
                if len(strPoint) > 0:
                    strPoint = strPoint + '|' + validPoint;
                else:
                    strPoint = validPoint;
            
            excelHelperTotal.append(strPoint,nRow, 2);
            excelHelperTotal.append(str(len(listPoint)),nRow, 4);
        else:
            excelHelperTotal.append(itemOrder,nRow, 2);
            excelHelperTotal.append('0',nRow, 3);
            excelHelperTotal.append('0',nRow, 4);
        
        return '';