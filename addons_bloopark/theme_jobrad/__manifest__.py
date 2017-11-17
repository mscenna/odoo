# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'JobRad Theme',
    'description': 'JobRad theme to showcase the company\'s main features.',
    'category': 'Theme/Hidden',
    'sequence': 1000,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'views/theme_jobrad_templates.xml',
    ],
    'images': [
        'static/description/cover.png',
        'static/description/theme_default_screenshot.jpg',
    ],
    'application': False,
}
