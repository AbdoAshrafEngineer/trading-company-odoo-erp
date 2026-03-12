# trading-company-odoo-erp

A techno-functional Odoo ERP implementation for a trading company — covering business process design, custom module development, and full system configuration.

👉 **[View the full case study](https://www.elsaka.com/case-study)**

---

## What is this?

This repo documents the full lifecycle of deploying Odoo ERP for a trading business — not just the code, but the *thinking* behind it: how the business works, how Odoo was configured to match it, and what was customized to fit.

---

## Structure

```
├── Business Process Map.bpmn     # How the business actually operates
├── Customization/                # Docker setup + 3 custom Odoo modules
└── Implementation/               # Master data + access/record rules
```

---

## Customization (Custom Modules)

Three modules were built to meet business-specific needs:

| Module | What it does |
|---|---|
| `hide_cost_price` | Hides product cost from unauthorized users |
| `sale_pricelist_max_discount` | Caps the maximum discount on pricelist items |
| `unit_price_readonly` | Locks unit price on sales orders for non-admin users |

Docker Compose is included to run the full Odoo stack locally.

---

## Implementation

### Master Data (loaded in order)

| # | File | Covers |
|---|------|--------|
| 0 | Tax Group | Tax configuration |
| 1 | Chart of Accounts | Accounting structure |
| 2 | Journal Entries | Opening entries |
| 3 | Customers | Contact records |
| 4 | Vendors | Supplier records |
| 5 | Customer Invoices | AR opening balances |
| 6 | Vendor Bills | AP opening balances |
| 7 | Product Categories | Product classification |
| 8 | Products | Full product catalog |
| 9 | Lot & Serial Numbers | Inventory traceability |
| 10 | Physical Inventory | Opening stock counts |

### Record Rules (Access Control)

- **Sales**: Own documents vs. all documents
- **Warehouse**: Inventory admin vs. inventory user

---

## Tech Stack

- **Odoo** (ERP platform)
- **Docker / Docker Compose** (local deployment)
- **PostgreSQL** (database)
- **Python** (custom module development)

---

## Case Study

For full business context, process walkthroughs, and outcomes — read the case study:
**[https://www.elsaka.com/case-study](https://www.elsaka.com/case-study)**
