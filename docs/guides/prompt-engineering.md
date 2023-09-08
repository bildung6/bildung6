---
description: "Bessere Prompts schreiben"
id: guide
image: guides/images/engineers.svg
tags:
- studierende
title: Bessere Chatbot-Antworten mit Prompt-Engineering
type: guide
--- 

???+ info "Intro"

    **An wen richtet sich dieser Guide?**<br>
    Dieser Guide richtet sich an alle, insbesondere an diejenigen, die Anregungen für einen effizienteren Umgang mit Chatbots (wie ChatGPT) suchen.

    **Was findest du hier?**<br>
    Hier findest du Tipps, wie du deine Prompts optimieren kannst, um bessere Chatbot-Antworten zu erhalten. Generell gilt für Chatbots: Je besser die Prompts, desto besser die Antworten.


    **Wie kannst du die Inhalte hier nutzen?**<br>
    Wir haben hier einige Strategien und Taktiken aus dem Bereich "Prompt Engineering" zusammengestellt. Die Strategien sind eher nur allgemeine Hinweise und dienen vor allem als Aufhänger für die Taktiken. Unter den Taktiken findest du konkrete Vorschläge und Beispiele.

    *Du kannst auch gerne die ganzen Erklärungen überspringen und nur die einzelnen Promptbeispiele "copy-pasten", um selbst damit zu experimentieren.*

    **Woher stammen die hier gezeigten Inhalte?**<br>
    Die Idee, die Tipps in Strategien und Taktiken zu unterteilen, haben wir teilweise aus den "Best Practices" der OpenAI-Dokumentation zur ChatGPT-API (GPT-4) übernommen und stellenweise ergänzt.

    Ganz unten finden sich Links, die u.a. zu den verwendeten Quellen führen.

    **Funktionieren die gezeigten Inhalte?**<br>
    Die meisten Beispiele wurden im September 2023 mit ChatGPT-3.5 getestet. Allerdings funktionieren sie mit anderen Chatbots(wie Bard von Google) möglicherweise nicht so gut. Auch kann es sein, dass die hier vorgestellten Inhalte mit jeder neuen Version von ChatGPT an Aktualität verlieren, bzw. nicht mehr effizient sind. 
    
    ***Tipp: Bevor du aufgibst, versuche beim Ausprobieren der Beispiele einen neuen Chat-Dialog zu öffnen oder benutze den "Regenerate"-Button in ChatGPT, um eine von mehreren Antworten auszuwählen.***



## Über Prompts

Prompts sind textbasierte Anfragen oder Befehle, die bei der Interaktion mit Large Language Models (LLMs) wie GPT-3.5 oder GPT-4 verwendet werden. Sie dienen als Eingabeaufforderungen, um eine bestimmte Ausgabe oder Antwort vom Modell zu erhalten. Während der Entwicklung oder des Trainings eines LLM werden Prompts verwendet, um das Verhalten des Modells zu testen und zu optimieren. 

Für **Endbenutzer:innen** sind Prompts das wichtigste Mittel, um mit Systemen wie ChatGPT zu kommunizieren, Fragen zu stellen, Text zu generieren oder bestimmte Aufgaben auszuführen. Prompts sind relevant, da sie die Qualität und Relevanz der Antworten des Modells beeinflussen können. Gut formulierte Prompts ermöglichen präzise, kontextbezogene und nuancierte Antworten. 

Um effektive Prompts zu schreiben, sollten diese z.B. klar und eindeutig formuliert sein, den Kontext berücksichtigen und ggf. mehrere Versuche erfordern, um die optimale Formulierung zu finden. 

??? info "Was ChatGPT-3.5 zur Formulierung von Prompts sagt:"

    *Diese Punkte können dazu beitragen, die Interaktion mit ChatGPT effizienter und informativer zu gestalten:*

    **Klarheit und Präzision:**	Formulieren Sie Ihre Fragen oder Anweisungen klar und eindeutig. Vagheit oder Mehrdeutigkeit kann zu ungenauen oder nicht hilfreichen Antworten führen.

    **Kontext bieten:** Wenn Ihre Frage auf vorherige Informationen aufbaut oder spezifisch ist, geben Sie ausreichend Kontext. Dies hilft dem Modell, Ihre Anfrage besser zu verstehen.

    **Frageform:** Überlegen Sie, ob eine offene oder geschlossene Frage angebracht ist. Offene Fragen fördern ausführlichere Antworten, während geschlossene Fragen kurze, direkte Antworten hervorbringen.

    **Zielformat definieren:** Wenn Sie eine bestimmte Art von Antwort möchten (z.B. eine Liste, ein Absatz, etc.), geben Sie dies in Ihrer Anfrage an.

    **Anzahl der gewünschten Punkte oder Beispiele:** Wenn Sie eine Liste von Punkten oder Beispielen wollen, geben Sie die gewünschte Anzahl an. Zum Beispiel: "Nenne mir drei Vorteile von…"

    **Begrenzung der Antwortlänge:** Wenn Sie eine kurze Antwort möchten, können Sie das explizit angeben, etwa "Bitte fasse die Antwort in einem Satz zusammen."

    **Fachspezifische Anfragen:** Wenn Ihre Frage fachspezifisch ist, versuchen Sie, die relevante Terminologie zu verwenden, damit das Modell den Kontext besser versteht.

    **Überprüfung der Informationen:** Denken Sie daran, dass ChatGPT zwar viele Informationen bereithält, aber nicht immer 100% akkurat ist. Für kritische Anwendungen sollten Sie die bereitgestellten Informationen überprüfen.

    **Anpassungen und Nachfragen:** Zögern Sie nicht, Nachfragen zu stellen oder das Modell um Klarstellungen zu bitten, wenn die erste Antwort nicht ausreichend oder klar ist.

    **Explizite ethische oder praktische Einschränkungen:** Wenn es ethische oder praktische Grenzen für Ihre Anfrage gibt, geben Sie diese an. Zum Beispiel: "Geben Sie mir Vorschläge, die umweltfreundlich sind."


## Allgemeingültige Prinzipen
Bevor wir zu den Strategien, Taktiken und Beispiel überhehen, hier noch ein paar allgemeingültige Tipps:

-	Formuliere deine Prompts klar und spezifisch
-	Sage dem Chatbot, was er tun soll, anstatt ihm vorzugeben, was er nicht tun soll
-	Reichere deine Prompts mit Details an
- Überprüfe ggf. die Antworten
- Experimentiere: schreibe um, kombiniere verschiedene "Taktiken", vergleiche deine Ergebnisse 

***Mit dem Gebrauch einer klaren und spezifischen Sprache lässt sich der Chatbot quasi in die korrekte Richtung lenken.*** 


## Strategie: Schreibe klare Instruktionen
Mit klar und spezifisch formulierten Anweisungen lässt sich vermeiden, dass dem LLM hinter dem Chatbot zu viel Interpretationsspielraum zugelassen wird. 


### Taktik: Details und Kontext angeben 
Um eine relevante Antwort zu erhalten, solltest du sicherstellen, dass die Anfragen alle wichtigen Details oder den Kontext enthalten. Andernfalls überlasst man es dem Modell, zu erraten, was du meinst (1). 

<table>
  <caption align="bottom"> 
    <div align="left" text-format="italic">
      <p style="text-indent:10px">
        <i>Beispiele mit optimierten Prompts. Quelle: 
            <a href="https://platform.openai.com/docs/guides/gpt-best-practices/tactic-include-details-in-your-query-to-get-more-relevant-answers">
              GPT Best Practises (OpenAI API), von OpenAI
            </a>
        </i>
      </p>
    </div>
  </caption>
  <tr>
    <th>Schlecht</th>
    <th>Besser</th>
  </tr>
  <tr>
    <td bgcolor="Snow">Wie kann ich in Excel Zahlen hinzufügen?</td>
    <td bgcolor="HoneyDew">Wie addiere ich eine Reihe von Dollarbeträgen in Excel? Ich möchte dies automatisch für ein ganzes Blatt von Zeilen tun, wobei alle Summen rechts in einer Spalte mit der Bezeichnung "Total" enden.</td>
  </tr>
  <tr>
    <td bgcolor="Snow">Wer ist Präsident?</td>
    <td bgcolor="HoneyDew">Wer war 2021 der Präsident Mexikos, und wie häufig werden Wahlen abgehalten?</td>
  </tr>
    <tr>
    <td bgcolor="Snow">Schreibe einen Code zur Berechnung der Fibonacci-Folge.</td>
    <td bgcolor="HoneyDew">Schreibe eine TypeScript-Funktion zur effizienten Berechnung der Fibonacci-Folge. Kommentiere den Code grosszügig, um zu erklären, was jeder Teil tut und warum er so geschrieben ist.</td>
  </tr>
    <tr>
    <td bgcolor="Snow">Fasse die Besprechungsnotizen zusammen.</td>
    <td bgcolor="HoneyDew">Fasse die Besprechungsnotizen in einem einzigen Absatz zusammen. Erstelle dann eine Liste der Redner und ihrer wichtigsten Punkte. Führe abschliessend die von den Rednern vorgeschlagenen nächsten Schritte oder Massnahmen auf, falls vorhanden. </td>
  </tr>
</table>


### Taktik: Role Prompting
Weist man dem Chatbot eine bestimmte Rolle (oder Persona) zu, spiegelt sich diese in seinen Antworten wider. Dies kann z.B. genutzt werden, wenn die Antworten in einer fachspezifischen Sprache erfolgen oder fachspezifische Inhalte enthalten sollen. 

***Tipp:** Im Internet gibt es etliche Beispiele, die unter den Begriffen "Role Prompting", "Persona", "Assigning Roles", "Role Based Prompts" oder "Act as" aufgefürt sind.*

<table>
  <caption align="bottom"> 
    <div align="left" text-format="italic">
      <p style="text-indent:10px">
        <i>Beispiele von Role Prompting für rollenspezifische Antworten. 
       </i>
     </p>
    </div>
  </caption>
  <tr>
    <th>Beispiele</th>
    <th>Bemerkungen</th>
  </tr>
  <tr>
    <td bgcolor="HoneyDew"><mark>Nimm die Rolle eines Studentenbetreuers an...</mark></td>
    <td bgcolor="White"></td>
  </tr>
    <tr>
    <td bgcolor="HoneyDew"><mark>...antworte mit einem konstruktiven Vorschlag zu jedem Kritikpunkt.</mark></td>
    <td bgcolor="White"></td>
  </tr>
    <tr>
    <td bgcolor="HoneyDew"><mark>...antworte mit kurzen und objektiven Antworten.</mark></td>
    <td bgcolor="White"></td>
  </tr>
  <tr>
    <td bgcolor="HoneyDew">
      <mark>Verhalte dich wie ein wissenschaftlicher Betreuer, der Studenten an einer Hochschule Feedback zum Schreiben wissenschaftsjournalistischer Artikel gibt.<br>
      Überprüfe und bewerte kritisch</mark> den aktuellen Stand dieses Teils meines wissenschaftsjournalistischen Artikels.<br>
      Beurteile die Klarheit meiner Erklärungen, die sprachliche Gewandtheit und die Art und Weise, wie ich den Text strukturiert habe, und<mark> übe konstruktive Kritik zu jedem Punkt.</mark><br>
      <mark> Achte darauf, den Text im Hinblick auf das geforderte Niveau wissenschaftsjournalistischen Schreibens zu beurteilen </mark> und gib an erster Stelle an, ob der Text das Niveau erreicht. <br><br>
      """<...Text...>"""
    </td>
    <td bgcolor="White">Eine etwas ausführlicher Prompt, um ein Feedback zur geschriebener Seminararbeit einzuholen.<br><br>
      Die hier verwendeten Prompts basieren teilweise auf Inhalte dieser Quellen:<br><br>
      <a href="https://github.com/f/awesome-chatgpt-prompts"><i>Awesome ChatGPT Prompt Repositiry von Fatih Kadir Akın</a><br><br>
      <a href="https://www.scribbr.com/ai-tools/chatgpt-assignments/"><i>Using ChatGPT for Assignments von Scribbr.com</a>
    </td>
  </tr>
</table>



### Taktik: Trennzeichen nutzen

Trennzeichen können verwendet werden, um dem Chatbot mitzuteilen, dass bestimmte Teile deines Prompts unterschiedlich zu behandeln sind (1).

Beispielsweise wird nach der eigentlichen Anweisung, eine Textzusammenfassung zu erstellen, der zusammenzufassende Text mit drei Anführungszeichen ("""...""") markiert, oder mit einem Präfix (Text: ..., Titel: ..., etc.).


<table>
  <caption align="bottom"> 
    <div align="left" text-format="italic">
      <p style="text-indent:10px">
        <i>Beispiel zum Nutzen von Trennzeichen. Auf Basis von
          <a href="https://platform.openai.com/docs/guides/gpt-best-practices/tactic-use-delimiters-to-clearly-indicate-distinct-parts-of-the-input">
            GPT Best Practises (OpenAI API), von OpenAI.
          </a>
       </i>
     </p>
    </div>
  </caption>
  <tr>
    <th>Beispiel</th>
    <th>Bemerkung</th>
  </tr>
  <tr>
    <td width="50%" bgcolor="HoneyDew">Fasse den in Anführungszeichen gesetzten Text auf Deutsch zusammen.<br><br>
      <mark>"""</mark>Lorem ipsum...<mark>"""</mark></td>
    <td width="50%" bgcolor="White"></td>
  </tr>
</table>



### Taktik: Step-by-Step anleiten
Einige Aufgaben lassen sich am besten als eine Abfolge von Schritten beschreiben. Wenn die Schritte explizit aufgeschrieben werden, kann das Modell sie leichter nachvollziehen (1).


<table>
  <caption align="bottom"> 
    <div align="left" text-format="italic">
      <p style="text-indent:10px">
        <i>Beispiele von Step-by-Step Anleitungen.</i>
     </p>
    </div>
  </caption>
  <tr>
    <th>Beispiel</th>
    <th>Bemerkung</th>
  </tr>
  <tr>
    <td width="50%" bgcolor="HoneyDew">
      Befolge die folgenden Schritt-für-Schritt-Anweisungen, um auf meine Eingaben zu reagieren.
      <br>
      <br>
      Schritt 1 - Ich gebe dir einen in dreifachen Anführungszeichen gesetzten Text. Fasse diesen Text in einem Satz mit dem Präfix "Zusammenfassung:" zusammen. 
      <br>
      <br>
      Schritt 2 - Übersetzen Sie die Zusammenfassung aus Schritt 1 ins Englische, mit einem Präfix "Uebersetzung:".
      <br>
      <br>
      """Lorem ipsum, ..."""
    </td>
    <td bgcolor="white"></td>
  </tr>
  <tr>
    <td bgcolor="HoneyDew">
      Halte dich an diese Schritte um auf meine Fragen zu reagieren: 
      <br>
      <br>
      Step 1 - Ich werde dir einen Text geben, der durch dreifache Anführungszeichen (""") begrenzt ist, merke dir diesen Text im weiteren Chat-Verlauf.
      <br>
      <br>
      Step 2 - Du bestätigst, dass du den Text erhalten hast und sagst mir, dass du nun bereit bist für meine Fragen. 
      <br>
      <br>
      Step 3- Du beantwortest jeder meiner Fragen, indem du den angegebenen Text verwendest. Wenn du die Antwort im angegebenen Text nicht findest, schreibe immer "Ich konnte keine Antwort finden". 
      <br>
      <br>
      """Lorem ipsum, ..."""
    </td>
    <td bgcolor="white">Dies ist eine erweiterte Version der obrigen Anweisung. Mit Step 2 und 3 wollten wir erreichen, dass der Chatbot auf unsere Fragen wartet. Ohne diese Anpassung hatte ChatGPT (ChatGPT-3.5) z.T. kuriose Antworten generiert. 
    <br>
    <br>
    Nutze diesen <a href="https://chat.openai.com/share/255d000a-6b4c-4452-b85b-0c179bbf8adb"> <i>Link,</i></a>um einen Chatverlauf (ChatGPT-3.5) zu diesem Beispiel anzuschauen. Der damals verwendete Text stammte von Wikipedia:  <br> (https://de.wikipedia.org/wiki/Joseph_Bazalgette).
    </td>
  </tr>
</table>


### Taktik: Beispiele angeben
 In einigen Fällen kann es einfacher sein, Beispiele für die erwartete Antwort zu geben. Zum Beispiel, wenn du beabsichtigst, dass das Modell einen bestimmten Stil der Beantwortung von Benutzeranfragen kopiert, der schwer explizit zu beschreiben ist (1). 

*Bemerkung: Das Angeben von Beispielen wird als «one shot», «two shot»-, bzw. «few-shot»-Prompting bezeichnet, wobei «shot» ein Synonym für «Beispiel» ist.*


<table>
  <caption align="bottom"> 
    <div align="left" text-format="italic">
      <p style="text-indent:10px">
        <i>Beispiel mit Few Shots.</i>
     </p>
    </div>
  </caption>
  <tr>
    <th>Beispiel</th>
    <th>Bemerkung</th>
  </tr>
  <tr>
     <td width="70%" bgcolor="HoneyDew">
    <i>Input:</i>
    </td>
  </tr>
    <td bgcolor="HoneyDew">
      Suggest three names for an animal that is a superhero.<br><br>
      <mark>Animal: Cat<br>
      Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline<br>
      Animal: Dog<br>
      Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot<br>
      Animal: Horse</mark><br>
      Names:
    </td>
    </td>
     <td bgcolor="white"> Quelle: <a href="https://platform.openai.com/docs/quickstart/add-some-examples">Quickstart (OpenAI API), von OpenAI</a>
    </td>
  </tr>
     <tr>
     <td bgcolor="F7F7F8">
      <i>Output:</i>
    </td>
  </tr>
    </tr>
     <tr>
     <td bgcolor="F7F7F8">
        For a superhero horse:<br>
        1. Thunderhoof<br>
        2. Equine Avenger<br>
        3. Stallion Sentinel<br>
  </tr>
</table>

<table>
  <caption align="bottom"> 
    <div align="left" text-format="italic">
      <p style="text-indent:10px">
        <i>Beispiel mit Few Shots.</i>
     </p>
    </div>
  </caption>
  <tr>
    <th>Beispiel</th>
    <th>Bemerkung</th>
  </tr>
  <tr>
     <td width="70%" bgcolor="HoneyDew">
    <i>Input:</i>
    </td>
  </tr>
    <td bgcolor="HoneyDew">
      Vervollständige<br><br>
      <mark>
        Typ: Blutzellen<br>
        Zellen: Erythrozyten, Leukozyten, Thrombozyten<br>
        Typ: Muskelzellen<br>
        Zellen: Skelettmuskulaturzellen, Herzmuskelzellen, glatte Muskelzellen<br>
      </mark>
        Typ: Gewebszellen<br>
        Zellen:<br>
    </td>
    </td>
     <td bgcolor="white">
      Nutze diesen <a href="https://chat.openai.com/share/febc2132-2245-4f37-9294-3d27d6e7c210"> <i>Link,</i></a>um den Chatverlauf (ChatGPT-3.5) zu diesem Beispiel anzuschauen.</a>
    </td>
  </tr>
     <tr>
     <td bgcolor="F7F7F8">
      <i>Output:</i>
    </td>
  </tr>
    </tr>
     <tr>
     <td bgcolor="F7F7F8">
        Typ: Gewebszellen<br>
        Zellen: Fibroblasten, Epithelzellen, Adipozyten (Fettzellen), Chondrozyten (Knorpelzellen), Osteozyten (Knochenzellen), Neuronen (Nervenzellen), Astrozyten (Gliazellen), Makrophagen, Mastzellen, Endothelzellen
  </tr>
</table>

<table>
  <caption align="bottom"> 
    <div align="left" text-format="italic">
      <p style="text-indent:10px">
        <i>Beispiel mit Few Shots.</i>
     </p>
    </div>
  </caption>
  <tr>
    <th>Beispiel</th>
    <th>Bemerkung</th>
  </tr>
  <tr>
     <td width="70%" bgcolor="HoneyDew">
    <i>Input:</i>
    </td>
  </tr>
    <td bgcolor="HoneyDew">
      Vervollständige<br><br>
      <mark>
       Input: "Stunde","Montag","Dienstag","Mittwoch","Donnerstag","Freitag" <br>
       Output: Stunde,Montag,Dienstag,Mittwoch,Donnerstag,Freitag<br>
       Input: "1","Mathematik","Deutsch","Englisch","Erdkunde","Politik"<br>
       Output: 1,Mathematik,Deutsch,Englisch,Erdkunde,Politik<br>
       Input: 'Sport','Religion','Kunst'<br>
       Output: Sport,Religion,Kunst<br>
      </mark>
       Input: 'Wüste', 'Tundra', 'Gebirge', 'Oase'<br>
       Output:
    </td>
    </td>
     <td bgcolor="white">
      Nutze diesen <a href="https://chat.openai.com/share/46eb4f1f-137b-4585-9c32-eb981ef7ac9d"> <i>Link</i></a>, um den Chatverlauf (ChatGPT-3.5) zu diesem Beispiel anzuschauen.</a>
    </td>
  </tr>
     <tr>
     <td bgcolor="F7F7F8">
      <i>Output:</i>
    </td>
  </tr>
    </tr>
     <tr>
     <td bgcolor="F7F7F8">
       Wüste,Tundra,Gebirge,Oase
  </tr>
</table>

<table>
  <caption align="bottom"> 
    <div align="left" text-format="italic">
      <p style="text-indent:10px">
        <i>Beispiel wie ChatGPT aus dem Referenztext zitieren soll.</i>
     </p>
    </div>
  </caption>
  <tr>
    <th>Beispiel</th>
    <th>Bemerkung</th>
  </tr>
  <tr>
     <td width="70%" bgcolor="HoneyDew">
    <i>Input:</i>
    </td>
  </tr>
    <td bgcolor="HoneyDew">
      You will be provided with a document delimited by triple quotes and a question. The you will wait for my questions. Your task is then to answer the question using only the provided document and to cite the passage(s) of the document used to answer the question. If the document does not contain the information needed to answer this question then simply write: "Insufficient information." If an answer to the question is provided, it must be annotated with a citation. Use always the following format for to cite relevant passages <mark> like ({"citation": the person was born in berlin}) </mark>
      <br><br>
      """Das Haus Anjou-Plantagenêt (französisch [ɑ̃ˈʒu-ˌplɑ̃taʒ'nɛ], ..."""
    </td>
    </td>
     <td bgcolor="white">
      Quelle:<a href="https://platform.openai.com/docs/guides/gpt-best-practices/tactic-instruct-the-model-to-answer-with-citations-from-a-reference-text">GPT Best Practises (OpenAI API), von OpenAI </a>und leicht adaptiert.
      <br>
      <br>
      Nutze diesen <a href="https://chat.openai.com/share/e9d59f03-ce82-498d-b076-be1556a32456"> <i>Link,</i></a>um einen Chatverlauf (ChatGPT-3.5) zu diesem Beispiel anzuschauen. Der dort verwendete Text stammte aus einem Wikipedia-Eintrag: <br> https://de.wikipedia.org/wiki/Haus_Plantagenet
    </td>
  </tr>
</table>


### Taktik: Gewünschtes Antwortformat verlangen
Das Modell kann angewiesen werden, Ausgaben mit einer bestimmten Ziellänge zu erzeugen. Die gewünschte Ausgabelänge kann als **Anzahl von Wörtern, Sätzen, Absätzen, Aufzählungspunkten usw.** angegeben werden. 

Es ist jedoch zu beachten, dass die Anweisung an das Modell, eine bestimmte Anzahl von Wörtern zu erzeugen, nicht mit hoher Genauigkeit funktioniert. Das Modell kann zuverlässiger Ausgaben mit einer bestimmten Anzahl von Absätzen oder Aufzählungspunkten erzeugen (1).


<table>
  <caption align="bottom"> 
    <div align="left" text-format="italic">
      <p style="text-indent:10px">
        <i>Beispiele zu gewünschten Antwortformaten. Quelle:<a href="https://platform.openai.com/docs/guides/gpt-best-practices/tactic-specify-the-desired-length-of-the-output">GPT Best Practises (OpenAI API) von OpenAI</a></i>
     </p>
    </div>
  </caption>
  <tr>
    <th>Beispiele</th>
    <th>Bemerkungen</th>
  </tr>
  <tr>
    <td bgcolor="HoneyDew">Fasse den durch dreifache Anführungszeichen markierten Text in <mark>etwa 50 Wörtern</mark> zusammen.<br>
    """Lorem ipsum, ... """</td>
    <td bgcolor="White"></td>
  </tr>
  <tr>
    <td bgcolor="HoneyDew">Fasse den durch dreifache Anführungszeichen abgegrenzten Text in <mark>2 Absätzen</mark> zusammen.<br>
    """Lorem ipsum, ... """</td>
    <td bgcolor="White"></td>
  </tr>
    <tr>
    <td bgcolor="HoneyDew">Fasse den durch dreifache Anführungszeichen abgegrenzten Text in <mark>3 Bullet Points </mark>zusammen.<br>
    """Lorem ipsum, ... """</td>
    <td bgcolor="White"></td>
  </tr>
</table>


---


## Strategie: Referenztexte nutzen
Chatbots wie ChatGPT generieren ihre Antworten anhand der verwendeten Trainingsdaten, was in einigen Fällen unzureichend sein kann. Im Falle von ChatGPT ist es möglich, einen Referenztext zur Verfügung zu stellen und den Chatbot anzuweisen, Antworten auf der Grundlage dieses Textes zu generieren. Zum Beispiel, um dem Chatbot Fragen zu einem bestimmten Artikel zu stellen.

***Hinweis:*** *Zu beachten ist, dass bei ChatGPT die Grösse der Prompts begrenzt ist (Context Limit) und längere Referenztexte diesen Rahmen schnell sprengen können. Dieses Problem kann ggf. dadurch umgangen werden, indem der Referenztext abschnittsweise in "Chunks" mit mehreren Prompts übermittelt wird (siehe "Strategie: In Teile zerlegen").*


### Taktik: Referenztexte als Basis für Antworten
Um Antworten zu generieren, die spezifisch für den Referenztext sind, kann der Chatbot angewiesen werden, Fragen mit Hilfe des übermittelten Textes zu beantworten (1).


<table>
  <caption align="bottom"> 
    <div align="left" text-format="italic">
      <p style="text-indent:10px">
        <i>Beispiel: Referenztexte als Basis für Antworten</i>
     </p>
    </div>
  </caption>
  <tr>
    <th>Beispiele</th>
    <th>Bemerkungen</th>
  </tr>
  <tr>
    <td width="70%" bgcolor="HoneyDew">
    Halte dich an diese Schritte um auf meine Fragen zu reagieren: 
    <br>
    <br>
    Step 1 - Ich werde dir einen Text, der durch dreifache Anführungszeichen (""") begrenzt ist, merke dir diesen Text im weiter Verlauf unserer Konversation (""") 
    <br>
    <br>
    Step 2 - Du bestätigst, dass du den Text erhalten hast und sagst mir, dass du nun bereit bist für meine Fragen 
    <br>
    <br>
    Step 3- Du beantwortest jeder meiner Fragen, indem du den angegebenen Text verwendest. Wenn du die Antwort im Angegebenen Text findest, schreibe "Ich konnte keine Antwort finden". 
    <br>
    <br>
    """Sir Joseph William Bazalgette (Aussprache: /ˈbæzəldʒɛt/; * 28. März 1819..."""
    </td>
    <td bgcolor="White">
    Dieser Prompt basiert auf den <a href="https://platform.openai.com/docs/guides/gpt-best-practices/tactic-instruct-the-model-to-answer-using-a-reference-text"> "Best Practices" der englischen OpenAI-Dokumentation zur OpenAI-API</a>. Wir haben die dortigen Prompts übersetzt und adaptiert. Da das Hochladen von Dokumenten bei der Freemium-Version noch nicht möglich war (Stand August 2023), wurde der Referenztext direkt in den Prompt reinkopiert.
    <br>
    <br>
    Nutze diesen <a href="https://chat.openai.com/share/255d000a-6b4c-4452-b85b-0c179bbf8adb"> <i>Link,</i></a>um einen Chatverlauf (ChatGPT-3.5) zu diesem Beispiel anzuschauen. Der dort verwendete Text stammte aus einem Wikipedia-Eintrag: <br> https://de.wikipedia.org/wiki/Joseph_Bazalgette
    </td>
  </tr>
</table>



### Taktik: Antworten mit Zitaten aus einem Referenztext generieren
Hier wird die oben beschriebene Taktik erweitert, indem der Chatbot angewiesen wird, die entsprechenden Passagen des Referenztextes wiederzugeben. Dies kann bei der Überprüfung der generierten Antworten hilfreich sein. Beispielsweise kann das Nachschlagen im verwendeten Referenztext so erleichtert werden.


<table>
  <caption align="bottom"> 
    <div align="left" text-format="italic">
      <p style="text-indent:10px">
        <i>Beispiel: Referenztexte als Basis für Antworten nutzen und mit Zitierungshinweisen antworten lassen.</i>
     </p>
    </div>
  </caption>
  <tr>
    <th>Beispiel</th>
    <th>Bemerkung</th>
  </tr>
  <tr>
    <td width="70%" bgcolor="HoneyDew">
      You will be provided with a document delimited by triple quotes and a question. The you will wait for my questions. Your task is then to answer the question using only the provided document and to cite the passage(s) of the document used to answer the question. If the document does not contain the information needed to answer this question then simply write: "Insufficient information." <mark> If an answer to the question is provided, it must always be annotated with a citation. Use always the following format for to cite relevant passages like ({"citation": the person was born in berlin})</mark> 
      <br>
      <br>
      Text:<br>
      """Sir Joseph William Bazalgette (Aussprache: /ˈbæzəldʒɛt/; 
    </td>
    <td bgcolor="white">
      Dies ist eine erweiterte Version der obrigen Anweisung. Mit Step 2 und 3 wollten wir erreichen, dass der Chatbot auf unsere Fragen wartet. Ohne diese Anpassung hatte ChatGPT (ChatGPT-3.5) z.T. kuriose Antworten generiert. 
      <br>
      <br>
      Nutze diesen <a href="https://chat.openai.com/share/58e061e4-a89a-47f4-ab72-649e0486319c">
          <i>Link,</i>
        </a>
      um einen Chatverlauf (ChatGPT-3.5) zu diesem Beispiel anzuschauen. Der damals verwendete Text stammte von Wikipedia: 
      <br>
      (https://de.wikipedia.org/wiki/Joseph_Bazalgette).
    </td>
  </tr>
</table>


---


## Strategie: In Teile zerlegen
Manchmal ist es sinvoller komplexere Aufgaben in kleinere Teilaufgaben zu zerlegen. 


### Taktik: Lange Texte stückweise übermitteln
Die Verarbeitung grösserer Texte kann ggf. durch das vorhandene Context Limit verhindert werden. Beispielsweise können längere Texte, die der Chatbot zusammenfassen soll, nicht in einem Prompt übermittelt werden. Diese Einschränkung lässt sich ggf. umgehen, indem die Texte in "Chunks" mit mehreren Prompts übermittelt werden.


<table>
  <caption align="bottom"> 
    <div align="left" text-format="italic">
      <p style="text-indent:10px">
        <i>Beispiel eines langen Texts, der stückweise übermittelt wird.</i>
     </p>
    </div>
  </caption>
  <tr>
    <th>Beispiel</th>
    <th>Bemerkung</th>
  </tr>
  <tr>
    <td width="60%" bgcolor="HoneyDew">
      <mark>Do not answer yet. This is just another part of the text I want to send you. Just receive and acknowledge as "Part 1/2 received" and wait for the next part.</mark>
      <br>
      <mark>[START PART 1/2]</mark>
      <br>
      """Lorem ipsum dolor sit amet, consetetur sadipscing elitr,  sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet..."""
      <br>
      <mark>[END PART 1/2]</mark>
      <br>
      <mark>Remember not answering yet. Just acknowledge you received this part with the message "Part 1/2 received" and wait for the next part.</mark>
    </td>
    <td bgcolor="white">
      Diese Prompts wurden aus dem <a href="https://chatgpt-prompt-splitter.jjdiaz.dev/">
        <strong><i>ChatGPT PROMPTs Splitter</strong></i> von Jose Diaz</a> übernommen. Mit diesem Tool lassen sich längere Texte einfach und mit passenden Prompt-Anweisungen aufteilen.
      <br>
      <br>
      Im ersten Prompt wird der erste Chunk des Textes übergeben.
    </td>
  </tr>
  <tr>
    <td width="60%" bgcolor="HoneyDew">
      <mark>[START PART 2/2]</mark>
      <br>
      ""...et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."""
      <br>
      <mark>[END PART 2/2]</mark>
      <br>
      <mark>ALL PARTS SENT. Now you can continue processing the request.</mark>
    </td>
     <td bgcolor="white">
      Im letzten Prompt wird der letzte Chunk des Textes übermittelt.
    </td>
  </tr>
</table>



---

## Relevante Anwendungsfälle
Bei diesen Anwendungsfällen könnten die hier aufgeführten Hinweise und Beispiele angewendet werden:

```yaml
condition: or
entityType: usecase
rules:
- condition: contains
  property: id
  value: chatgpt
```

---


## Links

ChatGPT Best Practices (OpenAI API):

-	https://platform.openai.com/docs/guides/gpt-best-practices

Weitere Onlinequellen zu Promting:

- https://github.com/openai/openai-cookbook/blob/main/techniques_to_improve_reliability.md
- https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api
- https://www.scribbr.com/ai-tools/chatgpt-prompts/

Sammlung von Promptbeispielen:

- https://github.com/f/awesome-chatgpt-prompts


---


## Quellen

1.	GPT best practices [Internet]. [zitiert 31. August 2023]. OpenAI Platform. Verfügbar unter: https://platform.openai.com
