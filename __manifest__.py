# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Technical reports',
    'version': '12.0.1.0.0',
    'description': "Technical Reports",
    'category': 'Reports',
    'author': 'Apulia Software s.r.l.',
    'website': 'http://www.apuliasoftware.it',
    'depends': [
                'base',
                'web',
                'base_geolocalize',
                'account',
                'project',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/technical_report_make_invoice_view.xml',
        'wizard/create_report_from_activity_view.xml',
        'views/technical_report_views.xml',
        'views/notes_view.xml',
        'views/task_view.xml',
        'reports/report.xml',
        'reports/technical_reports_qweb.xml',
        'reports/external_reports_qweb.xml',
        'data/ir_sequence_data.xml',
        'views/partner_view.xml',
        'views/project_view.xml',
        'views/res_config_view.xml',
        'views/res_company_view.xml'
    ],
    'installable': True
}
