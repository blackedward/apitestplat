import os
import sys as _sys
from pathlib import Path
from loguru import logger
from config import loglevel

log_path = Path(os.path.dirname(os.path.dirname(__file__)) + '/log')
log_file = str(log_path) + '/{time:YYYY-MM-DD}.log'
if not log_path.is_dir():
    log_path.mkdir()

# loguru默认添加了控制台输出,先去掉再添加(不然不知道怎么设置它的级别)
logger.remove(None)
logger.add(_sys.stderr, level=loglevel)

# 指定日志输出文件(0:0分割文件)
logger.add(log_file, rotation="0:0", level=loglevel, retention=100, encoding='utf-8')
