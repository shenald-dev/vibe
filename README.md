<div align="center">
  <img src="assets/logo.png" alt="vibe Logo" width="250" />
  
  <br/>

  <h1>✨ vibe</h1>
  <p><b>Minimalist Project Scaffolding Engine</b></p>
  <i>Scaffold projects at the speed of thought. Zero-config, beautiful starter kits.</i>

  <br/>
  
  [![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
  [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
</div>

---

## 📑 Table of Contents
- [🌟 Overview](#-overview)
- [🚀 Enterprise Features](#-enterprise-features)
- [⚡ Quick Start Guide](#-quick-start-guide)
- [💻 Comprehensive Usage](#-comprehensive-usage)
- [🤝 Contributing](#-contributing)

---

## 🌟 Overview

**vibe** is a blazing-fast project scaffolding CLI tool built to safeguard your flow state. Stop spending hours wiring up complex configurations before you even start coding. Just run a single command, choose a beautiful template, and start building.

---

## 🚀 Enterprise Features

- **🎨 Beautiful TUI**: Built with `Typer` and `Rich` for a stunning visual experience directly in your terminal. No ugly text prompts.
- **⚡ Zero Config**: Generates projects with zero configuration needed. Eslint, Prettier, TypeScript, and Docker are automatically configured.
- **🚀 Instant Starters**: Generates full-stack `React`, `FastAPI`, or `Node` templates perfectly tuned for modern Vibe Coders.
- **🪶 Unopinionated Defaults**: Focuses entirely on lightweight, dependency-free architecture without pushing you into restrictive frameworks.

---

## ⚡ Quick Start Guide

### Installation

Install the CLI tool globally:
```bash
pip install vibe-cli
```

---

## 💻 Comprehensive Usage

### Scaffold a New Project

Provide your project name and let the engine scaffold everything for you:
```bash
vibe create my-new-project
```
*An interactive prompt will guide you through selecting your tech stack.*

### Use a Direct Template Flag
Bypass the interactive menu to scaffold instantly in CI/CD pipelines:
```bash
vibe create api-service --template fastapi
vibe create frontend-app --template react
```

---

## 🤝 Contributing
Want to add a new beautiful template or improve the TUI? We'd love your help! 💖
- 🐛 **Found a bug?** Open an issue to let us know.
- ✨ **Have a template idea?** We are open to PRs! Just make sure to run tests and keep the CLI vibrant.
- 🎨 **Documentation tweaks?** Always welcome!

---
> *Built by a Vibe Coder. Let the flow begin.*
