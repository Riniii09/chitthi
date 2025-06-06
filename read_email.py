import imaplib
import email
from email.header import decode_header
from google import genai

# ENTER YOUR DETAILS
# username = 'username@mail.com'
# password = 'password'
# api_key = 'YOURAPIKEY'

# When using a gmail account
imap_server = 'imap.gmail.com'

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, password)

imap.select("INBOX")
status, message = imap.search(None, "ALL")
mail_ids = message[0].split()
# print(mail_ids)
latest_id = mail_ids[-1]
# print(latest_id)

result, target = imap.fetch(latest_id, "(RFC822)")
raw_email = target[0][1]
msg = email.message_from_bytes(raw_email)
# print(msg)

subject, encoding = decode_header(msg["Subject"])[0]
if isinstance(subject, bytes):
    subject = subject.decode(encoding if encoding else "utf-8")
    
if subject.strip().endswith("muhehehe"):
    print("sillyness detected")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content( 
        model="gemini-2.0-flash",
        contents="Make a one line joke and end with an evil laugh muhehehe",
    )

    print(response.text)
else:
    print("No sillyness")
    

