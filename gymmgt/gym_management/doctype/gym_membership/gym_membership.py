# Copyright (c) 2023, Jaydeep-Sigzen and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import *


class GymMembership(Document):

    def validate(self):
        if frappe.db.exists('Gym Membership',
                            {"member": self.member}) and self.is_new():
            gym_membership = frappe.get_last_doc(
                'Gym Membership', filters={"member": self.member})
            if str(gym_membership.end_date) >= nowdate():
                frappe.throw("Membership already active.")

        if self.end_date >= today():
            self.status = "Active"
        else:
            self.status = "Expired"
