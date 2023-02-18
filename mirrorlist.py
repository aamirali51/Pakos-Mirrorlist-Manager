#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import urllib.request
import pandas as pd


class Mirrorlist:
    def __init__(self):
        self.mirrorfile = "/tmp/mirrorlist.txt"
        self.country_code_dataset = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "country_code.data"
        )
        self.url = (
            "https://www.archlinux.org/mirrorlist/"
            "?country={}&protocol=http&protocol=https&ip_version=4"
        )

    def get_mirrorlist(self, country_code):
        country_code = self.country_code_detect(country_code)
        url = self.url.format(country_code)

        with urllib.request.urlopen(url) as response:
            mirrordata = response.read().decode()

        distro_name = self.get_distro_name()
        mirrordata = mirrordata.replace("#Server =", "Server =")
        mirrordata = mirrordata.replace("## Arch Linux", distro_name)
        mirrordata = mirrordata.replace(
            "Generated", "Generated with Mirrorlist Manager"
        )

        return mirrordata

    def create_url(self, country_code):
        return self.url.format(country_code)

    def country_code_detect(self, country_input):
        if country_input == "all":
            return "all"

        country_input = country_input.strip().lower()
        df = pd.read_csv(self.country_code_dataset)
        match = df["Country"].str.lower().str.contains(country_input)
        country_code = df[match].iloc[0]["Code"]

        return country_code

    def get_distro_name(self):
        distro_name = os.popen("lsb_release -i").read().strip()
        return "## " + distro_name.replace("Distributor ID:", "").strip()


if __name__ == "__main__":
    print("Hello World")
