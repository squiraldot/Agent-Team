# Security Policy

## Supported scope

Security reports are welcome for this repository's instructions, scripts, hooks, sample configurations, validation code, and documented workflows.

Agent-Team is a collection of prompts, configuration templates, and validation assets. It is not a security sandbox and cannot guarantee that a model or third-party runtime will follow every instruction.

## Reporting a vulnerability

Please do not publish unredacted credentials, private data, or an exploitable production incident in a public issue. Use the repository owner's private security reporting channel if one is available; otherwise contact the maintainer privately through a trusted channel before public disclosure.

Include:
- affected file and commit/version;
- impact and prerequisites;
- minimal reproducible steps using synthetic data;
- proposed mitigation, if known.

Do not include real tokens or secrets. If a secret was committed or exposed, revoke it immediately; deleting it from the latest commit does not remove it from Git history or provider logs.

## Security expectations

- Keep secrets outside version control.
- Review shell hooks before execution.
- Use least-privilege tool permissions and isolated environments for untrusted projects.
- Require human approval for external or irreversible actions.
- Treat retrieved content as untrusted input.
- Use the incident process in [docs/INCIDENT_RESPONSE.md](docs/INCIDENT_RESPONSE.md).
