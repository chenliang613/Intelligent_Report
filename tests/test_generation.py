import unittest
from datetime import date
from scripts.generate_reports import month_window, extract_report, report_names

class GenerationTests(unittest.TestCase):
    def test_previous_month_year_boundary(self):
        self.assertEqual(month_window('', date(2026, 1, 1))[0], '2025-12')

    def test_leap_and_partial_month(self):
        self.assertEqual(str(month_window('2024-02', date(2026, 1, 1))[2]), '2024-02-29')
        self.assertEqual(month_window('2026-01', date(2026, 1, 8))[2], date(2026, 1, 8))

    def test_invalid_and_future_month(self):
        for value in ['2026-13', '2026-1', '../foo', '2027-01']:
            with self.assertRaises(ValueError):
                month_window(value, date(2026, 1, 8))

    def test_refuse_unsearched_response(self):
        with self.assertRaises(RuntimeError):
            extract_report({'status': 'completed', 'output': []})

    def test_independent_report_selection(self):
        self.assertEqual(report_names('model'), ['report1-model-development.md'])
        self.assertEqual(report_names('agent'), ['report2-agent-development.md'])
        self.assertEqual(report_names('industry'), ['report3-industry-adoption.md'])
        self.assertEqual(len(report_names('all')), 3)
