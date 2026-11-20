# SM Acoustics platform adoption roadmap

Status: Proposed. No cross-product integration, runtime qualification, firmware flashing or automatic migration is claimed.

**P0 — Discover and preserve.** Inventory repositories/ADRs/licensing, capture hashes, map duplicated features, identify canonical owners and preserve project baselines.

**P1 — Contracts.** Agree on numeric layout, buffer ownership, parameter registry, event timing, state serialization, ABI and capability model; create generated TS bindings and conformance fixtures.

**P2 — Rust DSP reuse.** Extract a single proven primitive at a time from existing Rust kernels behind compatible product adapters, checking numerical vectors, memory and runtime budgets; keep legacy baselines.

**P3 — Host/backends.** Qualify native host, WASM, plugin, Android, ESP-IDF and esp-hal adapters individually. STM32 is deferred until there is a device. Do not assume AES67 readiness from UDP functionality.

**P4 — Interconnection.** Adopt versioned discovery/control and common preset/telemetry semantics, verify clock domains and RTP/PTP interoperability independently.

**P5 — Governance adoption.** Review ADRs and reconcile existing decisions through project-specific PRs; propose release and security controls, then enforce only the approved gates.

Prioritize a documentation-only adoption in the public PROPHET-XII repository and a private migration assessment for existing DSP repositories. Do not transfer them to the organization without explicit authorization.
