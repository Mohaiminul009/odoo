from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError


class ComputeField(models.Model):
    _name = 'compute_field'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'compute the fields'

    today = fields.Date(string='Today', default=fields.Date.context_today)
    date_of_birth = fields.Date(string='Date Of Birth')
    age = fields.Integer(string='Age', compute='_compute_age')

    html = fields.Html(String='Comments')

    line_ids = fields.One2many("test_model_line", "model_id")

    description = fields.Char(string='Description')
    is_partner = fields.Char(string='Partner')

    cover = fields.Binary(string='Cover')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = rec.today
            born = rec.date_of_birth
            if born:
                rec.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            else:
                rec.age = 0

    # @api.constrains('date_of_birth')
    # def _check_date_end(self):
    #     for record in self:
    #         print(type(record.date_of_birth))
    #         print(type(record.today))
    #         if record.date_of_birth < record.today:
    #             raise ValidationError("Date of birth can not be set in the future")


class TestModelLine(models.Model):
    _name = "test_model_line"
    _description = "Test Model Line"

    model_id = fields.Many2one("compute_field")
    field_1 = fields.Char()
    field_2 = fields.Char()
    field_3 = fields.Char()