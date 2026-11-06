## 2026-11-06 — Terminal Injection Security Fix
- **Learning:** C1 control characters (codepoints 128-159) can be used to bypass simplistic terminal injection filters (that only check for C0 and DEL) and can execute terminal escape sequences (like clearing the screen).
- **Action:** Always ensure terminal injection sanitization logic checks for both C0 (< 32) and C1 (128-159) control characters as well as the DEL character (127).
