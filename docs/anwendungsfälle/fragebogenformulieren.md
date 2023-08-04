---
description: "KI kann bei der Formulierung und Gestaltung von Frageb\xF6gen helfen,\
  \ um valide und zuverl\xE4ssige Daten zu erfassen."
id: fragebogenformulieren
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- fragebogen
- lehrende
title: Fragebogen formulieren
type: usecase
---


# Fragebogen formulieren

## Beschreibung

KI kann bei der Formulierung und Gestaltung von Fragebögen helfen, um valide und zuverlässige Daten zu erfassen.

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
  value: effizienz-steigerung
```

