// Copyright (c) 2023, Jaydeep-Sigzen and contributors
// For license information, please see license.txt


frappe.ui.form.on('Gym Members', {

	refresh: function (frm) {
		// if (!frm.is_new()) {
		// 	// frm.disable_save()
		// }
		if (frm.doc.member_name) {
			check_user(frm)
		}

	},
	date_of_birth: function (frm) {

		console.log(calculateAge(frm.doc.date_of_birth))
		frm.set_value({
			age: calculateAge(frm.doc.date_of_birth),
		})
		frm.refresh_field('age');
	}
});


function check_user(frm) {
	frappe.call({
		method: "gymmgt.api.gymmgt.check_user",
		args: {
			'user_name': frm.doc.member_name,
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

// Create User 
function create_user(frm) {
	frappe.call({
		method: "gymmgt.api.gymmgt.create_user",
		args: {
			'customer': frm.doc.member_name
		},
		callback: function (r) {
			frappe.validated = true;
			if (r.message) {
				frm.reload_doc()
			}
		}
	})
}


// This function calculates the age of a person based on their birth date
function calculateAge(dateString) {
	const today = new Date();
	const birthDate = new Date(dateString);
	let ageInDays = Math.floor((today - birthDate) / (1000 * 60 * 60 * 24));
	const ageInYears = Math.floor(ageInDays / 365);
	ageInDays -= ageInYears * 365;
	const ageInMonths = Math.floor(ageInDays / 30);
	ageInDays -= ageInMonths * 30;

	return `${ageInYears} years, ${ageInMonths} months, and ${ageInDays} days old`;
}
