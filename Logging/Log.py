import logging


'''
Simple logging class
To use in project: import Log
Log.Logger.LogInfo('***')
'''

class Logger:
    # create logger 
    logger = logging.getLogger('Snake')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('Snake.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
       
    #define methods for logging
    def LogInfo(mess):
        Logger.logger.info(mess)
        
    def LogWarning(mess):
        Logger.logger.warning(mess)
        
    def LogError(mess):
        Logger.logger.error(mess)
        
        
    



