#!/usr/bin/python

import cgi
import cgitb

cgitb.enable()

print("Content-Type: text/html\n\n")
print("<h1>Matrix Decomposition</h1>")

print("""
<form name="matrix" action="matrix.py" method="post">
How Many Columns in Matrix?<br>
  <input type="text" name="columns">
  <br>
  How Many Rows in Matrix?<br>
  <input type="text" name="rows">
  <br><br>
<input type="submit" value="Submit">
</form>
""")
