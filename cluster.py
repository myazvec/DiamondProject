#!/usr/bin/python
import cgi
import cgitb
import pandas as pd

cgitb.enable()
print("Content-Type: text/html\n\n")

#get form data
form = cgi.FieldStorage()
columns = int(form.getvalue('columns'))
rows = int(form.getvalue('rows'))

formData = {}
store = []
for col in range(1, columns+1):
    for row in range(1, rows+1):
        index = str(row) + str(col)
        store.append(int(form.getvalue(index)))
    formData[col] = store
    store = []

#create dataframe index
index = []
for i in range(1, rows+1):
    index.append(i)

#create dataframe
matrix = pd.DataFrame(formData, index= index)
print("<h2> Original Matrix </h2>")
print(matrix.to_html(col_space = 30))

cluster1Cols = []
cluster1Rows = []

#parses 1st row for data, returns colums where data is present
for col in range(0, columns):
    value = matrix.iloc[0,col]
    if(value > 0):
        cluster1Cols.append(col)

flag = 0
colFlag = 0
rowFlag = 0

while flag < 3:
    #parse rows
    for col in range(0, len(cluster1Cols)):
        for row in range(0, rows):
            value = matrix.iloc[row, cluster1Cols[col]]
            if value > 0 and row not in cluster1Rows:
                cluster1Rows.append(row)

    #parse columns
    for col in range(0, columns):
        for row in range(1, len(cluster1Rows)):
            value = matrix.iloc[cluster1Rows[row], col]
            if value > 0 and col not in cluster1Cols:
                cluster1Cols.append(col)

    if(len(cluster1Cols) == colFlag or len(cluster1Rows) == rowFlag):
        flag = flag + 1

    colFlag = len(cluster1Cols)
    rowFlag = len(cluster1Cols)

#populate the second group
cluster2Cols = []
for i in range(0, columns):
    if i in cluster1Cols:
        None
    else:
        cluster2Cols.append(i)

cluster2Rows = []
for i in range(0, rows):
    if i in cluster1Rows:
        None
    else:
        cluster2Rows.append(i)

#Convert python index to pandas index
cluster1Cols = [x+1 for x in cluster1Cols]
cluster1Rows = [x+1 for x in cluster1Rows]
cluster2Cols = [x+1 for x in cluster2Cols]
cluster2Rows = [x+1 for x in cluster2Rows]

#Determine if matrix is decomposable
if len(cluster2Cols) == 0 or len(cluster2Rows) == 0:
    print('<h2> The matrix is not decomposable </h2>')
else:

    cluster1Cols.sort()
    cluster1Rows.sort()
    cluster2Cols.sort()
    cluster2Rows.sort()

    cluster1Cols.extend(cluster2Cols)
    cluster1Rows.extend(cluster2Rows)

    #Reorder columns and rows
    matrix = matrix[cluster1Cols]
    matrix = matrix.reindex(cluster1Rows)
    print("<h2> Decomposed Matrix </h2>")
    print(matrix.to_html(col_space = 30))
