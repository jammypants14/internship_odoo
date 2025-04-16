from odoo import models, fields, api

class ModelOne(models.Model):
	
	_name = "model.one"
	_description = "Model One"
	
	seq = fields.Char(string="Sequence")
	name = fields.Char(string="Name", help='You can add your name here', copy=False)
	age = fields.Integer(string="Age", default=18)
	gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", required=True, copy=False)
	active = fields.Boolean('Active')
	description = fields.Text("Description", default="Test Description")
	date = fields.Date("Date")
	partner_ids = fields.Many2many('res.partner', string="Partner")
	product_ids = fields.Many2many('product.template', 'model_one_prduct_rel', 'model_one_id', 'product_id',  string="Products")
	model_one_line_ids = fields.One2many('model.one.lines', 'model_one_id',  string="Products")
	sale_id = fields.Many2one('sale.order', string="Sales")
	
	def helloworld(self):
		print("hello world")
	
	def show_wizard(self):
		return {
            'type': 'ir.actions.act_window',
            'name': 'My Sample Wizard',
            'res_model': 'sample.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('sample.view_form_sample_wizard').id,
            'target': 'new',
            'context' : {'default_name': 'Jishnu'}
        }
	    
	@api.model
	def create(self, vals):
		vals['seq'] = self.env['ir.sequence'].next_by_code('sequence.model.one')
		res = super(ModelOne, self).create(vals)
		return res
	
	
class ModelOneLines(models.Model):
	
	_name = "model.one.lines"
	_description = "Model One Lines"
	
	name = fields.Char(string="Name", help='You can add your name here')
	price = fields.Float(string="Price")
	product_id = fields.Many2one('product.template', string="Product")
	model_one_id = fields.Many2one('model.one', string="Model One", domain="['|', ('gender', '=', 'female'),('age', '>', 18)]")