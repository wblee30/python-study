import os
import logging
import pathlib
from logging.handlers import TimedRotatingFileHandler


file_path = pathlib.Path(__file__).parent.parent.absolute()/'log'/'Lebot.log'
print("pathlib.path().absolute()", pathlib.Path(__file__).parent.parent.absolute())
print("filepath", file_path)

print("file_path.parents[0]:", file_path.parents[0])
print("file_path.parents[1]:", file_path.parents[1])

logger = logging.getLogger(__name__)
print("logger:",logger)

# setLevel에서 로그 옵션 설정
logger.setLevel(logging.DEBUG)
print( logger.setLevel(logging.DEBUG))

stream_handler = logging.StreamHandler()
file_handler = TimedRotatingFileHandler(file_path, when="midnight", encoding='utf-8')

#formaater 생성 (log format 설정)
formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s> %(message)s')

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

file_handler.suffix = "%Y%m%d"

# logger instance에 handler 설정
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.debug('debug 모드')
logger.info('info 모드')
logger.warning('warning 모드')
logger.error('error 모드')
logger.critical('critical 모드')


