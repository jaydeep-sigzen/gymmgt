# Copyright (c) 2023, Jaydeep-Sigzen and Contributors

# Copyright (c) 2023, Jaydeep-Sigzen and Contributors
# See license.txt

# import frappe
import frappe
from frappe.tests.utils import FrappeTestCase
import unittest


class TestTrainerRating(unittest.TestCase):

    def test_trainer_rating(self):
        test_diet = frappe.get_doc({
            "doctype": "Trainer Rating",
            "member": "Member 2",
            "trainer": "Trainer",
            "rating": "0.80"
        }).insert()
