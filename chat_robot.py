#encoding=utf8
import itchat
import logging
import os
import sys
import json
import time
from tuling import get_response
from config import g_conf

def create_logger(logfilename, logName=""):
    """创建日志对象"""
    current_process = os.path.basename(sys.argv[0])
    current_process = current_process[0:current_process.rfind(".py")]
    import logging,logging.handlers
    logger = logging.getLogger(logName)
    infohdlr = logging.handlers.RotatingFileHandler(logfilename+current_process+'.info.log', maxBytes=100*1000*1000, backupCount=10)
    infohdlr.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(levelname)6s  %(threadName)-12s %(filename)-10s  %(lineno)4d:%(funcName)16s|| %(message)s')

    infohdlr.setFormatter(formatter)

    logger.addHandler(infohdlr)

    logger.setLevel(logging.INFO)
    return logger

logger = create_logger('./')

#@itchat.msg_register('Text')
#def text_reply(msg):
#    logger.info('private receive msg=%s', json.dumps(msg, ensure_ascii=False, indent=4))
#
#    if g_conf.FILTER_USER_NAME != '' and g_conf.FILTER_USER_NAME != msg.user['NickName']:
#        return
#
#    time.sleep(2)
#    logger.info('private wechat from name=%s, msg=%s' % (msg.user['NickName'], msg.text))
#    response = get_response(msg['Text']) or u'正在拯救世界，请稍等。。。'
#    logger.info('private wechat to name=%s, msg=%s' % (msg.user['NickName'], response))
#
#    return response

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
    if msg['isAt']:
    	logger.info('group receive msg=%s', json.dumps(msg, ensure_ascii=False, indent=4))
    	logger.info('group wechat from name=%s, msg=%s' % (msg.user['NickName'], msg.text))
        time.sleep(2)
    	response = get_response(msg['Text']) or u'正在拯救世界，请稍等。。。'
    	logger.info('group wechat to name=%s, msg=%s' % (msg.user['NickName'], response))

    	return response

itchat.auto_login(True, enableCmdQR=2)
itchat.run()
