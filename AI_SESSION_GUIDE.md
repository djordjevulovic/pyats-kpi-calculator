# AI Session Guide -- pyats-kpi-calculator

## Purpose

Paste this document into a new AI session to provide full
context for continuing development of pyats-kpi-calculator.

---

## Project Overview

pyats-kpi-calculator is a Python CLI tool that extracts KPIs
from offline Cisco device show command outputs using PyATS/Genie.

### Core Principles
- All files are exclusively AI-generated -- no manual edits
- Changes applied via bootstrap_project.py
- ai-bootstrap >= 0.2.0 manages git commits, file writing
  and push to GitHub
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

## Platform Requirements

PyATS runs on Linux/macOS/WSL2 only -- not native Windows.
Ubuntu 24.04 LTS on WSL2 is the recommended dev environment.

---

## Genie Parser Notes

NX-OS parsers use output= not text= for offline parsing.
Engine tries PARSE_PARAMS = ['output', 'text'] in order.

Verified NX-OS parser locations:
  show ip route summary  -> show_routing.ShowIpRouteSummary
  show mac address-table -> show_fdb.ShowMacAddressTable
  show bgp summary       -> show_bgp.ShowBgpSummary

---

## Bootstrap Setup

ai-bootstrap installed in dedicated venv:
  python3.11 -m venv ~/.bootstrap-venv
  ~/.bootstrap-venv/bin/pip install ~/projects/ai-bootstrap

Run bootstrap:
  cd ~/projects/pyats-kpi-calculator
  ~/.bootstrap-venv/bin/python bootstrap_project.py

---

## CLI Arguments

  --router      Router name (required)
  --os          OS type: nxos | iosxe | iosxr (required)
  --kpis        Space-separated KPI names (optional, default: all)
  --list-kpis   List available KPIs and exit
  --input-dir   Input files directory (default: input_files)
  --models      KPI models YAML file (default: kpi_models.yaml)

---

## Input Files

Default location: input_files/ directory
Convention: <router_name>__<show_command_underscored>.txt
Example: input_files/LaMSC1DC01__show_ip_route_summary.txt

File encoding: utf-8 preferred.
Engine also handles cp1252 and latin-1 automatically.

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

## Existing KPIs

total_routes         -- sum of routes across all VRFs
max_routes_in_vrf    -- max routes in a single VRF
total_vrfs           -- count of VRFs
total_mac_addresses  -- sum of MACs across all VLANs
total_bgp_neighbors  -- count of BGP neighbors
total_bgp_routes_rib -- sum of BGP prefixes received
total_bfd_sessions_up   -- count of BFD sessions Up
total_bfd_sessions_down -- count of BFD sessions Down

---

## Bootstrap File Rules

1.  Always include ALL files in FILES dict
2.  Always overwrite -- never skip or protect
3.  Triple-quoted strings for .py .yaml .toml
4.  Concatenated strings for .md with code blocks
5.  Escape internal quotes as \"
6.  Escape backslashes as \\
7.  Escape newlines as \\n
8.  End with if __name__ == '__main__': entry point
9.  Use project_path='.'
10. Use forward slashes in FILES keys
11. Update feature_description each session
12. Always include push=True, remote='origin', branch='main'

---

## Context Block for New AI Session

```
I am working on pyats-kpi-calculator.
All files are exclusively AI-generated.
Changes applied via:
  ~/.bootstrap-venv/bin/python bootstrap_project.py
We use ai-bootstrap >= 0.2.0:
  Bootstrap(project_path='.').run(
      feature_description='<desc>',
      files=FILES,
      push=True,
      remote='origin',
      branch='main'
  )
Key files:
  kpi_calculator.py    -- generic engine
  kpi_models.yaml      -- KPI definitions
  bootstrap_project.py -- master rebuild script
Supported OS: nxos, iosxe, iosxr
Operations: sum, count, max, min, avg, sum_lengths
Input files: input_files/<router>__<command>.txt
Genie NX-OS: PARSE_PARAMS=['output','text']
             show_fdb.ShowMacAddressTable for MAC KPI
CLI args: --router --os --kpis --list-kpis
          --input-dir --models
pyproject.toml: packages=[{include='kpi_calculator.py'}]
PyATS: Linux/macOS/WSL2 only
Bootstrap venv: ~/.bootstrap-venv
GitHub remote: origin/main
Please provide updated bootstrap_project.py with:
<DESCRIBE YOUR CHANGE HERE>
```

---

## Version History

| Version | Date       | Changes                                           |
|---------|------------|---------------------------------------------------|
| 0.1.0   | 2026-04-06 | Initial -- engine, 8 KPIs, schema validation      |
| 0.1.1   | 2026-04-06 | Fix -- add packages directive to pyproject.toml   |
| 0.1.2   | 2026-04-06 | Fix -- add input_files/ dir to file path          |
| 0.1.3   | 2026-04-06 | Add -- push to GitHub via ai-bootstrap 0.2.0      |
| 0.1.4   | 2026-04-07 | Fix -- use output= param, add encoding handling   |
| 0.1.5   | 2026-04-07 | Add -- --kpis and --list-kpis CLI arguments       |
| 0.1.6   | 2026-04-07 | Fix -- MAC parser module show_fdb not show_l2route|
