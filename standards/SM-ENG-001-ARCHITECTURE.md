# SM-ENG-001 — Portable Audio Architecture

Status: Proposed v1 (2026-11-13). Principle: **Write Core Once, Adapt Everywhere**.

## Dependency rule and ownership

L0 numeric primitives and arithmetic semantics.
L1 DSP algorithms, oscillators, filters, convolution, delays and meters.
L2 control/event/parameter/state schemas and off-callback graph planning.
L3 bounded runtime, graph executor, state activation and RT telemetry.
L4 independent transport and clock contracts (audio buffers, RTP/AES67, MIDI).
L5 platform/host adapters (esp-hal, ESP-IDF, STM32, desktop, Android, plugins, WASM).
L6 products (instruments, loudspeaker DSP, mixing console, spatial audio) and frontends.

Dependencies MUST point from product/adapter toward shared contracts and kernels, never from shared algorithms toward UI, OS, HAL or product. Each shared feature MUST have one authoritative owner and explicit consumers; copy/paste reuse is not architectural reuse.

## Portability and capabilities

Portable crates SHOULD target no_std + core by default; optional alloc/std must be explicit and additive, with no transitive heap activity in Class-A processing. Separate CPU/GPU/FPGA acceleration from algorithm semantics. Backends advertise supported sample rates, channels, numeric types, memory, block size, clocks, buses and transports; unsupported capabilities MUST fail closed or select a documented safe fallback.

Source compatibility does not imply binary compatibility or identical clock/peripheral resources. Platform code is expected at L5, limited to device-specific adaptation.

## Frontend contract

React/TSX, web/WASM, desktop, mobile and physical controllers consume the same typed parameter/event schema. DSP state lives in the audio runtime, not React. UI reads snapshots and enqueues bounded timestamped commands. IDs/units/ranges/defaults and smoothing semantics are canonical and generated where practical. No UI action may block the RT callback.

## Repository reuse

Before extraction, audit author rights, SPDX obligations, public API, test vectors and regressions. Keep existing source tags and compatibility wrappers until conformance is demonstrated; never automatically relicence GPL code.

References: Rust API Guidelines; Cargo SemVer Compatibility; WebAssembly Component Model for future optional host interfaces.
