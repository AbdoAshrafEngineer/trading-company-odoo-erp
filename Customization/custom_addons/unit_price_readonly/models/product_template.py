# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_allow_so_price_edit = fields.Boolean(
        string="Allow Sale Unit Price Edit",
        help="If enabled, users can edit the unit price on Sales Order Lines for this product, "
        "even if they belong to the 'Unit Price Readonly' group.",
    )
