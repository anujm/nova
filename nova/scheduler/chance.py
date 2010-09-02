# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2010 Openstack, LLC.
# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Chance (Random) Scheduler implementation
"""

import random

from nova.scheduler import driver


class ChanceScheduler(driver.Scheduler):
    """
    Implements Scheduler as a random node selector
    """

    def pick_compute_host(self, context, instance_id, **_kwargs):
        """
        Picks a host that is up at random
        """

        hosts = self.hosts_up(context, 'compute')
        if not hosts:
            raise driver.NoValidHost("No hosts found")
        return hosts[int(random.random() * len(hosts))]

    def pick_volume_host(self, context, volume_id, **_kwargs):
        """
        Picks a host that is up at random
        """

        hosts = self.hosts_up(context, 'volume')
        if not hosts:
            raise driver.NoValidHost("No hosts found")
        return hosts[int(random.random() * len(hosts))]

    def pick_network_host(self, context, network_id, **_kwargs):
        """
        Picks a host that is up at random
        """

        hosts = self.hosts_up(context, 'network')
        if not hosts:
            raise driver.NoValidHost("No hosts found")
        return hosts[int(random.random() * len(hosts))]
