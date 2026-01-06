def get_data():
	return {
		"fieldname": "shift",
		"non_standard_fieldnames": {"Employee": "default_shift", "Shift Assignment": "shift_type"},
		"transactions": [{"items": ["Employee", "Attendance", "Employee Checkin", "Shift Assignment"]}],
	}
