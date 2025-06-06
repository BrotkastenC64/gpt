# gpt
Sandbox for testing codex

## Invoice Web GUI

This repository now includes a simple Flask application for manually capturing invoice data. To start the server locally:

```bash
pip install -r requirements.txt
python invoice_app.py
```

The application will be available at `http://localhost:5000` and allows you to enter invoice metadata and multiple line items via a simple form. The metadata fields are:

- **Lieferant** (supplier)
- **Rechnungsdatum** (invoice date)
- **Rechnungsnummer** (invoice number)
- **Kundennummer** (customer number)

Each invoice line item collects:

- Position
- Länderkode (country of origin, e.g. `DE`)
- Interne Artikelnummer
- Produktbezeichnung
- Einheit
- Menge
- Warenwert Netto

Submitted invoices are stored in `invoices.json` in the project directory.
