


# 1. 下载安装  : pip install loguru

# 2. 导包  :
from loguru import logger

# 3. 打印一条日志 : hello world
logger.add('a.log',format="{time:YYYY-MM-DD HH:mm:ss} {level} {module} {line} {message}",level="DEBUG")
logger.debug("hello world")
logger.info("hello world")
logger.warning("hello world")
logger.success("hello world")
logger.error("hello world")