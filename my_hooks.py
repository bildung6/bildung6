import os
import re

import yaml
from bs4 import BeautifulSoup
from jinja2 import Environment, BaseLoader


class Global:
    nav = None
    config = None
    cache = {}


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
    desired_order = ["", "Quests", "Chancen & Risiken", "Guides", "Leitlinien", "Tools", 'Über das Projekt', "AnwenderInnen", "Anwendungsfälle"]

    for section in Navigation:
        if section.title == "Chancenrisiken":
            section.title = 'Chancen & Risiken'
        if section.title == "Projekt":
            section.title = 'Über das Projekt'

    title_to_element = {}
    for element in Navigation.items:
        if element.title is None:
            title_to_element[""] = element
        else:
            title_to_element[element.title] = element

    reordered_list = []
    for title in desired_order:
        if title in title_to_element:
            reordered_list.append(title_to_element[title])
    Navigation.items = reordered_list

    Global.nav = Navigation
    Global.config = config
    return Navigation


def on_page_markdown(markdown, page, config, files):
    if page.meta.get('type') is not None:
        if os.path.isfile("docs/overrides/blocks/single/" + page.meta.get('type') + ".html"):
            page.meta["template"] = "blocks/single/" + page.meta.get('type') + ".html"
    return markdown


def filter_entities(entities, filter_dict):
    op_map = {
        'equals': lambda x, y: x == y,
        'greater_than': lambda x, y: x > y,
        'less_than': lambda x, y: x < y,
        'contains': lambda x, y: y in x,
        'matches': lambda x, y: re.search(y, x)
    }

    def match(entity, rule):
        prop = rule['property']
        condition = rule.get('condition', 'and')
        value = rule['value']
        return op_map[condition](entity.meta.get(prop, ""), value)

    def evaluate(entity, filter_group):
        if 'property' in filter_group:
            return match(entity, filter_group)

        if len(filter_group['rules']) == 0:
            return True

        results = [evaluate(entity, rule) for rule in filter_group['rules']]
        return all(results) if filter_group.get("condition", "and") == 'and' else any(results)

    return [entity for entity in entities if
            evaluate(entity, filter_dict) and entity.meta.get('type', '') == filter_dict.get('entityType')]


def on_post_page(html, page, config):
    pages = get_children(Global.nav)
    # use html parser to find all blocks in html
    parsed = BeautifulSoup(html, 'html.parser')
    blocks = parsed.find_all('code')
    for block in blocks:
        if block.text.startswith('yaml') and block.text.find('entityType') > -1:
            parent = block.parent
            # remove yaml from block text
            text = block.text.replace('yaml\n', '')
            # parse yaml
            yaml_data = yaml.safe_load(text)
            filtered_pages = filter_entities(pages, yaml_data)
            block_template = load_block(yaml_data.get("entityType", "block") + '.html')
            block_render = block_template.render(elements=filtered_pages)
            parent.replace_with(BeautifulSoup(block_render, 'html.parser'))
        elif block.text.startswith("yaml") and block.text.find("question") > -1:
            parent = block.parent
            text = block.text.replace('yaml\n', '')
            yaml_data = yaml.safe_load(text)

            block_template = load_block('question.html')
            block_render = block_template.render(yaml_data)
            parent.replace_with(BeautifulSoup(block_render, 'html.parser'))

    return parsed.prettify()


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
