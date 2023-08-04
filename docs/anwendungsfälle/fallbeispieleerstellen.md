---
description: "KI kann bei der Erstellung von Fallbeispielen helfen, indem sie Vorschl\xE4\
  ge f\xFCr relevante und interessante F\xE4lle macht, die auf realen Situationen\
  \ oder Problemen basieren."
id: fallbeispieleerstellen
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- fallbeispiele
- lehrende
title: Fallbeispiele erstellen
type: usecase
---


# Fallbeispiele erstellen

## Beschreibung

KI kann bei der Erstellung von Fallbeispielen helfen, indem sie Vorschläge für relevante und interessante Fälle macht, die auf realen Situationen oder Problemen basieren.

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
  value: kompetenzverlust
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
  value: kreative-anstoesse
```

