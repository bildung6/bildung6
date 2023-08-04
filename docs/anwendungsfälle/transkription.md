---
description: KI kann bei der Transkription von Audioaufnahmen, wie Vorlesungen oder
  Interviews, helfen.
id: transkription
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- transkription
- studierende
title: Transkription
type: usecase
---


# Transkription

## Beschreibung

KI kann bei der Transkription von Audioaufnahmen, wie Vorlesungen oder Interviews, helfen.

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
  value: effizienz-steigerung
```

