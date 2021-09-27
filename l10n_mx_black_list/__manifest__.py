# -*- coding: utf-8 -*-
{
    'name': 'L10N MX Black List',
    'version': '13.0.1.6.0',
    'author': 'HomebrewSoft',
    'website': 'https://homebrewsoft.dev/',
    'license': 'LGPL-3',
    'depends': [
        'account',
        'sale',
        'purchase',
    ],
    'data': [
        # security
        'security/ir.model.access.csv',
        # data
        'data/ir_cron.xml',
        # reports
        # views
        'views/l10n_mx_black_list.xml',
        'views/res_config_settings.xml',
    ],
    'images': [
        'static/description/images/menu_blacklist_screenshot.png',
        'static/description/images/action_black_list.png'
        'static/description/images/function_constraint_black_list.png',
    ]
}
