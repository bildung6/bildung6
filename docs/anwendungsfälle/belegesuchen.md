---
description: "KI kann bei der Suche nach Belegen f\xFCr Argumente oder Hypothesen\
  \ helfen, indem sie relevante Studien, Artikel oder Daten identifiziert und pr\xE4\
  sentiert."
id: belegesuchen
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- belegesuchen
- studierende
title: Belege suchen
type: usecase
---


# Belege suchen

## Beschreibung

KI kann bei der Suche nach Belegen für Argumente oder Hypothesen helfen, indem sie relevante Studien, Artikel oder Daten identifiziert und präsentiert.

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
  value: bingchatbot
- condition: contains
  property: id
  value: composeai
```



## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: contains
  property: id
  value: bias-diskriminierung
- condition: contains
  property: id
  value: datenschutz
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

