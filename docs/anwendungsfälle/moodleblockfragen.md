---
description: "KI kann bei der Erstellung von Fragen f\xFCr Tests oder \xDCbungen helfen,\
  \ indem sie Vorschl\xE4ge f\xFCr relevante und herausfordernde Fragen macht, die\
  \ auf den Lernzielen des Kurses basieren."
id: moodleblockfragen
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- fragen
- lehrende
title: Fragen erstellen
type: usecase
---


# Fragen erstellen

## Beschreibung

KI kann bei der Erstellung von Fragen für Tests oder Übungen helfen, indem sie Vorschläge für relevante und herausfordernde Fragen macht, die auf den Lernzielen des Kurses basieren.

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

