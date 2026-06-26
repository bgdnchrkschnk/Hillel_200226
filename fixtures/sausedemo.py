import os
import pathlib

import allure
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Page

from page_objects.sausedemo.ProductsPage import ProductsPage

load_dotenv()
import pytest

from page_objects.sausedemo.LoginPage import LoginPage


@pytest.fixture
def clear_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless - запуск без візуалу
        context = browser.new_context()
        page: Page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture # user is not logged in
def login_page(clear_page) -> LoginPage:
    lp: LoginPage = LoginPage(clear_page)
    lp.open()
    return lp


@pytest.fixture # user is logger in
def products_page_logged_standard_user(login_page: LoginPage) -> ProductsPage:
    products_page: ProductsPage = login_page.login(
        username=os.getenv("SAUSEDEMO_STANDART_USERNAME"),
        password=os.getenv("SAUSEDEMO_PASSWORD"), delay=20
    )
    return products_page


@pytest.fixture(scope="function", autouse=True)
def trace_per_test(request, clear_page):

    context = clear_page.context

    trace_path = pathlib.Path(__file__).parent / 'pw_traces'
    trace_path.mkdir(exist_ok=True)

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield

    test_name = request.node.name
    trace_file = trace_path / f"{test_name}.zip"
    context.tracing.stop(path=str(trace_file))

    allure.attach.file(
        str(trace_file),
        name="playwright-trace",
        attachment_type="application/zip",
        extension="zip"
    )

