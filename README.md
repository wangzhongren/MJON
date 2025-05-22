# MJON · Minimal JSON for LLMs

> A lightweight, indentation-based data format for efficient communication with language models.

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

---

### Why MJON?

- **Line-by-line parsing:** MJON’s indentation and prefix-based syntax allows it to be parsed incrementally line-by-line, making it ideal for streaming large or partial data inputs.
- **Contrast with JSON:** Standard JSON requires the entire text to be loaded and parsed as a whole, which limits real-time processing and streaming use cases.
- **Token efficiency:** By removing braces, quotes, and commas, MJON reduces token consumption when used with LLMs.
- **Human and machine friendly:** Easy to read and write manually, yet structured enough for programmatic manipulation.

---

## Features

- Supports nested objects and arrays  
- Minimal syntax to save token costs  
- Easy to read and write by humans and models  
- Suitable for streaming and incremental generation  
- Converts seamlessly to and from standard JSON

---

## Example MJON

```mjon
@user:
  @name: Alice
  @roles:
    * admin
    * editor
@log:
  *
    @time: 2024-05-22
    @action: login
  *
    @time: 2024-05-23
    @action: edit_profile

