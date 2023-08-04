---
description: "KI kann bei der Text\xFCbersetzung helfen, indem sie automatisch Texte\
  \ von einer Sprache in eine andere \xFCbersetzt."
id: textuebersetzung
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- textuebersetzung
- studierende
title: "Text\xFCbersetzung"
type: usecase
---


# Textübersetzung

## Beschreibung

KI kann bei der Textübersetzung helfen, indem sie automatisch Texte von einer Sprache in eine andere übersetzt.

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

