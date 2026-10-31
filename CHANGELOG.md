# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- **[Added]:** Added missing edge-case unit tests to ensure exact empty strings and strings with only special whitespace characters (`\n`, `\t`) are robustly caught by the validation.
- **[Fixed]:** Synced README documentation to remove inaccurate mention of an interactive menu for template selection.
- **[Fixed]:** Safely strip trailing and leading whitespace from CLI inputs for project names to resolve output formatting issues.
- **[Added]:** Added missing edge-case unit test to ensure full coverage of option aliases (`-t`).
- Unit tests for the CLI `create` command.
- **[Fixed / Optimized]:** Replaced `.stdout` with `.output` in test assertions for accuracy.
- **[Added]:** Added missing edge-case unit test to verify that rich markup injection in user input is safely escaped.
- **[Added]:** Added missing edge-case unit test to verify that the CLI correctly handles omitted required name arguments.
- **[Added]:** Added edge-case unit tests to improve coverage by covering the `node` template and `--help` flag.
- **[Fixed]:** Fixed `F541` linting warning regarding an unnecessary `f` prefix string in `cli.py`.
- **[Fixed / Optimized]:** Fixed bug causing unnecessary simultaneous spinner re-renders in the `Progress` output of `cli.py`.
- **[Fixed / Optimized]:** Mocked `time.sleep` in the test suite to execute instantly, improving testing performance.

### Pruned
- **[Pruned]:** Removed orphaned `tests/__init__.py` file acting as dead code.
- Removed orphaned `__init__.py` file from the project root.
- **[Pruned / Optimized]:** Fixed dead code unused variable in test fixtures (using `_` instead of `x`).
- **[Fixed]:** Synced README documentation to accurately reflect existing CLI behavior (removed incorrect mentions of interactive prompt).
- **[Fixed]:** Synced README documentation to accurately reflect existing CLI behavior (removed `create` subcommand references).