import json

with open('executed_notebook.ipynb', 'r') as f:
    nb = json.load(f)

# Check key outputs
for cell in nb['cells']:
    if cell['cell_type'] == 'code' and cell.get('outputs'):
        for output in cell['outputs']:
            if output.get('output_type') == 'stream':
                text = ''.join(output.get('text', []))
                if 'VERIFICATION' in text or 'ALL VALUES MATCH' in text or 'VALUATION SUMMARY' in text:
                    print(text[:2000])
                    print('---')
