import frappe
from datetime import datetime, date
from frappe.utils.data import add_days, today

# mid core game
# hiberite casual game'
# WEb gls


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
        'default_amount': amount,
        'end_date': add_days(today(), days)
    }
    return obj


@frappe.whitelist()
def update_gym_membership(duration, activation_date):
    days = frappe.db.get_single_value('Gym Settings', 'default_days')
    amount = frappe.db.get_single_value('Gym Settings', 'registration_fee')
    if duration == 'Quarterly':
        days = days * 4
        amount = amount * 4
    elif duration == 'Yearly':
        days = days * 12
        amount = amount * 12

    obj = {
        'default_days': days,
        'default_amount': amount,
        'end_date': add_days(activation_date, days)
    }
    return obj


@frappe.whitelist()
def update_gym_membership_end_date(activation_date):
    days = frappe.db.get_single_value('Gym Settings', 'default_days')
    obj = {'end_date': add_days(activation_date, days)}
    return obj


@frappe.whitelist()
def get_default_diet_plan_days(from_date):
    days = frappe.db.get_single_value('Gym Settings', 'default_diet_plan_days')
    return add_days(from_date, days)


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
            'module_profile': "Gym Member Module Profile"
        })
        user.insert(ignore_permissions=True)
        frappe.msgprint('User Created')
        return True
    else:
        frappe.msgprint('Customer not exist Error')
        return False


@frappe.whitelist()
def create_sales_invoice(member, member_id, plan_name, amount):
    Item_name = frappe.db.get_value("Workout Plan", plan_name, 'item')
    # intermediate
    items = [{"item_code": Item_name, "qty": 1, "rate": amount}]

    sales_invoice = frappe.get_doc({
        "doctype": "Sales Invoice",
        "customer": member,
        "due_date": frappe.utils.nowdate(),
        "gym_member_id": member_id,
        "items": items
    })
    # frappe.throw('Error')
    sales_invoice.insert()
    sales_invoice.submit()
    return True