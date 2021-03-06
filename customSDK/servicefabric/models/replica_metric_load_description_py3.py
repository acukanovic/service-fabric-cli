# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReplicaMetricLoadDescription(Model):
    """Specifies metric loads of a partition's specific secondary replica or
    instance.

    :param node_name: Node name of a specific secondary replica or instance.
    :type node_name: str
    :param replica_or_instance_load_entries: Loads of a different metrics for
     a partition's secondary replica or instance.
    :type replica_or_instance_load_entries:
     list[~azure.servicefabric.models.MetricLoadDescription]
    """

    _attribute_map = {
        'node_name': {'key': 'NodeName', 'type': 'str'},
        'replica_or_instance_load_entries': {'key': 'ReplicaOrInstanceLoadEntries', 'type': '[MetricLoadDescription]'},
    }

    def __init__(self, *, node_name: str=None, replica_or_instance_load_entries=None, **kwargs) -> None:
        super(ReplicaMetricLoadDescription, self).__init__(**kwargs)
        self.node_name = node_name
        self.replica_or_instance_load_entries = replica_or_instance_load_entries
