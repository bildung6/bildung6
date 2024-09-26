---
title: Modulmanagement
type: "quest"
image: quests/images/modul.svg
description: Wie lässt sich KI in der Lehre verwenden, um die bei Modulen und Kursen anfallenden Arbeitsprozesse zu unterstützen?
disabled: False
---


In dieser Quest geht es darum, wie Künstliche Intelligenz (KI) in der Lehre eingesetzt werden kann, um die Arbeitsprozesse in Modulen und Kursen zu unterstützen.

###	Notizen ausformulieren
KI ermöglicht die effiziente Umwandlung knapper Notizen in strukturierte Texte in verschiedenen Kontexten.


```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: notizenausformulieren
```


###	Unterlagen übersetzen
KI ermöglicht die schnelle und effiziente Übersetzung von Texten und Dokumenten, wodurch sprachliche Barrieren überwunden werden.


```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: unterlagenuebersetzen
```


###	Fragen generieren
KI kann genutzt werden, um Prüfungs- und Quizfragen zu generieren. 


```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: fragengenerieren
```



###	Arbeitsaufträge generieren
Lehrende können KI für eine effiziente Erstellung von studentischen Arbeitsaufträgen einsetzen, um umgehend Vorschläge zu generieren.

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: arbeitsauftraege
```



