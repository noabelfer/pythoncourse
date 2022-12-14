#!/usr/bin/env python
import logging

logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.debug("This is a debug log {fname}".format(fname = 'gorg'))
logger.info("This is an info log")
logger.critical("This is critical")
logger.error("An error occurred")