---
description: "KI kann in der Beratung von Studierenden eingesetzt werden, indem sie\
  \ personalisierte Empfehlungen und Ratschl\xE4ge f\xFCr Studienentscheidungen, Karrierewege\
  \ oder pers\xF6nliche Herausforderungen gibt."
id: beratung
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- beratung
- studierende
title: Beratung
type: usecase
---


# Beratung

## Beschreibung

KI kann in der Beratung von Studierenden eingesetzt werden, indem sie personalisierte Empfehlungen und Ratschläge für Studienentscheidungen, Karrierewege oder persönliche Herausforderungen gibt.

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
  value: chatgpt
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
  value: kompetenzverlust
- condition: contains
  property: id
  value: datenschutz
```



## Chance

[chance=personalisiertes-lernen]
