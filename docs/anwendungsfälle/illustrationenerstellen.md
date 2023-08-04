---
description: KI kann bei der Erstellung von Illustrationen und Grafiken helfen.
id: illustrationenerstellen
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- illustrationen
- grafiken
- lehrende
title: Illustrationen, Grafiken erstellen
type: usecase
---


# Illustrationen, Grafiken erstellen

## Beschreibung

KI kann bei der Erstellung von Illustrationen und Grafiken helfen.

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
  value: deepl-write
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
  value: kompetenzverlust
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
  value: kreative-anstoesse
```

