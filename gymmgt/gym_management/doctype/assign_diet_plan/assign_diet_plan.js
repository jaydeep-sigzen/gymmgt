// Copyright (c) 2023, Jaydeep-Sigzen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Assign Diet Plan', {
	// refresh: function(frm) {

	// }
	start_date: function (frm) {
		console.log(frm.doc.start_date);
		frappe.call({
			method: 'gymmgt.api.gymmgt.get_default_diet_plan_days',
			args: {
				"from_date": frm.doc.start_date
			},
			callback: function (r) {

				console.log(r.message);
				frm.set_value({
					"end_date": r.message
				})
			}
		});
	}
});
