from lxml import etree
import psycopg2
import cgi
import cgitb
import os
cgitb.enable()
form = cgi.FieldStorage()
print("Content-type: text/html")
print()
print()
conn = psycopg2.connect(dbname="tourist", user="postgres", password="12345", host="localhost")
cursor = conn.cursor()

todo = form.getfirst("todo")
table = form.getfirst("table_name")
#print(table)
if todo=="import":
    file = form["xmlFileImport"]
    query = ""
    tree = etree.parse(file.filename)
    tree_str = etree.tostring(tree)
    root = etree.fromstring(tree_str)
    data = []
    for values in root:
        data_val = []
        for tags in values:
            data_val.append(tags.text)
        data.append(data_val)
    print(data)
    if table == "Tourists":
        query = "INSERT INTO Tourists (name, second_name, middle_name, passport, city, phone, zipcode) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    elif table == "Tours":
        query = "INSERT INTO Tours (name, season_id, price, info) VALUES (%s, %s, %s, %s)"
    elif table == "Trips":
        query = "INSERT INTO Trips (tourist_id, tour_id) VALUES (%s, %s)"
    elif table == "Payment":
        query = "INSERT INTO Payment (trip_id, payment_date, amount) VALUES (%s, %s, %s)"
    elif table == "Seasons":
        query = "INSERT INTO Seasons (start_date, end_date, closed) VALUES (%s, %s, %s)"
    cursor.executemany(query, data)
    conn.commit()
elif todo=="export":
    cursor.execute("SELECT * FROM " + table)
    data = cursor.fetchall()
    root = etree.Element(table)
    tags = []
    if table == "Tourists":
        tags = ["id", "name", "second_name", "middle_name", "passport", "city", "phone", "zipcode"]
    elif table == "Tours":
        tags = ["id", "name", "season_id", "price", "info"]
    elif table == "Trips":
        tags = ["id", "tourist_id", "tour_id"]
    elif table == "Payment":
        tags = ["id", "trip_id", "payment_date", "amount"]
    elif table == "Seasons":
        tags = ["id", "start_date", "end_date", "closed"]
    i = 1
    for values in data:
        value_tag = etree.SubElement(root, "value"+str(i))
        j = 0
        for tag in tags:
            column_tag = etree.SubElement(value_tag, tag)
            column_tag.text = str(values[j])
            j+=1
        i+=1
    export = open("export.xml", "w+")
    export.write(str(etree.tostring(root)))
# tree = etree.parse(file.filename)
# tree_str = etree.tostring(tree)
# tree = etree.fromstring(tree_str)
# #
# print(tree[0][0].text)

