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

    def validate(self):
        self.create_customer()

    def create_customer(self):
        if not frappe.db.exists('Customer',
                                {'customer_name': self.member_name}):
            customer = frappe.new_doc('Customer')
            customer.customer_name = self.member_name
            customer.email_id = self.email_id
            customer.mobile_no = self.mobile_number
            customer.customer_type = "Individual"
            customer.customer_group = "Individual"
            customer.territory = "India"
            customer.save()
            frappe.msgprint('CUstomer Created')