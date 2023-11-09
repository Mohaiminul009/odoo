from odoo import models, fields, api


class Fees(models.Model):
    _name = 'students_fees'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'students_monthly_fees'
    _rec_name = 'student_name'

    student_name = fields.Many2one('students_info', string='Student Name', tracking=True)
    shift = fields.Selection(related='student_name.shift')
    Class = fields.Selection(
        [('three', 'Three'), ('four', 'Four'), ('five', 'Five'), ('six', 'Six'), ('seven', 'Seven'), ('eight', 'Eight'),
         ('nine', 'Nine'), ('ten', 'Ten')], string='Class', tracking=True)
    section = fields.Char(related='student_name.section')
    roll = fields.Char(related='student_name.roll', readonly=False)
    submit_date = fields.Datetime(string='Submission Date', default=fields.Datetime.now, tracking=True)
    amount = fields.Float(string='Amount', tracking=True)
    deduction = fields.Float(string='Deduction', tracking=True)
    total_amount = fields.Float(string='Total', tracking=True, compute='_compute_total_amount')
    due = fields.Float(string='Due Amount (If any)')
    exam_fee = fields.Float(string='Exam Fees')
    auditorium_fee = fields.Float(string='Auditorium')
    others = fields.Float(string='Others')
    guardians = fields.Many2one('res.users', string='Guardian Name')

    test = fields.Text(string='Test')
    html = fields.Html(String='Comments')

    @api.depends('amount', 'deduction')
    def _compute_total_amount(self):
        for rec in self:
            amount = rec.amount
            deduction = rec.deduction
            if amount and deduction:
                rec.total_amount = amount - deduction
            elif amount:
                rec.total_amount = amount
            else:
                rec.total_amount = 0.00

    @api.onchange('student_name')
    def onchange_student_name(self):
        self.Class = self.student_name.Class

    def action_for_accept(self):
        for record in self:
            record.test = "Accepted"
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Successfully accepted!',
                'type': 'rainbow_man'
            }
        }

    def action_for_cancel(self):
        for record in self:
            record.test = "Canceled"
        return True

class ResStudents(models.Model):
    _inherit = 'students_info'

    fee_ids = fields.One2many('students_fees', 'student_name')