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


class ApplicationResourceUpgradeProgressInfo(Model):
    """This type describes an application resource upgrade.

    :param name: Name of the Application resource.
    :type name: str
    :param target_application_type_version: The target application version for
     the application upgrade.
    :type target_application_type_version: str
    :param start_timestamp_utc: The estimated UTC datetime when the upgrade
     started.
    :type start_timestamp_utc: str
    :param upgrade_state: The state of the application resource upgrade.
     Possible values include: 'Invalid', 'ProvisioningTarget',
     'RollingForward', 'UnprovisioningCurrent', 'CompletedRollforward',
     'RollingBack', 'UnprovisioningTarget', 'CompletedRollback', 'Failed'
    :type upgrade_state: str or
     ~azure.servicefabric.models.ApplicationResourceUpgradeState
    :param percent_completed: The estimated percent of replicas are completed
     in the upgrade.
    :type percent_completed: str
    :param service_upgrade_progress: List of service upgrade progresses.
    :type service_upgrade_progress:
     list[~azure.servicefabric.models.ServiceUpgradeProgress]
    :param rolling_upgrade_mode: The mode used to monitor health during a
     rolling upgrade. The values are UnmonitoredAuto, UnmonitoredManual, and
     Monitored. Possible values include: 'Invalid', 'UnmonitoredAuto',
     'UnmonitoredManual', 'Monitored'. Default value: "Monitored" .
    :type rolling_upgrade_mode: str or
     ~azure.servicefabric.models.RollingUpgradeMode
    :param upgrade_duration: The estimated amount of time that the overall
     upgrade elapsed. It is first interpreted as a string representing an ISO
     8601 duration. If that fails, then it is interpreted as a number
     representing the total number of milliseconds. Default value: "PT0H2M0S" .
    :type upgrade_duration: str
    :param application_upgrade_status_details: Additional detailed information
     about the status of the pending upgrade.
    :type application_upgrade_status_details: str
    :param upgrade_replica_set_check_timeout_in_seconds: The maximum amount of
     time to block processing of an upgrade domain and prevent loss of
     availability when there are unexpected issues. When this timeout expires,
     processing of the upgrade domain will proceed regardless of availability
     loss issues. The timeout is reset at the start of each upgrade domain.
     Valid values are between 0 and 42949672925 inclusive. (unsigned 32-bit
     integer). Default value: 42949672925 .
    :type upgrade_replica_set_check_timeout_in_seconds: long
    :param failure_timestamp_utc: The estimated UTC datetime when the upgrade
     failed and FailureAction was executed.
    :type failure_timestamp_utc: str
    """

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'target_application_type_version': {'key': 'TargetApplicationTypeVersion', 'type': 'str'},
        'start_timestamp_utc': {'key': 'StartTimestampUtc', 'type': 'str'},
        'upgrade_state': {'key': 'UpgradeState', 'type': 'str'},
        'percent_completed': {'key': 'PercentCompleted', 'type': 'str'},
        'service_upgrade_progress': {'key': 'ServiceUpgradeProgress', 'type': '[ServiceUpgradeProgress]'},
        'rolling_upgrade_mode': {'key': 'RollingUpgradeMode', 'type': 'str'},
        'upgrade_duration': {'key': 'UpgradeDuration', 'type': 'str'},
        'application_upgrade_status_details': {'key': 'ApplicationUpgradeStatusDetails', 'type': 'str'},
        'upgrade_replica_set_check_timeout_in_seconds': {'key': 'UpgradeReplicaSetCheckTimeoutInSeconds', 'type': 'long'},
        'failure_timestamp_utc': {'key': 'FailureTimestampUtc', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, target_application_type_version: str=None, start_timestamp_utc: str=None, upgrade_state=None, percent_completed: str=None, service_upgrade_progress=None, rolling_upgrade_mode="Monitored", upgrade_duration: str="PT0H2M0S", application_upgrade_status_details: str=None, upgrade_replica_set_check_timeout_in_seconds: int=42949672925, failure_timestamp_utc: str=None, **kwargs) -> None:
        super(ApplicationResourceUpgradeProgressInfo, self).__init__(**kwargs)
        self.name = name
        self.target_application_type_version = target_application_type_version
        self.start_timestamp_utc = start_timestamp_utc
        self.upgrade_state = upgrade_state
        self.percent_completed = percent_completed
        self.service_upgrade_progress = service_upgrade_progress
        self.rolling_upgrade_mode = rolling_upgrade_mode
        self.upgrade_duration = upgrade_duration
        self.application_upgrade_status_details = application_upgrade_status_details
        self.upgrade_replica_set_check_timeout_in_seconds = upgrade_replica_set_check_timeout_in_seconds
        self.failure_timestamp_utc = failure_timestamp_utc
