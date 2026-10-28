# Compatibility and Version Policy

## The word "all"
"All models and all versions" cannot be guaranteed literally: providers add/remove model IDs, runtimes expose different tools, and old versions may lack features. Agent-Team aims for a portable shared policy and clear adapters, with compatibility verified per runtime/model combination.

## Compatibility tiers
- **Portable policy:** shared Markdown instructions and workflows.
- **Native integration:** runtime-specific agent/rule/skill files.
- **Provider API:** requires an adapter mapping API schemas, authentication, tools, and error handling.
- **Verified:** exact CLI version, provider, model ID, and required capabilities have been tested and recorded.

## Version guidance
- Keep shared instructions free of model IDs.
- Prefer runtime defaults for easy setup.
- Pin exact model IDs when reproducibility matters.
- Record runtime version, provider, model ID, test date, and test results for verified combinations.
- Re-check official documentation before upgrading or relying on a new model alias.
- Do not promise that future models will retain the same API or capabilities.

## Reporting
A compatibility report should list runtime/version, provider, exact model ID, instruction discovery, tool capabilities, agent execution, approval behavior, test command, date, and known gaps.
