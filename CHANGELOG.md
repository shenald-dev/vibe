# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Unit tests for the CLI `create` command.
- **[Fixed / Optimized]:** Replaced `.stdout` with `.output` in test assertions for accuracy.
- **[Added]:** Added missing edge-case unit test to verify that rich markup injection in user input is safely escaped.

### Pruned
- Removed orphaned `__init__.py` file from the project root.