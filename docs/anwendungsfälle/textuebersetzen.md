---
description: "KI kann dazu verwendet werden, Texte zu \xFCbersetzen und so den Zugang\
  \ zu Ressourcen und Informationen in verschiedenen Sprachen zu erm\xF6glichen."
id: textuebersetzen
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- "text\xFCbersetzen"
- studierende
title: "Texte \xFCbersetzen"
type: usecase
---


# Texte übersetzen

## Beschreibung

KI kann dazu verwendet werden, Texte zu übersetzen und so den Zugang zu Ressourcen und Informationen in verschiedenen Sprachen zu ermöglichen.

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
  value: papago
- condition: contains
  property: id
  value: deepl-write
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

