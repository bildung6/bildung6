---
description: "KI kann beim Debuggen von Code helfen, indem sie automatisch Fehler\
  \ identifiziert und Vorschl\xE4ge f\xFCr deren Behebung macht."
id: codedebuggen
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- codedebuggen
- studierende
title: Code Debuggen
type: usecase
---


# Code Debuggen

## Beschreibung

KI kann beim Debuggen von Code helfen, indem sie automatisch Fehler identifiziert und Vorschläge für deren Behebung macht.

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
  value: tabnine
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

