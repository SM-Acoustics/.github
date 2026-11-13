# SM-GOV-001 — Engineering governance

**Status:** Proposed v1, 2026-11-13. Prospective policy, not a retroactive override of accepted project ADRs.

## Authority and decisions

For what a product SHALL do: approved requirements and accepted ADRs outweigh accidental implementation behavior. For what a product DOES: reproducible device evidence and independently verified tests outrank source inspection and agent reports. Preserve contradictory evidence rather than silently changing requirements.

Project maintainers own their release, contributor permissions, compatibility and licensing decisions. Cross-product contract changes require linked ADR, impact analysis, reviewed PR and migration path. No default branch, tag, binary, private repository, hardware device or production environment is changed automatically by a policy update.

## Evidence and provenance

Use PROVEN, INFERRED and OPEN for claims. Use HOST_ONLY, QEMU_VERIFIED and DEVICE_VERIFIED when relevant; record board revision, toolchain, commit, measurements and artifacts. Do not present a green CI build as proof of device qualification.

## Rules for agents

AI assistants may research, implement isolated changes and propose PRs. No agent report is proof without auditable commands and results. No force-push, destructive Git operations, unapproved deployment, hardware flashing, acquisition of credentials, publication of protected content or unexplained license change.

## Approval sequence

Issue or RFC -> compatibility/security/license assessment -> ADR if needed -> isolated branch -> conformance evidence -> maintainer review -> staged adoption -> release. ADR states: Proposed, Accepted, Superseded or Rejected; each records decision owner, alternatives, consequences, related contracts and rollback.

Capitalized MUST, SHOULD and MAY follow RFC 2119/RFC 8174. Existing project-specific rules take precedence until explicit adoption.
