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

from .partition_event_py3 import PartitionEvent


class PartitionReconfiguredEvent(PartitionEvent):
    """Partition Reconfiguration event.

    All required parameters must be populated in order to send to Azure.

    :param event_instance_id: Required. The identifier for the FabricEvent
     instance.
    :type event_instance_id: str
    :param category: The category of event.
    :type category: str
    :param time_stamp: Required. The time event was logged.
    :type time_stamp: datetime
    :param has_correlated_events: Shows there is existing related events
     available.
    :type has_correlated_events: bool
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param partition_id: Required. An internal ID used by Service Fabric to
     uniquely identify a partition. This is a randomly generated GUID when the
     service was created. The partition ID is unique and does not change for
     the lifetime of the service. If the same service was deleted and recreated
     the IDs of its partitions would be different.
    :type partition_id: str
    :param node_name: Required. The name of a Service Fabric node.
    :type node_name: str
    :param node_instance_id: Required. Id of Node instance.
    :type node_instance_id: str
    :param service_type: Required. Type of Service.
    :type service_type: str
    :param cc_epoch_data_loss_version: Required. CcEpochDataLoss version.
    :type cc_epoch_data_loss_version: long
    :param cc_epoch_config_version: Required. CcEpochConfig version.
    :type cc_epoch_config_version: long
    :param reconfig_type: Required. Type of reconfiguration.
    :type reconfig_type: str
    :param result: Required. Describes reconfiguration result.
    :type result: str
    :param phase0_duration_ms: Required. Duration of Phase0 in milli-seconds.
    :type phase0_duration_ms: float
    :param phase1_duration_ms: Required. Duration of Phase1 in milli-seconds.
    :type phase1_duration_ms: float
    :param phase2_duration_ms: Required. Duration of Phase2 in milli-seconds.
    :type phase2_duration_ms: float
    :param phase3_duration_ms: Required. Duration of Phase3 in milli-seconds.
    :type phase3_duration_ms: float
    :param phase4_duration_ms: Required. Duration of Phase4 in milli-seconds.
    :type phase4_duration_ms: float
    :param total_duration_ms: Required. Total duration in milli-seconds.
    :type total_duration_ms: float
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
        'partition_id': {'required': True},
        'node_name': {'required': True},
        'node_instance_id': {'required': True},
        'service_type': {'required': True},
        'cc_epoch_data_loss_version': {'required': True},
        'cc_epoch_config_version': {'required': True},
        'reconfig_type': {'required': True},
        'result': {'required': True},
        'phase0_duration_ms': {'required': True},
        'phase1_duration_ms': {'required': True},
        'phase2_duration_ms': {'required': True},
        'phase3_duration_ms': {'required': True},
        'phase4_duration_ms': {'required': True},
        'total_duration_ms': {'required': True},
    }

    _attribute_map = {
        'event_instance_id': {'key': 'EventInstanceId', 'type': 'str'},
        'category': {'key': 'Category', 'type': 'str'},
        'time_stamp': {'key': 'TimeStamp', 'type': 'iso-8601'},
        'has_correlated_events': {'key': 'HasCorrelatedEvents', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
        'node_name': {'key': 'NodeName', 'type': 'str'},
        'node_instance_id': {'key': 'NodeInstanceId', 'type': 'str'},
        'service_type': {'key': 'ServiceType', 'type': 'str'},
        'cc_epoch_data_loss_version': {'key': 'CcEpochDataLossVersion', 'type': 'long'},
        'cc_epoch_config_version': {'key': 'CcEpochConfigVersion', 'type': 'long'},
        'reconfig_type': {'key': 'ReconfigType', 'type': 'str'},
        'result': {'key': 'Result', 'type': 'str'},
        'phase0_duration_ms': {'key': 'Phase0DurationMs', 'type': 'float'},
        'phase1_duration_ms': {'key': 'Phase1DurationMs', 'type': 'float'},
        'phase2_duration_ms': {'key': 'Phase2DurationMs', 'type': 'float'},
        'phase3_duration_ms': {'key': 'Phase3DurationMs', 'type': 'float'},
        'phase4_duration_ms': {'key': 'Phase4DurationMs', 'type': 'float'},
        'total_duration_ms': {'key': 'TotalDurationMs', 'type': 'float'},
    }

    def __init__(self, *, event_instance_id: str, time_stamp, partition_id: str, node_name: str, node_instance_id: str, service_type: str, cc_epoch_data_loss_version: int, cc_epoch_config_version: int, reconfig_type: str, result: str, phase0_duration_ms: float, phase1_duration_ms: float, phase2_duration_ms: float, phase3_duration_ms: float, phase4_duration_ms: float, total_duration_ms: float, category: str=None, has_correlated_events: bool=None, **kwargs) -> None:
        super(PartitionReconfiguredEvent, self).__init__(event_instance_id=event_instance_id, category=category, time_stamp=time_stamp, has_correlated_events=has_correlated_events, partition_id=partition_id, **kwargs)
        self.node_name = node_name
        self.node_instance_id = node_instance_id
        self.service_type = service_type
        self.cc_epoch_data_loss_version = cc_epoch_data_loss_version
        self.cc_epoch_config_version = cc_epoch_config_version
        self.reconfig_type = reconfig_type
        self.result = result
        self.phase0_duration_ms = phase0_duration_ms
        self.phase1_duration_ms = phase1_duration_ms
        self.phase2_duration_ms = phase2_duration_ms
        self.phase3_duration_ms = phase3_duration_ms
        self.phase4_duration_ms = phase4_duration_ms
        self.total_duration_ms = total_duration_ms
        self.kind = 'PartitionReconfigured'
