# Copyright (c) 2023, Jaydeep-Sigzen and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_data(filters):
    conditions = "1=1"

    if (filters.get("trainer_name")):
        conditions += f" AND trainer='{filters.get('trainer_name')}'"

    my_query = f"""
		SELECT
			trainer,
			rating
		FROM 
  			`tabTrainer Rating`
		WHERE
			{conditions}
	"""

    data = frappe.db.sql(my_query)
    print(f" \n\n\n==>>data:{data}\n\n\n")
    return data

    # Skip Below Code
    # frappe.throw('Error Report Rating')
    return calculate_average_rating(data)


def get_columns():
    return [
        "Trainer Name:Link/Gym Trainer:200",
        "Rating:Rating:200",
    ]


def calculate_average_rating(person_ratings):

    if isinstance(person_ratings, tuple):
        num_persons = len(person_ratings)
        if num_persons == 0:
            return 0.0
        total_rating = sum([r for _, r in person_ratings])
    else:
        raise ValueError("person_ratings should be a dict or tuple object.")

    average_rating = total_rating / num_persons
    return average_rating
