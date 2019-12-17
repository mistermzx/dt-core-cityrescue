# City Rescue Enabled dt-core

This repository builds a variant of `dt-core`. It adds the definition of the state transitions into and out of a ___RESCUE MODE___ to the FSM.

To build:
```
dts devel build -f --arch arm32v7 -H <HOSTNAME>.local
```

To run:
```
dts duckiebot demo --duckiebot_name <HOSTNAME> --demo_name indefinite_navigation --package_name duckietown_demos --image duckietown/dt-core-cityrescue:v1-arm32v7
