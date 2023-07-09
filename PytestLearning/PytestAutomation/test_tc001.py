#Method name should be start with test to execute in pytest
#Testcase code must be written inside a method

import pytest


try:
    '''Use below command to execute only one TC
    pytest -s -v -k test_tc001 PytestAutomation'''

    def test_tc001():
        print("Pytest Method1")

    #Skip decorator to Skip perticular TCs
    # @pytest.mark.skip("Issue exist in this method, Developer will fix & give the fix in next build")
    # def test_tc002():
    #     print("Pytest Method2")


    ''' Right click on root project>>open terminal>> Enter below command to execute multiple testcases
    
        CMD>>pytest -s -v pytestAutomationTCs
        
        -s to display print statement items, -v Verbose, To verify & display testcases name with status (Success/Failed testcases reports)'''

    #Executing method based on the condition
    a=4
    @pytest.mark.skipif(a>5,reason="Issue exist in this method, Developer will fix & give the fix in next build")
    def test_tc002():
        print("Pytest Method2")
except Exception as e:
    print(e)