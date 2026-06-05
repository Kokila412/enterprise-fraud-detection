# Enterprise Real-Time Pre-Payment UPI Fraud Detection Engine
### **An Explainable AI (XAI) Architecture for Mitigation of In-Flight Financial Cybercrimes**

---

## Executive Summary
Modern financial infrastructures suffer from high-velocity asset draining due to social engineering and peer-to-peer (P2P) payment fraud. Traditional security frameworks operate post-facto (post-transaction), analyzing data patterns only after capital has physically left the source account. 

This project introduces a Pre-Authorization In-Flight Gateway that evaluates risk vectors and blocks malicious activities before the Unified Payments Interface (UPI) PIN entry screen is initialized. By combining an optimized Extreme Gradient Boosting (XGBoost) classifier with a simulated distributed historical ledger, the system detects transaction anomalies, account age exploitation, and coordinated money-mule layering structures within a sub-300ms execution envelope.

* **Engineering Core:** Machine Learning Classification, Explainable AI (XAI), Behavioral Engineering
* **Enterprise Stack:** Python, Flask, XGBoost, Pydantic, Scikit-Learn, JavaScript (ES6), HTML5/CSS3

---

## Strategic Project Objectives
* **Proactive Loss Prevention:** Terminate unauthorized payment routing loops at the interaction gateway to ensure customer capital remains securely inside the source institution.
* **Coordinated Network Identification:** Analyze transactional paths to uncover distributed money-mule routing patterns and automated funds-layering velocity.
* **Explainable AI (XAI) Implementation:** Demystify model outputs by mapping mathematical classification scores to clean, transparent diagnostic risk factors for enhanced system observability.

---

## Core Parameters & Inspection Architecture

The payment gateway evaluates incoming requests across four structural pillars prior to routing data to core banking transaction networks:

```mermaid
graph TD
    %% Define Styles and Colors
    classDef payload fill:#f1f5f9,stroke:#64748b,stroke-width:2px,stroke-dasharray: 5 5,color:#334155;
    classDef step fill:#ffffff,stroke:#0f172a,stroke-width:2px,color:#0f172a;
    classDef engine fill:#eff6ff,stroke:#2563eb,stroke-width:2px,color:#1e40af,font-weight:bold;
    classDef approved fill:#f0fdf4,stroke:#16a34a,stroke-width:2px,color:#15803d,font-weight:bold;
    classDef blocked fill:#fef2f2,stroke:#dc2626,stroke-width:2px,color:#b91c1c,font-weight:bold;

    %% Workflow Nodes
    A["[ INCOMING API PAYLOAD ]<br/>(Amount, Sender VPA, Receiver VPA)"]:::payload
    
    B["1. STRUCTURAL VPAs INTEGRITY CHECK<br/>Scans text strings for lookalike deceptive corporate identities."]:::step
    
    C["2. REPUTATION & TEMPORAL AGE AUDIT<br/>Checks if the UPI Handle and linked Bank Account are brand new."]:::step
    
    D["3. LAYERED VELOCITY & SPLIT-FUNDS ANALYSIS<br/>Identifies historic rapid fractional routing patterns (hot potato)."]:::step
    
    E["4. BALANCE DRAINAGE (MULE SIGNATURE) PROFILING<br/>Flags accounts utilizing rapid cash-out behaviors down to a ₹0 base."]:::step
    
    F["CORE XGBOOST INFERENCE ENGINE<br/>Evaluates combined structural risk score against transaction amount."]:::engine
    
    G["ACTION: APPROVED<br/>Transaction proceeds to banking PIN authorization."]:::approved
    H["ACTION: BLOCKED<br/>Gateway communication severed. Process terminated."]:::blocked

    %% Flow Connections
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    F --> H

Technical Parameter Metrics:
Virtual Payment Address (VPA) Integrity: Uses string-matching and natural language heuristics to scan for spoofed high-profile keywords (such as customer_care or verification) deployed to mimic official entities.

Account & Handle Temporal Age: Validates the creation timestamp of both the active UPI handle and the underlying bank account node to catch zero-reputation, high-velocity malicious endpoints.

Layering Layer Analysis: Evaluates historical ledger records to flag if the receiver possesses a statistical variance of receiving large sums and immediately splitting them into fractional outflows across secondary nodes within tight time windows.

Mule Liquidity Profile: Cross-references historical balance baselines to calculate if incoming funds are instantly drained via high-frequency electronic routing or ATM cash-out thresholds.

Machine Learning Pipeline & Observability
Because real-world financial fraud represents highly skewed, imbalanced datasets (~3% anomalies vs. ~97% baseline operations), basic binary classifiers frequently fall victim to severe precision degradation.

To counter class imbalance, the system leverages XGBoost (Extreme Gradient Boosting) optimized via gradient-boosted decision trees to map multi-variable contextual data.

Rather than outputting an opaque classification value, the framework integrates an Explainable AI Layer. It extracts feature weights from the computation and translates mathematical thresholds into clear, localized user diagnostics to lower customer support overhead and prevent unnecessary false positives.

Live Production Simulation Workflow
The Active Interception Timeline:
Payload Submission: A user attempts to transfer ₹2,500 to a compromised target account (fresh_scammer@okaxis).

Gateway Interception: The client-side application traps the form-submit handler, disables page interactives, and transmits a validated JSON object to the Flask /predict microservice.

Compound Risk Analysis: The backend queries the historical ledger database. It confirms that the receiver profile matches a newly activated handle linked to a fresh bank account exhibiting automated layering characteristics.

Active Gateway Termination: The engine executes a safety override, sets a BLOCKED status, and breaks the communication loop to core banking settlement networks.

Diagnostic Output Rendered: The front end catches the payload and prints out an observable log interface, neutralizing the threat before a transaction can build legal execution:

Plaintext
[TRANSACTION BLOCKED] Status: Fraudulent Activity Intercepted

SAFETY WARNING: This transaction has been terminated to protect your funds. The money has NOT left your account.

RISK FACTORS DETECTED:
  • Newly Activated UPI Handle (Zero Reputation)
  • Freshly Opened Bank Account Node
  • Historical High-Velocity Split-Fund Behavior (Layering Network)
  • Mule Account Profile Signature (Rapid Balance Drainage Target)

Action Restricted: Gateway communication severed. UPI PIN Pad initialization suspended.
Key Engineering Milestones
Pre-PIN Interception Blueprint: Successfully demonstrated that isolating payment parameters prior to PIN authorization structurally eliminates the success rate of human social engineering vectors.

Observable Structural Diagnostics: Built a translation layer converting raw machine learning matrix weights into localized, human-readable user alert overlays.

Conditional Override Architecture: Designed a threshold override engine capable of cross-referencing live transactional state changes with static database ledgers to execute zero-latency hard blocks.

enterprise_fraud_detection/
│
├── backend/
│   ├── app.py            # Flask Web Controller & Pre-Payment Inspection Layer
│   └── schemas.py        # Pydantic Structural Data Security Schemas
│
├── ml_training/
│   └── train_model.py    # XGBoost Mathematical Pipeline & Synthetic Data Synthesis
│
└── frontend/
    ├── index.html        # Interactive Fintech Core Simulation Screen
    ├── style.css         # Security Terminal Dashboard Layout Theme
    └── script.js         # Asynchronous Event Triggers & Network Handshake Layer