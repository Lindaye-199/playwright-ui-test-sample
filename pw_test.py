import os.path

from playwright.sync_api import Page ,expect
def test_link(page: Page):
    page.goto("/demo/link",wait_until="networkidle")
    page.get_by_text("本页跳转到百度").click()
    expect(page.get_by_text("百度一下",exact=True)).to_be_visible()
def test_new_page(page: Page):
    page.goto("/demo/link",wait_until="networkidle")
    with page.expect_popup() as new_page:
        page.get_by_text("新页面跳转到淘宝").click()
    page_new=new_page.value
    expect(page_new.locator(".search-button")).to_be_attached()
def test_hover(page: Page):
    page.goto("/demo/hover",wait_until="networkidle")
    page.locator("#c4").hover()
    expect(page.get_by_text("你已经成功悬浮")).to_be_visible()
def test_dropdown(page: Page):
    page.goto("/demo/dropdown",wait_until="networkidle")
    page.get_by_text("点击选择").click()
    page.get_by_text("playwright").click()
    expect(page.get_by_text("你选择了websocket")).to_be_visible()

def test_input(page: Page):
    page.goto("/demo/input", wait_until="networkidle")
    page.get_by_placeholder("不用管我,我是placeholder").fill("12345")
    page.get_by_label("也许你可以").fill("label定位")
    page.get_by_label("数字输入专用").fill("123.12345678902")
    page.get_by_label("数字输入专用").blur()
    page.wait_for_timeout(1_000)
    assert page.get_by_label("数字输入专用").input_value()== "123.12345678902"

def test_pw_textarea(page: Page):
    page.goto("/demo/textarea", wait_until="networkidle")
    page.locator("textarea").fill("12345")
    page.locator("textarea").fill("123\n45")
    page.locator("textarea").fill("""123
456""")
    expect(page.locator("textarea")).to_have_value("123\n456")
    page.locator("textarea").press_sequentially("789",delay=1_000)
    expect(page.locator("textarea")).to_have_value("123\n456789")
def test_radio(page: Page):
    page.goto("/demo/radio", wait_until="networkidle")
    page.get_by_text("草莓").locator("input").check()
    expect(page.get_by_text("草莓").locator("input")).to_be_checked()
    page.get_by_text("香蕉").locator("input").check()
    expect(page.get_by_text("香蕉").locator("input")).to_be_checked()
    page.get_by_text("苹果").locator("input").check()
    expect(page.get_by_text("苹果").locator("input")).to_be_checked()

def test_checkbox(page: Page):
    page.goto("/demo/checkbox", wait_until="networkidle")
    page.get_by_text("开发").locator("input").set_checked(True)
    expect(page.get_by_text("开发").locator("input")).to_be_checked()
    page.wait_for_timeout(1_000)
    page.get_by_text("测试").locator("input").set_checked(True)
    expect(page.get_by_text("测试").locator("input")).to_be_checked()
    page.wait_for_timeout(1_000)
    page.get_by_text("美团").locator("input").set_checked(True)
    expect(page.get_by_text("美团").locator("input")).to_be_checked()
    page.get_by_text("开发").locator("input").set_checked(False)
    expect(page.get_by_text("开发").locator("input")).not_to_be_checked()
    page.wait_for_timeout(1_000)
    page.get_by_text("测试").locator("input").set_checked(False)
    expect(page.get_by_text("测试").locator("input")).not_to_be_checked()
    page.wait_for_timeout(1_000)
    page.get_by_text("美团").locator("input").set_checked(False)
    expect(page.get_by_text("美团").locator("input")).not_to_be_checked()

def test_switch(page: Page):
    page.goto("/demo/switch", wait_until="networkidle")
    page.locator('//div[@aria-checked]').click()
    expect(page.locator('//div[@aria-checked="true"]')).to_be_visible()
    expect(page.get_by_text("已经学会了")).to_be_visible()
    page.locator('//div[@aria-checked]').click()
    expect(page.locator('//div[@aria-checked="false"]')).to_be_visible()

def test_upload(page: Page):
    page.goto("/demo/upload", wait_until="networkidle")
    page.locator('//input[@type="file"]').set_input_files("my_search_baidu.py")

def test_download(page: Page):
    page.goto("/demo/download", wait_until="networkidle")
    page.locator("textarea").fill("12345")
    with page.expect_download() as file:
        page.get_by_text("download").click()
    file.value.save_as("123456.txt")
    assert os.path.exists("123456.txt")
def test_drag(page: Page):
    page.goto("/demo/drag", wait_until="networkidle")
    page.get_by_text("去壶口瀑布").drag_to(page.get_by_text("正在做"))
    expect(page.get_by_text("正在做").locator("xpath=/..").get_by_text("去壶口瀑布").last).to_be_visible()

def test_role(page: Page):
    page.goto("/demo/dialog", wait_until="networkidle")
    page.get_by_text("点我开启一个dialog").click()
    expect(page.get_by_role(role="dialog")).to_be_visible()
    page.goto("/demo/checkbox", wait_until="networkidle")
    page.get_by_role("checkbox",name="开发",checked=False).set_checked(True)
    page.goto("/demo/table", wait_until="networkidle")
    expect(page.get_by_role("table")).to_be_visible()

def test_text(page: Page):
    page.goto("/demo/getbytext", wait_until="networkidle")
    expect(page.get_by_text("确定",exact=True)).to_have_count(2)

def test_getbylable(page: Page):
    page.goto("/demo/input", wait_until="networkidle")
    page.get_by_label("任何文字").fill("123456")
def test_placeholder(page: Page):
    page.goto("/demo/input", wait_until="networkidle")
    page.get_by_placeholder("我是placeholder").fill("19996")

def test_title(page: Page):
    page.goto("/demo/image", wait_until="networkidle")
    expect(page.get_by_title("这是一个title")).to_be_visible()


def test_alt_text(page: Page):
    page.goto("/demo/image", wait_until="networkidle")
    expect(page.get_by_alt_text("这是图片占位符")).to_be_visible()

def test_get_by_locator_css(page: Page):
    page.goto("http://taobao.com")
    expect(page.locator("#q")).to_be_visible()
    expect(page.locator(".image-icon-text")).to_be_visible()
    expect(page.locator(".tbh-service.J_Module>div>div")).to_have_count(1)
    expect(page.locator(".tbh-service.J_Module ul")).to_have_count(1)

def test_filter(page: Page):
    page.goto("http://taobao.com")
    assert page.locator('[aria-label="查看更多"]').filter(has_text="工业品").get_by_role("link").all_text_contents()[-1]=="定制"

def test_and_or_visible(page: Page):
    page.goto("http://taobao.com")
    expect(page.get_by_text("电脑",exact=True).and_(page.get_by_role("link")).and_(page.locator(".cate-content-href--HI8wwRts"))).to_be_visible()
    expect(page.get_by_text("电脑").locator("visible=True")).to_be_visible()
