---
name: disable
runner_type: python-script
description: Enable monitoring on a node
enabled: true
entry_point: run.py
parameters:
  action:
    type: string
    immutable: true
    default: ex_disable
  region:
    type: string
    description: The region code
    default: dd-na
  node_id:
    type: string
    description: The ID of the node (VM)
