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
    
    def loginAdmin(self,url,userID,loginKey):
        proLoginEnv = url + 'system/login.login';
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
        headers = {'User-Agent':user_agent};
        r = self.session.post(proLoginEnv, {'loginId': userID, 'password': loginKey},headers);
        print(r.status_code)
        if r.status_code != 200:
            self.logger.warn('error login failed, precess stop');
            self.logged = False;
        else:
            self.logged = True;
            
        return self.logged;