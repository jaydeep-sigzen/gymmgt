// Copyright (c) 2023, Jaydeep-Sigzen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Membership', {
	refresh: function (frm) {

	},
	workout_plan: function (frm) {
		console.log(frm.doc.workout_plan);
		frappe.call({
			method: 'gymmgt.api.gymmgt.get_default_plan',
			args: {
				'name': frm.doc.name
			},
			callback: function (r) {
				frappe.validated = true;
				// frappe.msgprint('Customer Created' + r.message.default_days);
				frm.set_value({
					"valid_days": r.message.default_days,
					"amount": r.message.default_amount
				})
			}
		});
		frappe.validated = false;
	}
});
