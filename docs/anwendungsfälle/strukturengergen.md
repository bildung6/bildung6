---
description: "KI kann dabei helfen, Strukturen f\xFCr Texte, Projekte oder Lektionen\
  \ zu erstellen, um die Informationen klar, logisch und verst\xE4ndlich zu pr\xE4\
  sentieren."
id: strukturengergen
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- strukturengergen
- lehrende
title: Strukturen geben
type: usecase
---


# Strukturen geben

## Beschreibung

KI kann dabei helfen, Strukturen für Texte, Projekte oder Lektionen zu erstellen, um die Informationen klar, logisch und verständlich zu präsentieren.

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
  value: zeitersparnis
```

