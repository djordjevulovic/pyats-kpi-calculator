# pyats-kpi-calculator

PyATS Offline KPI Calculator -- Extract KPIs from captured
NX-OS, IOS-XE and IOS-XR show command outputs.

## Installation

```bash
poetry install
```

## Usage

```bash
# Run all KPIs (normal output)
poetry run kpi-calculator --router n7k --os nxos

# Minimal one-line output
poetry run kpi-calculator --router n7k --os nxos \
                          --verbosity 1

# Full verbose output
poetry run kpi-calculator --router n7k --os nxos \
                          --verbosity 3

# Silent with JSON output only
poetry run kpi-calculator --router n7k --os nxos \
                          --verbosity 0 \
                          --output-json results.json

# Specific KPIs + JSON output
poetry run kpi-calculator --router n7k --os nxos \
                          --kpis total_routes total_vrfs \
                          --output-json n7k_kpis.json

# List available KPIs
poetry run kpi-calculator --router n7k --os nxos \
                          --list-kpis
```

## Verbosity Levels

```
0 = silent   No console output
1 = minimal  One line per KPI: name + value
2 = normal   Condensed output (default)
3 = verbose  Full output with breakdown
```

## JSON Output Format

```json
{
  "router": "n7k",
  "os": "nxos",
  "timestamp": "2026-04-07T10:22:01",
  "kpis": {
    "total_routes": {
      "description": "Total number of IP routes",
      "value": 47,
      "status": "ok",
      "operation": "sum"
    }
  }
}
```

## Input File Convention

```
<input_dir>/<router_name>__<show_command>.txt

Default input_dir: input_files/

NX-OS examples (n7k):
  input_files/n7k__show_ip_route_summary.txt
  input_files/n7k__show_mac_address-table.txt

IOS-XE examples (cat9k):
  input_files/cat9k__show_ip_route_summary.txt

IOS-XR examples (asr9k):
  input_files/asr9k__show_route_summary.txt
```

## Adding New KPIs

Edit kpi_models.yaml only -- no Python changes needed.

## License
MIT
