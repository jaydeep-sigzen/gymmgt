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
				frm.set_value({
					"valid_days": r.message.default_days,
					"amount": r.message.default_amount,
					"end_date": r.message.end_date
				}).then(() => {
					// do something after value is set
				})
			}
		});
	},
	activation_date: function (frm) {
		frappe.call({
			method: 'gymmgt.api.gymmgt.update_gym_membership',
			args: {
				'duration': frm.doc.plan_duration,
				'activation_date': frm.doc.activation_date
			},
			callback: function (r) {
				frappe.validated = true;
				frm.set_value({
					"end_date": r.message.end_date
				})

			}
		});
	},
	plan_duration: function (frm) {
		frappe.call({
			method: 'gymmgt.api.gymmgt.update_gym_membership',
			args: {
				'duration': frm.doc.plan_duration,
				'activation_date': frm.doc.activation_date
			},
			callback: function (r) {
				frappe.validated = true;
				frm.set_value({
					"valid_days": r.message.default_days,
					"amount": r.message.default_amount,
					"end_date": r.message.end_date
				})

			}
		});
	},
	before_submit: function (frm) {
		frappe.validated = false;
		console.log(frm.doc.name);
		frappe.call({
			method: 'gymmgt.api.gymmgt.create_sales_invoice',
			args: {
				'member': frm.doc.member,
				'member_id': frm.doc.name,
				'plan_name': frm.doc.workout_plan,
				'amount': frm.doc.amount
			},
			callback: function (r) {
				frappe.validated = true;
			}
		});
		frappe.validated = false;
	}


});
