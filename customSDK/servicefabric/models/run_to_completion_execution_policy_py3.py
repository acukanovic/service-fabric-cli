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

from .execution_policy_py3 import ExecutionPolicy


class RunToCompletionExecutionPolicy(ExecutionPolicy):
    """The run to completion execution policy, the service will perform its
    desired operation and complete successfully. If the service encounters
    failure, it will restarted based on restart policy specified. If the
    service completes its operation successfully, it will not be restarted
    again.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param restart: Required. Enumerates the restart policy for
     RunToCompletionExecutionPolicy. Possible values include: 'OnFailure',
     'Never'
    :type restart: str or ~azure.servicefabric.models.RestartPolicy
    """

    _validation = {
        'type': {'required': True},
        'restart': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'restart': {'key': 'restart', 'type': 'str'},
    }

    def __init__(self, *, restart, **kwargs) -> None:
        super(RunToCompletionExecutionPolicy, self).__init__(**kwargs)
        self.restart = restart
        self.type = 'RunToCompletion'
