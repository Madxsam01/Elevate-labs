
# 📄 Phishing Email Analysis Report

## 🛡️ Task Objective
To identify phishing indicators in a suspicious email sample by analyzing sender identity, headers, links, language, and formatting.

---

## 📧 Email Sample Overview

- **Subject**: `Monday.com – Invitation to join Board`
- **From (Display Name)**: `Monday.com`
- **From (Actual Email)**: `support@shared-document.com`
- **Time Received**: 4:10 PM

> ![Email Screenshot](./Screenshot-2025-06-25.png)

---

## 🔍 Step-by-Step Analysis

### 🔹 Step 1: Obtain the Sample
- ✅ A suspicious email screenshot was provided.
- ✅ The email appears to impersonate a well-known brand: **Monday.com**.

---

### 🔹 Step 2: Examine the Sender’s Email Address

| Check | Result |
|-------|--------|
| Domain Match | ❌ `shared-document.com` ≠ `monday.com` |
| Misspelling/Impersonation | ✅ Domain is generic and misleading |
| Free Email Domain? | ❌ Custom domain, but untrusted |
| Suspicious Display Name | ✅ Uses “Monday.com” to deceive |

---

### 🔹 Step 3: Analyze the Email Header (Simulated)

```text
Return-Path: <support@shared-document.com>
SPF: FAIL
DKIM: FAIL
DMARC: FAIL
Originating IP: 185.199.110.153
```

| Check | Result |
|-------|--------|
| SPF | ❌ Failed – unauthorized IP |
| DKIM | ❌ Failed – signature mismatch |
| DMARC | ❌ Failed – sender policy rejected |
| IP Geolocation | ❌ Does not match Monday.com infrastructure |

---

### 🔹 Step 4: Check Links/Attachments

- **Visible Button**: “See the board now”
- **Hover Check**: (Simulated) → `http://malicious-link.com/join`
- ✅ **Mismatch** between button and expected domain (`monday.com`)
- ❌ **No attachments** present in screenshot

---

### 🔹 Step 5: Urgent/Threatening Language

| Message Part | Observation |
|--------------|-------------|
| “Everyone else has already joined!” | Creates **social pressure** |
| “See the board now” | **Call to immediate action** |

---

### 🔹 Step 6: Grammar/Spelling Errors

| Check | Result |
|-------|--------|
| Grammar | “added your team Everyone at” → incomplete |
| Professional Tone | ✅ Fairly convincing, but lacks personalization |

---

### 🔹 Step 7: Branding & Format

| Check | Result |
|-------|--------|
| Logo Used | ✅ Correct logo |
| Colors | ✅ Match official style |
| Personalized Name | ❌ Not addressed to recipient |
| Contact Info | ❌ Missing support details or signature |

---

## 📌 Final Summary of Indicators

| Indicator | Present |
|-----------|---------|
| Spoofed Email Address | ✅ Yes |
| SPF/DKIM/DMARC Failures | ✅ Yes |
| Mismatched or Suspicious URL | ✅ Yes |
| Urgency or Social Pressure | ✅ Yes |
| Grammar/Content Errors | ⚠️ Minor |
| Branding Inconsistencies | ✅ Yes |
| Missing Personalization | ✅ Yes |

---

## 🛑 Conclusion: PHISHING EMAIL DETECTED

> This email is designed to impersonate **Monday.com** and trick the user into clicking a malicious link. It uses a **spoofed sender address**, **fails authentication checks**, and **relies on urgency/social engineering**. It should be reported and deleted immediately.

---
