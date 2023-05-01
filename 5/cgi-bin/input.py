print("Content-type: text/html")
print()

def print_form(table, inputs):
    print('''<div class="text-light h3 bg-primary py-2 text-center">Form '''+table+'''</div>''')
    print('''
                <form id="'''+table+'''Form" class="px-2 mt-2" action="/cgi-bin/handler.py" method="POST" enctype="multipart/form-data" accept-charset="UTF-8">
                    <div class="form-row text-light">''')
    print('''<input type="text" name="table_name" value="'''+table.title()+'''" hidden="true">''')
    for value in inputs:
        print('''<div class="col pt-1">
                            <div class="h5">
                                '''+value.title()+''':
                            </div>
                            <label class="w-75 mx-auto">
                                <input class="form-control form-control-md info" type="text" name="'''+value+'''"autocomplete="off" value="">
                            </label><br/>
                        </div>''')
    print('''<div class="col mt-3 pb-3 w-100">
                                <input class="btn btn-danger btn-lg w-100" type="submit" id="submitButton''' + table.title() + '''" value="Submit">
                        </div>''')
    print('''</div>
                </form>''')


print('''<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv='X-UA-Compatible' content='IE=edge'/>
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
        <title>Input Ex5</title>
        <link rel="stylesheet" href="../css/bootstrap.css">
        <link rel="stylesheet" href="../css/style.css">
    </head>
    <body>''')

print('''
<body>
    <div class="container-fluid">
        <div class="row d-flex">
            <div class="bg-dark px-0">''')
print_form("tourists", ["id", "name", "second_name", "middle_name", "passport", "city", "phone", "zipcode"])
print_form("trips", ["id", "tourist_id", "tour_id"])
print_form("payment", ["id", "trip_id", "payment_date", "amount"])
print_form("seasons", ["id", "start_date", "end_date", "closed"])
print_form("tours", ["id", "name", "season_id", "price", "info"])
print('''    </div>
        </div>
    </div>

<script src="../js/bootstrap.js"></script>

''')

print('''</body>
      </html>''')