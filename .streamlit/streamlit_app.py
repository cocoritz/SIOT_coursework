st.write("""
# Siot web app

Shown are the stock closing price and volume of Google!

""")

html_string = '''
<h1>HTML string in RED</h1>

<script language="javascript">
  document.querySelector("h1").style.color = "red";
</script>
'''

components.html(html_string)  # JavaScript works
