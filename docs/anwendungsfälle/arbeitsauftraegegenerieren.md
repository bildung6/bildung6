---
description: "KI kann helfen, relevante und ansprechende Arbeitsauftr\xE4ge f\xFC\
  r Studierende zu generieren."
id: arbeitsauftraegegenerieren
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- arbeitsauftraege
- studierende
title: "Arbeitsauftr\xE4ge generieren"
type: usecase
---


# Arbeitsaufträge generieren

## Beschreibung

KI kann helfen, relevante und ansprechende Arbeitsaufträge für Studierende zu generieren.

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
