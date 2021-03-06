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

from .fabric_event import FabricEvent


class PartitionEvent(FabricEvent):
    """Represents the base for all Partition Events.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: PartitionAnalysisEvent, PartitionNewHealthReportEvent,
    PartitionHealthReportExpiredEvent, PartitionReconfiguredEvent,
    ChaosPartitionSecondaryMoveScheduledEvent,
    ChaosPartitionPrimaryMoveScheduledEvent

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
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
        'partition_id': {'required': True},
    }

    _attribute_map = {
        'event_instance_id': {'key': 'EventInstanceId', 'type': 'str'},
        'category': {'key': 'Category', 'type': 'str'},
        'time_stamp': {'key': 'TimeStamp', 'type': 'iso-8601'},
        'has_correlated_events': {'key': 'HasCorrelatedEvents', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
    }

    _subtype_map = {
        'kind': {'PartitionAnalysisEvent': 'PartitionAnalysisEvent', 'PartitionNewHealthReport': 'PartitionNewHealthReportEvent', 'PartitionHealthReportExpired': 'PartitionHealthReportExpiredEvent', 'PartitionReconfigured': 'PartitionReconfiguredEvent', 'ChaosPartitionSecondaryMoveScheduled': 'ChaosPartitionSecondaryMoveScheduledEvent', 'ChaosPartitionPrimaryMoveScheduled': 'ChaosPartitionPrimaryMoveScheduledEvent'}
    }

    def __init__(self, **kwargs):
        super(PartitionEvent, self).__init__(**kwargs)
        self.partition_id = kwargs.get('partition_id', None)
        self.kind = 'PartitionEvent'
