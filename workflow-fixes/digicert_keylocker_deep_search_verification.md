# Deep Search Verification: DigiCert KeyLocker Cloud HSM EV Code Signing v2 in Spring Boot

**Component**: `Spring Boot 4.1.2`  
**Reference Upstream Commit**: `2904c4c0c49`  
**Date**: 2026-11-12  

---

## 1. Conclusion

**No — the Spring Boot project does NOT use DigiCert KeyLocker (or any Cloud HSM EV code-signing service).**

A repository-wide search across both upstream commit `2904c4c0c49` and current `HEAD` (excluding the planning spreadsheets/docs generated under [`workflow-fixes/`](.)) confirms **zero usage** of DigiCert KeyLocker anywhere in the codebase, build scripts, or CI/CD workflows.

---

## 2. Deep Search Evidence

| Search Pattern | Scope Searched | Result in Codebase (`2904c4c0c49` & `HEAD`) |
| :--- | :--- | :--- |
| `digicert`, `keylocker`, `smctl`, `authenticode`, `notarize`, `cosign`, `sigstore` | Entire repo (`.github/`, `buildSrc/`, `cli/`, `build-plugin/`, `core/`, `build.gradle`) | **0 matches** — no workflows, scripts, secrets (`KEYLOCKER_TOKEN`), or Gradle plugins reference DigiCert or KeyLocker. |
| `CodeSigner` (`codesign`) | Java source tree (`loader/`) | **Only standard JDK API usage** in [`NestedJarFile.java`](../loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/jar/NestedJarFile.java#L589) and [`SecurityInfo.java`](../loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/jar/SecurityInfo.java#L17) (`java.security.CodeSigner`) for reading signatures from nested JAR entries at runtime. |
| `PKCS11` | Java source & tests (`core/`, `test-support/`) | **Only runtime SSL bundle configuration** in [`JksSslStoreBundle.java`](../core/spring-boot/src/main/java/org/springframework/boot/ssl/jks/JksSslStoreBundle.java#L112) allowing Spring Boot *user applications* to configure PKCS#11 SSL keystores. Not used to sign Spring Boot releases. |

---

## 3. What Spring Boot Actually Uses for Signing

1. **Snapshot / Artifact Deployment Signing ([`.github/workflows/build-and-deploy-snapshot.yml`](../.github/workflows/build-and-deploy-snapshot.yml#L31-L39))**:
   Spring Boot signs published Maven JARs/POMs using **standard PGP/GPG** via `spring-io/artifactory-deploy-action` with two GPG secrets:
   ```yaml
   signing-key: ${{ secrets.GPG_PRIVATE_KEY }}
   signing-passphrase: ${{ secrets.GPG_PASSPHRASE }}
   ```
2. **GA Release Publication ([`.github/workflows/publicize-release.yml`](../.github/workflows/publicize-release.yml))**:
   Uses **no code-signing service or KeyLocker** at all — it publishes already-staged artifacts to the Gradle Plugin Portal (`GRADLE_PLUGIN_PUBLISH_KEY` / `GRADLE_PLUGIN_PUBLISH_SECRET`), SDKMAN, Homebrew, and GitHub Releases.

---

## 4. Why `DigiCert KeyLocker ($996/yr)` Appeared in Earlier Spreadsheets

The `DigiCert KeyLocker` label and `$996/yr` estimate did **not** originate from Spring Boot’s code — it was introduced during earlier cost estimation in [`workflow-fixes/data1.xlsx`](data1.xlsx) (`master_list` Row 172) as an initial assumption for a generic `"code-signing service"`.

The review columns of `master_list` Row 172 in [`workflow-fixes/spring_boot_ml_entries.json`](spring_boot_ml_entries.json#L1001-L1003) already flagged that assumption as incorrect:
* **`Plan based on Review`**: `Tool Assumption Wrong or NA`
* **`Quaote Required?`**: `Not Applicable`
* **`Yearly Cost - Reviewed ($)`**: `$0`

---

## 5. Bottom-Line Takeaway

You do **not** need to purchase or integrate DigiCert KeyLocker for Spring Boot (`$0` cost; use standard free OpenPGP/GPG via `GPG_PRIVATE_KEY` and `GPG_PASSPHRASE` just like upstream).
