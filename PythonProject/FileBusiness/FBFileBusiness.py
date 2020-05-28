#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

class FBFileBusiness(object):
    def __init__(self):
        self.main_dir = '/Users/Shared/driver_point/';
        if not os.path.exists(self.main_dir):
            os.mkdir(self.main_dir);
        #else cont.
        
        self.log_dir = self.main_dir + 'log_dir/';
        if not os.path.exists(self.log_dir):
            os.mkdir(self.log_dir);
        #else cont.
        
            
sharedFileBusiness = FBFileBusiness();
