---
description: "KI kann bei der Planung von Lektionen unterst\xFCtzend wirken, indem\
  \ sie Vorschl\xE4ge f\xFCr Struktur, Inhalte und Aktivit\xE4ten macht, die auf den\
  \ Lernzielen und den Bed\xFCrfnissen der Studierenden basieren."
id: lektionenplanen
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- lektionenplanen
- lehrende
title: Lektionen planen
type: usecase
---


# Lektionen planen

## Beschreibung

KI kann bei der Planung von Lektionen unterstützend wirken, indem sie Vorschläge für Struktur, Inhalte und Aktivitäten macht, die auf den Lernzielen und den Bedürfnissen der Studierenden basieren.

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

