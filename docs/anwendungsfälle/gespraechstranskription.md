---
description: "KI kann bei der Transkription von Gespr\xE4chen helfen, indem sie automatisch\
  \ den gesprochenen Text in geschriebenen Text umwandelt."
id: gespraechstranskription
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- gespraechstranskription
- lehrende
- studierende
title: "Gespr\xE4chstranskription"
type: usecase
---


# Gesprächstranskription

## Beschreibung

KI kann bei der Transkription von Gesprächen helfen, indem sie automatisch den gesprochenen Text in geschriebenen Text umwandelt.

## AnwenderInnen

```yaml
condition: or
entityType: user
rules:
- condition: contains
  property: id
  value: lehrende
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
  value: whisper
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
  value: effizienzsteigerung
```

