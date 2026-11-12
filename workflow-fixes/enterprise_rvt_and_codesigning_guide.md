# Enterprise Usage & Subscription Guide: Broadcom RVT and Code-Signing Service (DigiCert KeyLocker)

**Component**: `Spring Boot 4.1.2`  
**Reference Upstream Commit**: `2904c4c0c49`  
**Related Assessment Files**: [`workflow-fixes/data1.xlsx`](data1.xlsx), [`workflow-fixes/verify.md`](verify.md), [`workflow-fixes/spring_boot_data1_assessment.md`](spring_boot_data1_assessment.md)

---

## Executive Summary

| Tool / Infrastructure | Upstream Reality (Commit `2904c4c0c49`) | Enterprise Fork Usage | Subscription to Purchase |
| :--- | :--- | :--- | :--- |
| **1. Broadcom RVT** (`spring-projects/spring-boot-release-verification`) | Private, proprietary Broadcom repository checked out in `verify.yml` (`ref: 'v0.0.15'`) | **Cannot clone upstream repo.** Replace with internal/native smoke & acceptance tests (`:smoke-test:*`, `:system-test:*`, `:integration-test:*`). | **None / Not sold standalone** (`$0` with native smoke suite; bundled only in Broadcom Tanzu Spring Enterprise at ~\$50k–\$200k+/yr). |
| **2. Code-Signing Service** (`DigiCert KeyLocker Cloud HSM EV v2`) | Not invoked in `publicize-release.yml`; upstream snapshot deployment signs via **GPG/PGP** (`GPG_PRIVATE_KEY`, `GPG_PASSPHRASE`). Flagged in `data1.xlsx` (`master_list` Row 172) as `Tool Assumption Wrong or NA` (`$0`). | Use **GnuPG (GPG)** `.asc` signatures + **GitHub Artifact Attestations / Sigstore Cosign** for Java/Maven & container releases. Only use KeyLocker if shipping Windows/macOS native executables or required by InfoSec. | **None (`$0`)** for Java/Maven/container releases. *(If Windows/macOS EV binary signing is mandated and no corporate PKI exists: DigiCert EV + KeyLocker ~\$600–\$996/yr, or Azure Trusted Signing ~\$120/yr).* |

---

## Part 1: Broadcom RVT (`Broadcom RVT upstream`)

### 1.1 What Is Broadcom RVT?
**Broadcom RVT (Release Verification Tests)** is Broadcom/VMware’s internal, **private, closed-source verification test repository** ([`spring-projects/spring-boot-release-verification`](https://github.com/spring-projects/spring-boot-release-verification)) used to validate Spring Boot snapshots, staged releases, and commercial builds before promotion.

**Verified Code Evidence (Upstream Commit `2904c4c0c49`)**:
* **Caller**: [`.github/workflows/build-and-deploy-snapshot.yml`](../.github/workflows/build-and-deploy-snapshot.yml#L67-L75) invokes reusable workflow [`.github/workflows/verify.yml`](../.github/workflows/verify.yml).
* **Execution Steps in `verify.yml` (Lines 40–81)**:
  1. Checks out the private repository `spring-projects/spring-boot-release-verification` (`ref: 'v0.0.15'`) using `secrets.token` (`GH_ACTIONS_REPO_TOKEN`).
  2. Sets up Java 17 and (for `!vars.COMMERCIAL`) **Homebrew** (`Homebrew/actions/setup-homebrew`).
  3. Executes `./gradlew spring-boot-release-verification-tests:test` with environment variables:
     * `RVT_RELEASE_TYPE`: `'commercial'` (when `vars.COMMERCIAL` is set) or `'oss'`
     * `RVT_STAGING`: `${{ inputs.staging }}`
     * `RVT_VERSION`: `${{ inputs.version }}`
     * Repository credentials (`RVT_OSS_REPOSITORY_*` / `RVT_COMMERCIAL_REPOSITORY_*`) to pull staged/snapshot artifacts from JFrog Artifactory (`repo.spring.io`) and test Maven/Gradle consumption and Homebrew CLI installation.

### 1.2 How Can I Use It in My Enterprise?

#### Direct Usage: Not Possible Without a Broadcom Contract
* External forks **cannot** clone or run `spring-projects/spring-boot-release-verification`.
* Without an internal Broadcom token (`GH_ACTIONS_REPO_TOKEN`) authorized on that private repository, `actions/checkout` fails immediately with an **HTTP 404 / authentication error**.

#### Recommended Enterprise Approach: Replace with Internal / Native Verification Tests
Because an enterprise Apache 2.0 fork publishes to its own artifact registry (e.g., GitHub Packages, Nexus, internal Artifactory, or Maven Central) rather than Broadcom’s `repo.spring.io` or Spring Homebrew tap, replace the upstream private RVT checkout with an **enterprise-owned verification suite** inside your fork:

1. **Use Spring Boot’s Built-In Open-Source Test Modules** (already included in the repository under Apache 2.0):
   * [`smoke-test/`](../smoke-test) (e.g., `:smoke-test:spring-boot-smoke-test-simple:test`) — verifies core Spring context, auto-configuration, and embedded server startup.
   * [`integration-test/`](../integration-test) and [`system-test/`](../system-test) — verify container, database, and build-plugin integrations.
2. **Verify Against Your Own Staged Artifacts**:
   * Point your verification job to your local deployment repository (`deployment-repository`) or internal registry to confirm that downstream consumers can resolve your fork’s POMs/JARs cleanly.
3. **Add Enterprise-Specific Compatibility Checks**:
   * Maintain 1–3 lightweight sample applications matching your target production stack (JDK version, Tomcat/Jetty/Netty, Spring Security, Actuator, PostgreSQL/Kafka) and execute them in `verify.yml` before tagging releases.

*(See [`workflow-fixes/verify.md`](verify.md) for the dual-mode native fallback design using `:smoke-test:spring-boot-smoke-test-simple:test`.)*

### 1.3 Which Subscription Do I Need to Purchase?
* **Standalone RVT Subscription**: **None exists.** Broadcom does **not** sell `spring-boot-release-verification` as a standalone product or GitHub add-on.
* **Commercial Bundle**: Access to Broadcom’s verified commercial artifacts and Broadcom-backed SLA verification is only available through an enterprise **Broadcom Tanzu Spring Enterprise** agreement (**~\$50,000 – \$200,000+ / year**, core-based vendor quote) via [https://tanzu.vmware.com/spring-enterprise](https://tanzu.vmware.com/spring-enterprise).
* **Recommended Enterprise Action**: **\$0 Purchase.** Replace RVT with your own fork-hosted smoke and acceptance tests unless your organization explicitly requires a Broadcom commercial support contract.

---

## Part 2: Code-Signing Service (`DigiCert KeyLocker Cloud HSM EV Code Signing v2`)

### 2.1 What Is This (`code-signing service` / DigiCert KeyLocker)?
**DigiCert KeyLocker** is DigiCert’s cloud-based Hardware Security Module (Cloud HSM) service for storing **X.509 EV/OV Code Signing Certificates** and signing binaries remotely via CI/CD APIs without exporting private keys to build runners. Under CA/Browser Forum requirements (effective June 2023), commercial Windows/macOS OV and EV code-signing private keys must be stored in FIPS-compliant hardware or Cloud HSMs such as KeyLocker.

**Important Code & Review Reality Check for Spring Boot 4.1.2**:
* In [`.github/workflows/publicize-release.yml`](../.github/workflows/publicize-release.yml) (upstream commit `2904c4c0c49`), Spring Boot does **not** call DigiCert KeyLocker.
* Upstream artifact signing occurs in [`.github/workflows/build-and-deploy-snapshot.yml`](../.github/workflows/build-and-deploy-snapshot.yml#L38-L39), which uses standard **GPG/PGP signing** via `secrets.GPG_PRIVATE_KEY` and `secrets.GPG_PASSPHRASE` (producing `.asc` signatures).
* In [`workflow-fixes/data1.xlsx`](data1.xlsx) (`master_list` Row 172), the reviewed assessment explicitly marks this entry as:
  * **`Plan based on Review`**: `Tool Assumption Wrong or NA`
  * **`Quote Required?`**: `Not Applicable`
  * **`Yearly Cost - Reviewed ($)`**: `$0`

### 2.2 How Can I Use It in My Enterprise?

Your enterprise signing approach depends on the **artifact types** distributed by your Spring Boot fork:

#### Option A: Standard Java / Maven / Container Distribution (Recommended — **\$0**)
Maven Central, GitHub Packages, Gradle, and Java tooling verify **PGP/GPG `.asc` signatures**—they do **not** use DigiCert X.509 EV code-signing certificates.
1. Generate an **Enterprise Release GPG Key Pair** owned by your organization.
2. Store `GPG_PRIVATE_KEY` and `GPG_PASSPHRASE` in **GitHub Actions Organization/Repository Secrets**.
3. Sign `.jar`, `.pom`, `.zip`, and `.tar.gz` artifacts during Gradle build/publish (`$0`, open source) and optionally attach **GitHub Artifact Attestations / Sigstore Cosign** (`$0`) for SLSA build provenance and container image signing.

#### Option B: Only If Distributing Windows/macOS Native Executables or Mandated by Corporate InfoSec
You only need an X.509 / Cloud HSM service such as DigiCert KeyLocker if:
1. You distribute custom **Windows `.exe`/`.msi` or macOS native CLI executables** (e.g., native GraalVM binaries or Windows installers) that must pass Windows SmartScreen or macOS Gatekeeper reputation checks; **or**
2. Corporate InfoSec policy strictly prohibits GPG keys and mandates X.509 Cloud HSM signing for all release binaries.

If Option B applies, check with your corporate Security/PKI team first—many enterprises already license a corporate DigiCert, Sectigo, Entrust, or cloud KMS (AWS KMS / Azure Key Vault / GCP Cloud HSM) signing service that can be reused at **\$0 incremental cost**.

### 2.3 Which Subscription Do I Need to Purchase?

| Scenario | Subscription to Purchase | Estimated Annual Cost | Licensing & Cost Notes |
| :--- | :--- | :--- | :--- |
| **Standard Spring Boot Java Fork** *(JARs, POMs, Starters, Docker images)* | **None (`$0`)** | **\$0 / year** | Use **GnuPG (GPG)** for `.asc` Maven/JAR signatures + **GitHub Artifact Attestations / Sigstore Cosign** (`$0`). Matches the `$0` reviewed cost in `master_list` Row 172. |
| **Corporate PKI Already Exists in Enterprise** | **None (`$0` incremental)** | **\$0 / year** | Reuse your company's existing DigiCert/KMS/HSM code-signing account via a CI service credential. |
| **New Windows/macOS EV Code Signing Required** *(No existing corporate PKI)* | **DigiCert EV Code Signing Certificate + KeyLocker** *(Cloud HSM)* | **~\$600 – \$996 / year** | Priced **per certificate + signing operations/HSM tier** (not per 5 human user seats); CI pipelines share KeyLocker API credentials. *(Lower-cost Windows-only option: **Microsoft Azure Trusted Signing** at ~\$9.99/mo = \$120/yr).* |

**Bottom Line**: For a Spring Boot 4.1.2 fork distributing Java/Maven artifacts and container images, **you do not need to purchase DigiCert KeyLocker (\$996/yr)**—use free **GPG signing**, matching upstream Spring Boot’s actual implementation.
