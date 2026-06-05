async function handleTransactionSubmit(event) {
    event.preventDefault();
    
    const resultContainer = document.getElementById("transaction-result");
    const submitBtn = document.getElementById("submit-btn");
    
    resultContainer.innerHTML = "<p class='loading'>Processing in-flight security evaluation...</p>";
    submitBtn.disabled = true;

    const payload = {
        sender_upi_id: document.getElementById("sender_id").value.trim(),
        receiver_upi_id: document.getElementById("receiver_id").value.trim(),
        amount: parseFloat(document.getElementById("amount").value)
    };

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (data.action === "BLOCKED") {
            let factorListItems = data.factors.map(f => `<li>${f}</li>`).join("");
            
            resultContainer.innerHTML = `
                <div class="security-alert-box">
                    <h3>[TRANSACTION BLOCKED] Status: Fraudulent Activity Intercepted</h3>
                    <p class="safety-warning"><strong>SAFETY WARNING:</strong> This transaction has been terminated to protect your funds. The money has NOT left your account.</p>
                    
                    <div class="risk-factors">
                        <strong>RISK FACTORS DETECTED:</strong>
                        <ul>
                            ${factorListItems}
                        </ul>
                    </div>
                    
                    <p class="restriction-footer"><strong>Action Restricted:</strong> Gateway communication severed. UPI PIN Pad initialization suspended.</p>
                </div>
            `;
        } else {
            resultContainer.innerHTML = `
                <div class="security-success-box">
                    <h3>[TRANSACTION APPROVED]</h3>
                    <p>${data.explanation}</p>
                </div>
            `;
        }

    } catch (error) {
        resultContainer.innerHTML = `<p class="error">Gateway Connection Fault: Unable to reach verification server.</p>`;
    } finally {
        submitBtn.disabled = false;
    }
}