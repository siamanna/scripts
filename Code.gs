// Script to get data from Google Sheets

function getData() {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const sheet = ss.getSheetbyName('Sheet1');
    const data = sheet.getDataRange().getValues();
    for (int i = 1; i < data.length; i++) {
        //Enter your variables that you want to print accordingly
        const var1 = data[i][0];
        const var2 = data[i][1];
        const var3 = data[i][2];

        console.log('var1: ' + var1 + ' var2: ' + var2 + ' var3: ' + var3);
    }
}