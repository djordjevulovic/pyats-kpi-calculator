# pyats-kpi-calculator

PyATS Offline KPI Calculator — Extract KPIs from captured
NX-OS, IOS-XE and IOS-XR show command outputs.

## Installation

```bash
poetry install
```

## Usage

```bash
poetry run kpi-calculator --router core-sw-01 --os nxos
poetry run kpi-calculator --router edge-rtr-02 --os iosxe
poetry run kpi-calculator --router pe-router-01 --os iosxr
```

## Input File Convention

```
<router_name>__<show_command>.txt

Examples:
  core-sw-01__show_ip_route_summary.txt
  core-sw-01__show_bgp_summary.txt
  pe-router-01__show_route_summary.txt
```

## Adding New KPIs

Edit kpi_models.yaml only — no Python changes needed.

## License
MIT
