import unittest
import os
from main import simple, find_twin_primes, write_results_to_file


class TestPrimeFunctions(unittest.TestCase):

    def test_simple_with_primes(self):
        self.assertTrue(simple(2))
        self.assertTrue(simple(3))
        self.assertTrue(simple(5))
        self.assertTrue(simple(7))
        self.assertTrue(simple(11))
        self.assertTrue(simple(13))
        self.assertTrue(simple(17))
        self.assertTrue(simple(19))
        self.assertTrue(simple(23))

    def test_simple_with_non_primes(self):
        self.assertFalse(simple(1))
        self.assertFalse(simple(4))
        self.assertFalse(simple(6))
        self.assertFalse(simple(8))
        self.assertFalse(simple(9))
        self.assertFalse(simple(10))
        self.assertFalse(simple(12))
        self.assertFalse(simple(14))
        self.assertFalse(simple(15))
        self.assertFalse(simple(16))
        self.assertFalse(simple(18))
        self.assertFalse(simple(20))
        self.assertFalse(simple(21))
        self.assertFalse(simple(22))
        self.assertFalse(simple(24))
        self.assertFalse(simple(25))
        self.assertFalse(simple(26))
        self.assertFalse(simple(27))
        self.assertFalse(simple(28))
        self.assertTrue(simple(29))  

    def test_simple_with_edge_cases(self):
        self.assertFalse(simple(0))
        self.assertFalse(simple(-1))
        self.assertFalse(simple(-2))

    def test_find_twin_primes_with_valid_range(self):
        self.assertEqual(find_twin_primes(1, 10), [(3, 5), (5, 7)])
        self.assertEqual(find_twin_primes(10, 20), [(11, 13), (17, 19)])
        self.assertEqual(find_twin_primes(1, 20), [(3, 5), (5, 7), (11, 13), (17, 19)])
        self.assertEqual(find_twin_primes(3, 10), [(3, 5), (5, 7)])
        self.assertEqual(find_twin_primes(5, 15), [(5, 7), (11, 13)])

    def test_find_twin_primes_with_no_twin_primes(self):
        self.assertEqual(find_twin_primes(20, 28), [])
        self.assertEqual(find_twin_primes(1, 2), [])
        self.assertEqual(find_twin_primes(1, 3), [])


    def test_find_twin_primes_with_invalid_range(self):
        self.assertEqual(find_twin_primes(10, 1), []) 

    def test_write_results_to_file_row_format(self):
        twin_primes = [(3, 5), (5, 7)]
        filename = "test_row.txt"
        delimiter = ","
        write_results_to_file(filename, twin_primes, delimiter, "row")
        with open(filename, "r") as f:
            content = f.read().strip()
        self.assertEqual(content, "3,5\n5,7")
        os.remove(filename)  # очистка

    def test_write_results_to_file_column_format(self):
        twin_primes = [(3, 5), (5, 7)]
        filename = "test_column.txt"
        delimiter = ","
        write_results_to_file(filename, twin_primes, delimiter, "column")
        with open(filename, "r") as f:
            content = f.read().strip()
        self.assertEqual(content, "3\n5\n5\n7")
        os.remove(filename)  # очистка

    def test_write_results_to_file_invalid_format(self):
        twin_primes = [(3, 5), (5, 7)]
        filename = "test_invalid.txt"
        delimiter = ","

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        write_results_to_file(filename, twin_primes, delimiter, "wrong_format")

        sys.stdout = sys.__stdout__
        printed_message = captured_output.getvalue().strip()

        self.assertEqual(printed_message, "Ошибка: Неверный формат вывода.  Используйте 'row' или 'column'.")

        self.assertFalse(os.path.exists(filename))

if __name__ == '__main__':
    unittest.main()