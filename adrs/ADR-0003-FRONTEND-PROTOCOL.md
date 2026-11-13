# ADR-0003 — Versioned UI-control and audio-runtime separation

Status: Proposed; Date: 2026-11-13.

## Decision
All UIs (React/TSX web, native, WASM wrappers, MIDI controllers) use the same canonical parameter/event protocol. Stable integer IDs, typed units/ranges, schema version, frame/sample timestamp policy, bounded event queues, smoothing, telemetry snapshots and error semantics are required.

The UI must not own Class-A state. React state controls intent and visualization; Rust audio runtime owns deterministic processing. Generate TypeScript definitions and validators from the authoritative contract when possible. Changes to automation IDs and saved presets require migration tests.

## Alternatives
Avoid direct JSON parsing in callbacks, independent hand-authored TS/Rust parameter tables and host-specific DSP copies. WIT is optional for future component interoperability; do not require it for ordinary WebAssembly exports.
