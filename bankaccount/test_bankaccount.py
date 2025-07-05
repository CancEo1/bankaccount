# Purpose: tests for the BankAccount class contructor, deposit, withdraw, addInterest, and getBalance methods.
# test each method that was provided in the bankaccount module
# designed to identify bugs for project 6 requirements
import unittest
from bankaccount import BankAccount

class TestBankAccount(unittest.TestCase):
    # Test cases for the BankAccount class
    @classmethod
    def setUpClass(cls):
        # Set up any state specific to the execution of the given class.
        print("Setting up BankAccount tests...")
    @classmethod
    def tearDownClass(cls):
        # Clean up any state that was set up for the class.
        print("Tearing down BankAccount tests...")

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
        self.assertEqual(acct.getBalance(), 150) 

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
        self.assertAlmostEqual(acct.getBalance(), 50) 

        acct = BankAccount(90)
        acct.withdraw(100)  # Triggers PENALTY
        self.assertAlmostEqual(acct.getBalance(), 80)  # PENALTY applied

        acct = BankAccount(100)
        acct.withdraw(0)
        self.assertAlmostEqual(acct.getBalance(), 100)
    
    # test method to add interest to the account
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
    
    # test method to get the current balance of the account
    def test_getBalance(self):
        # test getBalance with various initial balances
        acct = BankAccount(100)
        acct.deposit(50)
        self.assertEqual(acct.getBalance(), 150)

        acct = BankAccount(200)
        acct.deposit(100)
        self.assertEqual(acct.getBalance(), 300)

        acct = BankAccount(50)
        acct.deposit(0)
        self.assertEqual(acct.getBalance(), 50)

    def test_negative_deposit(self):
        acct = BankAccount(100)
        acct.deposit(-50)
        self.assertEqual(acct.getBalance(), 100)  # Currently fails silently
        print("Negative deposit did not change balance as expected.")
        # Expected: Should raise error or ignore deposit

    def test_negative_withdrawal(self):
        acct = BankAccount(100)
        acct.withdraw(-25)
        self.assertEqual(acct.getBalance(), 100)  # Penalizes even for negative
        # Expected: Should raise error or ignore the transaction

    def test_withdraw_exceeds_balance_penalty(self):
        acct = BankAccount(0)
        acct.withdraw(20)
        self.assertEqual(acct.getBalance(), -10)
        # Current logic allows overdraw via penalty without warning

    def test_negative_interest(self):
        acct = BankAccount(100)
        acct.addInterest(-5)
        self.assertEqual(acct.getBalance(), 100)
        # Applying negative interest reduces balance, which should not happen

if __name__ == '__main__':
    unittest.main()