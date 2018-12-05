{
	"name": "vitSMS - Promedia Gateway Implementation",
	"version": "1.2",
	"depends": [
		"vit_sms",
	],
	"author": "Akhmad D. Sembiring [vitraining.com]",
	"category": "Extra Tools",
	'website': 'http://www.vitraining.com',
	'summary': 'Promedia gateway implementation',
	"description": """
Promedia gateway implementation for vit_sms addon. Inheriting methods:

* send_gateway()

For more information of getting username and password and top up for sending credits 
please click contact us for the most competitive price per SMS.

Email: info@vitraining.com

    

Find our other interesting modules that can make your life easier:
https://www.odoo.com/apps/modules/browse?search=vitraining

""",
	"data": [
		"data/config.xml",
		"view/config.xml"
	],
	"installable": True,
	"auto_install": False,
    "application": True,
}