#used to manipulate different parts of python runtime env Allows us to operate on interpreter itself
import sys
import logging
from src.logger import logging
#function to get the custom message for any error
def error_message_details(error,error_details):
    _,_,exc_tb = error_details.exc_info() #gives all the information like file locaton ,line number etc

    file_name = exc_tb.tb_frame.f_code.co_filename


    error_message = f"""Error occurred in python
                    File_name = [{file_name}],
                    Line_number = [{exc_tb.tb_lineno}],
                    Error_message = [{str(error)}]
                        """
    return error_message

class CustomException(Exception) :
    def __init__(self,error_message,error_detail) :
        super().__init__(error_message)

        self.error_message = error_message_details(
            error_message,
            error_details= error_detail
            ) 
    def __str__(self):
        return self.error_message
    


#Documentation :
"""
======================== FILE EXPLANATION ========================

PURPOSE OF THIS FILE:
This file creates a custom exception handling system.
Instead of showing Python's default error message, it creates
a cleaner and more detailed error message containing:

1. File name where error occurred
2. Line number where error occurred
3. Actual error message


---------------------------------------------------------------
1) import sys
---------------------------------------------------------------

import sys

-> sys is a built-in Python module.
-> It allows interaction with Python runtime/interpreter.

Examples:
sys.exit()       -> terminates program
sys.argv         -> command line arguments
sys.path         -> shows module search paths
sys.exc_info()   -> returns current exception details

In this file we only use:
sys.exc_info()


---------------------------------------------------------------
2) error_message_details() function
---------------------------------------------------------------

def error_message_details(error,error_details):

This is a USER DEFINED function.

Purpose:
- Accepts error information
- Extracts traceback details
- Creates formatted custom error message
- Returns that message


---------------------------------------------------------------
3) Parameter: error
---------------------------------------------------------------

Stores actual exception object/message.

Example:

ZeroDivisionError("division by zero")

If code does:

1/0

Then error contains:
"division by zero"


---------------------------------------------------------------
4) Parameter: error_details
---------------------------------------------------------------

Usually receives:

sys

Example:

raise CustomException(e,sys)

This means:

error_details.exc_info()

becomes:

sys.exc_info()


---------------------------------------------------------------
5) sys.exc_info()
---------------------------------------------------------------

_,_,exc_tb = error_details.exc_info()

Built-in function from Python's sys module.

Returns:

(exception_type, exception_value, traceback_object)

Example:

(<class ZeroDivisionError>,
 ZeroDivisionError('division by zero'),
 traceback object)


---------------------------------------------------------------
6) _
---------------------------------------------------------------

_ means values are intentionally ignored.

First _  -> ignores exception type
Second _ -> ignores exception value

Only traceback object is needed.


---------------------------------------------------------------
7) exc_tb
---------------------------------------------------------------

Stores traceback object.

Traceback contains:

- file location
- line number
- function call stack
- execution path


---------------------------------------------------------------
8) file_name
---------------------------------------------------------------

file_name = exc_tb.tb_frame.f_code.co_filename

Breakdown:

exc_tb.tb_frame
-> gets current execution frame

f_code
-> gets compiled code object

co_filename
-> gets file name where error happened

Example output:

main.py


---------------------------------------------------------------
9) error_message variable
---------------------------------------------------------------

Stores final formatted error message.

Example output:

Error occurred in python
File_name = [main.py]
Line_number = [24]
Error_message = [division by zero]


---------------------------------------------------------------
10) str(error)
---------------------------------------------------------------

Built-in function.

Converts exception object into readable string.

Example:

ZeroDivisionError(...)
becomes:

division by zero


---------------------------------------------------------------
11) return error_message
---------------------------------------------------------------

Returns final formatted message.

Without return:
function would return None


---------------------------------------------------------------
12) CustomException class
---------------------------------------------------------------

class CustomException(Exception)

This is a USER DEFINED class.

It inherits from Python's built-in Exception class.

Meaning:
It behaves like normal exceptions
but allows customization.


---------------------------------------------------------------
13) Exception
---------------------------------------------------------------

Built-in parent class for most Python errors.

Examples:

ValueError
TypeError
ZeroDivisionError

Your class extends this functionality.


---------------------------------------------------------------
14) __init__()
---------------------------------------------------------------

def __init__(self,error_message,error_detail)

Constructor function.

Automatically runs when object is created.

Example:

raise CustomException(e,sys)


---------------------------------------------------------------
15) self
---------------------------------------------------------------

Represents current object instance.

Used to store variables specific to that object.


---------------------------------------------------------------
16) super().__init__(error_message)
---------------------------------------------------------------

Calls parent Exception class constructor.

Ensures your custom exception behaves like normal Python exceptions.


---------------------------------------------------------------
17) self.error_message
---------------------------------------------------------------

Stores final formatted custom error message inside object.


---------------------------------------------------------------
18) error_message_details() function call
---------------------------------------------------------------

self.error_message = error_message_details(
    error_message,
    error_details=error_detail
)

This calls your custom function and generates
the final detailed error message.


---------------------------------------------------------------
19) __str__()
---------------------------------------------------------------

def __str__(self):

Special built-in method.

Automatically runs when:

print(exception_object)

or

str(exception_object)

is called.


---------------------------------------------------------------
20) return self.error_message
---------------------------------------------------------------

Returns custom formatted message instead of Python default error.


---------------------------------------------------------------
FULL EXECUTION FLOW
---------------------------------------------------------------

Error occurs
    ↓
CustomException is raised
    ↓
__init__() runs
    ↓
error_message_details() runs
    ↓
traceback information extracted
    ↓
custom message created
    ↓
__str__() returns final message


---------------------------------------------------------------
EXAMPLE USAGE
---------------------------------------------------------------

try:
    a = 1/0

except Exception as e:
    raise CustomException(e,sys)


OUTPUT:

Error occurred in python
File_name = [main.py]
Line_number = [2]
Error_message = [division by zero]


===============================================================
"""