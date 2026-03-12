# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    x_price_unit_readonly = fields.Boolean(
        compute="_compute_x_price_unit_readonly", store=False
    )

    @api.depends_context("uid")
    @api.depends("product_id", "product_template_id")
    def _compute_x_price_unit_readonly(self):
        readonly_group = "unit_price_readonly.groups_view_cost_price"
        user_has_ro_group = self.env.user.has_group(readonly_group)

        for line in self:
            # product flag (works for both variant/template)
            tmpl = line.product_template_id or line.product_id.product_tmpl_id
            allow_override = bool(tmpl and tmpl.x_allow_so_price_edit)

            # readonly only if user is in RO group AND product does NOT allow override
            line.x_price_unit_readonly = bool(user_has_ro_group and not allow_override)
