// Copyright (c) 2023, Jaydeep-Sigzen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Member', {

	setup(frm) {
		// write setup code
		console.log("Form=", frm)
		console.log(new Date());

		if (frm.is_new()) {

			frm.add_custom_button('Click me', () => console.log('Clicked custom button'))

			frm.set_value({
				// member_name: "TEST",
				// joining_date: "12-04-2023"
			})
			frm.refresh_field('member_name');

		}
	}


});
