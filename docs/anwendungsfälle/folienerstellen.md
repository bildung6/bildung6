---
description: "KI kann bei der Erstellung von Folien f\xFCr Pr\xE4sentationen helfen,\
  \ indem sie Vorschl\xE4ge f\xFCr Design, Layout und Inhalt macht, um die Informationen\
  \ klar und ansprechend zu pr\xE4sentieren."
id: folienerstellen
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- folienerstellen
- lehrende
title: Folien erstellen
type: usecase
---


# Folien erstellen

## Beschreibung

KI kann bei der Erstellung von Folien für Präsentationen helfen, indem sie Vorschläge für Design, Layout und Inhalt macht, um die Informationen klar und ansprechend zu präsentieren.

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

