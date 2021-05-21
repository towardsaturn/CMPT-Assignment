<?xml version="1.0" encoding="ISO-8859-1"?> 

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match = "/">
	<html>
	<head><title>Night Crystals: Inventory List</title></head>
	<body>
	
	<h1>Night Crystals</h1>
<ul>
  <xsl:for-each select="products/item">
  <xsl:sort select="name"/>
<li>

<span style="color:purple;font-weight:bold">
	<xsl:value-of select="name"/></span><br />
	<span style="color:olive">
	<xsl:value-of select="price"/></span><br />
	<span style="color:navy">
	<xsl:value-of select="description"/></span><br />
	<xsl:if test="inventory &lt;=23">
	Inventory:<span style="color:red; font-weight:bold"><xsl:value-of select="inventory"/></span><br /><br />
	</xsl:if>
	<xsl:if test="inventory &gt;23">
	Inventory:<span style="color:blue"><xsl:value-of select="inventory"/></span><br /><br />
	</xsl:if>
</li>
	</xsl:for-each>
</ul>
	
	
	</body>
	</html>
</xsl:template>
</xsl:stylesheet>

