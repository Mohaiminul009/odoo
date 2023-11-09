# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Student Information',
    'version' : '1.0',
    'summary': 'Student List And Information',
    'sequence': -100,
    'description': """

    """,
    'category': '',
    'author': 'MD. MOHAIMINUL',
    'website': 'https://www.odoo.com',
    'images' : [],
    'depends' : ['mail', 'contacts'],
    'data': [
        'security\ir.model.access.csv',
        'views\menu.xml',
        'views\students.xml',
        'views\inactive_students.xml',
        'views/fees_chart.xml',
        'views/compute_field.xml',
        'views/templates.xml',
        'reports/student_fees_template.xml',
        'reports/student_fees_report.xml',
    ],
    'demo': [

    ],
    'installable': True,
    # 'assets': {
    #         'web.assets_backend': [
    #             'static/src/js/component.js',
    #         ],
    #     },
    'application': True,
    'license': 'LGPL-3',
}
