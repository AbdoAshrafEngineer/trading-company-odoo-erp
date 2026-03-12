# -*- coding: utf-8 -*-
from odoo import api, models, _
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _get_max_discount_from_rule(self):
        """Return max discount from the applied pricelist item, or None if unlimited/not available."""
        self.ensure_one()
        # Odoo 19 typically stores applied rule in pricelist_item_id
        item = getattr(self, "pricelist_item_id", False)
        if not item:
            return None

        max_d = item.x_max_discount
        # Treat empty/0/negative as unlimited
        if not max_d or max_d <= 0:
            return None
        return max_d

    @api.onchange("discount", "pricelist_item_id")
    def _onchange_discount_cap_by_rule(self):
        for line in self:
            max_d = line._get_max_discount_from_rule()
            if max_d is not None and (line.discount or 0.0) > max_d:
                line.discount = max_d
                return {
                    "warning": {
                        "title": _("Discount limited"),
                        "message": _(
                            "Maximum allowed discount for this pricelist rule is %s%%."
                        )
                        % (max_d,),
                    }
                }

    @api.constrains("discount", "pricelist_item_id")
    def _constrains_discount_cap_by_rule(self):
        for line in self:
            max_d = line._get_max_discount_from_rule()
            if max_d is not None and (line.discount or 0.0) > max_d:
                raise ValidationError(
                    _(
                        "Discount (%s%%) cannot exceed the maximum allowed (%s%%) for the applied pricelist rule."
                    )
                    % (line.discount, max_d)
                )
