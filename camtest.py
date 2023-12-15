import camelot.io as camelot
pdf_path = "/app/sauvieduckcounts.pdf"

tables = camelot.read_pdf('/app/sauvieduckcounts.pdf', pages='2')
print(tables)
tables[0].df
tables[0].to_html('foo.html')
tables[0].to_csv('foo.csv')
