import smtplib

server= smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("sharmishri@gmail.com", "@!#shri1810@")
server.sendmail("sharmishri@gmail.com", "ssrikanth@tologix.com", "testagain")
server.quit()