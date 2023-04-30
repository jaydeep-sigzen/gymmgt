# Copyright (c) 2023, Jaydeep-Sigzen and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_data(filters):
    conditions = "1=1"
    data = []

    if (filters.get("trainer_name")):
        conditions += f" AND trainer='{filters.get('trainer_name')}'"
        my_query = f"""
		SELECT
			trainer,
			AVG(rating) AS avg_rating,
			COUNT(*) AS member
		FROM 
  			`tabTrainer Rating`
		WHERE
			{conditions}	
		"""
        data = frappe.db.sql(my_query)
    else:
        all_trainers = frappe.db.get_list('Gym Trainer',
                                          fields=['trainer_name'])
        for trainer in all_trainers:
            print(f"\n\n\n trainer===> {trainer.get('trainer_name')}\n\n\n")
            my_query1 = f"""
			SELECT
				trainer,
				AVG(rating) AS avg_rating,
				COUNT(*) AS member
			FROM 
				`tabTrainer Rating`
			GROUP BY Trainer	
			"""
            data = frappe.db.sql(my_query1)
    return data


def get_columns():
    return [
        "Trainer Name:Link/Gym Trainer:200", "Avg Rating:Rating:200",
        "Members Rating Count:Data:200"
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
