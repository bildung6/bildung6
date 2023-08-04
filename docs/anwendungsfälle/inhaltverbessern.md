---
description: "KI kann dazu beitragen, Inhalte besser zu finden, indem sie Suchvorg\xE4\
  nge optimiert und personalisierte Empfehlungen f\xFCr Ressourcen und Materialien\
  \ basierend auf den Interessen und Bed\xFCrfnissen der Studierenden anbietet."
id: inhaltverbessern
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- inhaltverbessern
- studierende
title: Inhalte besser finden
type: usecase
---


# Inhalte besser finden

## Beschreibung

KI kann dazu beitragen, Inhalte besser zu finden, indem sie Suchvorgänge optimiert und personalisierte Empfehlungen für Ressourcen und Materialien basierend auf den Interessen und Bedürfnissen der Studierenden anbietet.

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
  value: bingchatbot
```



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
  value: zuganglichkeit-247
```

