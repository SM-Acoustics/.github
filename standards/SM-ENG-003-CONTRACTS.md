# SM-ENG-003 — Contract Registry, ABI and Compatibility

Status: Proposed v1.

## Compatibility surfaces

Version Rust public APIs, C ABI, over-the-wire control, saved presets, DAW automation IDs, telemetry schemas, MIDI mapping and DSP numeric semantics separately. A crate SemVer version does not itself define the ABI or protocol schema revision. Every shared contract identifies its authority, owner, version, consumer matrix and migration.

Rust crates follow Cargo SemVer compatibility guidelines; additive feature design is preferred. Public FFI must document repr, exact widths/size/alignment, pointer validity, ownership, lifetime, cross-thread safety, error codes and panic/unwind policy. Never equate an address-range preflight with proof that caller memory is valid.

Parameter IDs MUST be stable: never reuse retired IDs for new meanings. Define canonical unit, normalization, min/max, defaults, interpolation/smoothing, automation timestamps, channel scope and readback semantics. Generate TypeScript types and validation fixtures from the canonical schema; avoid untested hand-maintained duplicated JSON/TSX mappings.

Audio buffers declare planar/interleaved layout, frames/channels, numeric format (f32 or fixed-point Q31 etc), saturation/clipping/denormals, reset and latency. Cross-target tests MUST declare bit-exact requirements or justified numeric tolerance.

WASM binding generation MAY use wasm-bindgen/typed exports; WIT/Component Model MAY be evaluated later for component linking. Neither is mandatory for a browser UI. Version negotiation and feature/capability negotiation MUST fail closed on incompatible major versions.
