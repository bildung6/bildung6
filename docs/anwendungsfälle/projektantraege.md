---
description: "KI kann beim Verfassen von Projektantr\xE4gen helfen, indem sie Vorschl\xE4\
  ge f\xFCr Struktur, Inhalt und Argumentation liefert."
id: projektantraege
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- projektantraege
- studierende
title: "Projektantr\xE4ge schreiben"
type: usecase
---


# Projektanträge schreiben

## Beschreibung

KI kann beim Verfassen von Projektanträgen helfen, indem sie Vorschläge für Struktur, Inhalt und Argumentation liefert.

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

[tool=deepl-write,wolframalpha]


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
  value: effizienzsteigerung
```

