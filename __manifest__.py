# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Technical reports',
    'version': '10.0.1.2.0',
    'description': "Technical reports",
    'category': 'Reports',
    'author': 'Apulia Software s.r.l.',
    'website': 'http://www.apuliasoftware.it',
    'depends': ['base', 'account','project', 'report'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/technical_report_make_invoice_view.xml',
        'wizard/create_report_from_activity_view.xml',
        'views/reports_view.xml',
        'views/notes_view.xml',
        'views/task_view.xml',
        'reports/technical_reports_qweb.xml',
        'reports/external_reports_qweb.xml',
        'reports/report.xml',
        'data/ir_sequence_data.xml',
        'views/partner_view.xml',
        'views/project_view.xml',
        'views/res_config_view.xml',

    ],
    'installable': True
}
