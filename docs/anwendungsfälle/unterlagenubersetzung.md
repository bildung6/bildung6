---
description: "KI kann bei der \xDCbersetzung von Unterlagen in verschiedene Sprachen\
  \ helfen."
id: unterlagenubersetzung
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- unterlagenubersetzung
- lehrende
- studierende
title: "Unterlagen-\xDCbersetzung"
type: usecase
---


# Unterlagen-Übersetzung

## Beschreibung

KI kann bei der Übersetzung von Unterlagen in verschiedene Sprachen helfen.

## AnwenderInnen

```yaml
condition: or
entityType: user
rules:
- condition: contains
  property: id
  value: lehrende
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
  value: papago
- condition: contains
  property: id
  value: ibmwatson
```



## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: contains
  property: id
  value: bias-diskriminierung
- condition: contains
  property: id
  value: datenschutz
```



## Chance

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: zuganglichkeit-247
```

