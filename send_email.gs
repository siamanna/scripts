function sendPlainTextEmail() {
    const recipient = 'recipientemailaddress@gmail.com'
    const subject = 'Subject of the email'
    const body = 'This email is sent and automated by Google Scripts!'
    GmailApp.sendEmail(recipient, subject, body)
    console.log('Email sent to: ' + recipient)
}

//Press Run on Extensions-> scripts to send emails