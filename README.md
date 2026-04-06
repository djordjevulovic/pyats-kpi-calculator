# pyats-kpi-calculator

PyATS Offline KPI Calculator — Extract KPIs from captured
NX-OS, IOS-XE and IOS-XR show command outputs.

## Installation

```bash
poetry install
```

## Usage

```bash
# Default input_files/ directory
poetry run kpi-calculator --router LaMSC1DC01 --os nxos

# Custom input directory
poetry run kpi-calculator --router LaMSC1DC01 --os nxos \
                          --input-dir /path/to/files
```

## Input File Convention

```
<input_dir>/<router_name>__<show_command>.txt

Default input_dir: input_files/

Examples:
  input_files/LaMSC1DC01__show_ip_route_summary.txt
  input_files/LaMSC1DC01__show_bgp_summary.txt
  input_files/pe-router-01__show_route_summary.txt
```

## Adding New KPIs

Edit kpi_models.yaml only — no Python changes needed.

## License
MIT
