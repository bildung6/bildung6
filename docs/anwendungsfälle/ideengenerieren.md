---
description: "KI kann bei der Ideenfindung und beim Brainstorming helfen, indem sie\
  \ kreative und innovative Vorschl\xE4ge f\xFCr Projekte, Aufgaben oder Forschungsthemen\
  \ macht."
id: ideengenerieren
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- ideengenerieren
- lehrende
title: Ideen generieren / Brainstorming
type: usecase
---


# Ideen generieren / Brainstorming

## Beschreibung

KI kann bei der Ideenfindung und beim Brainstorming helfen, indem sie kreative und innovative Vorschläge für Projekte, Aufgaben oder Forschungsthemen macht.

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

