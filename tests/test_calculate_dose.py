# test_calculate_dose.py

import pytest
from main import calculate_dose
import streamlit as st

"""
Code Analysis:
--The function calculates the amount of medication to be administered based on the prescribed dose, the available dose, 
and the quantity of medication available.
- It is commonly used in nursing to ensure that the correct amount of medication is given to a patient.
- The function takes three inputs: dose (the prescribed amount of medication), available_dose (the amount of medication 
available in a single dose), and quantity (the total quantity of medication available).
- If the quantity is not zero, the function calculates the amount of medication to be administered by dividing the 
prescribed dose by the available dose and multiplying it by the quantity.
- If the quantity is zero, the function returns 0, indicating that no medication can be administered.
- The function returns the calculated amount of medication to be administered.
"""

"""
Test Plan:
- test_calculate_dose_happy_path(): tests that the function returns the correct amount of medication to be administered when dose, available_dose, and quantity are all positive integers. Tags: [happy path]
- test_calculate_dose_happy_path_equal(): tests that the function returns the correct amount of medication to be administered when dose is equal to available_dose and quantity is greater than zero. Tags: [happy path]
- test_calculate_dose_happy_path_multiple(): tests that the function returns the correct amount of medication to be administered when dose is a multiple of available_dose and quantity is greater than zero. Tags: [happy path]
- test_calculate_dose_edge_case_zero_available_dose(): tests that the function returns 0 when available_dose is zero. Tags: [edge case]
- test_calculate_dose_edge_case_zero_quantity(): tests that the function returns 0 when quantity is zero. Tags: [edge case]
- test_calculate_dose_general_behavior_negative_values(): tests that the function handles negative values for dose, available_dose, or quantity. Tags: [general behavior]
- test_calculate_dose_edge_case_zero_dose(): tests that the function returns 0 when dose is zero. Tags: [edge case]
- test_calculate_dose_edge_case_greater_dose(): tests that the function returns 20 when dose is greater than quantity * available_dose. Tags: [edge case]
"""


class TestCalculateDose:

    def test_calculate_dose_happy_path(self):
        assert calculate_dose(600, 500, 1) == 1.2
        assert calculate_dose(400, 500, 1) == 0.8
        assert calculate_dose(400, 200, 1) == 2
        assert calculate_dose(1000, 200, 5) == 25

    def test_calculate_dose_happy_path_equal(self):
        assert calculate_dose(10, 10, 2) == 2

    def test_calculate_dose_happy_path_multiple(self):
        assert calculate_dose(20, 5, 4) == 16

    def test_calculate_dose_edge_case_zero_quantity(self):
        assert calculate_dose(10, 5, 0) == 0

    def test_calculate_dose_general_behavior_negative_values(self):
        assert calculate_dose(-10, 5, 2) == -4
        assert calculate_dose(10, -5, 2) == -4
        assert calculate_dose(10, 5, -2) == -4

    def test_calculate_dose_edge_case_zero_dose(self):
        assert calculate_dose(0, 5, 2) == 0

    def test_calculate_dose_edge_case_greater_dose(self):
        assert calculate_dose(10, .5, 1) == 20
