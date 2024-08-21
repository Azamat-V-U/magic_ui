import pytest


@pytest.mark.extended
def test_header_title(sale_page):
    # sale_page = SalePage(driver)
    sale_page.open_page()
    sale_page.check_header_tittle_is("Sale")
