---
title: Wissenschaftliches Arbeiten
type: "quest"
image: quests/images/wissenschaftlich.svg
description: Welche KI-Tools unterstützen mich beim wissenschaftlichen Arbeiten? 
---


In diesem Quest geht es darum, wie KI zur Unterstützung beim wissenschaftlichen Arbeiten eingesetzt werden kann. 

###	Fragestellung generieren
<!-- 
1.	Ein Tool nutzen mit mind. 3 verschiedenen Prompts, um Ideen zu generieren
2.	Feedback zur Fragestellung einholen (Prompt vorgeben, darf adaptiert werden)
3.	Tool: ChatGPT oder ähnliches, Elicit 
-->

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: fragestellungengenerieren
```


###	Journalistischer Artikel
<!-- 
1.	Feedback einholen und optimieren
2.	Tool: ChatGPT oder ähnliches
-->

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: journalistischerartikelfeedback
```


<!--
---

### Präsentation üben

1.	Powerpoint Speaker Coach 

```yaml
condition: or
entityType: usecase
rules:
- condition: contains
  property: id
  value: powerpoint
```
-->

---

### Literaturrecherche


```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: literaturrecherche
```

### Summary erstellen


```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: summariesgenerieren
```



### Sprachliche Korrektur

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: sprachlichekorrektur
```




