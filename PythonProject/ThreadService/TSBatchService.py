
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import _thread
from ThreadService.TSBatchTargetDTO import TSBatchTargetDTO
class TSBatchService:
    #批量请求
    def batchFunc(self,taskList,target:TSBatchTargetDTO):
        taskCount = len(taskList);
        self.finishCount = 0;
        
        nThreadCount = 10;
        if taskCount < nThreadCount:
            nThreadCount = taskCount;
        #else cont.
        
        #生成分配队列
        subListArray = [];
        nSubArrayCount = 0;
        while nSubArrayCount < nThreadCount:
            subListArray.append([]);
            nSubArrayCount += 1;
        #endw
        
        #分配order到不同的队列
        i = 0
        for aorder in taskList:
            if True:
                t = i % nThreadCount;
                subListArray[t].append(aorder);
                i=i+1
        #endf
        
        nThreadIndex = 0;
        #生成对应的多线程
        
        while nThreadIndex < nThreadCount:
            threadName = 'thread' + str(nThreadIndex);
            _thread.start_new_thread( threadTaskFunc, (subListArray[nThreadIndex],threadName ,target) )
            nThreadIndex += 1;
        
        #等待结束
        while self.finishCount < nThreadCount:
            pass

shareBatchService = TSBatchService();

#task Func
def threadTaskFunc(threadTaskList,threadname,target:TSBatchTargetDTO):
    totle = len(threadTaskList)
    remain = totle;
    for taskItem in threadTaskList :
        target.func(taskItem);
        remain = remain-1
        print(threadname + ' : remain='+str(remain));
    #endf
    print('%s>>queryOrder end\n'%(threadname),flush = True)
    shareBatchService.finishCount = shareBatchService.finishCount + 1;