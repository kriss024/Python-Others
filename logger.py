import logging

def init_logger():
    log_format = "%(asctime)s:%(levelname)s:%(name)s:" \
                "%(filename)s:%(lineno)d:%(message)s"

    logging.basicConfig(level = logging.DEBUG
                        , format = log_format)

def main():
    logging.info('Started')
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
    logging.info('Finished')

if __name__ == "__main__":
    init_logger()
    main()