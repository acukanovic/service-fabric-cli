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

from .partition_scheme_description_py3 import PartitionSchemeDescription


class NamedPartitionSchemeDescription(PartitionSchemeDescription):
    """Describes the named partition scheme of the service.

    All required parameters must be populated in order to send to Azure.

    :param partition_scheme: Required. Constant filled by server.
    :type partition_scheme: str
    :param count: Required. The number of partitions.
    :type count: int
    :param names: Required. Array of size specified by the ‘Count’ parameter,
     for the names of the partitions.
    :type names: list[str]
    """

    _validation = {
        'partition_scheme': {'required': True},
        'count': {'required': True},
        'names': {'required': True},
    }

    _attribute_map = {
        'partition_scheme': {'key': 'PartitionScheme', 'type': 'str'},
        'count': {'key': 'Count', 'type': 'int'},
        'names': {'key': 'Names', 'type': '[str]'},
    }

    def __init__(self, *, count: int, names, **kwargs) -> None:
        super(NamedPartitionSchemeDescription, self).__init__(**kwargs)
        self.count = count
        self.names = names
        self.partition_scheme = 'Named'
