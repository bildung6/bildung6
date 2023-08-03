---
description: "KI kann verwendet werden um Pr\xE4sentationen zu verbessern."
id: powerpoint
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- powerpoint
- studierende
- lehrende
title: PowerPoint
type: usecase
---


# PowerPoint

## Beschreibung

KI kann verwendet werden, um die sprachliche Korrektur von Studierenden zu unterstützen. Dies kann in Form von automatischen Korrekturen oder als Feedback für Studierende erfolgen.

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

[tool=chatgpt,deepl-write]


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

