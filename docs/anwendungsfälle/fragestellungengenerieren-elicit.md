---
description: "KI kann bei der Erstellung von Fragestellungen helfen, indem sie Vorschl\xE4\
  ge f\xFCr relevante und interessante Fragestellungen generiert."
id: fragestellungengenerieren-elicit
image: "anwendungsf\xE4lle/images/researching.svg"
tags:
- fragestellungen
- studierende
title: Fragestellungen generieren Elicit
type: usecase
---


# Fragestellungen generieren mit Elicit

## Beschreibung


Ausganspunkt
Seed Articels finden
Überblick schaffen



## Anwender:innen

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
  value: elicit
```



## Risiken

Bias


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