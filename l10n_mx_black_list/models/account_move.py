# -*- coding: utf-8 -*-
from odoo import _, api, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.onchange('partner_id')
    def _warning_partner_not_in_blacklist(self):
        if self.env['ir.config_parameter'].get_param('blacklist.invoice') == 'warning':
            return self.partner_id and self.partner_id.warning_vat_not_in_blacklist()

    @api.constrains('partner_id')
    def _verify_partner_not_in_blacklist(self):
        for record in self:
            if self.env['ir.config_parameter'].get_param('blacklist.invoice') == 'deny':
                self.partner_id and self.partner_id.verify_vat_not_in_blacklist()
