# ADR-0002 — Capability-driven adapters, not target-specific forks

Status: Proposed; Date: 2026-11-13.

## Decision
Backends implement explicit capabilities for audio I/O, clock domain, transport, DMA memory ownership, channel count, frame size, numeric format and hardware accelerators. Runtime contract validation happens before activation. Unsupported capabilities must return a typed error or an agreed safe fallback; no silent approximations.

ESP-IDF/FreeRTOS and esp-hal/Embassy are independent ESP adapters. STM32/embassy-stm32 is an optional later target, requiring board-specific qualification. Cross-core scheduling and cache/DMA coherence are target-specific. A single peripheral must have one owner per firmware configuration.

## Alternatives
No global feature flags that silently change DSP meaning; no hard dependency of kernels on one chip family. Validation goes from host oracle through device-specific gates. Acceptance is per target/capability pair.
