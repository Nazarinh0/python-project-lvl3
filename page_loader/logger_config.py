import logging


ERROR_LOG_FILENAME = '.page-loader-errors.log'

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s:%(name)s:%(process)d:%(lineno)d ' '%(levelname)s %(message)s',  # noqa: E501, WPS326
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(message)s',
        },
    },
    'handlers': {
        'logfile': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'filename': ERROR_LOG_FILENAME,
            'formatter': 'default',
            'backupCount': 2,
        },
        'verbose_output': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        'page-loader-info': {
            'level': 'INFO',
            'handlers': [
                'verbose_output',
            ],
        },
        'page-loader-error': {
            'level': 'ERROR',
            'handlers': [
                'logfile',
            ],
        },
    },
}

log_error = logging.getLogger('page-loader-error')
log_info = logging.getLogger('page-loader-info')
