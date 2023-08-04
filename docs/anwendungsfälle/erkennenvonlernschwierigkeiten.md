---
description: KI kann dabei helfen, Lernschwierigkeiten bei Studierenden zu erkennen,
  indem sie Muster im Lernverhalten und in den Leistungen identifiziert.
id: erkennenvonlernschwierigkeiten
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- erkennenvonlernschwierigkeiten
- studierende
- lehrende
title: Erkennen von Lernschwierigkeiten
type: usecase
---


# Erkennen von Lernschwierigkeiten

## Beschreibung

KI kann dabei helfen, Lernschwierigkeiten bei Studierenden zu erkennen, indem sie Muster im Lernverhalten und in den Leistungen identifiziert.

## AnwenderInnen

```yaml
condition: or
entityType: user
rules:
- condition: contains
  property: id
  value: studierende
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
  value: ai-text-classifier
- condition: contains
  property: id
  value: bard
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
  value: geringere-fragenbeteiligung-der-studierenden
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

