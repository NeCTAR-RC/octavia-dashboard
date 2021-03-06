/*
 * Copyright 2018 Walmart.
 *
 * Licensed under the Apache License, Version 2.0 (the 'License');
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an 'AS IS' BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
(function() {
  'use strict';

  angular
    .module('horizon.dashboard.project.lbaasv2.l7rules')
    .factory('horizon.dashboard.project.lbaasv2.l7rules.actions.create', createService);

  createService.$inject = [
    'horizon.dashboard.project.lbaasv2.l7rules.resourceType',
    'horizon.framework.util.actions.action-result.service',
    '$q',
    'horizon.dashboard.project.lbaasv2.workflow.modal',
    'horizon.app.core.openstack-service-api.policy',
    'horizon.framework.util.i18n.gettext'
  ];

  /**
   * @ngDoc factory
   * @name horizon.dashboard.project.lbaasv2.l7rules.actions.createService
   *
   * @description
   * Provides the service for creating a l7rule resource.
   *
   * @param resourceType The l7rule resource type.
   * @param actionResultService The horizon action result service.
   * @param $q The angular service for promises.
   * @param workflowModal The LBaaS workflow modal service.
   * @param policy The horizon policy service.
   * @param gettext The horizon gettext function for translation.
   *
   * @returns The l7rule create service.
   */

  function createService(
    resourceType, actionResultService,
    $q, workflowModal, policy, gettext
  ) {
    return workflowModal.init({
      controller: 'CreateL7RuleWizardController',
      message: gettext('A new l7 policy is being created.'),
      handle: handle,
      allowed: allowed
    });

    //////////////

    function allowed() {
      return $q.all([
        policy.ifAllowed({ rules: [['load-balancer', 'os_load-balancer_api:l7rule:post']] })
      ]);
    }

    function handle(response) {
      return actionResultService.getActionResult()
        .created(resourceType, response.data.id)
        .result;
    }
  }
})();
