import frappe


def execute():
	employee_advance = frappe.get_all("Employee Advance", pluck="name", filters={"status": "Paid"})
	for advance in employee_advance:
		frappe.get_doc("Employee Advance", advance).set_status(True)
