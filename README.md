<!-- chptr-fleet-managed:start -->
## Managed Chapter Publishing baseline

This repository is part of the Chapter Publishing `.github` boundary. The managed baseline adds:

- deterministic zed-pkg lifecycle gates in `.zed/`;
- private per-user/per-session ores-otel envelopes suitable for Supabase Realtime ingestion;
- a repository-local quality gate that rejects empty managed files, stale generated artifacts, invalid JSON, and credential-shaped values;
- architecture and provenance documents derived from a live inventory of twenty sibling organizations;
- test-only fixtures and failure-oriented validation; production data is never required.

Run `python3 scripts/chptr_quality.py` before publishing. The source of dependency truth is `.zpkg.toml`; native package manifests are projections.
<!-- chptr-fleet-managed:end -->
