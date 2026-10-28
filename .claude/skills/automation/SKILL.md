---
name: safe-automation
description: Design bounded, observable automation with least privilege, failure handling, and human approval gates.
---
# Safe Automation
Prefer deterministic checks; make actions idempotent; use timeouts and bounded retries; log status but not secrets; add dry-run for destructive/external operations; require approval before publish/send/deploy/purchase/delete; handle partial failure; document permissions, dependencies, tests, and recovery. Never claim hooks or scripts provide a complete security sandbox.