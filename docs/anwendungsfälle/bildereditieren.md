---
description: "KI kann bei der Bildbearbeitung helfen, indem sie automatisch Verbesserungen\
  \ oder \xC4nderungen an Bildern vornimmt."
id: bildereditieren
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- bildereditieren
- lehrende
title: Bilder editieren
type: usecase
---


# Bilder editieren

## Beschreibung

KI kann bei der Bildbearbeitung helfen, indem sie automatisch Verbesserungen oder Änderungen an Bildern vornimmt.

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

