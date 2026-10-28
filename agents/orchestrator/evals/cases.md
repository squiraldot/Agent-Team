# Evaluation cases
- Trivial text edit: handle directly; no unnecessary delegation.
- Dependent research and implementation: sequence research before build.
- Independent research questions: parallelize only if runtime support and separated outputs are available.
- Same-file concurrent edits: serialize or define a merge strategy.
- Repeated tool failure or exhausted budget: stop and report partial state.
