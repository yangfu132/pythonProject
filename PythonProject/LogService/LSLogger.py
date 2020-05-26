#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
def get_logger(fileName: str):        
    # 获取logger实例，如果参数为空则返回root logger
    logger = logging.getLogger(fileName);
    # 制定logger 输出格式
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s');
    # 文件日志
    file_handler = logging.FileHandler(fileName);
    file_handler.setFormatter(formatter); #可以通过setFormatter制定输出格式
    
    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout);
    console_handler.formatter = formatter;
    
    # 为logger 添加的日志处理器
    logger.addHandler(file_handler);
    logger.addHandler(console_handler);
    
    # 指定日志的最低输出级别，默认为WARN级别
    logger.setLevel(logging.INFO);

    #输出不同级别的log
    logger.debug('this is debug info');
    logger.info('this is information');
    logger.warn('this is warning message');
    logger.error('this is a error message');
    logger.fatal('this is fatal message, it is same as logger.critical');
    logger.critical('this is critical message');
    return logger;