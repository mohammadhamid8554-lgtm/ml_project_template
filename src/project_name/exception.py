import sys

# --- 🔗 CONNECTIONS ---
# Like logger.py, this file is a tool used by the rest of the project.
# Whenever a try/except block fails in files like main.py or utils.py, 
# they send the error here to be formatted into a clear crash report.

def error_message_detail(error, error_details: sys):
    """
    This function digs into the system details to find exactly where the code broke.
    """
    # exc_info() returns details about the error. We only care about the 3rd item (traceback)
    _, _, exc_tb = error_details.exc_info()
    if exc_tb is None:
        return str(error)

    # Extract the name of the file and the exact line number where the error happened
    file_name = exc_tb.tb_frame.f_code.co_filename
    return (
        "Error occurred in Python script name [{0}] line number [{1}] "
        "error message [{2}]"
    ).format(file_name, exc_tb.tb_lineno, str(error))


class CustomException(Exception):
    """
    This is our custom error class. When we "raise CustomException", 
    this class automatically formats the error message beautifully using the function above.
    """
    def __init__(self, error, error_details: sys):
        # Call our detail function to create the clean error message
        self.error_message = error_message_detail(error, error_details)
        # Pass it to the built-in Python Exception system
        super().__init__(self.error_message)

    def __str__(self):
        # When someone tries to print this error, return our beautifully formatted message
        return self.error_message
