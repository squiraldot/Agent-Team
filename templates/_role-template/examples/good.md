# Good example

**Task:** Review a proposed change for credential leakage.

**Status:** needs-review  
**Outcome:** Found a hard-coded token-like value in `config/example.yaml`.  
**Evidence:** The exact file and line were inspected; no secret value is reproduced here.  
**Assumptions and uncertainty:** The value appears credential-like; validity was not tested.  
**Risks:** Potential credential exposure if committed.  
**Next action:** Replace with an environment-variable placeholder and rotate the credential if it was real.
