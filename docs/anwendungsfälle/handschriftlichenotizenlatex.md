---
description: KI kann helfen, handschriftliche Notizen in Latex oder Markdown zu konvertieren.
id: handschriftlichenotizenlatex
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- handschriftlichenotizen
- latex
- markdown
- studierende
title: Handschriftliche Notizen zu Latex / Markdown
type: usecase
---


# Handschriftliche Notizen zu Latex / Markdown

## Beschreibung

KI kann helfen, handschriftliche Notizen in Latex oder Markdown zu konvertieren.

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
  value: photomath
```



## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: contains
  property: id
  value: konsequenzen-fuer-das-schriftliche-arbeiten
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
  value: effizienz-steigerung
```

