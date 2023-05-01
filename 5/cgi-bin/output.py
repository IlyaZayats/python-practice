import psycopg2
conn = psycopg2.connect(dbname="tourist", user="postgres", password="12345", host="localhost")
cursor = conn.cursor()

def print_table(table, columns):
    print('''<div class="bg-primary text-light text-center h3 py-2 mb-0">'''+table+'''</div>''')
    print('''<table class="table table-dark table-hover mb-0">
            <thead>
                <tr>''')
    for value in columns:
        print('''<th class="col">''' + str(value) + '''</th>''')
    print('''</tr>
        </thead>
        <tbody>''')
    cursor.execute("SELECT * FROM " + table)
    data = cursor.fetchall()
    for row in data:
        print("<tr>")
        for value in row:
            print('''<th class="col">''' + str(value) + '''</th>''')
        print("</tr>")
    print('''</tbody>
               </table>''')
    print('''<div class="container-fluid"><div class="row d-flex bg-dark"><div class="col-6"><form id="xmlExport'''+table+'''" class="px-2 mt-2" action="/cgi-bin/lmxl_magic.py" method="POST" enctype="multipart/form-data" accept-charset="UTF-8">
    <input type="text" name="table_name" value="'''+table+'''" hidden="true">
    <input type="text" name="todo" value="export" hidden="true">
    <div class="col mt-3 pb-3 w-100">
    <input class="btn btn-danger btn-lg w-100" type="submit" id="xmlExportButton'''+table+'''" value="Export">
    </div>
    </div>
    </form>
    <div class="col-6">
    <form id="xmlImport'''+table+'''" class="px-2 mt-2" action="/cgi-bin/lmxl_magic.py" method="post" enctype="multipart/form-data">
    <input type="text" name="table_name" value="'''+table+'''" hidden="true">
    <input type="text" name="todo" value="import" hidden="true">
    <div class="d-flex row mt-3 pb-3 w-100">
    <input class="col-6 form-control btn-lg w-100" type="file" name="xmlFileImport" accept="application/xml, text/xml">
    <input class="col-6 btn btn-danger btn-lg w-100" type="submit" id="xmlImportButton'''+table+'''" value="Import">
    </div>
    </form></div></div></div>''')


print("Content-type: text/html")
print()

print('''<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv='X-UA-Compatible' content='IE=edge'/>
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
        <title>Output Ex5</title>
        <link rel="stylesheet" href="../css/bootstrap.css">
        <link rel="stylesheet" href="../css/style.css">
    </head>
    <body>''')

print_table("Tourists", ["id", "name", "second_name", "middle_name", "passport", "city", "phone", "zipcode"])
print_table("Trips", ["id", "tourist_id", "tour_id"])
print_table("Payment", ["id", "trip_id", "payment_date", "amount"])
print_table("Seasons", ["id", "start_date", "end_date", "closed"])
print_table("Tours", ["id", "name", "season_id", "price", "info"])
print('''</body>
      </html>''')
