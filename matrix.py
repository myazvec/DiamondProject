#!/usr/bin/python
import cgi
import cgitb

cgitb.enable()

print("Content-Type: text/html\n\n")

form = cgi.FieldStorage()
columns = int(form.getvalue('columns'))
rows = int(form.getvalue('rows'))

print("""
<h1> Incidence Matrix </h1>
<form action="cluster.py" method="post">
<input type="hidden" name="columns" value=""" '"' + str(columns) +  '"' """>
<input type="hidden" name="rows" value=""" '"' + str(rows) +  '"' """>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: center;">
      <th></th>
""")

for colCount in range(1, columns + 1):
    print('<th>'+ str(colCount) + '</th>')

print("""
    </tr>
  </thead>
  <tbody>
 """)

for rowCount in range(1, rows + 1):
    print("""
    <tr>
      <th>""" + str(rowCount) + """</th>
    """)
    for inputCount in range(1, columns + 1):
        index = str(rowCount) + str(inputCount)
        print("""<td><input type="text" name=""" '"' + index +  '"' """ size= "1" value= 0></td>""")

    print("""
    </tr>
    """)

print(""" </tbody>
</table>
<br>
<input type="submit" value="Submit">
</form>
""")
