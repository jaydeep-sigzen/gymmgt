# Copyright (c) 2023, Jaydeep-Sigzen and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from gymmgt.api.gymmgt import calculate_age


class GymMember(Document):
    def before_insert(self):
        self.age = f'{calculate_age(self.date_of_birth)} Year Old'
