# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Technical reports',
    'version': '10.0.1.2.0',
    'description': "Technical reports",
    'category': 'Reports',
    'website': 'https://apuliasoftware.it',
    'depends': ['base', 'project', 'web_digital_sign'],
    'data': [
        'views/notes_view.xml',
        'views/reports_view.xml',
        'views/task_view.xml'
    ],
    'installable': True
}