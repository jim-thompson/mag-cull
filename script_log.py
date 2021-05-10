'''
Created on Apr 17, 2021

@author: jct
'''

_nslog_ptr = None

def setup_nslog(log_func):
    global _nslog_ptr
    _nslog_ptr= log_func
    
def nslog(msg):
    global _nslog_ptr

    if _nslog_ptr is not None:
        _nslog_ptr(msg)
    else:
        print(msg)
        

# #import sys
#
# # Log the given message - if running inside an Automator script, the
# # message will go to the system log via NSLog(); if running outside of
# # Automator, the message will go to the log file.
#
# def mc_nslog(msg):
    # # Call _nslog. When running inside an Automator script, this
    # # function will be defined by the Automator stub. When running
    # # outside of Automator, this function will be defined in the try
    # # clause below.
    # _mc_nslog(msg)
    #
# # try:
    # # # Make a test calls to _nslog. When running inside an Automator
    # # # script, this function will already be defined by the Automator
    # # # stub, so the call to _nslog will succeed and the message will go
    # # # to the system log...
    # # _mc_nslog("Test - probe to see if _nslog is defined.") #@UndefinedVariable
# # except NameError:
    # # # ...when running outside of Automator, a NameError exception will
    # # # be thrown, which we will catch here, and will use to define the
    # # # _nslog function.
    # # def _mc_nslog(msg):
        # # print(msg)

