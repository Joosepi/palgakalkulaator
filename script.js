function calculateSalary() {
   
    const employeeName = document.getElementById('employeeName').value;
    const hoursWorked = parseFloat(document.getElementById('hoursWorked').value);
    const payRate = parseFloat(document.getElementById('payRate').value);

    
    const overtimePayRate = payRate * 1.5;
    const regularHours = hoursWorked > 40 ? 40 : hoursWorked;
    const overtimeHours = hoursWorked > 40 ? hoursWorked - 40 : 0;
    const regularPay = regularHours * payRate;
    const overtimePay = overtimeHours * overtimePayRate;
    const totalBrutoPay = regularPay + overtimePay;
    const taxRate = 0.20;
    const totalDeductions = totalBrutoPay * taxRate;
    const totalNetoPay = totalBrutoPay - totalDeductions;

   
    const resultHTML = `
        <p><strong>Employee Name:</strong> ${employeeName}</p>
        <p><strong>Hours Worked:</strong> ${hoursWorked.toFixed(2)}</p>
        <p><strong>Pay Rate:</strong> ${payRate.toFixed(2)}</p>
        <p><strong>Regular Hours:</strong> ${regularHours.toFixed(2)}</p>
        <p><strong>Overtime Hours:</strong> ${overtimeHours.toFixed(2)}</p>
        <p><strong>Regular Hour Pay:</strong> $${regularPay.toFixed(2)}</p>
        <p><strong>Overtime Pay:</strong> $${overtimePay.toFixed(2)}</p>
        <p><strong>Bruto Pay:</strong> $${totalBrutoPay.toFixed(2)}</p>
        <p><strong>Deductions:</strong> $${totalDeductions.toFixed(2)}</p>
        <p><strong>Neto Pay:</strong> $${totalNetoPay.toFixed(2)}</p>
    `;

   
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = resultHTML;
}
