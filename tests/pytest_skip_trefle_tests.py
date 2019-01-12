import pytest


def is_trefle_package_installed():
    try:
        from trefle_engine import TrefleFIS
        return True
    except ImportError:
        return False


run_if_trefle_is_installed = pytest.mark.skipif(
    not is_trefle_package_installed(),
    reason="Trefle is not installed. Install it to run these tests",
)
