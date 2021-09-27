from odoo import api, models, _
from odoo.exceptions import ValidationError


class res_partner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('vat')
    def _verify_vat_not_in_blacklist(self):
        for record in self:
            if self.env['ir.config_parameter'].get_param('blacklist.partner') == 'deny':
                record.verify_vat_not_in_blacklist()

    @api.onchange('vat')
    def _warning_vat_not_in_blacklist(self):
        if self.env['ir.config_parameter'].get_param('blacklist.partner') == 'warning':
            return self.warning_vat_not_in_blacklist()

    def verify_vat_not_in_blacklist(self):
        if self.env['l10n.mx.black_list'].search([('name', '=', self.vat)], limit=1):
            raise ValidationError(_('The RFC of {} is on the black list').format(self.name))

    def warning_vat_not_in_blacklist(self):
        if self.env['l10n.mx.black_list'].search([('name', '=', self.vat)], limit=1):
            return {
                'warning': {
                    'title': _('RFC in the black list'),
                    'message': _('The RFC of {} is on the black list').format(self.name),
                },
            }
