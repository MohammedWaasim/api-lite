import inspect
import logging
import pdb
from traceback import print_stack
import allure
from allure_commons.model2 import Attachment

from utils import custom_logger as cl

class TestStatus():
    log = cl.customLogger(logging.INFO)

    def __init__(self):
        self.resultlist=[]

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("PASS")
                    self.log.info("###Verification Successful")
                    cl.allurelogs("###Verification Successful")
                else:
                    self.resultlist.append("FAIL")
                    self.log.info("###Verification Failed :: " +resultMessage)
                    cl.allurelogs("###Verification Failed :: " + resultMessage)
            else:
                self.resultlist.append("FAIL")
                self.log.error("###Verification Failed :: " + resultMessage)
                cl.allurelogs("###Verification Failed :: " + resultMessage)

        except:
            self.resultlist.append("FAIL")
            self.log.error("###Exception Occurred!!! ")
            cl.allurelogs("###Exception Occurred!!! ")


    def mark(self, result, resultMessage):
        self.setResult(result,resultMessage)

    def markFinal(self,result, resultMessage):
        self.setResult(result,resultMessage)
        test_case_name=inspect.stack()[1][3]
        if "FAIL" in self.resultlist:
            self.log.error(test_case_name +" ###### TEST FAILED")
            cl.allurelogs(test_case_name +" ###### TEST FAILED")
            self.resultlist.clear()
            assert True==False
        else:
            self.log.info(test_case_name + " ###### TEST PASSED")
            cl.allurelogs(test_case_name + " ###### TEST PASSED")
            self.resultlist.clear()
            assert True==True