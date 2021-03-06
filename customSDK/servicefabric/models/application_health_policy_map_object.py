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


class ApplicationHealthPolicyMapObject(Model):
    """Represents the map of application health policies for a ServiceFabric
    cluster upgrade.

    :param application_health_policy_map: Defines a map that contains specific
     application health policies for different applications.
     Each entry specifies as key the application name and as value an
     ApplicationHealthPolicy used to evaluate the application health.
     If an application is not specified in the map, the application health
     evaluation uses the ApplicationHealthPolicy found in its application
     manifest or the default application health policy (if no health policy is
     defined in the manifest).
     The map is empty by default.
    :type application_health_policy_map:
     list[~azure.servicefabric.models.ApplicationHealthPolicyMapItem]
    """

    _attribute_map = {
        'application_health_policy_map': {'key': 'ApplicationHealthPolicyMap', 'type': '[ApplicationHealthPolicyMapItem]'},
    }

    def __init__(self, **kwargs):
        super(ApplicationHealthPolicyMapObject, self).__init__(**kwargs)
        self.application_health_policy_map = kwargs.get('application_health_policy_map', None)
