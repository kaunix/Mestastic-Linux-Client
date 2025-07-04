# AGENT Instructions for Meshtastic Linux Client

## Required Checks
- Run `flake8` for style and syntax errors.
- Execute `bandit -r . -n 5` for basic security scanning.
- Validate markdown docs with `mdl README.md docs/README.md`.
- Build packaging artifacts using:
  - `fpm -s dir -t deb -n meshtastic-client -v 1.0 --prefix=/opt/meshtastic-linux-client .`
  - `fpm -s dir -t rpm -n meshtastic-client -v 1.0 --prefix=/opt/meshtastic-linux-client .`

## Pull Request Notes
Summarize significant changes and include the test results output. If package or test commands fail due to missing dependencies or network limits, mention that in the Testing section.
