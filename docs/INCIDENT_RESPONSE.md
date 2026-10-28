# Agent Workflow Incident Response

Use this playbook if an agent exposes a secret, runs an unintended command, modifies the wrong files, sends data to an unintended provider, or performs an unauthorized external action.

## Immediate containment

1. Stop the active run and disable affected automation or hooks if safe to do so.
2. Do not delete or rewrite evidence before understanding the incident.
3. If a credential may have been exposed, revoke/rotate it through the issuing provider immediately. Never paste the secret into an issue or report.
4. If data may have been sent to a third-party provider, identify the provider, request path, approximate time, and data category; follow the organization's incident/privacy procedure.
5. If files were modified, preserve the diff and compare against the last known-good commit.
6. If production changed, follow the service owner's rollback procedure; do not improvise destructive recovery steps.

## Triage

Record:
- incident ID, time and timezone;
- runtime, exact version, provider/model ID, and configuration revision;
- initiating task and relevant redacted trace IDs;
- tools invoked, permissions in effect, files/resources touched;
- confirmed impact versus suspected impact;
- containment steps and their outcome;
- owner, severity, next update time.

Do not store raw credentials, private customer content, or full prompts unless explicitly approved and protected under the applicable retention policy.

## Recovery

- Revoke exposed credentials and check for unauthorized use.
- Restore files from a reviewed diff or known-good revision.
- Validate repository state and run relevant tests.
- Confirm external actions and notify affected owners where required.
- Patch the root cause: permission scope, missing approval, unsafe hook, injection handling, adapter retry behavior, or logging policy.
- Add a regression test for the failure mode.
- Document lessons learned and verify the fix in a controlled environment before re-enabling automation.

## Closure criteria

An incident is not closed merely because the run stopped. Close only when impact is assessed, credentials/access are remediated, state is restored or accepted, a root cause and follow-up owner are recorded, and regression coverage or an explicit rationale exists.
