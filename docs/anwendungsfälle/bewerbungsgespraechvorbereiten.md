---
description: "KI kann bei der Vorbereitung von Bewerbungsgespr\xE4chen helfen."
id: bewerbungsgespraechvorbereiten
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- bewerbungsgespraeche
- studierende
title: "Bewerbungsgespr\xE4che vorbereiten"
type: usecase
---


# Bewerbungsgespräche vorbereiten

## Beschreibung

KI kann bei der Vorbereitung von Bewerbungsgesprächen helfen.

## AnwenderInnen

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
  value: motivation
```

