---
description: KI kann Transkriptionen von Audioaufnahmen, wie Vorlesungen oder Interviews,
  erstellen und so den Zugang zu den Informationen erleichtern.
id: kitranskription
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- kitranskription
- studierende
title: KI Transkription
type: usecase
---


# KI Transkription

## Beschreibung

KI kann Transkriptionen von Audioaufnahmen, wie Vorlesungen oder Interviews, erstellen und so den Zugang zu den Informationen erleichtern.

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
  value: bard
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
  value: effizienzsteigerung
```

