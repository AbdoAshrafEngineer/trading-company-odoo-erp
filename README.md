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

**Sales**
- **Own documents**: Salesperson sees and interacts with only their own sales documents
- **All documents**: Sales admin sees and interacts with all sales documents across the team

**Warehouse**
- **Inventory User**: Sees and interacts with their own assigned warehouse only — no visibility into other warehouses
- **Inventory Admin**: Sees and manages all warehouses across the company

> This ensures each warehouse operator works in isolation while management retains full visibility.

---

## Tech Stack

- **Odoo** (ERP platform)
- **Docker / Docker Compose** (local deployment)
- **PostgreSQL** (database)
- **Python** (custom module development)

---

## How to Run Locally

**Step 1 — Add your Odoo Enterprise addons**

Place your Odoo Enterprise addons folder inside `Customization/` and rename it to `enterprise`:

```
Customization/
└── enterprise/       ← your enterprise addons go here
```

> ⚠️ The `enterprise` folder is required. Without it, Docker will fail to start correctly.

**Step 2 — Start the stack**

```bash
git clone git@github.com:AbdoAshrafEngineer/trading-company-odoo-erp.git
cd trading-company-odoo-erp/Customization
docker compose up -d
```

Access Odoo at `http://localhost:9090`

---

## Case Study

For full business context, process walkthroughs, and outcomes — read the case study:
**[https://www.elsaka.com/case-study](https://www.elsaka.com/case-study)**
