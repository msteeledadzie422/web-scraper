from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=3000)
        page = browser.new_page()
        page.goto('https://en.wikipedia.org/wiki/History_of_Islam')

        browser.close()


if __name__ == '__main__':
    main()
