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


class ContainerApiResponse(Model):
    """Response body that wraps container API result.

    :param container_api_result: Container API result.
    :type container_api_result: ~azure.servicefabric.models.ContainerApiResult
    """

    _validation = {
        'container_api_result': {'required': True},
    }

    _attribute_map = {
        'container_api_result': {'key': 'ContainerApiResult', 'type': 'ContainerApiResult'},
    }

    def __init__(self, container_api_result):
        self.container_api_result = container_api_result