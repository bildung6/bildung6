---
description: "KI kann bei der Erstellung von Dokumentation f\xFCr Projekte oder Kurse\
  \ helfen."
id: dokumentation
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- dokumentation
- lehrende
title: Dokumentation
type: usecase
---


# Dokumentation

## Beschreibung

KI kann bei der Erstellung von Dokumentation für Projekte oder Kurse helfen.

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
  value: composeai
- condition: contains
  property: id
  value: elicit
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

