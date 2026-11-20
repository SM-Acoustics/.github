# ADR-0001 — Shared no_std Rust core with host-owned resources

Status: Proposed; Date: 2026-11-13.

## Context
Previously developed portable Rust kernels, a C++/ESP-IDF runtime and a Rust/React synthesizer already contain reusable components. Per-product rewrites would create incompatible numerical semantics, conflicting control IDs and duplicated validation.

## Decision
Create a single canonical home for each shared numeric/DSP/graph/control contract. Keep the portable Class-A core no_std, with caller-owned buffers and no HAL or UI dependency. Products and platform adapters are consumers. Existing project behavior and accepted ADRs remain in effect until explicitly migrated.

## Alternatives
A giant monorepo for all products risks license mixing, large build scope and loss of autonomy. Copying crates into each product causes drift. Mandatory ESP-IDF for all targets precludes native Rust. Select modular repositories, versioned dependencies and an optional integration workspace.

## Consequences
Migration requires ownership/license review, compatibility wrappers and conformance evidence. 'One source' does not guarantee identical binaries or zero adapter work. This document alone does not relicense or move any code.
