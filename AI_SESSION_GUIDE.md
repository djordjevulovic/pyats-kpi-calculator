# AI Session Guide — pyats-kpi-calculator

## Purpose

Paste this document into a new AI session to provide full
context for continuing development of pyats-kpi-calculator.

---

## Project Overview

pyats-kpi-calculator is a Python CLI tool that extracts KPIs
from offline Cisco device show command outputs using PyATS/Genie.

### Core Principles
- All files are exclusively AI-generated — no manual edits
- Changes applied via: python bootstrap_project.py
- ai-bootstrap library manages git commits and file writing
- KPI definitions live in kpi_models.yaml

---

## Tech Stack

```toml
python              = >=3.10,<4.0
pyats               = >=23.0
genie               = >=23.0
genie.libs.parser   = >=23.0
PyYAML              = >=6.0
schema              = >=0.7.5
```

---

## pyproject.toml — packages directive

Project uses single-file module structure.
packages directive is required in pyproject.toml:

```toml
packages = [{include = "kpi_calculator.py"}]
```

---

## Platform Requirements

PyATS is NOT supported on Windows.
Supported platforms: Linux, macOS, WSL2.
Recommended for Windows users: WSL2 + PyCharm WSL interpreter.

---

## Supported OS Types

nxos | iosxe | iosxr

---

## Supported Operations

sum | count | max | min | avg | sum_lengths

---

## KPI Model Structure

```yaml
<kpi_name>:
  description: <str>
  source:
    <os_type>:
      show_command:  <str>
      parser_module: <str>
      parser_class:  <str>
  iterate:   <str or list>
  value_key: <str>        # optional
  operation: <str>
  filter:                 # optional
    key:   <str>
    value: <str>
  default: 0
```

---

## File Naming Convention

<router_name>__<show_command_underscored>.txt
Example: core-sw-01__show_ip_route_summary.txt

---

## Bootstrap Workflow

```bash
python bootstrap_project.py
poetry install
poetry run pytest
git log --oneline
```

---

## Bootstrap File Rules

1.  Always include ALL files in FILES dict
2.  Always overwrite — never skip or protect
3.  Triple-quoted strings for .py .yaml .toml
4.  Concatenated strings for .md with code blocks
5.  Escape internal quotes as \"
6.  Escape backslashes as \\
7.  Escape newlines as \\n
8.  End with if __name__ == '__main__': entry point
9.  Use project_path='.'
10. Use forward slashes in FILES keys
11. Update feature_description each session

---

## Existing KPIs

total_routes         — sum of routes across all VRFs
max_routes_in_vrf    — max routes in a single VRF
total_vrfs           — count of VRFs
total_mac_addresses  — sum of MACs across all VLANs
total_bgp_neighbors  — count of BGP neighbors
total_bgp_routes_rib — sum of BGP prefixes received
total_bfd_sessions_up   — count of BFD sessions Up
total_bfd_sessions_down — count of BFD sessions Down

---

## Context Block for New AI Session

```
I am working on pyats-kpi-calculator.
All files are exclusively AI-generated.
Changes applied via: python bootstrap_project.py
We use ai-bootstrap library:
  Bootstrap(project_path='.').run(
      feature_description='<desc>', files=FILES)
Key files:
  kpi_calculator.py  — generic engine
  kpi_models.yaml    — KPI definitions
  bootstrap_project.py — master rebuild script
Supported OS: nxos, iosxe, iosxr
Operations: sum, count, max, min, avg, sum_lengths
File convention: <router>__<command>.txt
pyproject.toml requires: packages=[{include='kpi_calculator.py'}]
PyATS runs on Linux/macOS/WSL2 only — not native Windows
Please provide updated bootstrap_project.py with:
<DESCRIBE YOUR CHANGE HERE>
```

---

## Version History

| Version | Date       | Changes                                           |
|---------|------------|---------------------------------------------------|
| 0.1.0   | 2026-04-06 | Initial — engine, 8 KPIs, schema validation       |
| 0.1.1   | 2026-04-06 | Fix — add packages directive to pyproject.toml    |
