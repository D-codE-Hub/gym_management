frappe.pages['my-page-'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Hi',
		single_column: true
	});

	// frappe.require()
	frappe.require('my_page_.bundle.js').then(() => {
		// main.bundle.js is now loaded
	  })
}