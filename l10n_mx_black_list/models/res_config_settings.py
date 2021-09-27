# -*- coding: utf-8 -*-
from odoo import api, fields, models, fields, _


class Company(models.TransientModel):
    _inherit = 'res.config.settings'

    blacklist_sale_config = fields.Selection(
        string='Sale',
        selection=[
            ('allow', _('Allow')),
            ('warning', _('Warning')),
            ('deny', _('Deny')),
        ],
        default='warning',
        required=True,
        help='''allow: There is no check.
            deny: If the VAT is on the list, the record cannot be saved.
            warning: If the VAT is on the list, a warning is displayed.''',
        config_parameter='blacklist.sale',
    )
    blacklist_purchase_config = fields.Selection(
        string='Purchase',
        selection=[
            ('allow', _('Allow')),
            ('warning', _('Warning')),
            ('deny', _('Deny')),
        ],
        default='warning',
        required=True,
        help='''allow: There is no check.
            deny: If the VAT is on the list, the record cannot be saved.
            warning: If the VAT is on the list, a warning is displayed.''',
        config_parameter='blacklist.purchase',
    )
    blacklist_invoice_config = fields.Selection(
        string='Invoice',
        selection=[
            ('allow', _('Allow')),
            ('warning', _('Warning')),
            ('deny', _('Deny')),
        ],
        default='warning',
        required=True,
        help='''allow: There is no check.
            deny: If the VAT is on the list, the record cannot be saved.
            warning: If the VAT is on the list, a warning is displayed.''',
        config_parameter='blacklist.invoice',
    )
    blacklist_partner_config = fields.Selection(
        string='Partner',
        selection=[
            ('allow', _('Allow')),
            ('warning', _('Warning')),
            ('deny', _('Deny')),
        ],
        default='warning',
        required=True,
        help='''allow: There is no check.
            deny: If the VAT is on the list, the record cannot be saved.
            warning: If the VAT is on the list, a warning is displayed.''',
        config_parameter='blacklist.partner',
    )
