import psycopg2
import cgi
conn = psycopg2.connect(dbname="tourist", user="postgres", password="12345", host="localhost")
cursor = conn.cursor()
form = cgi.FieldStorage()
print("Content-type: text/html")
print()
print('''<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="0;URL=http://localhost:8000/cgi-bin/input.py" />
        <meta http-equiv='X-UA-Compatible' content='IE=edge'/>
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
        <title>Input Ex5</title>
        <link rel="stylesheet" href="../css/bootstrap.css">
        <link rel="stylesheet" href="../css/style.css">
    </head>''')

id = form.getfirst("id", "None")
table_name = form.getfirst("table_name", "None")
if table_name=="Tourists":
    if id=="0":
        values = (
        form.getfirst("name", "None"), form.getfirst("second_name", "None"), form.getfirst("middle_name", "None"),
        form.getfirst("passport", "None"), form.getfirst("city", "None"), form.getfirst("phone", "None"),
        form.getfirst("zipcode", "None"))
        cursor.execute("INSERT INTO Tourists (name, second_name, middle_name, passport, city, phone, zipcode) VALUES (%s, %s, %s, %s, %s, %s, %s)", values)
        conn.commit()
    else:
        values = (
            form.getfirst("name", "None"), form.getfirst("second_name", "None"), form.getfirst("middle_name", "None"),
            form.getfirst("passport", "None"), form.getfirst("city", "None"), form.getfirst("phone", "None"),
            form.getfirst("zipcode", "None"), int(id))
        cursor.execute(
            "UPDATE Tourists SET name=%s, second_name=%s, middle_name=%s, passport=%s, city=%s, phone=%s, zipcode=%s WHERE id=%s",values)
        conn.commit()
elif form.getfirst("table_name", "None")=="Tours":
    if id=="0":
        values = (
        form.getfirst("name", "None"), int(form.getfirst("season_id", "None")), float(form.getfirst("price", "None")),
        form.getfirst("info", "None"))
        cursor.execute("INSERT INTO Tours (name, season_id, price, info) VALUES (%s, %s, %s, %s)", values)
        conn.commit()
    else:
        values = (
            form.getfirst("name", "None"), int(form.getfirst("season_id", "None")), float(form.getfirst("price", "None")),
            form.getfirst("info", "None"), int(id))
        cursor.execute(
            "UPDATE Tours SET name=%s, season_id=%s, price=%s, info=%s WHERE id=%s", values)
        conn.commit()
elif form.getfirst("table_name", "None") == "Trips":
    if id=="0":
        values = (
        int(form.getfirst("tourist_id", "None")), int(form.getfirst("tour_id", "None")))
        cursor.execute("INSERT INTO Trips (tourist_id, tour_id) VALUES (%s, %s)", values)
        conn.commit()
    else:
        values = (
            int(form.getfirst("tourist_id", "None")), int(form.getfirst("tour_id", "None")), int(id))
        cursor.execute(
            "UPDATE Trips SET tourist_id=%s, tour_id=%s WHERE id=%s",values)
        conn.commit()
elif form.getfirst("table_name", "None") == "Payment":
    if id=="0":
        values = (
        int(form.getfirst("trip_id", "None")), form.getfirst("payment_date", "None"), float(form.getfirst("amount", "None")))
        cursor.execute("INSERT INTO Payment (trip_id, payment_date, amount) VALUES (%s, %s, %s)", values)
        conn.commit()
    else:
        values = (
            int(form.getfirst("trip_id", "None")), form.getfirst("payment_date", "None"), float(form.getfirst("amount", "None")), int(id))
        cursor.execute(
            "UPDATE Payment SET trip_id=%s, payment_date=%s, amounte=%s WHERE id=%s",values)
        conn.commit()
elif form.getfirst("table_name", "None") == "Seasons":
    if id=="0":
        values = (
        form.getfirst("start_date", "None"), form.getfirst("end_date", "None"), bool(form.getfirst("closed", "None")))
        print(values)
        cursor.execute("INSERT INTO Seasons (start_date, end_date, closed) VALUES (%s, %s, %s)", values)
        conn.commit()
    else:
        values = (
            form.getfirst("start_date", "None"), form.getfirst("end_date", "None"), bool(form.getfirst("closed", "None")), int(id))
        print(values)
        cursor.execute(
            "UPDATE Seasons SET start_date=%s, end_date=%s, closed=%s WHERE id=%s",values)
        conn.commit()
print('''</html>''')