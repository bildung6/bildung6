---
description: "KI kann bei der Priorisierung von Aufgaben in der Projektplanung helfen,\
  \ indem sie Vorschl\xE4ge f\xFCr die Reihenfolge und Wichtigkeit von Aufgaben macht,\
  \ um die Effizienz und den Erfolg des Projekts zu maximieren."
id: priorisieren
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- priorisieren
- lehrende
title: Priorisieren
type: usecase
---


# Priorisieren

## Beschreibung

KI kann bei der Priorisierung von Aufgaben in der Projektplanung helfen, indem sie Vorschläge für die Reihenfolge und Wichtigkeit von Aufgaben macht, um die Effizienz und den Erfolg des Projekts zu maximieren.

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
  value: monopolbildung
```



## Chance

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: effizienzsteigerung
```

