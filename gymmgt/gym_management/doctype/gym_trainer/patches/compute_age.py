from __future__ import unicode_literals
import frappe


def execute():
    for trainer in frappe.db.get_all('Gym Trainer', pluck='name'):
        doc = frappe.get_doc('Gym Trainer', trainer)
        print(f'\n\n\n\ Patches- {doc}')
        doc.compute_age()
        doc.save()
