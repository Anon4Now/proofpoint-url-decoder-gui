"""Module containing Utility Functions"""

# Standard Library imports
import logging


#####################################
# Create logger func
#####################################
def create_logger() -> logging:
    """
    Create a logger
    :return: logger
    """
    # Creating and Configuring Logger
    Log_Format = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(filename="logfile.log",
                        filemode="w",
                        format=Log_Format,
                        level=logging.ERROR)

    log = logging.getLogger()
    return log


logger = create_logger()


###########################
# Custom Error Handler func
###########################

def error_handler(func):
    # exception handling decorator function

    def inner_func(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except FileNotFoundError as err:
            logger.error("FileNotFoundError: error=%s func=%s", err, func.__name__)
        except EOFError as err:
            logger.error("EOFError: error=%s func=%s", err, func.__name__)
        except KeyError as err:
            logger.error("KeyError: error=%s func=%s", err, func.__name__)
        except TypeError as err:
            logger.error("TypeError: error=%s func=%s", err, func.__name__)
        except ValueError as err:
            logger.error("ValueError: error=%s func=%s", err, func.__name__)
        except Exception as err:
            logger.error("GeneralException: error=%s func=%s", err, func.__name__)

    return inner_func
