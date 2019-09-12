from unittest import TestLoader, TestSuite, TextTestRunner
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from Scripts.Tests_ContactUs import ContactPage
from Scripts.Tests_HomePage import HomePage
from Scripts.Tests_LoginPage import LoginPage
from Scripts.Tests_SignUp import SignUpPage
from Scripts.Tests_AccountPage import AccountPage
from Scripts.Tests_HistoryRecording import HistoryRecording



if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(ContactPage),
        loader.loadTestsFromTestCase(HomePage),
        loader.loadTestsFromTestCase(LoginPage),
        loader.loadTestsFromTestCase(SignUpPage),
        loader.loadTestsFromTestCase(AccountPage),
        loader.loadTestsFromTestCase(HistoryRecording)
        ))

#run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

