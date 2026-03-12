# -*- coding: utf-8 -*-
{
    "name": "Sale Pricelist Max Discount",
    "version": "19.0.1.0.0",
    "category": "Sales/Sales",
    "summary": "Add max discount on pricelist rules and enforce it on sale order lines",
    "depends": ["sale", "product"],
    "data": [
        "views/product_pricelist_item_views.xml",
        "views/product_pricelist_views.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
