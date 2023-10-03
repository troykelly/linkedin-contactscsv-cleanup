from script import custom_merge
import unittest
import pandas as pd


class TestCSVCleanup(unittest.TestCase):
    def setUp(self):
        self.data = ['FirstName', 'LastName', 'PhoneNumbers', 'Emails']
        self.df = pd.DataFrame([['John Doe', 'Doe', '1234567890', 'johndoe@example.com'],
                                ['John Doe Doe', 'Doe', '1234567890',
                                    'johndoe@example.com'],
                                ['John', 'Doe', '1234567890', 'johndoe@example.com']],
                               columns=self.data)

    def tearDown(self):
        del self.df

    def test_custom_merge(self):
        right = self.df.loc[1]
        left = self.df.loc[0]
        merged = custom_merge(left, right)
        self.assertEqual(merged['FirstName'], 'John Doe')


if __name__ == "__main__":
    unittest.main()
