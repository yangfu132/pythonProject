#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import Session
from bs4 import BeautifulSoup
from LogService.LSLogger import get_logger
from FileBusiness.FBFileBusiness import sharedFileBusiness 

class SessionDriverService(object):
    def __init__(self):
        self.session = Session();
        self.logger = get_logger(sharedFileBusiness.log_dir + 'SessionDriverService.log');
        
    
        
    def post(self,url,param):
        result = '';
        self.main_url = url;
        # query order
        response = self.session.post(url, param);

        if response.status_code == 200 :
            # prase content
            result = BeautifulSoup(response.content, 'html.parser');
        #else 
        
        return result;