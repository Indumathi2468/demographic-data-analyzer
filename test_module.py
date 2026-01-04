import unittest
import demographic_data_analyzer as dda


class DemographicAnalyzerTest(unittest.TestCase):

    def test_calculate_demographic_data(self):
        result = dda.calculate_demographic_data("adult.data.csv")
        self.assertIsInstance(result, dict)


if __name__ == "__main__":
    unittest.main()
