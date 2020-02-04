import smtplib
import email.utils
from email.mime.text import MIMEText

msg = MIMEText('siehe subject', 'plain')
msg['Subject'] = 'Subject.'
msg['From'] = email.utils.formataddr(('Warning','warning@beersaturday.com'))
msg['To'] = email.utils.formataddr(('personToBeWarned','recieving@someOtherAccount'))

with smtplib.SMTP('domain') as smtp:
    smtp.set_debuglevel(True)
    smtp.login('sending@myAccount','myPassword')
    success = smtp.sendmail("sending@myAccount", ['recieving@someOtherAccount'], msg.as_string())
    print(success)