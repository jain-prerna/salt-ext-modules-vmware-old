# pylint: disable=missing-module-docstring
import setuptools

if __name__ == "__main__":
    setuptools.setup(use_scm_version=True, package_data={'saltext.vmware': ['modules/templates/*.json']})
