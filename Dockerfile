FROM ghcr.io/afritzler/mkdocs-material:latest

RUN pip install mkdocs-macros-plugin
RUN pip install mkdocs-mermaid2-plugin
