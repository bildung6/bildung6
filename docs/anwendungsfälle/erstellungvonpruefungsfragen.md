---
description: "KI kann bei der Erstellung von Pr\xFCfungsfragen helfen, indem sie Vorschl\xE4\
  ge f\xFCr relevante und herausfordernde Fragen macht."
id: erstellungvonpruefungsfragen
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- "pr\xFCfungsfragen"
- lehrende
title: "Erstellung von Pr\xFCfungsfragen"
type: usecase
---


# Erstellung von Prüfungsfragen

## Beschreibung

KI kann bei der Erstellung von Prüfungsfragen helfen, indem sie Vorschläge für relevante und herausfordernde Fragen macht.

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
