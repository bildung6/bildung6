---
description: KI kann dabei helfen, Lernschwierigkeiten bei Studierenden zu erkennen,
  indem sie Muster im Lernverhalten und in den Leistungen identifiziert.
id: erkennenvonlernschwierigkeiten
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- erkennenvonlernschwierigkeiten
- studierende
- lehrende
title: Erkennen von Lernschwierigkeiten
type: usecase
---


# Erkennen von Lernschwierigkeiten

## Beschreibung

KI kann dabei helfen, Lernschwierigkeiten bei Studierenden zu erkennen, indem sie Muster im Lernverhalten und in den Leistungen identifiziert.

## AnwenderInnen

```yaml
condition: or
entityType: user
rules:
- condition: contains
  property: id
  value: studierende
- condition: contains
  property: id
  value: lehrende
```



## Tools

[tool=ai-text-classifier,bard]


## Risiken

[risk=datenschutz,geringere-fragenbeteiligung-der-studierenden]


## Chance

[chance=zuganglichkeit-247]
