sg = sendgrid.SendGridAPIClient('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')
from_email = Email("susanthika02m@gmail.com")
to_email = To("sruthiramesh270@gmail.com")
subject = "Sending with SendGrid"
content = Content("text/plain", "SendGrid Integrated With Python Successfully!")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)