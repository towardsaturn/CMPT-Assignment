import cgi
form = cgi.FieldStorage()

ItemOne=form["item1"].value
ItemTwo=form["item2"].value
ItemThree=form["item3"].value
ItemFour=form["item4"].value
ItemFive=form["item5"].value
QuantityOne=form["quantity1"].value
QuantityTwo=form["quantity2"].value
QuantityThree=form["quantity3"].value
QuantityFour=form["quantity4"].value
QuantityFive=form["quantity5"].value
CustName=form["name"].value
Email=form["email"].value
Address=form["address"].value
City=form["city"].value
PostCode=form["postalcode"].value
Prov=form["province"].value
CardType=form["creditcardtype"].value
CardNum=form["cardnumber4"].value
CardExpir=form["expiration"].value
GiftWrap=form["giftwrap"].value
Updates=form["updates"].value

#start variables
price=5.99
purchaseone= price*int(form["quantity1"].value)
purchasetwo=price*int(form["quantity2"].value)
purchasethree=price*int(form["quantity3"].value)
purchasefour=price*int(form["quantity4"].value)
purchasefive=price*int(form["quantity5"].value)
total=purchaseone+purchasetwo+purchasethree+purchasefour+purchasefive

if total > 150:
        d=(total*0.15)
else:
        d=0
        

if  GiftWrap=="Yes":
        g=(int(QuantityOne)+int(QuantityTwo)+int(QuantityThree)+int(QuantityFour)+int(QuantityFive))
else:
        g=0
        

if Prov=="BC" or Prov=="bc" or Prov=="bC"or Prov=="Bc":
    secondtotal=total-int(d)+int(g)
    tax=secondtotal*0.12
else:
    secondtotal=total-int(d)+int(g)
    tax=secondtotal*0.06

if Prov=="BC" or Prov=="bc" or Prov=="bC"or Prov=="Bc":
    s=5
else:
    s=10

def updates():
        if  Updates=="Yes":
                 message="You have selected to recieve updates. We will send you e-mails to notify you about promotions and new products."
                 return message
        else:
                message=""
                return message
        

def thankyou():
        print "<p>Your receipt is listed below</p>"
        print "<p>Click <a href='home.html'>here</a> to go back to the homepage.</p>"



finaltotal=(total+int(g)-int(d))+tax+int(s)

#Start HTML
print "Content-type: text/html"
print
print"""<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
<html xmlns='http://www.w3.org/1999/xhtml'><head>
<meta http-equiv='content-type' content='text/html; charset=UTF-8' />
<title>Your Order has been Submitted</title>
<link rel = "alternate stylesheet" href = "stylesheet1.css" type = "text/css" title = "Starry Night" />
<link rel = "stylesheet" href = "stylesheet2.css" type = "text/css" title = "Cotton Candy" />
<style type="text/css">
b
{
color:#000;
text-decoration:none;
}

.table
{
width:550px;
border: 2px solid #292b55;
text-align:left;
padding:8px;
}
</style>

</head><body>
<p><img src='images/banner.jpg' alt='Night Crystals' /></p>"""

print"""<div id="sidebar">
<ul id="navigation" style="list-style: none;">
<li><a href="home.html">Home Page</a></li>
<li><a href="about.html">Our Company</a></li>
<li><a href="products.html">Products</a></li>
<li><a href="order.html">Order</a></li>
<li><a href="testimonials.html">Testimonials</a></li>
</ul>
</div><div id="content">"""

print "<h1>Thank-you for ordering!</h1>"
thankyou()
print "<div class='table'>"
print "<p><b>Name:</b>",CustName,"</p>"
print "<p><b>Email:</b>",Email,"</p>"
print "<p><b>Address:</b>",Address,"</p>"
print "<p><b>City:</b>",City,"</p>"
print "<p><b>Province:</b>",Prov,"</p>"
print "<p><b>Postal Code</b>",PostCode,"</p>"
print "<p><b>Card Type:</b>",CardType,"</p>"
print "<p><b>Card Number:</b> xxxx xxxx xxxx ",CardNum,"</p>"
print "<p><b>Card Expiration</b>",CardExpir,"</p></div><br /><div class='table'>"
print "<p><b>", ItemOne, "</b></p><p><b>Quantity:</b>" ,QuantityOne, "</p><p><b>Price: </b>", purchaseone ,"at a rate of <b>" ,price, "</b> each</p></div><br /><div class='table'>"
print "<p><b>", ItemTwo, "</b></p><p><b>Quantity:</b>" ,QuantityTwo, "</p><p><b>Price: </b>", purchasetwo ,"at a rate of <b>" ,price, "</b> each</p></div><br /><div class='table'>"
print "<p><b>", ItemThree, "</b></p><p><b>Quantity:</b>" ,QuantityThree, "</p><p><b>Price: </b>", purchasethree ,"at a rate of <b>" ,price, "</b> each</p></div><br /><div class='table'>"
print "<p><b>", ItemFour, "</b></p><p><b>Quantity:</b>" ,QuantityFour, "</p><p><b>Price: </b>", purchasefour ,"at a rate of <b>" ,price, "</b> each</p></div><br /><div class='table'>"
print "<p><b>", ItemFive, "</b></p><p><b>Quantity:</b>" ,QuantityFive, "</p><p><b>Price: </b>", purchasefive ,"at a rate of <b>" ,price, "</b> each</p></div><br /><div class='table'>"
print "<p><b>Total Before Tax:</b>$", total, "</p>"
print "<p><b>Discount</b>(15% off if total is over $150): $",int(d),"OFF</p>" 
print "<p><b>GiftWrap:($1 Per Item)</b>$",int(g),"</p>" 
print "<p><b>Tax (After Giftwrap and Discount)</b>:$",int(tax) ,"</p>"
print "<p><b>Shipping</b>: $",int(s),"</p>"
print "<p><b>TOTAL COST:</b>$",int(finaltotal), "</p>"
print updates()

print "</div></div></body></html>"





