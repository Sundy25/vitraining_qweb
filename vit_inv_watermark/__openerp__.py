{
	"name": "Add Watermark Image on Invoice",
	"version": "1.0", 
	"depends": [
		"base",
		"account"
	], 
	"author": "Akhmad D. Sembiring [vitraining.com]",
	"website": "www.vitraining.com",
	"category": "Accounting",
	"description": """\
Features
======================================================================

* Add Watermark on Invoice depending it's state: Open, Draft, Paid
* Addons ini adalah bahan praktek pada traning "Odoo QWeb Programming" yang diselenggarakan di vitraining.com dan E-Book "Panduang Lengkap Pemrograman QWeb Odoo v10"
* Klik http://shop.vitraining.com untuk info lebih lanjut

""",
	"data": [
		"report/invoice.xml",
	],
	"installable": True,
	"application": True,
	"auto_install": False,
}