from gmail import GMail, Message
#select a random file
from random import choice
file_names = ['1.html','2.html', '3.html']
file_name = choice(file_names)

#read html-content
template_file = open(file_name, encoding="utf-8")
html_content = template_file.read()
template_file.close()

#render reason
reasons = ['đậu má','lá xanh','đau bụng']
reason = choice(reasons)

html_content = html_content.replace('{{reason}}', reason)

gmail = GMail('coderyan62@gmail.com','04042204')
msg = Message('Xin nghỉ phép',to='coderyan62@gmail.com', html=html_content)
gmail.send(msg)
