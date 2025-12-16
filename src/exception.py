import sys 

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    error_message='Error occured in python script [{0}] [{1}] [{2}]'
    file_name=exc_tb.tb_frame.f_code.co_filename