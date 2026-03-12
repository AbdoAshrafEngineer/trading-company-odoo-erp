# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductPricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    x_max_discount = fields.Float(
        string="Max Discount (%)",
        help=(
            "Maximum discount allowed on Sale Order Lines when this pricelist rule applies. "
            "Leave empty or 0 for no limit."
        ),
    )
