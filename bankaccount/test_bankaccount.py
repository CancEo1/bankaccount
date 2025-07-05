# Purpose: tests for the BankAccount class contructor, deposit, withdraw, addInterest, and getBalance methods.
# test each method that was provided in the bankaccount module
# designed to identify bugs for project 6 requirements
import unittest
from bankaccount import BankAccount

class TestBankAccount(unittest.TestCase):
    # Test cases for the BankAccount class
    # test method to retrieve the initial balance of the account
    def test_initial_balance(self):
        # test initial balances with various amounts
        self.assertEqual(BankAccount().getBalance(), 0.0)
        self.assertEqual(BankAccount(100).getBalance(), 100.0)
        self.assertEqual(BankAccount(50.5).getBalance(), 50.5)
    
    # test method to deposit money into the account
    def test_deposit(self):
        # test deposits with various amounts
        acct = BankAccount(100)
        acct.deposit(50)
        self.assertEqual(acct.getBalance(), 150)  # Error in original code, should be 150
        acct = BankAccount(100)
        acct.deposit(0)
        self.assertEqual(acct.getBalance(), 100)
        acct = BankAccount(150)
        acct.deposit(50)
        self.assertEqual(acct.getBalance(), 200)

    # test method to withdraw money from the account
    def test_withdraw(self):
        # test withdraws with or/and without penalty
        acct = BankAccount(100)
        acct.withdraw(50)
        self.assertAlmostEqual(acct.getBalance(), 50)  # Error in original code, should be 50

        acct = BankAccount(90)
        acct.withdraw(100)  # Triggers PENALTY
        self.assertAlmostEqual(acct.getBalance(), 80)  # PENALTY applied

        acct = BankAccount(100)
        acct.withdraw(0)
        self.assertAlmostEqual(acct.getBalance(), 100)
    
    def test_addInterest(self):
        # add interests at various rates
        acct = BankAccount(100)
        acct.addInterest(10)
        self.assertAlmostEqual(acct.getBalance(), 110.0)

        acct = BankAccount(200)
        acct.addInterest(12)
        self.assertAlmostEqual(acct.getBalance(), 224.0)

        acct = BankAccount(100)
        acct.addInterest(0)
        self.assertAlmostEqual(acct.getBalance(), 100.0)

    def test_getBalance(self):
        acct = BankAccount(100)
        acct.deposit(50)
        self.assertEqual(acct.getBalance(), 150)

        acct = BankAccount(200)
        acct.deposit(100)
        self.assertEqual(acct.getBalance(), 300)

        acct = BankAccount(50)
        acct.deposit(0)
        self.assertEqual(acct.getBalance(), 50)

if __name__ == '__main__':
    unittest.main()