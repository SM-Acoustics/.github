# SM-ENG-002 — Audio Real-Time and Safety Contract

Status: Proposed v1. Existing accepted target-specific RT contracts remain authoritative.

Class A = audio I/O and DSP with hard block deadlines. Class B = bounded control/preparation/telemetry. Class C = UI, storage, networking management, OTA, parsing, graph compiling, coefficient design and AI.

In Class A: MUST NOT allocate/free, take blocking locks, sleep/await, perform network/filesystem I/O, serialize JSON, format logs, wait on another core/task or execute unbounded retries. Ownership of buffers MUST be explicit; DMA descriptors and cache operations must be reviewed and tested on each MCU revision. No heap allocation is permitted through an indirect dependency in the hot path.

Audio time is measured in sample frames; a host clock, wall clock or RTOS tick is not an authoritative audio timeline. State is prepared off-thread and adopted at an explicitly bounded block boundary with generation IDs. Live parameter modulation must have defined timestamp and smoothing semantics; continuously sounding notes cannot require note release for eligible controls unless product behavior explicitly says so.

Each target declares Fs, maximum block frames, physical deadline, measured WCET/ISR jitter, resource admission policy, memory classes, clock drift budget and fail-safe outputs. Average CPU usage and successful compilation are not hard-real-time proof.

On lost sync, overload, driver fault or invalid configuration, transitions MUST be bounded and safe (mute, bypass or last-known-good as specified). Independent testing must verify output safety. RT logging captures fixed counters or bounded snapshots for later consumption by Class B/C.
