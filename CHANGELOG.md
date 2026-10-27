# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Unit tests for the CLI `create` command.
- **[Fixed / Optimized]:** Replaced `.stdout` with `.output` in test assertions for accuracy.
- **[Added]:** Added missing edge-case unit test to verify that rich markup injection in user input is safely escaped.
- **[Added]:** Added missing edge-case unit test to verify that the CLI correctly handles omitted required name arguments.
- **[Added]:** Added edge-case unit tests to improve coverage by covering the `node` template and `--help` flag.
- **[Fixed]:** Fixed `F541` linting warning regarding an unnecessary `f` prefix string in `cli.py`.
- **[Fixed / Optimized]:** Fixed bug causing unnecessary simultaneous spinner re-renders in the `Progress` output of `cli.py`.
- **[Fixed / Optimized]:** Mocked `time.sleep` in the test suite to execute instantly, improving testing performance.

### Pruned
- Removed orphaned `__init__.py` file from the project root.