// Copyright (c) 2023, Jaydeep-Sigzen and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Fitness Journey"] = {
	"filters": [
		{
			"fieldname": "assign_to_member",
			"label": "Gym Member",
			"fieldtype": "Link",
			"options": "Gym Members",
			"width": 200,
			"reqd": 0
		}
	]
};
