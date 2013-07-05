#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By

from base import Base


class StatsRegion(Base):

    _vital_stats_header_locator = (By.CSS_SELECTOR, '.statsBoxSection:nth-child(1) .statsBoxSection-header')
    _vital_stats_section_locator = (By.ID, 'vital_stats')
    _vital_stats_browser_version_locator = (By.CSS_SELECTOR, '#vital_stats li:nth-child(1) .statsBoxSection-value')