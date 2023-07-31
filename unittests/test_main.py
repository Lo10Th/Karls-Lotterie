import unittest
from main import app
from unittest.mock import patch

class ColoredTextTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.writeln("")


class TestLotteryApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True

    def tearDown(self):
        pass

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Karls Lotterie", response.data)

    @patch('main.random.randint')
    def test_loskaufen(self, mock_randint):
        mock_randint.return_value = 1  # Mocken Sie den Rückgabewert von random.randint, um vorhersagbare Ergebnisse zu erzielen
        response = self.app.post('/loskaufen', data={'einsatz': '3'})
        self.assertIn(b"won4", response.data)  # Test if "won4" is present in the response
        self.assertEqual(response.status_code, 200)

    def test_uebergangend_page(self):
        response = self.app.get('/uebergangend?type=won4&gewinn=100&benutztergewinn=133')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"133.0 Euro", response.data)

    def test_admin_page(self):
        response = self.app.get('/admin')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Lottery Admin", response.data)


if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestLotteryApp)
    test_result = unittest.TextTestRunner(verbosity=2, resultclass=ColoredTextTestResult).run(test_suite)

    if test_result.wasSuccessful():
        print("\033[92m\nAll tests passed!\033[0m")
    else:
        print("\033[91m\nSome tests failed!\033[0m")
