function sendCustomEmail() {
    const numRecipientsInput = Browser.inputBox("Enter the number of recipients:");
    if (numRecipientsInput === "cancel" || numRecipientsInput === null) return;
    const numRecipients = parseInt(numRecipientsInput);

    let recipients = [];
    for (let i = 0; i < numRecipients; i++) {
        const recipientEmail = Browser.inputBox(`Enter the email address for recipient ${i + 1}:`);
        if (recipientEmail === "cancel" || recipientEmail === null) return;
        recipients.push(recipientEmail);
    }

    const subject = Browser.inputBox("Enter the subject of the email:");
    if (subject === "cancel" || subject === null) return;

    const body = Browser.inputBox("Enter the body of the email:");
    if (body === "cancel" || body === null) return;

    const attachmentResponse = Browser.inputBox("Do you want to add an attachment? (yes/no)");
    if (attachmentResponse === "cancel" || attachmentResponse === null) return;

    let attachments = [];
    if (attachmentResponse.toLowerCase() === "yes") {
        const attachmentId = Browser.inputBox("Please enter the Google Drive file ID for the attachment:");
        if (attachmentId === "cancel" || attachmentId === null) return;
        const file = DriveApp.getFileById(attachmentId);
        attachments.push(file);
    }

    recipients.forEach(recipient => {
        if (attachments.length > 0) {
            GmailApp.sendEmail(recipient, subject, body, {
                attachments: attachments
            });
        } else {
            GmailApp.sendEmail(recipient, subject, body);
        }
        console.log('Email sent to: ' + recipient);
    });

    Browser.msgBox("Emails sent successfully!");
}
