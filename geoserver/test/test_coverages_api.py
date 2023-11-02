# coding: utf-8

"""
    GeoServer Workspace

    A workspace is a grouping of data stores. Similar to a namespace, it is used to group data that is related in some way.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import geoserver
from geoserver.api.coverages_api import CoveragesApi  # noqa: E501
from geoserver.rest import ApiException


class TestCoveragesApi(unittest.TestCase):
    """CoveragesApi unit test stubs"""

    def setUp(self):
        self.api = CoveragesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_coverage_at_store(self):
        """Test case for create_coverage_at_store

        """
        pass

    def test_create_coverage_at_workspace(self):
        """Test case for create_coverage_at_workspace

        """
        pass

    def test_delete_coverage(self):
        """Test case for delete_coverage

        """
        pass

    def test_find_coverage_by_store(self):
        """Test case for find_coverage_by_store

        """
        pass

    def test_find_coverages_by_store(self):
        """Test case for find_coverages_by_store

        """
        pass

    def test_find_coverages_by_workspace(self):
        """Test case for find_coverages_by_workspace

        """
        pass

    def test_get_coverage_at_workspace(self):
        """Test case for get_coverage_at_workspace

        """
        pass

    def test_update_coverage(self):
        """Test case for update_coverage

        """
        pass


if __name__ == '__main__':
    unittest.main()
