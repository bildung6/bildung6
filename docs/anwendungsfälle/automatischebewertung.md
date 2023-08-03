---
description: "KI kann bei der automatischen Auswertung von Tests helfen, indem sie\
  \ Antworten auf objektive Fragen bewertet und so die Zeit und den Aufwand f\xFC\
  r die manuelle Bewertung reduziert."
id: automatischebewertung
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- automatischebewertung
- lehrende
title: Automatische Auswertung von Tests
type: usecase
---


# Automatische Auswertung von Tests

## Beschreibung

KI kann bei der automatischen Auswertung von Tests helfen, indem sie Antworten auf objektive Fragen bewertet und so die Zeit und den Aufwand für die manuelle Bewertung reduziert.

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

[tool=bard,deepl-write]


## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: contains
  property: id
  value: datenschutz
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

