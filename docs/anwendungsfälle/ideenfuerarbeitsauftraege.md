---
description: "KI kann bei der Entwicklung von Arbeitsauftr\xE4gen hilfreich sein,\
  \ indem sie Vorschl\xE4ge f\xFCr relevante und ansprechende Themen und Aufgaben\
  \ erstellt."
id: ideenfuerarbeitsauftraege
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- arbeitsauftraege
- lehrende
title: "Ideen f\xFCr Arbeitsauftr\xE4ge"
type: usecase
---


# Ideen für Arbeitsaufträge

## Beschreibung

KI kann bei der Entwicklung von Arbeitsaufträgen hilfreich sein, indem sie Vorschläge für relevante und ansprechende Themen und Aufgaben erstellt.

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

[chance=kreative-anstoesse]
