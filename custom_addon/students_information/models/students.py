from odoo import models, fields


class Students(models.Model):
    _name = 'students_info'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'students_information'

    name = fields.Char(string='Student Name',
                       tracking=True,
                       help='Students full name')
    f_name = fields.Char(string='Father Name',
                         tracking=True)
    m_name = fields.Char(string='Mother Name',
                         tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              string='Gender',
                              tracking=True,
                              help='Male or female')
    dob = fields.Date(string='Date Of Birth',
                      tracking=True)
    phone = fields.Char(string='Guardian Phone',
                        tracking=True)
    address = fields.Char(string='Address',
                          tracking=True)
    shift = fields.Selection([('morning', 'Morning'), ('day', 'Day')],
                             string='Shift',
                             tracking=True)
    Class = fields.Selection(
        [('three', 'Three'), ('four', 'Four'), ('five', 'Five'), ('six', 'Six'), ('seven', 'Seven'), ('eight', 'Eight'),
         ('nine', 'Nine'), ('ten', 'Ten')],
        string='Class',
        tracking=True)
    section = fields.Char(string='Section',
                          tracking=True)
    roll = fields.Char(string='Roll No',
                       tracking=True,
                       help='Roll number')
    join_date = fields.Date(string='Date Of Admit',
                            default=fields.Date.context_today,
                            tracking=True,
                            help='Students admit date')
    active = fields.Boolean(String="Active",
                            default=True)

    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')],
        string="Priority")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Canceled')],
        string="Status",
        default='draft',
        required=True)

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_in_progress(self):
        for record in self:
            record.state = 'in_progress'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_cancel(self):
        for record in self:
            record.state = 'cancel'