---
description: "KI kann Bilder generieren, die auf bestimmten Themen, Stilen oder Anforderungen\
  \ basieren, um den Lerninhalten visuelle Unterst\xFCtzung und Attraktivit\xE4t zu\
  \ verleihen."
id: bildergenerieren
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- bildergenerieren
- lehrende
title: Bilder generieren
type: usecase
---


# Bilder generieren

## Beschreibung

KI kann Bilder generieren, die auf bestimmten Themen, Stilen oder Anforderungen basieren, um den Lerninhalten visuelle Unterstützung und Attraktivität zu verleihen.

## AnwenderInnen

```yaml
condition: or
entityType: user
rules:
- condition: contains
  property: id
  value: lehrende
```



## Tools

[tool=starryai,deepl-write]


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

[chance=kreative-anstoesse]
