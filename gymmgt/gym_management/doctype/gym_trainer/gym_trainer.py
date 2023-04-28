# Copyright (c) 2023, Jaydeep-Sigzen and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from gymmgt.api.gymmgt import calculate_age


class GymTrainer(WebsiteGenerator):

    def before_insert(self):
        self.age = f"{calculate_age(self.date_of_birth)} Year Old"

    def compute_age(self):
        if self.date_of_birth:
            print(f'\n\n\n\ compute_age- {self.date_of_birth}')
            self.age = f"{calculate_age(self.date_of_birth)} Year Old"

    def validate(self):
        if frappe.db.get_single_value('Gym Settings', 'link_to_customer'):
            self.create_customer()

    def create_customer(self):
        if not frappe.db.exists('Customer',
                                {'customer_name': self.trainer_name}):
            customer = frappe.new_doc('Customer')
            customer.customer_name = self.trainer_name
            customer.email_id = self.email_id
            customer.mobile_no = self.mobile_number
            customer.customer_type = "Individual"
            customer.customer_group = "Commercial"
            customer.territory = "India"
            customer.save()
            frappe.msgprint('CUstomer Created')


@frappe.whitelist()
def create_user(user_name, email_id):
    if not frappe.db.exists('User', {'name': user_name}):
        user = frappe.get_doc({
            'doctype': 'User',
            'email': email_id,
            'first_name': user_name,
            'send_welcome_email': 1,
            'enabled': 1,
            'role_profile_name': "Gym Trainer",
            'user_type': "System User",
        })
        user.insert(ignore_permissions=True)
        frappe.msgprint('User Created')
        return True


@frappe.whitelist(allow_guest=True)
def test(user_name):
    return user_name
