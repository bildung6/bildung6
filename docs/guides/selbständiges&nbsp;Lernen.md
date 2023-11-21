---
description: "KI beim selbstständigen Lernen nutzen"
id: guide
image: guides/images/studying.svg
tags:
- studierende
title: Effizienteres Selbststudium mit KI
type: guide
--- 

???+ info "Einleitende Fragen"

    **An wen richtet sich dieser Guide?**<br>
    Dieser Guide richtet sich an Studierende die KI beim selbständigen Lernen einsetzen möchten. 

    **Was findest du hier?**<br>
    Hier findest du ein Konzept für eine dreiphasige Vorgehensweise wie KI im Selbststudium eingesetzt werden kann. Z.B. können Studierende ChatGPT als Lerncoach einsetzen um sie beim Lernen zu entlasten, indem verschiedene Aufgaben an den Chatbot ausgelagert werden.


    **Wie kannst du die Inhalte hier nutzen?**<br>
    Hier findest du Hinweise, wie ChatGPT zur Informationsbeschaffung und Strukturierung des Lernprozesses eingesetzt werden kann, beispielsweise für die Generierung von Lernplänen oder Quizfragen zur Selbstüberprüfung.


    **Woher stammen die hier gezeigten Inhalte?**<br>
    Das Konzept wurde von Luka Dimitrijevic, derzeit Student im Bachelorstudiengang Physiotherapie an der Berner Fachhochschule, entwickelt und im Rahmen eines Discord-Events im Projekt "Bildung 6.0" vorgestellt.



## Einleitung

Das von Luka Dimitrijevic vorgestellte Konzept des KI-basierten Selbststudiums umfasst drei Phasen - Construct, Connect und Challenge - zur Optimierung des Lernprozesses. Dabei stehen kognitive Entlastung und effizientes Lernen im Vordergrund. So können einige Arbeitsschritte an die KI ausgelagert werden, wie z.B. das Erstellen eigener Lernpläne oder die Generierung von Quizfragen.


|                                                |                                              |
|:-----------------------------------------------|:---------------------------------------------|
| ![alt text](../guides/images/entlastung_1.jpg) |![alt text](../guides/images/entlastung_2.jpg)|
*Abb.: Selbststudium mit KI von Luka Dimitrijevic*


**Hinweise zum freien Selbststudium**

Im Gegensatz zum *begleiteten* Selbststudium, bei dem die Studierenden von einer Lehrperson angeleitet werden, agieren die Studierenden beim *freien* Selbststudium autonom. Dies bedeutet, dass die Studierenden darauf achten müssen, die für sie relevanten Lerninhalte und deren Zusammenhänge selbstständig zu erkennen. Im Kontext der vollständigen Autonomie, wenn die Studierenden mit der KI interagieren, umfasst die kritische Betrachtung sowohl die Lerninhalte als auch die von der KI generierten Vorschläge und Inhalte. Beispielsweise sind KI-generierte Lernpläne zur Prüfungsvorbereitung als Vorschläge zu betrachten, die ggf. individuell angepasst werden müssen.

Der Einsatz von KI im *freien Selbststudium* kann verschiedene Vor- und Nachteile mit sich bringen:

| **Vorteile:**                                  | **Nachteile:**                               |
|:-----------------------------------------------|:---------------------------------------------|
| KI ermöglicht flexibleres Lernen <br> (z.B. schnelle Generierung von Quizfragen zur Wiederholung) | Fehlende soziale Einbindung |
| Individualisiertes Lernen <br> (Erklärung einzelner Sachverhalte, z.B. bei der Anwendung statistischer Methoden kann ChatGPT punktuell nach dem Rechenweg gefragt werden) | Fehlende direkte Interaktion <br>  (der Austausch mit Lehrenden und Mitstudierenden ist für den Lernerfolg unerlässlich) |
| Individuelle Auftragserteilung <br> (Generierung von individuellen Lernplänen) |  Keine Garantie, dass die KI-generierten Vorschläge mit den wichtigen Lehrinhalten des Unterrichts übereinstimmen oder für Prüfungen relevant sind, da die Führung durch die Lehrbeauftragten hier wegfällt |



---



## Drei Phasen 


Der von Luka Dimitrijevic vorgeschlagene Drei-Phasen-Ansatz strukturiert den Lernprozess in drei aufeinander aufbauende Phasen.


![alt text](../guides/images/3phasen_luca.jpg){style="width:400px"} <br>
*Abb.: 3-Phasen-Konzept, von Luka Dimitrijevic*
<br>

Ziel ist es, aus Informationen Wissen zu erarbeiten, das als Grundlage dient und in weiteren Schritten vertieft und verknüpft wird. Abschliessend wird das erworbene Wissen durch Anwendung gefestigt.

<br>
**Construct-Phase (Aufbau):** 

Hier geht es darum, Grundwissen und wesentliche Informationen zu einem Thema zu sammeln. Es geht um die Identifizierung und das Verständnis der Grundkonzepte, die für das weitere Lernen notwendig sind.

Die KI kann in dieser Phase als Werkzeug dienen, um Informationen zu sammeln und strukturiert darzustellen. Zum Beispiel kann ChatGPT verwendet werden, um einen strukturierten Lehrplan zu einem bestimmten Thema zu erstellen und helfen, wichtige Inhalte zu identifizieren und hervorzuheben.


```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: lernplangenerieren-chatgpt
```

<br>
**Connect-Phase (Verknüpfung):** 

Nachdem das Grundwissen erarbeitet wurde, geht es in der Connect-Phase darum, die Beziehungen und Zusammenhänge zwischen den verschiedenen Informationen zu erkennen und zu verstehen. Hier wird versucht, tiefere Zusammenhänge zu erkennen, was zu kritischem Denken anregt und ein umfassenderes Verständnis ermöglicht. 

![alt text](../guides/images/wissensbausteineverbinden_luca.jpg){style="width:500px"} <br>
*Abb.: Verknüpfung von "Wissensbausteinen", von Luka Dimitrijevic*
<br>

KI kann dabei helfen, komplexe Informationen gezielt zu vertiefen, um Zusammenhänge leichter erkennbar zu machen.



```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: wissenvertiefen-chatgpt
```

<br>
**Challenge-Phase (Herausforderung):**

In der letzten Phase wird das angeeignete Wissen angewendet und überprüft. Das kann durch die Durchführung eines Quiz oder durch die Überprüfung selbst erstellter Zusammenfassungen geschehen.

![alt text](../guides/images/challenge_kritischeval.jpg){style="width:500px"} <br>
*Abb.: Selbstüberprüfung, von Luka Dimitrijevic*
<br>

KI-Tools können hier zum Einsatz kommen, um beispielsweise Quizfragen zu generieren.


```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: fragengenerieren-chatgpt
```


---



## Links

Video des Discord Events, wo Luka Dimitrijevic seine Konzepte vorstellte:

- https://www.youtube.com/watch?v=R9V8KjDD39w



---


## Über diesen Beitrag

Beim Verfassen dieses Beitrags haben die Autor:innen ChatGPT-4 (Ver. 21.11.23), DeepL Write (Beta Ver. 21.11.2023) verwendet, um die sprachliche Darstellung ihrer Gedanken zu verbessern. Die volle Verantwortung für den Inhalt liegt bei den Autor:innen.

### Lizenz

![cc-by-sa-icon](../../leitlinien/images/Cc_by-sa_120x42.png){ align=left } Dieser Beitrag enthält Inhalte, die auf dem Modell (Construct, Connect, Challenge) von Luka Dimitrijevic basieren und wurde zusammen mit dem zugrunde liegenden Konzept während eines
<a rel="Discord-Event" href="https://www.youtube.com/watch?v=R9V8KjDD39w">Discord-Events am 3. November 2023 </a> im Rahmen des Projekts <a rel="bildung6" href="https://belearn.swiss/projekt/bildung-6-0-lernen-und-lehren-mit-ku%cc%88nstlicher-intelligenz-inklusion-statt-disruption/"> Bildung 6.0  </a> /  <a rel="belearn" href="https://belearn.swiss/"> BeLEARN </a> vorgestellt. Die inhaltliche und textliche Bearbeitung erfolgte durch das Projektteam von Bildung 6.0 / BeLEARN. Sowohl das Modell (Construct, Connect, Challenge) als auch das dazugehörige Konzept und dieser Beitrag stehen unter der <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution ShareAlike 4.0 (CC BY-SA 4.0 International License) </a> Lizenz.





