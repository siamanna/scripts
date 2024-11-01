function sendCustomEmail() {
    const ui = SpreadsheetApp.getUi(); // Assuming this runs from a Google Sheets environment
    const numRecipients = parseInt(ui.prompt("Enter the number of recipients:").getResponseText());

    let recipients = [];
    for (let i = 0; i < numRecipients; i++) {
        const recipientEmail = ui.prompt(`Enter the email address for recipient ${i + 1}:`).getResponseText();
        recipients.push(recipientEmail);
    }

    const subject = ui.prompt("Enter the subject of the email:").getResponseText();
    const body = ui.prompt("Enter the body of the email:").getResponseText();

    const attachmentResponse = ui.prompt("Do you want to add an attachment? (yes/no)").getResponseText().toLowerCase();
    let attachments = [];

    if (attachmentResponse === "yes") {
        const attachmentId = ui.prompt("Please enter the Google Drive file ID for the attachment:").getResponseText();
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

    ui.alert("Emails sent successfully!");
}
