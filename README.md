# gpt
Sandbox for testing codex

## Invoice Web GUI

This repository now includes a simple Flask application for manually capturing invoice data. To start the server locally:

```bash
pip install -r requirements.txt
python invoice_app.py
```

The application will be available at `http://localhost:5000` and allows you to enter invoice metadata and multiple line items via a web form. Submitted invoices are stored in `invoices.json` in the project directory.
