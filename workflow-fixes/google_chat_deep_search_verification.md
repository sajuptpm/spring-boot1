# Deep Search Verification & Enterprise Guide: Google Chat (`GOOGLE_CHAT_WEBHOOK_URL`) in Spring Boot

**Component**: `Spring Boot 4.1.2`  
**Reference Upstream Commit**: `2904c4c0c49`  
**Vendor**: Google LLC (<https://workspace.google.com/products/chat/>)  
**Date**: 2026-11-12  

---

## 1. What Is This (`Google Chat`)?

**Google Chat Incoming Webhook API** is a Google Workspace messaging endpoint (`https://chat.googleapis.com/v1/spaces/.../messages`) that allows external CI/CD pipelines to post real-time HTTP POST JSON alerts (`{ text: "..." }`) into a team’s Google Chat Space when builds succeed, fail, or get cancelled.

---

## 2. Does This Project Use It? (Deep Search Evidence)

**Yes — Google Chat notifications are genuinely implemented in upstream Spring Boot (`2904c4c0c49`) across 1 shared action and 4 workflows.**

| File | Verified Code Evidence | What It Does |
| :--- | :--- | :--- |
| **[`.github/actions/send-notification/action.yml`](../.github/actions/send-notification/action.yml#L1-L39)** | Line 2: `'Sends a Google Chat message as a notification of the job''s outcome'`<br>Lines 14–16: `webhook-url` (`'Google Chat Webhook URL'`, `required: true`)<br>Lines 27–39: `curl -X POST '${{ inputs.webhook-url }}' -H 'Content-Type: application/json' -d '{ text: "..." }' \|\| true` | Posts success, failure (`<users/all>`), or cancelled alerts with run URL and Develocity build-scan link. |
| **[`.github/workflows/build-and-deploy-snapshot.yml`](../.github/workflows/build-and-deploy-snapshot.yml#L45-L71)** | Lines 45–50 & Line 71 | Sends `secrets.GOOGLE_CHAT_WEBHOOK_URL` on snapshot deployment and passes it to `verify.yml`. |
| **[`.github/workflows/ci.yml`](../.github/workflows/ci.yml#L62-L67)** | Lines 62–67 | Sends `secrets.GOOGLE_CHAT_WEBHOOK_URL` for every OS/Java CI matrix job outcome. |
| **[`.github/workflows/run-system-tests.yml`](../.github/workflows/run-system-tests.yml#L48-L53)** | Lines 48–53 | Sends `secrets.GOOGLE_CHAT_WEBHOOK_URL` after Testcontainers system test runs. |
| **[`.github/workflows/verify.yml`](../.github/workflows/verify.yml#L21-L93)** | Lines 21–24, 49–50, 89–93 | Sparse-checks out `send-notification` and posts verification status to `secrets.google-chat-webhook-url`. |

**Critical Operational Note**: Because `send-notification/action.yml` appends `|| true` to every `curl` command, **a missing webhook URL does not fail the Gradle build or release artifacts** — alerts are simply dropped.

---

## 3. How Can I Use It in My Enterprise?

* **Option A — Use Existing Enterprise Chat / GitHub Summaries (Recommended — `$0`)**:
  * Most enterprises already run **Microsoft Teams** (included in M365), **Slack**, or corporate email.
  * Update the single 40-line file [`.github/actions/send-notification/action.yml`](../.github/actions/send-notification/action.yml) to write to **GitHub Step Summaries (`$GITHUB_STEP_SUMMARY`)**, post to a **Microsoft Teams / Slack webhook**, or guard `curl` with `if: inputs.webhook-url != ''`.
  * This matches the preferred replacement in [`workflow-fixes/spring_boot_ml_entries.json`](spring_boot_ml_entries.json#L406) (`master_list` Row 82): *"Use existing Microsoft Teams/email."*
* **Option B — If Your Enterprise Already Uses Google Workspace**:
  * In a Google Chat Space, go to **Apps & integrations → Manage webhooks → Add webhook**, copy the URL, and store it in GitHub repository secrets as `GOOGLE_CHAT_WEBHOOK_URL`.

---

## 4. Which Subscription Do I Need to Purchase?

| Your Enterprise Environment | Subscription to Purchase | Annual Cost | Notes |
| :--- | :--- | :--- | :--- |
| **Uses Microsoft Teams / Slack / Email / GitHub UI** | **None (`$0`)** | **\$0 / year** | Adapt [`send-notification/action.yml`](../.github/actions/send-notification/action.yml) to your existing tool or `$GITHUB_STEP_SUMMARY`. |
| **Already Pays for Google Workspace** | **None extra (`$0`)** | **\$0 / year** | Google Chat Spaces + Incoming Webhooks are included in existing Google Workspace plans. |
| **Does NOT Have Google Workspace, but Demands Google Chat Webhooks** | **Google Workspace Business Starter** *(1 seat minimum)* **or Business Standard** *(5 seats)* | **\$84 / year** *(1 Starter seat)*<br>or **~\$420 – \$840 / year** *(5 users)* | Free personal `@gmail.com` accounts do **not** support Google Chat Space incoming webhooks. In `master_list` Row 82, the review notes 1 Business Starter account (`~$84/yr`) can own the Space/webhook, while full 5-user Business Standard (`$12–$14/user/mo`) runs `~$720–$840/yr`. |

---

## 5. Why Did This Appear in Your Table?

1. **Real Upstream Dependency**: Upstream Spring engineering uses Google Chat internally, and `secrets.GOOGLE_CHAT_WEBHOOK_URL` is hardcoded into 4 upstream workflows via [`send-notification/action.yml`](../.github/actions/send-notification/action.yml).
2. **Upstream Inventory Tracking**: Your sheet records every paid SaaS integration present in the unedited upstream pipelines (`Upstream Original Tool`) alongside its vendor (`Google LLC`) and commercial Workspace requirement.
3. **Why You Don't Need to Buy It**: As flagged in `master_list` Row 82 (`Plan based on Review: Need IT Review`), unless your IT department already standardizes on Google Workspace, swapping the webhook destination to your existing **Microsoft Teams / Slack / GitHub Step Summary** drops this cost to **`$0`**.
