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


class QueryResponse(Model):
    """Query result.

    All required parameters must be populated in order to send to Azure.

    :param total_records: Required. Number of total records matching the
     query.
    :type total_records: long
    :param count: Required. Number of records returned in the current
     response. In the case of paging, this is the number of records in the
     current page.
    :type count: long
    :param result_truncated: Required. Indicates whether the query results are
     truncated. Possible values include: 'true', 'false'
    :type result_truncated: str or
     ~azure.mgmt.resourcegraph.models.ResultTruncated
    :param skip_token: When present, the value can be passed to a subsequent
     query call (together with the same query and subscriptions used in the
     current request) to retrieve the next page of data.
    :type skip_token: str
    :param data: Required. Query output in tabular format.
    :type data: object
    :param facets: Query facets.
    :type facets: list[~azure.mgmt.resourcegraph.models.Facet]
    """

    _validation = {
        'total_records': {'required': True},
        'count': {'required': True},
        'result_truncated': {'required': True},
        'data': {'required': True},
    }

    _attribute_map = {
        'total_records': {'key': 'totalRecords', 'type': 'long'},
        'count': {'key': 'count', 'type': 'long'},
        'result_truncated': {'key': 'resultTruncated', 'type': 'ResultTruncated'},
        'skip_token': {'key': '$skipToken', 'type': 'str'},
        'data': {'key': 'data', 'type': 'object'},
        'facets': {'key': 'facets', 'type': '[Facet]'},
    }

    def __init__(self, **kwargs):
        super(QueryResponse, self).__init__(**kwargs)
        self.total_records = kwargs.get('total_records', None)
        self.count = kwargs.get('count', None)
        self.result_truncated = kwargs.get('result_truncated', None)
        self.skip_token = kwargs.get('skip_token', None)
        self.data = kwargs.get('data', None)
        self.facets = kwargs.get('facets', None)
