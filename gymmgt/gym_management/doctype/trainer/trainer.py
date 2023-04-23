# Copyright (c) 2023, Jaydeep-Sigzen and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
from gymmgt.api.gymmgt import calculate_age


class Trainer(WebsiteGenerator):

    def before_insert(self):
        self.age = f"{calculate_age(self.date_of_birth)} Year Old"
