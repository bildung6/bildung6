---
description: "KI kann bei der Protokollf\xFChrung von Meetings oder Veranstaltungen\
  \ helfen."
id: protokollfuehrung
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- "protokollf\xFChrung"
- lehrende
title: "Protokollf\xFChrung"
type: usecase
---


# Protokollführung

## Beschreibung

KI kann bei der Protokollführung von Meetings oder Veranstaltungen helfen.

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
  value: zeitersparnis
```

