#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver
from unittestzero import Assert

from pages.home import HomePage
from pages.fhr_graph_region import GraphRegion


class TestFHR():

    @pytest.mark.nondestructive
    def test_that_page_has_correct_title(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        Assert.equal('Firefox Health Report', home_page.page_title)

    @pytest.mark.nondestructive
    def test_the_correct_firefox_version_is_displayed(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        firefox_version = mozwebqa.selenium.capabilities['version']
        Assert.equal(firefox_version, u'22.0')

    # @pytest.mark.nondestructive
    # def test_graph_date_locale(self, mozwebqa):
    #     home_page = HomePage(mozwebqa)
    #     home_page.go_to_page()
    #
    #     first_date_xaxis = home_page.wait_for_element_present(By.CSS_SELECTOR, '.xAxis .tickLabel:first-child')
    #
    #     Assert.equal('Jun', first_date_xaxis.text)
