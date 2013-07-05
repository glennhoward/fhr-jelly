#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By

from base import Base


class GraphRegion(Base):

    _x_axis_label_locator = (By.CSS_SELECTOR, '.xAxis .tickLabel:first-child')