#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostEndianConan(base.BoostBaseConan):
    name = "boost_endian"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_endian"
    lib_short_names = ["endian"]
    header_only_libs = ["endian"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_predef",
        "boost_static_assert",
        "boost_system",
        "boost_type_traits",
        "boost_utility"
    ]
