# SM-ENG-005 — Licensing, Security and Provenance

Status: Proposed v1.

Every third-party component requires origin, version/commit, SPDX identifier, modifications and permitted-use analysis. Public source is not necessarily permissively licensed. Distinguish institutional independent implementations from private research with proprietary synthesizer firmware, samples, ROMs or closed protocol binaries.

Licenses remain per repository and per rights holder. GPL-3.0-only and GPL-3.0-or-later are not identical grants; any proposed extraction, dual licensing or link to products with other license requirements needs explicit authorship/rightsholder and redistribution review. No automatic reassignment of copyright or retroactive license rewriting.

Baseline dependency checks SHOULD cover RustSec advisories, cargo-deny or equivalent license/advisory policy, secret scanning, reproducible locked dependencies and release SBOM. OpenSSF Scorecard can inform prioritization but never substitutes for a direct audit.

Restrict automation to minimum token permissions. No unreviewed publication, force-push, firmware flash, OTA, security-sensitive config change or destructive operation. Physical audio safety (amplifier output, transducer protection, gain fail-safe), DMA/cross-core memory ownership and OTA rollback require explicit threat and failure-mode analysis.
