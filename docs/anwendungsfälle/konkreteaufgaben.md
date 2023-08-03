---
description: "KI kann bei der Erstellung von konkreten Aufgaben unterst\xFCtzen, wie\
  \ das L\xF6sen von Gleichungen oder das Generieren von Bildern."
id: konkreteaufgaben
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- konkreteaufgaben
- studierende
title: Konkrete Aufgaben
type: usecase
---


# Konkrete Aufgaben

## Beschreibung

KI kann bei der Erstellung von konkreten Aufgaben unterstützen, wie das Lösen von Gleichungen oder das Generieren von Bildern.

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
  value: starryai
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
  value: effizienzsteigerung
```

