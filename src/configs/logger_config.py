class LoggerConfig:
    dictConfig = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(threadName)s - %(levelname)s - '
                          '%(message)s - [in %(filename)s:%(lineno)d]'
            },
            'brief': {
                'format': '%(message)s'
            }
        },
        'handlers': {
            'info': {
                'level': 'INFO',
                'formatter': 'standard',
                'class': 'logging.StreamHandler'
            },
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO'
            }
        },
        'loggers': {
            'main': {
                'handlers': ['info'],
                'level': 'INFO',
                'propagate': True
            }
        },
        'root': {
            'level': 'INFO',
            'handlers': ['info']
        }
    }