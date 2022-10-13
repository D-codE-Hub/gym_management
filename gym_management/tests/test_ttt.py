# Copyright (c) 2022, D-codE and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

def create_gym_member():
	if frappe.flags.test_gym_member_created:
		return
	frappe.set_user("Administrator")
	doc = frappe.get_doc({
        "doctype": "Gym Member",
        "first_name":"_Test 1",
    }).insert()

	doc = frappe.get_doc({
        "doctype": "Gym Member",
        "first_name":"_Test 2",
        
    }).insert()

	frappe.flags.gym_member_created = True

class TestGymMember(FrappeTestCase):
	
	def setUp(self):
		create_gym_member()

	def tearDown(self):
		frappe.set_user("Administrator")

	def test_allowed_public(self):
		frappe.set_user("test1@example.com")
		doc = frappe.get_doc("Gym Member", frappe.db.get_value("Gym Member",
            {"first_name":"_Test 1"}))

		self.assertEqual(doc.first_name, "_Test 1")