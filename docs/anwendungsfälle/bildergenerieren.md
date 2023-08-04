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

```yaml
condition: or
entityType: tool
rules:
- condition: contains
  property: id
  value: starryai
- condition: contains
  property: id
  value: deepl-write
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

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: kreative-anstoesse
```

