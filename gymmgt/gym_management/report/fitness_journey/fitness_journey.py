# Copyright (c) 2023, Jaydeep-Sigzen and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_data(filters):
    conditions = "1=1"

    if (filters.get("assign_to_member")):
        conditions += f" AND assign_to_member='{filters.get('assign_to_member')}'"

    my_query = f"""
		SELECT
			measurement_date,
			height_cent,
			weight_kg,
			bmi,
			weight_status,
			arms_cent,
			calves_cent

		FROM 
  			`tabAssign Member Metrics`
		WHERE
			{conditions}
	"""

    data = frappe.db.sql(my_query)
    return data


def get_columns():
    return [
        "Date:Date:200", "Height (Cent):Data:200", "Weight (KG):Data:200",
        "BMI:Data:200", "Weight Status:Link/Weight Status:200",
        "Arms (Cent):Data:200", "Calves (Cent):Data:200"
    ]
