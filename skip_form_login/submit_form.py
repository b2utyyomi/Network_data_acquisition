# 表单位于http://pythonscraping.com/pages/files/form.html
# 网页源代码 
'''
<h2>Tell me your name!</h2>
<form method="post" action="processing.php">
First name: <input type="text" name="firstname"><br>
Last name: <input type="text" name="lastname"><br>
<input type="submit" value="Submit" id="submit">
</form>
'''

import requests

params = {'firstname':'b2uty', 'lastname':'yomi'}
r = requests.post("http://pythonscraping.com/pages/files/processing.php", data = params)
print(r.text)

# r是Response object 
