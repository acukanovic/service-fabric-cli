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


class RepairTask(Model):
    """Represents a repair task, which includes information about what kind of
    repair was requested, what its progress is, and what its final result was.
    This type supports the Service Fabric platform; it is not meant to be used
    directly from your code.

    All required parameters must be populated in order to send to Azure.

    :param task_id: Required. The ID of the repair task.
    :type task_id: str
    :param version: The version of the repair task.
     When creating a new repair task, the version must be set to zero.  When
     updating a repair task,
     the version is used for optimistic concurrency checks.  If the version is
     set to zero, the update will not check for write conflicts.  If the
     version is set to a non-zero value, then the
     update will only succeed if the actual current version of the repair task
     matches this value.
    :type version: str
    :param description: A description of the purpose of the repair task, or
     other informational details.
     May be set when the repair task is created, and is immutable once set.
    :type description: str
    :param state: Required. The workflow state of the repair task. Valid
     initial states are Created, Claimed, and Preparing. Possible values
     include: 'Invalid', 'Created', 'Claimed', 'Preparing', 'Approved',
     'Executing', 'Restoring', 'Completed'
    :type state: str or ~azure.servicefabric.models.State
    :param flags: A bitwise-OR of the following values, which gives additional
     details about the status of the repair task.
     - 1 - Cancellation of the repair has been requested
     - 2 - Abort of the repair has been requested
     - 4 - Approval of the repair was forced via client request
    :type flags: int
    :param action: Required. The requested repair action. Must be specified
     when the repair task is created, and is immutable once set.
    :type action: str
    :param target: The target object determines what actions the system will
     take to prepare for the impact of the repair, prior to approving execution
     of the repair.
     May be set when the repair task is created, and is immutable once set.
    :type target: ~azure.servicefabric.models.RepairTargetDescriptionBase
    :param executor: The name of the repair executor. Must be specified in
     Claimed and later states, and is immutable once set.
    :type executor: str
    :param executor_data: A data string that the repair executor can use to
     store its internal state.
    :type executor_data: str
    :param impact: The impact object determines what actions the system will
     take to prepare for the impact of the repair, prior to approving execution
     of the repair.
     Impact must be specified by the repair executor when transitioning to the
     Preparing state, and is immutable once set.
    :type impact: ~azure.servicefabric.models.RepairImpactDescriptionBase
    :param result_status: A value describing the overall result of the repair
     task execution. Must be specified in the Restoring and later states, and
     is immutable once set. Possible values include: 'Invalid', 'Succeeded',
     'Cancelled', 'Interrupted', 'Failed', 'Pending'
    :type result_status: str or ~azure.servicefabric.models.ResultStatus
    :param result_code: A numeric value providing additional details about the
     result of the repair task execution.
     May be specified in the Restoring and later states, and is immutable once
     set.
    :type result_code: int
    :param result_details: A string providing additional details about the
     result of the repair task execution.
     May be specified in the Restoring and later states, and is immutable once
     set.
    :type result_details: str
    :param history: An object that contains timestamps of the repair task's
     state transitions.
     These timestamps are updated by the system, and cannot be directly
     modified.
    :type history: ~azure.servicefabric.models.RepairTaskHistory
    :param preparing_health_check_state: The workflow state of the health
     check when the repair task is in the Preparing state. Possible values
     include: 'NotStarted', 'InProgress', 'Succeeded', 'Skipped', 'TimedOut'
    :type preparing_health_check_state: str or
     ~azure.servicefabric.models.RepairTaskHealthCheckState
    :param restoring_health_check_state: The workflow state of the health
     check when the repair task is in the Restoring state. Possible values
     include: 'NotStarted', 'InProgress', 'Succeeded', 'Skipped', 'TimedOut'
    :type restoring_health_check_state: str or
     ~azure.servicefabric.models.RepairTaskHealthCheckState
    :param perform_preparing_health_check: A value to determine if health
     checks will be performed when the repair task enters the Preparing state.
    :type perform_preparing_health_check: bool
    :param perform_restoring_health_check: A value to determine if health
     checks will be performed when the repair task enters the Restoring state.
    :type perform_restoring_health_check: bool
    """

    _validation = {
        'task_id': {'required': True},
        'state': {'required': True},
        'action': {'required': True},
    }

    _attribute_map = {
        'task_id': {'key': 'TaskId', 'type': 'str'},
        'version': {'key': 'Version', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'state': {'key': 'State', 'type': 'str'},
        'flags': {'key': 'Flags', 'type': 'int'},
        'action': {'key': 'Action', 'type': 'str'},
        'target': {'key': 'Target', 'type': 'RepairTargetDescriptionBase'},
        'executor': {'key': 'Executor', 'type': 'str'},
        'executor_data': {'key': 'ExecutorData', 'type': 'str'},
        'impact': {'key': 'Impact', 'type': 'RepairImpactDescriptionBase'},
        'result_status': {'key': 'ResultStatus', 'type': 'str'},
        'result_code': {'key': 'ResultCode', 'type': 'int'},
        'result_details': {'key': 'ResultDetails', 'type': 'str'},
        'history': {'key': 'History', 'type': 'RepairTaskHistory'},
        'preparing_health_check_state': {'key': 'PreparingHealthCheckState', 'type': 'str'},
        'restoring_health_check_state': {'key': 'RestoringHealthCheckState', 'type': 'str'},
        'perform_preparing_health_check': {'key': 'PerformPreparingHealthCheck', 'type': 'bool'},
        'perform_restoring_health_check': {'key': 'PerformRestoringHealthCheck', 'type': 'bool'},
    }

    def __init__(self, *, task_id: str, state, action: str, version: str=None, description: str=None, flags: int=None, target=None, executor: str=None, executor_data: str=None, impact=None, result_status=None, result_code: int=None, result_details: str=None, history=None, preparing_health_check_state=None, restoring_health_check_state=None, perform_preparing_health_check: bool=None, perform_restoring_health_check: bool=None, **kwargs) -> None:
        super(RepairTask, self).__init__(**kwargs)
        self.task_id = task_id
        self.version = version
        self.description = description
        self.state = state
        self.flags = flags
        self.action = action
        self.target = target
        self.executor = executor
        self.executor_data = executor_data
        self.impact = impact
        self.result_status = result_status
        self.result_code = result_code
        self.result_details = result_details
        self.history = history
        self.preparing_health_check_state = preparing_health_check_state
        self.restoring_health_check_state = restoring_health_check_state
        self.perform_preparing_health_check = perform_preparing_health_check
        self.perform_restoring_health_check = perform_restoring_health_check