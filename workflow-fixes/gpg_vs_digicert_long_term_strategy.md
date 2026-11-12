# Long-Term Enterprise Signing Strategy: OpenPGP/GPG vs. DigiCert KeyLocker

**Portfolio Context**: `Spring Boot 4.1.2`, `Angular 21.2.25`, `Node.js 26.13.0`, `GraalVM 25`, `K3s 1.35` ([`workflow-fixes/data1.xlsx`](data1.xlsx))  
**Date**: 2026-11-12  

---

## 1. Should You Purchase DigiCert as a Future Long-Term Plan?

**No — do not buy it speculatively now.** Purchase a commercial X.509 code-signing service **only if and when you ship native desktop/Windows executables** to external end-users.

* Code-signing certificates are time-limited (1–3 year validity with annual fees). Buying DigiCert KeyLocker before you have Windows `.exe`/`.msi` deliverables means paying **~\$600–\$996/year** for an unused subscription.
* Across all 5 components in [`workflow-fixes/data1.xlsx`](data1.xlsx) (`Spring Boot 4.1.2`, `Angular 21.2.25`, `Node.js 26.13.0`, `GraalVM 25`, `K3s 1.35`), **none** of the reviewed baselines require DigiCert KeyLocker.

---

## 2. Does GPG Provide All Features That DigiCert Provides?

**No — GPG and DigiCert KeyLocker serve two completely different trust ecosystems and are NOT interchangeable:**

| Capability / Feature | **OpenPGP / GPG** (`$0`) | **DigiCert KeyLocker** (`~$600–$996/yr`) |
| :--- | :--- | :--- |
| **Trust Model** | Decentralized Web-of-Trust / public key fingerprint published by your company | **Certificate Authority (CA) chain** pre-trusted by Microsoft Windows & OS vendors |
| **Maven Central / Java `.jar` `.asc` Signatures** | **Required & Standard** | **Not accepted** by Maven Central (Maven Central mandates `.asc` PGP signatures) |
| **Windows SmartScreen / Authenticode (`.exe`, `.msi`, `.dll`)** | **No** (Windows still blocks with *"Unknown Publisher"*) | **Yes** (Eliminates SmartScreen warnings & verifies corporate publisher identity) |
| **Cloud HSM Key Custody & Audit Logs (FIPS 140-2)** | **No** (Unless paired with Cloud KMS / YubiKey) | **Yes** (Private key never leaves DigiCert HSM; full enterprise audit trail) |
| **RFC 3161 Trusted Timestamping** | **No** | **Yes** (Signatures stay valid after certificate expiration) |
| **macOS Gatekeeper / Notarization** | **No** | **No** (macOS requires an **Apple Developer ID** certificate, `\$99/yr`) |
| **Containers & Supply-Chain Provenance (SLSA)** | Partial (prefer **Sigstore Cosign** / **GitHub Attestations**, `$0`) | Limited (enterprise X.509 only; container ecosystems standardize on Sigstore/OIDC) |

---

## 3. Drawbacks of GPG (and How to Mitigate Them for Free)

Using plain GPG in CI/CD has real operational limitations you should plan around:

1. **Software Key Exposure in CI Memory**:
   * Storing `GPG_PRIVATE_KEY` in GitHub Secrets means the key is decrypted in runner RAM during builds.
   * *Free Mitigation*: Keep your master GPG key offline, export only a **time-bounded signing subkey** (1–2 year expiry) to CI, and pair releases with **GitHub Artifact Attestations / Sigstore Cosign** (`$0`, keyless OIDC-backed hardware provenance).
2. **Manual Identity Verification**:
   * Anyone can create a GPG key labeled `"Company X"`. Consumers must verify your key fingerprint via your official website/HTTPS domain (`SECURITY.md` or keyserver).
3. **No OS Executable Trust**:
   * If you ever compile GraalVM native Windows `.exe` binaries or Node.js Windows installers, GPG signatures will **not** satisfy Windows Defender / SmartScreen.
4. **Key Rotation Overhead**:
   * Your team must manually rotate and redistribute public keys every 1–2 years.

---

## 4. Will DigiCert Be Useful for Other Products If Purchased?

It depends entirely on **what types of products** your enterprise builds:

### Where DigiCert KeyLocker IS Useful
* **Windows Desktop Software & Installers** (`.exe`, `.msi`, `.dll`, `.ps1` PowerShell scripts, NuGet `.nupkg`, Electron apps, Windows CLI binaries from **Node.js** or **GraalVM**).
* **Regulated Enterprise Contracts** where a customer explicitly requires **FIPS Cloud HSM–backed X.509 `jarsigner` signatures** inside JAR manifests (`META-INF/*.RSA` / `*.SF`).

### Where DigiCert KeyLocker Is NOT Useful
* **Spring Boot / Java libraries**: Maven Central and Gradle Plugin Portal still require GPG `.asc`, not DigiCert X.509.
* **Angular / npm packages**: npm uses registry ECDSA provenance signatures, not DigiCert.
* **K3s / Docker / Kubernetes workloads**: Container ecosystems use **Sigstore Cosign** / **GitHub Attestations** (`$0`).
* **Web Apps / REST APIs / Cloud Services**: Backend services are not Authenticode-signed (server TLS uses standard HTTPS/TLS certs such as Let's Encrypt or internal PKI, which are separate from Code Signing certificates).

---

## 5. Strategic Recommendation

1. **Today (Spring Boot / Java / Containers / Web)**: Use **GPG (with an offline master key + CI subkey)** + **GitHub Artifact Attestations / Sigstore Cosign** (`$0`).
2. **In the Future (only if you ship Windows `.exe`/`.msi` installers)**:
   * Evaluate **Microsoft Azure Trusted Signing** first (**~\$9.99/month = \$120/year** for basic tier) — it provides cloud HSM Authenticode signing and instant Windows SmartScreen trust at ~1/8th the price of DigiCert KeyLocker.
   * Choose **DigiCert KeyLocker** (`~\$600–\$996/yr`) only if you specifically need cross-vendor EV HSM compliance, custom Java `jarsigner` X.509 support, or already standardize on DigiCert enterprise PKI.
