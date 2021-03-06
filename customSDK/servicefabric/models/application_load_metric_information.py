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


class ApplicationLoadMetricInformation(Model):
    """Describes load information for a custom resource balancing metric. This can
    be used to limit the total consumption of this metric by the services of
    this application.

    :param name: The name of the metric.
    :type name: str
    :param reservation_capacity: This is the capacity reserved in the cluster
     for the application.
     It's the product of NodeReservationCapacity and MinimumNodes.
     If set to zero, no capacity is reserved for this metric.
     When setting application capacity or when updating application capacity
     this value must be smaller than or equal to MaximumCapacity for each
     metric.
    :type reservation_capacity: long
    :param application_capacity: Total capacity for this metric in this
     application instance.
    :type application_capacity: long
    :param application_load: Current load for this metric in this application
     instance.
    :type application_load: long
    """

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'reservation_capacity': {'key': 'ReservationCapacity', 'type': 'long'},
        'application_capacity': {'key': 'ApplicationCapacity', 'type': 'long'},
        'application_load': {'key': 'ApplicationLoad', 'type': 'long'},
    }

    def __init__(self, **kwargs):
        super(ApplicationLoadMetricInformation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.reservation_capacity = kwargs.get('reservation_capacity', None)
        self.application_capacity = kwargs.get('application_capacity', None)
        self.application_load = kwargs.get('application_load', None)
