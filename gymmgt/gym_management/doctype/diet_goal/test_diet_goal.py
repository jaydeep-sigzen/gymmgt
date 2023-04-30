# Copyright (c) 2023, Jaydeep-Sigzen and Contributors
# See license.txt

# import frappe
import frappe
from frappe.tests.utils import FrappeTestCase
import unittest


class TestDietGoal(unittest.TestCase):

    def test_diet_goal(self):
        test_diet = frappe.get_doc({
            "doctype": "Diet Goal",
            "diet_goal": "Test Weight Loose 1234",
        }).insert()
