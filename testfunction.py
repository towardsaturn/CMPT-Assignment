import cgi
form = cgi.FieldStorage()
ItemOne=form["item1"].value
QuantityOne=form["quantity1"].value

price=5.99

def printpurchaseone():
    price=5.99
    totalprice=price*int(form["quantity1"].value)
    return totalprice


print "Content-type: text/html"
print
print"""<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
<html xmlns='http://www.w3.org/1999/xhtml'><head>
<meta http-equiv='content-type' content='text/html; charset=UTF-8' />
<title>Your Order has been Submitted</title>
</head><body>"""

print "<p><b>", ItemOne, "</b></p><p><b>Quantity:</b>" ,QuantityOne, "</p><p><b>Price: </b>", printpurchaseone() ,"at a rate of <b>" ,price, "</b> each</p>"

print "</div></body></html>"
