// Copyright (c) 2023, Jaydeep-Sigzen and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Top Trainers Report"] = {
	"filters": [
		{
			"fieldname": "trainer_name",
			"label": "Gym Trainer",
			"fieldtype": "Link",
			"options": "Gym Trainer",
			"width": 200,
			"reqd": 0
		}

	]
};
