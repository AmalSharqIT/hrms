from frappe.model.document import Document


class PayrollSettingsSalaryComponent(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		currency: DF.Link
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		salary_component: DF.Link
		type: DF.Literal[
			"Incentive",
			"Loan Installment",
			"Penalty",
			"Reward",
			"Rounding",
			"Withholding",
			"Transportation Allowance",
		]
	# end: auto-generated types

	pass
