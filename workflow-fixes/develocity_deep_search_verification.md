# Deep Search Verification & Enterprise Guide: Develocity (`ge.spring.io`) in Spring Boot

**Component**: `Spring Boot 4.1.2`  
**Reference Upstream Commit**: `2904c4c0c49`  
**Vendor**: Gradle Inc. (<https://gradle.com/develocity>)  
**Date**: 2026-11-12  

---

## 1. What Is Develocity (`ge.spring.io`)?

**Develocity** (formerly **Gradle Enterprise**, developed by **Gradle Inc.**) is a commercial build acceleration and observability platform. It provides:
* **Remote Distributed Build Cache**: Shares compiled Gradle task outputs and test results across CI runners and developer machines.
* **Build Scans**: Deep build timelines, dependency graphs, console logs, and failure diagnostics hosted on a central server (`https://ge.spring.io`).
* **Test Retry & Predictive Test Selection**: Automatically retries flaky tests and selectively skips tests unaffected by recent code changes.

---

## 2. Does This Project Use It? (Deep Search Evidence)

**Yes — Develocity is genuinely integrated in Spring Boot’s build logic and upstream CI workflows (`2904c4c0c49` & `HEAD`), though `DEVELOCITY_ACCESS_KEY` is optional.**

| Component / File | Verified Code Evidence | What It Does |
| :--- | :--- | :--- |
| **[`settings.gradle`](../settings.gradle#L29)** | Line 29: `id "io.spring.develocity.conventions" version "0.0.25"`<br>Lines 38–47: `develocity { buildScan { ... } }` | Applies Spring’s Develocity conventions plugin targeting `ge.spring.io` and attaches `Toolchain version` metadata to build scans. |
| **[`buildSrc/build.gradle`](../buildSrc/build.gradle#L38)** | Line 38: `implementation("com.gradle:develocity-gradle-plugin:4.2.2")` | Pulls the Develocity Gradle plugin into Spring Boot’s build convention classes. |
| **[`JavaConventions.java`](../buildSrc/src/main/java/org/springframework/boot/build/JavaConventions.java#L216-L247)** | Lines 224–247: `DevelocityTestConfiguration`, `TestRetryConfiguration`, `PredictiveTestSelectionConfiguration` | Configures CI test retries (`maxRetries = isCi() ? 3 : 0`) and predictive test selection (when `ENABLE_PREDICTIVE_TEST_SELECTION=true`). |
| **[`prepare-gradle-build/action.yml`](../.github/actions/prepare-gradle-build/action.yml#L8-L55)** & **[`build/action.yml`](../.github/actions/build/action.yml#L16-L57)** | `develocity-access-key` (`required: false`) passed to `gradle/actions/setup-gradle@v6.4.0` (`cache-provider: basic`) | Authenticates CI builds to `ge.spring.io` when a key is supplied; **falls back gracefully** if omitted. |
| **Upstream Workflows (`2904c4c0c49`)** | • [`.github/workflows/build-and-deploy-snapshot.yml`](../.github/workflows/build-and-deploy-snapshot.yml#L27)<br>• [`.github/workflows/ci.yml`](../.github/workflows/ci.yml#L54)<br>• [`.github/workflows/run-system-tests.yml`](../.github/workflows/run-system-tests.yml#L31) | Passes `secrets.DEVELOCITY_ACCESS_KEY` to publish build scans and use Spring's remote cache. |
| **[`README.adoc`](../README.adoc#L1)** | Line 1: `"Revved up by Develocity"` badge | Links publicly to `https://ge.spring.io/scans`. |

**Critical Operational Note**: Builds do **not** fail without `DEVELOCITY_ACCESS_KEY`. Because [`gradle.properties`](../gradle.properties#L5) already enables `org.gradle.caching=true` and `setup-gradle` uses `cache-provider: basic`, builds still compile and cache locally in GitHub Actions without any Develocity server key.

---

## 3. How Can I Use It in My Enterprise?

* **Recommended for a 5-User Enterprise Fork (`$0` — Replace / Omit Key)**:
  1. **Leave `DEVELOCITY_ACCESS_KEY` unset** (external forks cannot write to Spring’s `ge.spring.io` anyway — only Spring committers have access keys).
  2. Rely on **Gradle Local Build Cache** (`org.gradle.caching=true`) + **GitHub Actions Cache** (`gradle/actions/setup-gradle@v6.4.0`, `cache-provider: basic`), which is already built into the repository workflows.
  3. *(Optional for clean isolation)* Override or remove `io.spring.develocity.conventions` in [`settings.gradle`](../settings.gradle#L29) so forked builds never attempt outbound build-scan telemetry to `ge.spring.io`.
* **Only If Your Enterprise Mandates Central Build Telemetry / Remote Caching**:
  * Deploy your own self-hosted **Develocity Server** (on-prem / cloud VM / Kubernetes) or license Develocity Cloud from Gradle Inc., configure `develocity { server = "https://develocity.yourcompany.com" }`, and supply your own organization `DEVELOCITY_ACCESS_KEY`.

---

## 4. Which Subscription Do I Need to Purchase?

* **Recommended Purchase for 5 Users**: **None (`$0`).**
  * In [`workflow-fixes/data1.xlsx`](data1.xlsx) (`master_list` Row 27 in [`spring_boot_ml_entries.json`](spring_boot_ml_entries.json#L189-L195)), the review already updated Develocity to **`Plan based on Review: Replace`** and **`Yearly Cost - Reviewed ($): 0`** (*"Changed 50000 to 0 (Not Required)"*).
* **If You Choose to License Develocity**:
  * Gradle Inc. does **not** offer a low-cost 5-seat self-serve Team tier for Develocity. It is sold strictly via **custom Enterprise annual quote** at <https://gradle.com/develocity> (enterprise minimums typically start around **~\$25,000 – \$50,000+/year**, making it economical primarily for large engineering organizations with 50–1,000+ developers).

---

## 5. Why Did This Appear in Your Table?

1. **Real Upstream Usage**: Unlike DigiCert KeyLocker, Develocity **genuinely appears** in Spring Boot’s upstream `settings.gradle`, `buildSrc/build.gradle`, `JavaConventions.java`, and CI workflows (`build-and-deploy-snapshot.yml`, `ci.yml`, `run-system-tests.yml`).
2. **Upstream Original Inventory**: Because your table tracks `Record Type = Upstream Original Tool`, it accurately lists `Develocity` as used by upstream `Spring Boot 4.1.2` along with its commercial vendor (`Gradle Inc.`) and enterprise quote requirement.
3. **Why You Don't Buy It**: In a 5-user open-source fork, the `Recommended Fork Alternate` row (matching `master_list` Row 27) replaces it with **Gradle Local Cache + GitHub Actions Cache (`$0`)**, since `ge.spring.io` is inaccessible and an enterprise Develocity contract is unnecessary.
