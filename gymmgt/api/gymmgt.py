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
def create_customer(name):

    member = frappe.db.sql(
        f"Select member_name from `tabGym Members` where name='{name}'", as_dict=1)[0]

    # print(f'===> Member {member}')
    # frappe.throw('API Error')

    customer = frappe.get_doc({

        "doctype": "Customer",
        "customer_name": member['member_name'],
        "customer_type": 'Company',
        "territory": 'India',
        "customer_group": 'Individual'
    })
    customer.insert()
    return "Success"
