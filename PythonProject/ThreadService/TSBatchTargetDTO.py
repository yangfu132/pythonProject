#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class TSBatchTargetDTO:
    def __init__(self):
        self.func = self.targetFunc();
        self.params = {};
        
    def targetFunc(self,task):
        print('复制为其它函数');