import frappe
from datetime import datetime, date


@frappe.whitelist()
def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
    today = date.today()
    age = today.year - birthdate.year - \
        ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

@frappe.whitelist()
def check_user(user_name, email_id):
    if not frappe.db.exists('User', {
            'full_name': user_name,
            'name': email_id
    }):
        return True

@frappe.whitelist()
def get_default_plan():
    days = frappe.db.get_single_value('Gym Settings', 'default_days')
    amount = frappe.db.get_single_value('Gym Settings', 'registration_fee')
    obj = {
        'default_days': days,
        'default_amount': amount
    }
    return obj

@frappe.whitelist()
def create_user(customer):
    if frappe.db.exists('Customer', {'name': customer}):
        customer_doc = frappe.get_doc('Customer', {'name': customer})
        user = frappe.get_doc({
            'doctype': 'User',
            'email': customer_doc.email_id,
            'first_name': customer_doc.customer_name,
            'enabled': 1,
            'role_profile_name': "Gym Member",
            'user_type': "Website User",
        })
        user.insert(ignore_permissions=True)
        frappe.msgprint('User Created')
        return True
    else:
        frappe.msgprint('Customer not exist Error')
        return False
        
