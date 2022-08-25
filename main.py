#from maskpass import askpass, advpass
import pwinput
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def lazyMailer():
    # Login for the mail account
    u_email = "your_email@gmail.com"
    u_pass = pwinput.pwinput(prompt='Enter password for mail account:', mask='#')
    receiver_mail = input("Enter company email : ")

    # Message Body
    company = input("Enter the companies name: ")
    text = """Hello """ + company + """,
            
            Custom Body of the Mail
            
            Regards,
            your_beautiful_name

            PS: This mail was sent through a python automation tool LazyMailer
                 https://github.com/notson00b/LazyMailer/"""

    # Setup the MIME

    message = MIMEMultipart()
    message['From'] = u_email
    message['To'] = receiver_mail
    message['Subject'] = 'your_subject_line'

    # Attaching text variable with MIME instance
    message.attach(MIMEText(text, 'plain'))

    # Attaching resume file
    file_name = "your_resume_file"
    file_path = r"path_for_your_resume_file"
    attachment = open(file_path, 'rb')

    # MIMEBase, encoding and wrapping
    msg_part = MIMEBase('application', 'octet-stream')
    msg_part.set_payload((attachment).read())
    encoders.encode_base64(msg_part)
    msg_part.add_header('Content-Disposition', "attachment;filename = %s" % file_name)

    # Attaching MIMEBase instance to the message instance
    message.attach(msg_part)

    # Converting multipart message into string
    body = message.as_string()

    # Initialization of SMTP server and TLS for security
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.starttls()
    mail.login(u_email, u_pass)

    # Mailing
    mail.sendmail(u_email, receiver_mail, body)

    # Terminating the session
    mail.quit()


    # Main of the code
if __name__ == '__main__':
    print("""_                     __  __       _ _           
    	    | |                   |  \/  |     (_) |          
    	    | |     __ _ _____   _| \  / | __ _ _| | ___ _ __ 
    	    | |    / _` |_  / | | | |\/| |/ _` | | |/ _ \ '__|
    	    | |___| (_| |/ /| |_| | |  | | (_| | | |  __/ |   
    	    |______\__,_/___|\__, |_|  |_|\__,_|_|_|\___|_|   
    	                      __/ |                           
    	                     |___/                         """)
    print("Ahhh! I'm bored of copying and pasting the same stuff")
    print('Behold! Fruit of my laziness!')

    lazyMailer()


