---
description: "KI kann bei der Literaturrecherche unterst\xFCtzend wirken, indem sie\
  \ relevante Artikel und Studien identifiziert und vorschl\xE4gt."
id: literaturrecherche
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- literaturrecherche
- studierende
title: Literaturrecherche
type: usecase
---


# Literaturrecherche

## Beschreibung

KI kann bei der Literaturrecherche unterstützend wirken, indem sie relevante Artikel und Studien identifiziert und vorschlägt.

## AnwenderInnen

```yaml
condition: or
entityType: user
rules:
- condition: contains
  property: id
  value: studierende
```



## Tools

```yaml
condition: or
entityType: tool
rules:
- condition: contains
  property: id
  value: composeai
- condition: contains
  property: id
  value: bingchatbot
```



## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: contains
  property: id
  value: datenschutz
- condition: contains
  property: id
  value: monopolbildung
```



## Chance

[chance=effizienz-steigerung]
