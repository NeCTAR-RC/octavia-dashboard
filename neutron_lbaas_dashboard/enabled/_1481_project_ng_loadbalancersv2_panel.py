# Copyright 2015 IBM Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The slug of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'ngloadbalancersv2'
# The slug of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'project'
# The slug of the panel group the PANEL is associated with.
PANEL_GROUP = 'network'

# Python panel class of the PANEL to be added.
ADD_PANEL = (
    'neutron_lbaas_dashboard.dashboards.project.ngloadbalancersv2.panel'
    '.NGLoadBalancers')

ADD_INSTALLED_APPS = ['neutron_lbaas_dashboard']

ADD_ANGULAR_MODULES = ['horizon.dashboard.project.lbaasv2']

# AUTO_DISCOVER_STATIC_FILES = True

ADD_JS_FILES = [
    'app/core/openstack-service-api/lbaasv2.service.js',
    'dashboard/project/lbaasv2/lbaasv2.module.js',
    'dashboard/project/lbaasv2/loadbalancers/loadbalancers.module.js',
    'dashboard/project/lbaasv2/loadbalancers/table.controller.js',
    'dashboard/project/lbaasv2/loadbalancers/detail.controller.js',
    'dashboard/project/lbaasv2/loadbalancers/filters.js',
    'dashboard/project/lbaasv2/loadbalancers/actions/batch-actions.service.js',
    'dashboard/project/lbaasv2/loadbalancers/actions/row-actions.service.js',
    ('dashboard/project/lbaasv2/loadbalancers/actions/create/'
        'wizard.controller.js'),
    ('dashboard/project/lbaasv2/loadbalancers/actions/edit/'
        'wizard.controller.js'),
    'dashboard/project/lbaasv2/workflow/modal.service.js',
    'dashboard/project/lbaasv2/workflow/model.service.js',
    'dashboard/project/lbaasv2/workflow/workflow.service.js',
    ('dashboard/project/lbaasv2/workflow/loadbalancer/'
        'loadbalancer.controller.js'),
    'dashboard/project/lbaasv2/workflow/listener/listener.controller.js',
    'dashboard/project/lbaasv2/workflow/pool/pool.controller.js',
    'dashboard/project/lbaasv2/workflow/members/members.controller.js',
    'dashboard/project/lbaasv2/workflow/monitor/monitor.controller.js',
    'dashboard/project/lbaasv2/listeners/listeners.module.js',
    'dashboard/project/lbaasv2/listeners/table.controller.js',
    'dashboard/project/lbaasv2/listeners/detail.controller.js',
    'dashboard/project/lbaasv2/listeners/filters.js',
    'dashboard/project/lbaasv2/pools/pools.module.js',
    'dashboard/project/lbaasv2/pools/detail.controller.js',
    'dashboard/project/lbaasv2/members/members.module.js',
    'dashboard/project/lbaasv2/members/detail.controller.js',
    'dashboard/project/lbaasv2/members/table.controller.js'
]

ADD_JS_SPEC_FILES = [
    'app/core/openstack-service-api/lbaasv2.service.spec.js',
    'dashboard/project/lbaasv2/lbaasv2.module.spec.js',
    'dashboard/project/lbaasv2/loadbalancers/loadbalancers.module.spec.js',
    'dashboard/project/lbaasv2/loadbalancers/table.controller.spec.js',
    'dashboard/project/lbaasv2/loadbalancers/detail.controller.spec.js',
    'dashboard/project/lbaasv2/loadbalancers/filters.spec.js',
    ('dashboard/project/lbaasv2/loadbalancers/actions/'
        'batch-actions.service.spec.js'),
    ('dashboard/project/lbaasv2/loadbalancers/actions/'
        'row-actions.service.spec.js'),
    ('dashboard/project/lbaasv2/loadbalancers/actions/create/'
        'wizard.controller.spec.js'),
    ('dashboard/project/lbaasv2/loadbalancers/actions/edit/'
        'wizard.controller.spec.js'),
    'dashboard/project/lbaasv2/workflow/modal.service.spec.js',
    'dashboard/project/lbaasv2/workflow/model.service.spec.js',
    'dashboard/project/lbaasv2/workflow/workflow.service.spec.js',
    ('dashboard/project/lbaasv2/workflow/loadbalancer/'
        'loadbalancer.controller.spec.js'),
    'dashboard/project/lbaasv2/workflow/listener/listener.controller.spec.js',
    'dashboard/project/lbaasv2/workflow/pool/pool.controller.spec.js',
    'dashboard/project/lbaasv2/workflow/members/members.controller.spec.js',
    'dashboard/project/lbaasv2/workflow/monitor/monitor.controller.spec.js',
    'dashboard/project/lbaasv2/listeners/listeners.module.spec.js',
    'dashboard/project/lbaasv2/listeners/table.controller.spec.js',
    'dashboard/project/lbaasv2/listeners/detail.controller.spec.js',
    'dashboard/project/lbassv2/listeners/filters.spec.js',
    'dashboard/project/lbaasv2/pools/pools.module.spec.js',
    'dashboard/project/lbaasv2/pools/detail.controller.spec.js',
    'dashboard/project/lbaasv2/members/members.module.spec.js',
    'dashboard/project/lbaasv2/members/detail.controller.spec.js',
    'dashboard/project/lbaasv2/members/table.controller.spec.js'
]

ADD_SCSS_FILES = [
    'dashboard/project/lbaasv2/lbaasv2.scss',
]