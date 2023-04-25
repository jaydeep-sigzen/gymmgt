# Copyright (c) 2023, Jaydeep-Sigzen and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from gymmgt.api.gymmgt import calculate_age


class GymMembers(Document):
    def before_insert(self):
        if not frappe.db.get_single_value('Gym Settings', 'link_to_customer'):
            frappe.throw(
                'Please enable Link to Customer Check box from Gym Settings.')
