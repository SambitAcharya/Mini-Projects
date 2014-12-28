page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
string=page[start_link:]
start_link_2 = string.find('"') + 1
url = string[start_link_2:-2]
print url
