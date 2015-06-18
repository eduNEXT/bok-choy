"""
Tests for the WebAppTest class.
"""
import os
from unittest import expectedFailure

from bok_choy.web_app_test import WebAppTest
from .pages import ImagePage


class ScreenshotAssertTest(WebAppTest):
    """
    Test the integration with needle and its screenshot assertion capability.
    """
    def test_needle_screenshot_success(self):
        """
        Test the integration with needle to capture and assert on a screenshot of an element.

        Note that the baseline_directory is computed in the __init__ method of NeedleTestCase,
        so we can monkeypatch it here in the testcase itself.
        """
        self.baseline_directory = os.path.realpath(os.path.join(os.getcwd(), 'tests', 'baseline'))
        self.page = ImagePage(self.browser).visit()
        self.assertScreenshot('#green_check', 'correct-icon')

    @expectedFailure
    def test_needle_screenshot_failure(self):
        """
        Test the integration with needle to capture and assert on a screenshot of an element.

        Note that the baseline_directory is computed in the __init__ method of NeedleTestCase,
        so we can monkeypatch it here in the testcase itself.
        """
        self.baseline_directory = os.path.realpath(os.path.join(os.getcwd(), 'tests', 'baseline'))
        self.page = ImagePage(self.browser).visit()
        self.assertScreenshot('#green_check', 'incorrect-icon')