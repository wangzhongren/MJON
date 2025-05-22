# MJON · Minimal JSON for LLMs

> A lightweight, indentation-based data format for efficient communication with language models.

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

---

## ✨ What is MJON?

**MJON (Minimal JSON)** is a simplified data format designed to reduce verbosity and token overhead in LLM interactions. Inspired by YAML and JSON, it uses indentation and minimal syntax (`@key:`, `* item`) to represent structured data clearly and compactly.

MJON is **human-writable**, **LLM-friendly**, and ideal for **streaming responses**, **token-efficient generation**, and **structured data exchange** between humans and large language models.

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

