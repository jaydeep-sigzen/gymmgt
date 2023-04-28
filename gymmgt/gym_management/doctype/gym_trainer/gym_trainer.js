// Copyright (c) 2023, Jaydeep-Sigzen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Trainer', {
	refresh: function (frm) {
		if (frm.doc.trainer_name) {
			check_user(frm)
		}
	},
});

function check_user(frm) {
	frappe.call({
		method: "gymmgt.api.gymmgt.check_user",
		args: {
			'user_name': frm.doc.trainer_name,
			'email_id': frm.doc.email_id
		},
		callback: function (r) {
			if (r.message) {
				frm.add_custom_button('User', () => {
					create_user(frm)
				}, (' Create '))
			}
		}
	})
}

// http://gym10.com:8002/api/method/gymmgt.gym_management.doctype.gym_trainer.gym_trainer.create_user

// Create User 
function create_user(frm) {
	frappe.call({
		method: "gymmgt.gym_management.doctype.gym_trainer.gym_trainer.create_user",
		args: {
			'user_name': frm.doc.trainer_name,
			'email_id': frm.doc.email_id
		},
		callback: function (r) {
			if (r.message) {
				frm.reload_doc()
			}
		}
	})
}
