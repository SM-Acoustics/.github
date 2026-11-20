# SM-ENG-004 — Evidence, Gates and Release Qualification

Status: Proposed v1.

Claims: PROVEN = independently reproducible evidence; INFERRED = analysis without complete exercise; OPEN = unresolved. Provenance: HOST_ONLY, QEMU_VERIFIED, DEVICE_VERIFIED. Host simulation is not device qualification; an agent completion report is not evidence without inspectable artifacts.

Required evidence record: source commit, toolchain/lockfile, target triple, hardware board/revision, configuration, exact commands, numerical vectors, logs/counters, outputs with hashes, test date, limitations and independent reproduction.

Progressive gates:
- G0 baseline + repository/license inventory.
- G1 interface, schema and API contract checks.
- G2 numerical golden vectors, edge conditions and partition invariance.
- G3 host functional/RT-like stress and regression.
- G4 cross-compile/link tests for approved targets.
- G5 device-level clocks, I2S, DMA, Ethernet and error handling.
- G6 real-time WCET, interruptions, underruns, watchdog, thermal and stress.
- G7 interoperable network/audio hosts, external clocks and fault injection.
- G8 security, license, reproducibility, rollback and release signoff.

Omitted gates require recorded rationale; never label a target qualified from a build alone. A hard-real-time test must include representative competing loads and instrumented maxima, not mean CPU. Keep raw measurements and golden references alongside summarized results.

CI SHOULD run format, Clippy, unit/property tests, dependency/license checks and interface conformance. Hardware-in-loop and flash jobs MUST remain approval-controlled. CI is not authorized to publish, deploy or overwrite devices by default.
