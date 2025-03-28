from odoo import models, fields

class ModelOne(models.Model):
	
	_name = "model.one"
	_description = "Model One"
	
	name = fields.Char(string="Name", help='You can add your name here', copy=False)
	age = fields.Integer(string="Age", default=18)
	gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", required=True, copy=False)
	active = fields.Boolean('Active')
	description = fields.Text("Description", default="Test Description")
	date = fields.Date("Date")