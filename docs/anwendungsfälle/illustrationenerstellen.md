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

[tool=deepl-write,starryai]


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

[chance=kreative-anstoesse]
