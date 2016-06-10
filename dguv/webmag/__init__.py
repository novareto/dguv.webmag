import logging
logger = logging.getLogger('uvcsite.dguv.webmag')

def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)
