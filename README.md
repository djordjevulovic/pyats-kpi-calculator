# pyats-kpi-calculator

PyATS Offline KPI Calculator -- Extract KPIs from captured
NX-OS, IOS-XE and IOS-XR show command outputs.

## Installation

```bash
poetry install
```

## Usage

```bash
# Run all KPIs
poetry run kpi-calculator --router n7k --os nxos

# List available KPIs
poetry run kpi-calculator --router n7k --os nxos \
                          --list-kpis

# Run specific KPIs only
poetry run kpi-calculator --router n7k --os nxos \
                          --kpis total_routes total_vrfs

# IOS-XE example
poetry run kpi-calculator --router cat9k --os iosxe \
                          --kpis total_routes total_mac_addresses

# IOS-XR example
poetry run kpi-calculator --router asr9k --os iosxr \
                          --kpis total_routes total_bgp_neighbors

# Custom input directory
poetry run kpi-calculator --router n7k --os nxos \
                          --input-dir /path/to/files
```

## Input File Convention

```
<input_dir>/<router_name>__<show_command>.txt

Default input_dir: input_files/

NX-OS examples:
  input_files/n7k__show_ip_route_summary.txt
  input_files/n7k__show_mac_address-table.txt
  input_files/n7k__show_bgp_summary.txt

IOS-XE examples:
  input_files/cat9k__show_ip_route_summary.txt
  input_files/cat9k__show_mac_address-table.txt

IOS-XR examples:
  input_files/asr9k__show_route_summary.txt
  input_files/asr9k__show_bgp_summary.txt
```

## Adding New KPIs

Edit kpi_models.yaml only -- no Python changes needed.

## License
MIT
