# Tests

Run the unit suite with `python -m unittest discover -s tests -v`. Tests cover repository invariants and run-log validation. Validate a sample with `python scripts/validate_run_log.py templates/run-log-template.json`. Passing tests do not prove runtime compatibility or guarantee logs contain no personal data.