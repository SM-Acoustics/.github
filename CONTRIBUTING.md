# Contributing to SM Acoustics

Work through scoped feature branches and pull requests; preserve original authorship, tagged baselines and existing behavior. State the user problem, affected products, prior implementations, compatibility concerns, test evidence and rollback.

Core principles:

1. Reuse existing contracts instead of copying a feature into each product.
2. Keep portable DSP independent of ESP-IDF, FreeRTOS, RTOS, HAL, browser, UI and host APIs.
3. Never allocate, block, sleep, perform network/file operations or format logs in a hard-real-time audio callback.
4. Treat Rust API, C ABI, serialization formats, parameter IDs, control events and preset formats as separately versioned compatibility surfaces.
5. Keep unsafe code and FFI isolated; document ownership, alignment, lifetime, data races and error semantics.
6. Attach reproducible test commands, exact target and evidence provenance.
7. Review licensing, security, safety and rights before moving code between repositories.
8. Hardware integration and production publication require explicit gates.

Start with [SM-ENG-001](standards/SM-ENG-001-ARCHITECTURE.md), [SM-ENG-002](standards/SM-ENG-002-REALTIME.md), [SM-ENG-004](standards/SM-ENG-004-EVIDENCE.md).

A contributor may propose an incompatible change but MUST document its migration. Reviewers should ask for evidence instead of assuming that generated documentation reflects the running software.
