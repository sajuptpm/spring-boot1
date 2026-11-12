# Spring Boot Apache 2.0 License Compliance Assessment for Company X Fork & Redistribution

**Reference Project**: `spring-projects/spring-boot`  
**Reference Upstream Commit**: `2904c4c0c49`  
**Applicable License**: Apache License, Version 2.0 (`Apache-2.0`)  
**Upstream License URL**: <https://github.com/spring-projects/spring-boot/blob/main/LICENSE.txt>  
**Upstream NOTICE Template URL**: <https://github.com/spring-projects/spring-boot/blob/main/buildSrc/src/main/resources/org/springframework/boot/build/legal/NOTICE.txt>  

---

## 1. Executive Conclusion

**Yes.** Company X can legally fork Spring Boot, apply bug fixes, patch vulnerabilities, build enhancements, release the distribution under Company X’s own name, redistribute source code and compiled binaries (commercially or non-commercially), and keep the code open-sourced.

The Spring Boot open-source repository is governed by the **Apache License, Version 2.0** (`Apache-2.0`), an OSI-approved permissive open-source license explicitly designed to allow commercial and open-source derivative works, provided attribution, change notice, and trademark rules are respected.

---

## 2. Master Legal Evidence Table

| Item / Action | Permissible for Company X? | License & Section | License File Location (Upstream URL) | Exact Verbatim Words in the License Allowing / Governing This | Mandatory Compliance Conditions & Additional Considerations |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **1. Fork the Project** | **YES** | **Apache 2.0**<br>§ 2 (*Grant of Copyright License*) | [`LICENSE.txt#L67-L73`](https://github.com/spring-projects/spring-boot/blob/main/LICENSE.txt#L67-L73) | *"Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form."* | Company X may create public or private forks. Must retain a copy of `LICENSE.txt` in the repository root and distributed artifacts. |
| **2. Bug Fixes & Vulnerability Fixes** | **YES** | **Apache 2.0**<br>§ 1 (*Derivative Works*) & § 2 | [`LICENSE.txt#L41-L47`](https://github.com/spring-projects/spring-boot/blob/main/LICENSE.txt#L41-L47) | *"'Derivative Works' shall mean any work, whether in Source or Object form, that is based on (or derived from) the Work and for which the editorial revisions, annotations, elaborations, or other modifications represent, as a whole, an original work of authorship."* | **Mandatory Notice (§ 4b)**: *"You must cause any modified files to carry prominent notices stating that You changed the files"* (e.g., in file headers and changelog/release notes). |
| **3. Feature Enhancements** | **YES** | **Apache 2.0**<br>§ 2 & § 4 (*Redistribution*, Para 2) | [`LICENSE.txt#L124-L130`](https://github.com/spring-projects/spring-boot/blob/main/LICENSE.txt#L124-L130) | *"You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License."* | Company X retains copyright over its newly authored code and enhancements and may add its copyright notice (e.g., `Copyright 2026 Company X Inc.`). |
| **4. Release in the Name of Company X (Branding)** | **YES**<br>*(Subject to Trademark Rules)* | **Apache 2.0**<br>§ 6 (*Trademarks*) & § 4(d) | [`LICENSE.txt#L139-L143`](https://github.com/spring-projects/spring-boot/blob/main/LICENSE.txt#L139-L143) | *"This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file."* | **Critical Requirement**: Company X **MUST** market and release the fork under its own product name/trademark (e.g., *CompanyX Boot*). Company X **cannot** name it "Spring Boot" or imply VMware/Broadcom sponsorship. Nominative attribution (e.g., *"Derived from Spring Boot"*) is permitted. |
| **5. Redistribute Binaries & Source Code** | **YES** | **Apache 2.0**<br>§ 3 & § 4 (*Redistribution*) | [`LICENSE.txt#L90-L122`](https://github.com/spring-projects/spring-boot/blob/main/LICENSE.txt#L90-L122) | *"You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions..."* | Must satisfy all 4 conditions in § 4: **(a)** deliver License copy; **(b)** add modification notices on edited files; **(c)** retain all upstream copyright/patent/trademark/attribution notices; **(d)** include readable `NOTICE` attributions. |
| **6. Keep Code Open-Sourced** | **YES** | **Apache 2.0**<br>§ 4 (*Redistribution*, Para 2) | [`LICENSE.txt#L124-L130`](https://github.com/spring-projects/spring-boot/blob/main/LICENSE.txt#L124-L130) | *"provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License."* | Company X may publish and maintain the fork as a public open-source project under Apache 2.0 (standard practice) or any compatible open-source license. |
| **7. Patent License Grant & Defensive Termination** | **PROTECTED** | **Apache 2.0**<br>§ 3 (*Grant of Patent License*) | [`LICENSE.txt#L74-L89`](https://github.com/spring-projects/spring-boot/blob/main/LICENSE.txt#L74-L89) | *"...each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work..."* | Grants Company X royalty-free patent rights to upstream contributions. **Termination trigger**: If Company X initiates patent litigation alleging that the Work infringes a patent, its patent license under § 3 terminates. |
| **8. Warranty Disclaimer & Liability Limits** | **PROTECTED** | **Apache 2.0**<br>§ 7 & § 8 | [`LICENSE.txt#L144-L165`](https://github.com/spring-projects/spring-boot/blob/main/LICENSE.txt#L144-L165) | *"Licensor provides the Work (and each Contributor provides its Contributions) on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND... In no event and under no legal theory... shall any Contributor be liable to You for damages..."* | Upstream authors/Broadcom bear zero warranty or legal liability for Company X's fork. Company X assumes responsibility for its own distribution. |
| **9. Commercial Support, SLAs & Paid Warranties** | **YES** | **Apache 2.0**<br>§ 9 (*Accepting Warranty or Additional Liability*) | [`LICENSE.txt#L166-L176`](https://github.com/spring-projects/spring-boot/blob/main/LICENSE.txt#L166-L176) | *"While redistributing the Work or Derivative Works thereof, You may choose to offer, and charge a fee for, acceptance of support, warranty, indemnity, or other liability obligations... However, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility... and only if You agree to indemnify, defend, and hold each Contributor harmless..."* | Company X may charge customers for enterprise support, extended maintenance, CVE backports, and SLAs, provided Company X indemnifies upstream contributors against claims tied to those commercial warranties. |
| **10. Exclusion of Upstream Proprietary Commercial Infra** | **EXCLUDED** | Separate Commercial Agreements *(Broadcom / Gradle Inc.)* | [`release-train-build.yml` (`2904c4c0c49`:L50-L52)](https://github.com/spring-projects/spring-boot/blob/2904c4c0c49/.github/workflows/release-train-build.yml#L50-L52) | *Commercial toggles (`vars.COMMERCIAL=true`), Tanzu repos (`spring-enterprise-maven-dev-local`), and private `spring-projects/spring-boot-release-verification` are NOT licensed under Apache 2.0.* | Company X **cannot** access or redistribute Broadcom Tanzu commercial feeds or proprietary RVT suites. The fork must disable `COMMERCIAL` mode and build purely from open-source Apache 2.0 code. |

---

## 3. Detailed Compliance Breakdown

### A. Forking, Bug Fixes, Vulnerability Patches, and Enhancements (§ 1 & § 2)
* Under **Section 2**, upstream contributors grant Company X a **perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license** to reproduce and prepare Derivative Works.
* Under **Section 1**, bug fixes, security CVE patches, and feature enhancements qualify as *Derivative Works*. No prior approval from VMware, Broadcom, or Pivotal is needed.

### B. Naming and Branding in Company X's Name (§ 6 Trademarks)
* **Permitted**:
  * Releasing under Company X's own product name and Maven coordinates (e.g., `com.companyx.boot:companyx-boot-starter`, *CompanyX Enterprise Boot*).
  * Including factual origin statements in documentation or README files (e.g., *"CompanyX Boot is an open-source distribution derived from Spring Boot®."*).
* **Prohibited**:
  * Using `"Spring"`, `"Spring Boot"`, `"VMware"`, `"Tanzu"`, `"Pivotal"`, or `"Broadcom"` as Company X's product brand name or logo in a way that causes consumer confusion or implies upstream endorsement.

### C. Mandatory Redistribution Conditions (§ 4)
Whenever Company X redistributes source code or compiled JARs/distributions, all four conditions of **Section 4** apply:

1. **§ 4(a) License Delivery**: Distribute a complete copy of [`LICENSE.txt`](LICENSE.txt) in the repository root and inside packaged artifacts (`META-INF/LICENSE.txt`).
2. **§ 4(b) Prominent Modification Notices**: Any source file modified by Company X must include a clear notice indicating that Company X modified it:
   ```java
   /*
    * Copyright 2012-2026 the original author or authors.
    * Modifications Copyright 2026 Company X Inc.
    *
    * Licensed under the Apache License, Version 2.0 (the "License");
    * ...
    * Modified by Company X: Security patch for CVE-2026-XXXX and custom enhancements.
    */
   ```
3. **§ 4(c) Notice Retention**: Preserve all existing upstream copyright, patent, trademark, and attribution notices in source files.
4. **§ 4(d) NOTICE File Preservation**: Retain the upstream attribution notice from [`buildSrc/src/main/resources/org/springframework/boot/build/legal/NOTICE.txt`](buildSrc/src/main/resources/org/springframework/boot/build/legal/NOTICE.txt) (`Copyright (c) 2012-2026 VMware, Inc.`) and append Company X’s notice if desired:
   ```text
   Spring Boot
   Copyright (c) 2012-2026 VMware, Inc.

   This product includes software developed by Company X Inc.
   Copyright 2026 Company X Inc.
   ```

### D. Additional Items Required for Legal & Engineering Governance
1. **Upstream Commercial Assets Exclusion**: Ensure CI/CD workflows run purely in open-source mode (`vars.COMMERCIAL` unset/false) and exclude private repositories (`spring-projects/spring-boot-release-verification`) and commercial feeds (`repo.spring.io` enterprise repos).
2. **Third-Party Transitive Dependencies**: Standard Spring Boot runtime dependencies use permissive or weak-copyleft licenses with classpath exceptions (Apache-2.0, MIT, BSD, EPL/CDDL). Company X should run automated license scanning (e.g., SBOM / FOSSA / CycloneDX) on every release to ensure no restricted third-party dependencies are introduced by new enhancements.
3. **Export Control & Cryptographic Notices**: If Company X redistributes binaries globally, review standard U.S. EAR / open-source cryptography notice procedures when packaging TLS/security libraries.

---

## 4. Company X Release Readiness Checklist

- [ ] **Fork Setup**: Host fork under Company X namespace (e.g., `company-x/companyx-boot`) keeping root `LICENSE.txt` intact.
- [ ] **Branding & Coordinates**: Update Maven `groupId` / `artifactId` and product branding to Company X trademarks; retain only nominative *"based on Spring Boot"* origin references.
- [ ] **NOTICE File**: Generate/include `NOTICE.txt` retaining `Copyright (c) 2012-2026 VMware, Inc.` and appending Company X attribution.
- [ ] **File-Level Change Notices**: Add prominent `"Modified by Company X"` notices to all modified source files (§ 4b).
- [ ] **Clean Open-Source Build Path**: Remove or disable upstream `vars.COMMERCIAL`, Develocity (`ge.spring.io`), Artifactory (`repo.spring.io`), and RVT dependencies per [`workflow-fixes/spring_boot_data1_assessment.md`](spring_boot_data1_assessment.md).
- [ ] **SBOM & Third-Party License Audit**: Generate an SBOM for each release to verify transitive dependency compliance.
