import os
import re

from jinja2 import Environment, BaseLoader


class Global:
    nav = None
    config = None


def load_block(block_name):
    content = ""
    # check if file exists
    if not os.path.isfile("docs/overrides/blocks/" + block_name):
        block_name = "block.html"
    with open("docs/overrides/blocks/" + block_name) as f:
        content = f.read()

    env = Environment(loader=BaseLoader)
    env.filters['url'] = url
    rtemplate = env.from_string(content)
    return rtemplate


def on_nav(Navigation, config, files):
    Global.nav = Navigation
    Global.config = config
    return Navigation




def on_page_markdown(markdown, page, config, files):
    print(page.meta)
    if page.meta.get('type') is not None:
        print("Found block type: " + page.meta.get('type'))
        if os.path.isfile("docs/overrides/blocks/single/" + page.meta.get('type') + ".html"):
            page.meta["template"] = "blocks/single/" + page.meta.get('type') + ".html"
            print("Using custom template for " + page.meta.get('type'))
            print(page.meta)
    return markdown


def on_post_page(html, page, config):
    pages = get_children(Global.nav)

    # find all [asfsd=sdfsdf] with regex
    blocks = re.findall(r'\[[a-zA-Z\=0-9,\-]+\]', html)
    for block in blocks:
        original = block
        block = block.strip("[]")
        if len(block.split('=')) == 2:
            block_name, tags = block.split('=')
            tags = tags.split(',')
        else:
            block_name = block
            tags = []

        filtered_pages = filter_by_meta(pages, 'type', block_name)

        if len(tags) > 0:
            tagged_pages = []
            for tag in tags:
                for page in filtered_pages:
                    if page.meta.get('tags') is not None:
                        for page_tag in page.meta.get('tags'):
                            if page_tag == tag:
                                tagged_pages.append(page)
            filtered_pages = tagged_pages

        block_template = load_block(block_name + '.html')
        block_render = block_template.render(elements=filtered_pages)
        html = html.replace(original, block_render)

    return html


def url(path):
    return Global.config['site_url'] + path


def get_children(list):
    pages = []
    for item in list:
        if item.children:
            pages.extend(get_children(item.children))
        else:
            pages.append(item)
    return pages


def filter_by_meta(pages, tag, value):
    list = []
    for page in pages:
        if page.meta.get(tag) == value:
            list.append(page)
    return list
