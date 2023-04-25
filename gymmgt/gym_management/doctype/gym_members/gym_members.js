// Copyright (c) 2023, Jaydeep-Sigzen and contributors
// For license information, please see license.txt


frappe.ui.form.on('Gym Members', {

	refresh: function (frm) {
		if (!frm.is_new()) {
			frm.disable_save()
		}
	},
	date_of_birth: function (frm) {

		console.log(calculateAge(frm.doc.date_of_birth))
		frm.set_value({
			age: calculateAge(frm.doc.date_of_birth),
		})
		frm.refresh_field('age');

		frappe.validated = false;
	},
	after_save: function (frm) {
		// frappe.msgprint('Before Save')
		frappe.call({
			method: 'gymmgt.api.gymmgt.create_customer',
			args: {
				'name': frm.doc.name
			},
			callback: function (r) {
				frappe.validated = true;
				frappe.msgprint('Customer Created');
			}
		});

		frappe.validated = false;
	}


});


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
