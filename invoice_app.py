from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

DATA_FILE = "invoices.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return []


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


@ app.route('/', methods=['GET', 'POST'])
def index():
    data = load_data()
    if request.method == 'POST':
        invoice = {
            'supplier': request.form.get('supplier'),
            'invoice_date': request.form.get('invoice_date'),
            'invoice_number': request.form.get('invoice_number'),
            'customer_number': request.form.get('customer_number'),
            'items': []
        }
        idx = 0
        while True:
            pos = request.form.get(f'pos_{idx}')
            if pos is None:
                break
            # skip empty rows
            if not any([
                pos,
                request.form.get(f'country_{idx}'),
                request.form.get(f'article_{idx}'),
                request.form.get(f'description_{idx}'),
                request.form.get(f'unit_{idx}'),
                request.form.get(f'quantity_{idx}'),
                request.form.get(f'net_value_{idx}')
            ]):
                idx += 1
                continue
            invoice['items'].append({
                'pos': pos,
                'country': request.form.get(f'country_{idx}'),
                'article': request.form.get(f'article_{idx}'),
                'description': request.form.get(f'description_{idx}'),
                'unit': request.form.get(f'unit_{idx}'),
                'quantity': request.form.get(f'quantity_{idx}'),
                'net_value': request.form.get(f'net_value_{idx}')
            })
            idx += 1
        data.append(invoice)
        save_data(data)
        return redirect('/')
    return render_template('index.html', invoices=data)


if __name__ == '__main__':
    app.run(debug=True)
