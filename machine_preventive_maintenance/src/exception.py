import sys
from src.logger import logging

def error_message_details(error, error_details: sys):
    """
    Generate a detailed error message with file name and line number.
    """
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in Python script: [{file_name}] "
        f"at line [{exc_tb.tb_lineno}] with message: [{str(error)}]"
    )
    return error_message


class customException(Exception):
    """
    Custom Exception class to wrap standard errors with trace details.
    """
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details=error_details)
    
    def __str__(self):
        return self.error_message
