---
description: "ChatGPT nutzen, um dein Wissen zu vertiefen"
id: wissenvertiefen-chatgpt
image: "anwendungsfälle/images/chatbot.svg"
tags:
- studierende
title: Wissen aneignen und vertiefen mit ChatGTP
type: usecase
---


# Wissen aneignen und vertiefen mit ChatGPT

Die Aneignung und Vertiefung von Wissen im Selbststudium kann durch ChatGPT unterstützt werden, indem individuelle Erklärungen angeboten werden, die auf die spezifischen Fragen und Bedürfnisse der Lernenden zugeschnitten sind.


## Beschreibung

ChatGPT fördert den Wissenserwerb und die Wissensvertiefung im Selbststudium, indem es als interaktiver Gesprächspartner fungiert, der auf punktuelle Fragen reagiert und individuelle Erklärungen liefert. Es ermöglicht eine gesprächsbasierte Lernumgebung, in der Lernende durch gezielte Fragen tiefere Einblicke gewinnen und komplexe Zusammenhänge verständlich erklärt bekommen.



## Beispiele

Durch das Einsetzen eines Chatbots in der Rolle eines Tutors können Lernende in einer konversationellen Form Fragen stellen und erhalten daraufhin massgeschneiderte Antworten sowie praktische Beispiele, die das Verständnis fördern und den Lernprozess interaktiv gestalten.


### Mit ChatGPT lernen

ChatGPT-3.5 wurde hier gebeten, die Rolle eines Tutors zu übernehmen und beantwortete zunächst eine spezifische Frage. Durch Nachfragen konnte der Chatbot zusätzliche Erklärungen liefern, was den Lernprozess beschleunigte, da keine Sekundärliteratur konsultiert werden musste.


<table >
  <tr>
    <th>Beispiel</th>
  </tr>
  <tr>
    <td bgcolor="5D6CC0">
      <p style="color:white">
        <i>Input:</i></td>
      </p>
  </tr>
  <tr>
    <td bgcolor="5D6CC0">
      <p style="color:white">
       Nimm die Rolle eines Tutors ein, der in Deep Learning, Machine Learning und Python spezialisiert ist und Studierende beim Lernen unterstützt.
      </p>
    </td>
  </tr>
  <tr>
    <td bgcolor="white"><i>Output:</i></td>
  </tr>
  <tr>
    <td bgcolor="white">
    Selbstverständlich, ich übernehme gerne die Rolle eines Tutors für Deep Learning, Machine Learning und Python. Wie kann ich Ihnen bei Ihrem Lernprozess behilflich sein? Haben Sie Fragen zu bestimmten Konzepten, möchten Sie Ratschläge zur Auswahl von Projekten oder benötigen Sie Hilfe bei der Lösung von Problemen? Lassen Sie mich wissen, wie ich Ihnen am besten helfen kann.
    </td>
  </tr>
  <tr>
    <td bgcolor="5D6CC0">
      <p style="color:white">
        <i>Input:</i></td>
      </p>
  </tr>
  <tr>
    <td bgcolor="5D6CC0">
      <p style="color:white">
       Erkläre mir in 1 und 2 Sätzen  welche Ableitungsregel bei Neuronalen Netzen genutzt wird, bezüglich Backpropagation.
      </p>
    </td>
  </tr>
  <tr>
    <td bgcolor="white"><i>Output:</i></td>
  </tr>
  <tr>
    <td bgcolor="white">
    Bei Backpropagation in neuronalen Netzen wird die Kettenregel verwendet, um die Ableitungen der Verlustfunktion nach den Gewichtungen und Bias der Neuronen in den Schichten des Netzwerks zu berechnen. Diese Ableitungen sind entscheidend für das Trainieren des Netzes durch Anpassen der Gewichtungen und Bias während des Lernprozesses.
    </td>
  </tr>
  <tr>
  <tr>
    <td bgcolor="5D6CC0">
      <p style="color:white">
        <i>Input:</i></td>
      </p>
  </tr>
  <tr>
    <td bgcolor="5D6CC0">
      <p style="color:white">
       Erkläre mir die Ableitungsregel und gib mir ein Beispiel einer Anwendung bei einem Neuronalen Netz.
      </p>
    </td>
  </tr>
  <tr>
    <td bgcolor="white"><i>Output:</i></td>
  </tr>
  <tr>
    <td bgcolor="white">
    Die Ableitungsregel, die in Backpropagation für neuronale Netze verwendet wird, ist die Kettenregel. Die Kettenregel ermöglicht es, die Ableitungen einer verschachtelten Funktion zu berechnen, indem sie die Ableitungen der inneren Funktionen miteinander verknüpft.
    <br>
    <br>
    Hier ist die mathematische Form der Kettenregel:
    <br>
    <br>
    Wenn Sie eine Funktion f(g(x)) haben, wobei f und g Funktionen sind, dann ist die Ableitung dieser verschachtelten Funktion f'(g(x)) * g'(x), wobei f'(g(x)) die Ableitung von f nach g(x) ist und g'(x) die Ableitung von g nach x ist. ...
    </td>
  </tr>
  <tr>
  <tr>
    <td  bgcolor="f1f1f1"><i>Chatverlauf: Mit ChatGPT-3.5 lernen. Nutze diesen <a href="https://chat.openai.com/share/7fb908d1-f657-426f-9e43-fc86cfb738f9"> Link,</a>um den Chatverlauf (ChatGPT-3.5) zu diesem Beispiel anzuschauen.</a></i>
    </td>
  </tr>
</table>



---


## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: equals
  property: id
  value: halluzinationen
```


---

## Chancen

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: entlastung-durch-automatisierung
```


---

## Über diesen Beitrag

Beim Verfassen dieses Beitrags haben die Autor:innen ChatGPT-3.5 (Ver. 21.11.2023) und DeepL Write (Ver. 21.11.2023) verwendet, um die sprachliche Darstellung ihrer Gedanken zu verbessern. Die volle Verantwortung für den Inhalt liegt bei den Autor:innen. 


---


## Links

OpenAI, ChatGPT-Entwicklerseite:

- https://openai.com/


OpenAI Blog "Teaching with AI":

- https://openai.com/blog/teaching-with-ai


Chatverlauf: Mit ChatGPT-3.5 lernen:

- https://chat.openai.com/share/7fb908d1-f657-426f-9e43-fc86cfb738f9


