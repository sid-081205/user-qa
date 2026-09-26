# UserQA report: Margaret Ellison on https://ourlegacy.family/storybooks

*Persona:* **Margaret Ellison** (71) - Retired primary-school teacher who wants to pass family stories on to her grandchildren.  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 30 steps | *Pages reviewed:* 4 | *Issues:* 40 | *LLM calls:* 40 | *Wall time:* 1006.5 s

## What the agent understood the website to be
- **what it is:** A signed-in library of family storybooks created from supplied memories.
- **who it is for:** People who want to turn family memories into personal illustrated storybooks.
- **value proposition:** Creates a keepsake storybook with scenes and illustrations based on a family memory.
- **pricing model:** The header shows a balance of $4.00 in credits, but this page does not explain what the balance can buy or what further output may cost.
- **fit for me:** This is directly relevant because it provides access to the family storybook I previously made and should let me continue personalising it before creating a preview or export.
- **main tasks:** Open an existing storybook, Review and edit its scenes, Continue to personalisation, preview, PDF, or export, Create another storybook

## Scores
- SUS: **25.0** (grade F; 68 = industry average)
- UEQ-S: pragmatic -1.0, hedonic 0.75 (range -3..+3)
- Likelihood to recommend (0-10): 2
- Output keepsake-worthiness (1-5): 1
- Verdict: *"The website made a pretty book with a lovely blue kite, but it did not yet make my family's story true, so I would not give it to Oliver."*

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 4 | CONTENT | Review Storybook (x3) | The remaining scenes still contain the wrong family story | Scene 3 says “Grandpa's daddy threw the kite up into the wind,” Scene 4 says “Grandpa's daddy showed him how to hold the string,” and Scene 5 says “Now Grandpa  | Edit every remaining scene's text to identify my father, little Margaret, present-day Grandma Maggie and Oliver correctly. |
| 4 | CONTENT | Review Storybook | The story has the wrong family relationships | Scene 1 text: “One summer, Grandpa’s daddy made something very special.” Scene 2 text: “Grandpa and his daddy carried it up the big windy hill...” | Allow the text in every scene to be edited directly, and clearly show which changes are saved before export. |
| 4 | CONTENT | Review Storybook | The first visible illustration does not represent the requested characters | The Scene 1 image shows a child and an adult man, while the requested memory is Margaret as a child with her father and the present-day story should feature Oli | Provide a visible character-correction tool or a scene-level redraw option, with the requested relationships and appearances clearly repeated in the editing instructions. |
| 4 | VALUE | Review Storybook | The output remains unsuitable while the later scenes are unchanged | Scenes 3–10 are still marked with the old story text, including “Grandpa” and “Grandpa's daddy.” | Provide a clear warning or validation before Export Storybook that scenes may still need editing, and allow each scene to be reviewed before export. |
| 4 | CONTENT | Book output and personalisation | The personalised PDF still contains the unresolved family errors | The output was generated after only Scenes 1 and 2 were changed; Scenes 3–10 had not been corrected, and the cover is [81] “Scene 8.” | Allow every scene to be reviewed and revised from the export, or warn before PDF generation that uncorrected scenes will be included. I should be able to choose an appropriate final scene as the cover |
| 3 | CONTENT | Review Storybook (x3) | Scene 2 picture has the wrong child | Scene 2 image shows a young boy with my father, while the corrected text says “My father and I carried it.” | Regenerate Scene 2 with my father carrying the blue kite and little Margaret accompanying him on the hill behind the farmhouse. |
| 3 | H2 | Book output and personalisation (x2) | The PDF gives Margaret's age as five | The opening reads “The Blue Kite told by Margaret Ellison, age 5,” while the field [78] is labelled “Teller’s age” and contains “5.” | Clarify the field as “Age of the person telling the story,” and either allow adult ages or explain that this field is intended for the child narrator. In this book it should say 71. |
| 3 | H5 | Review Storybook | The review page gives no warning that the output may still be incorrect | The book is labelled “Complete” even though the visible text begins with “Grandpa’s daddy” and contradicts the requested family story. | Do not imply completion until the user has reviewed the story, or show a clear reminder that the generated relationships and illustrations should be checked before export. |
| 3 | H9 | Review Storybook | Saved text is not reflected on the review page | Scene 1 displays “One summer, Grandpa’s daddy made something very special.” after Save | Show a clear “Text updated” confirmation and immediately display the new sentence after saving; if saving failed, explain why and keep my typed text in the box. |
| 3 | CONTENT | Review Storybook | Scene 1 illustration still contradicts the requested memory | The Scene 1 image shows a man and a young child, and the scene text still identifies “Grandpa’s daddy” | Provide an image-editing or regeneration control that can specifically correct the people and relationship, then show a preview before replacing the illustration. |
| 3 | H3 | Corrected PDF title page | The PDF viewer has no obvious next-page control | Only two embedded frames are offered as controls, and the visible toolbar has no clearly labelled next-page button. | Provide clearly labelled previous and next controls in the embedded preview, and make keyboard page navigation work reliably. |
| 2 | H4 | Book output and personalisation (x4) | The output page still calls the book “Grandpa's Blue Kite” | The page heading reads “Grandpa's Blue Kite” even though the title field contains “The Blue Kite”. | Update the book heading to match the personalised title, or explain clearly that the heading is the original project name and the cover title has been changed. |
| 2 | ACC | Review Storybook (x2) | The image-version control lacks a simple descriptive label | [34] is exposed as a long instruction beginning “Scene 1 image, version 2 of 2. Show Grandma Maggie as the little girl with short silver hair…” rather than simp | Use a concise accessible name such as “Version 2 of 2 for Scene 1,” with the full generation instruction in supporting information rather than as the control name. |
| 2 | CONTENT | Review Storybook (x2) | The revised instruction was contradictory for a childhood scene | The Scene 1 image description says “Show Grandma Maggie as the little girl with short silver hair, round glasses and a blue cardigan”. | Let me distinguish childhood appearance from present-day appearance and offer a simple instruction template, such as “Margaret as a little girl in period clothes; Grandma Maggie today with silver hair |
| 2 | VALUE | My Storybooks | The meaning of the $4.00 balance is not explained | The header shows “$4.00” linking to billing, but the storybook card does not say whether this is a credit balance, what it covers, or whether export is included | Label the balance clearly, such as “$4.00 story credits,” and state on the storybook card what actions are included and what further actions cost. |

## Page-by-page
### My Storybooks  (step 1)
`https://ourlegacy.family/storybooks`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Provides access to storybooks already created in the account.
- **What's happening:** The page shows one saved item, “Grandpa’s Blue Kite,” represented by a watercolor cover. Its card says “Waterbook,” “10 scenes,” and “22 minutes ago,” with a separate three-dot “Storybook options” control.
- **First impression (Margaret):** "This is pleasantly clear and familiar. The book title and cover stand out, although the style label “Waterbook” sounds as though it may be a spelling mistake."
- **Cognitive walkthrough:** Q1 Yes. I want to reopen the storybook to continue to its remaining step. / Q2 Yes. The title “Grandpa’s Blue Kite” is presented as a link, both in the card text and twice in the underlying controls. / Q3 Yes. The storybook title clearly identifies the item I made last time, although the repeated links are unnecessary.
  - [VALUE sev 2] **The meaning of the $4.00 balance is not explained** - evidence: The header shows “$4.00” linking to billing, but the storybook card does not say whether this is a credit balance, what it covers, or whether export is included.. Fix: Label the balance clearly, such as “$4.00 story credits,” and state on the storybook card what actions are included and what further actions cost.
  - [ACC sev 2] **The three-dot options control lacks a visible name** - evidence: [9] button “Storybook options” appears only as a vertical three-dot mark in the card.. Fix: Give the control a visible “Options” label as well as an accessible name, and open a clearly titled menu that explains the available actions.
  - [CONTENT sev 1] **The illustration style is labelled with a questionable word** - evidence: The card says “Waterbook”; the screenshot appears to show “Waterbook,” while the page text reports “Watercolor.”. Fix: Correct the style label to “Watercolor” and ensure the label is generated from an approved list of style names.
- **Positives:** The page has a clean, calm layout with strong contrast and large readable text.; The storybook title and cover are easy to recognise.; The card provides useful basic status information: style, scene count, and creation time.; There is a clear route to reopen the existing storybook.

### Review Storybook  (step 2)
`https://ourlegacy.family/storybook/0bc53638-4e6d-4682-afe2-f4bfda08a148`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** Review the completed storybook, edit individual scenes, and proceed to export or output.
- **What's happening:** The storybook is marked Complete and the page shows ten scene cards with text and illustrations. A prominent Export Storybook link is available, while each scene has a separate options button for possible changes.
- **First impression (Margaret):** "The page is neat and easy to scan, and the storybook has clearly reopened. However, seeing “Grandpa’s Blue Kite” and the first scenes immediately reminds me that the important family relationships are still wrong."
- **Cognitive walkthrough:** Q1 Yes, I would try opening the options for the first scene because I need to correct the people and relationships before making an export. / Q2 Yes, I noticed the “Options for Scene 1” button above the first scene. / Q3 Partly. “Options for Scene 1” tells me there are controls, but it does not tell me whether I can change the wording, the people, or the illustration.
  - [CONTENT sev 4] **The story has the wrong family relationships** - evidence: Scene 1 text: “One summer, Grandpa’s daddy made something very special.” Scene 2 text: “Grandpa and his daddy carried it up the big windy hill...”. Fix: Allow the text in every scene to be edited directly, and clearly show which changes are saved before export.
  - [CONTENT sev 4] **The first visible illustration does not represent the requested characters** - evidence: The Scene 1 image shows a child and an adult man, while the requested memory is Margaret as a child with her father and the present-day story should feature Oliver and Grandma Maggie.. Fix: Provide a visible character-correction tool or a scene-level redraw option, with the requested relationships and appearances clearly repeated in the editing instructions.
  - [CONTENT sev 4] **The remaining scenes still contain the wrong family story** - evidence: Scene 3 says “Grandpa's daddy threw the kite up into the wind,” Scene 4 says “Grandpa's daddy showed him how to hold the string,” and Scene 5 says “Now Grandpa was old — and he had a grandson of his own.”. Fix: Edit every remaining scene's text to identify my father, little Margaret, present-day Grandma Maggie and Oliver correctly.
  - [VALUE sev 4] **The output remains unsuitable while the later scenes are unchanged** - evidence: Scenes 3–10 are still marked with the old story text, including “Grandpa” and “Grandpa's daddy.”. Fix: Provide a clear warning or validation before Export Storybook that scenes may still need editing, and allow each scene to be reviewed before export.
  - [CONTENT sev 4] **Later scenes still contain incorrect family relationships** - evidence: Scene 3 says “Grandpa’s daddy threw the kite”; Scene 4 says “Grandpa’s daddy showed him how to hold the string”; Scene 5 says “Grandpa was old”; Scene 8 says “Grandpa helped Oliver hold the string.”. Fix: Correct Scenes 3–8 so my father is the maker, I am the child, Oliver is my grandson, and I am present with him in the present-day scenes.
  - [H5 sev 3] **The review page gives no warning that the output may still be incorrect** - evidence: The book is labelled “Complete” even though the visible text begins with “Grandpa’s daddy” and contradicts the requested family story.. Fix: Do not imply completion until the user has reviewed the story, or show a clear reminder that the generated relationships and illustrations should be checked before export.
  - [H9 sev 3] **Saved text is not reflected on the review page** - evidence: Scene 1 displays “One summer, Grandpa’s daddy made something very special.” after Save. Fix: Show a clear “Text updated” confirmation and immediately display the new sentence after saving; if saving failed, explain why and keep my typed text in the box.
  - [CONTENT sev 3] **Scene 1 illustration still contradicts the requested memory** - evidence: The Scene 1 image shows a man and a young child, and the scene text still identifies “Grandpa’s daddy”. Fix: Provide an image-editing or regeneration control that can specifically correct the people and relationship, then show a preview before replacing the illustration.
  - [CONTENT sev 3] **Scene 2 picture has the wrong child** - evidence: Scene 2 image shows a young boy with my father, while the corrected text says “My father and I carried it.”. Fix: Regenerate Scene 2 with my father carrying the blue kite and little Margaret accompanying him on the hill behind the farmhouse.
  - [CONTENT sev 3] **Scene 2 image still does not show little Margaret** - evidence: Scene 2's displayed picture shows a man and a child who appears to be a boy, while the text says 'My father and I'.. Fix: Use Scene 2's image-edit control to specify that the child is little Margaret, with my father, carrying the blue kite on the windy hill.
  - [CONTENT sev 3] **Scene 2 image still shows the wrong child** - evidence: Scene 2 image, version 2 of 2: the child visibly appears to be a boy, while the corrected text says “My father and I”.. Fix: Regenerate the image with an explicit instruction that the child is a little girl, not a boy, and that she is carrying the kite with her father.
  - [CONTENT sev 3] **Later scenes retain the original incorrect relationships** - evidence: Scene 3: “Grandpa’s daddy threw the kite…”; Scene 5: “Now Grandpa was old…”; Scene 8: “Grandpa helped Oliver…”. Fix: Edit each remaining scene individually to identify my father and me in the past, and Grandma Maggie with Oliver in the present.
  - [H2 sev 2] **The scene options do not explain what can be changed** - evidence: The control is labelled only “Options for Scene 1”.. Fix: Label the controls with the exact actions, such as “Edit text” and “Edit illustration”, and state whether a credit will be used.
  - [CONTENT sev 2] **Image change instruction does not explain the character identities** - evidence: The text box only says “Describe what to change” and the example is “Make the sky more blue, add a rainbow in the background...”. Fix: Include examples showing that people can be described by their relationships and appearance, for example “Show Grandma Maggie as the little girl and her father making the kite.”
  - [VALUE sev 2] **No visible indication of the credit cost of updating an image** - evidence: The “Update Image” button is visible beside the instruction box, but no cost is shown.. Fix: State the credit cost beside the Update Image button, or explain it before the update is confirmed.
  - [H1 sev 2] **Image update gave no clear success message** - evidence: After using “Update Image,” the page only showed a new Scene 1 picture and [34] “2 versions”; there was no message such as “Image updated” or explanation of the selected version.. Fix: After regeneration, show a clear confirmation, identify the currently selected version, and offer a simple comparison of all versions with Keep selected.
  - [ACC sev 2] **The image-version control lacks a simple descriptive label** - evidence: [34] is exposed as a long instruction beginning “Scene 1 image, version 2 of 2. Show Grandma Maggie as the little girl with short silver hair…” rather than simply as the image itself.. Fix: Use a concise accessible name such as “Version 2 of 2 for Scene 1,” with the full generation instruction in supporting information rather than as the control name.
  - [CONTENT sev 2] **The revised instruction was contradictory for a childhood scene** - evidence: The Scene 1 image description says “Show Grandma Maggie as the little girl with short silver hair, round glasses and a blue cardigan”.. Fix: Let me distinguish childhood appearance from present-day appearance and offer a simple instruction template, such as “Margaret as a little girl in period clothes; Grandma Maggie today with silver hair, round glasses, and a blue cardigan.”
  - [ACC sev 2] **Scene 1's accessible description is incomplete and confusing** - evidence: The Scene 1 image control is described as “Scene 1 image, version 2 of 2. Show Grandma Maggie as the little girl with short silver hair, round glasses and a blue cardigan, even though”. Fix: Provide a complete, concise alternative description of the current picture, followed by a separate description of the requested change.
  - [H2 sev 2] **The output step is not clearly explained** - evidence: The control is labelled “Export Storybook,” but no visible text explains whether it will create a preview, a PDF, or both, or whether it will use the current selected versions.. Fix: Label the control with the exact action, such as “Create PDF preview,” and explain whether selected image versions and edits are included.
  - [CONTENT sev 1] **The revised image does not visibly retain an identifiable child** - evidence: The regenerated Scene 1 shows an unidentified little girl with my father; the child has no short silver hair, round glasses, or blue cardigan, although those adult traits were unnecessarily included in my instruction.. Fix: Preserve a recognisable likeness from the original memory or earlier version when possible, while correctly understanding that the child is a younger version of Grandma Maggie.
- **Positives:** The title and “Complete” status are easy to find.; The scene cards make the text and pictures easy to compare.; There is a clearly visible “Export Storybook” control.; The page has a clean layout with readable text and good contrast.

### Book output and personalisation  (step 19)
`https://ourlegacy.family/storybook/0bc53638-4e6d-4682-afe2-f4bfda08a148/export`

![screenshot](screenshots/step_19.jpg)
- **Purpose:** To personalise the storybook’s cover information, generate a watermarked PDF preview, and offer a printed-hardcopy purchase.
- **What's happening:** The page shows personalisation fields for title, author, teller’s age, story date, dedication, ownership, and cover image, followed by PDF generation. A $59 hardcover is also shown, but ordering is disabled and printing is described as coming soon.
- **First impression (Margaret):** "This looks orderly and fairly understandable, although the title field is empty despite the existing book title, and I want to see the remaining instructions before pressing Generate PDF."
- **Cognitive walkthrough:** Q1 Yes, I would try personalising the PDF preview because it is explicitly described as showing the exact book that could be printed. / Q2 I notice the labelled textboxes, the Change button for the cover image, and the Generate PDF button. / Q3 Yes. The labels are plain and mostly match what I want, though “Teller’s age” is less familiar than “Grandma Maggie’s age.”
  - [CONTENT sev 4] **The personalised PDF still contains the unresolved family errors** - evidence: The output was generated after only Scenes 1 and 2 were changed; Scenes 3–10 had not been corrected, and the cover is [81] “Scene 8.”. Fix: Allow every scene to be reviewed and revised from the export, or warn before PDF generation that uncorrected scenes will be included. I should be able to choose an appropriate final scene as the cover and regenerate the PDF after correcting all ten scenes.
  - [H2 sev 3] **The PDF gives Margaret's age as five** - evidence: The opening reads “The Blue Kite told by Margaret Ellison, age 5,” while the field [78] is labelled “Teller’s age” and contains “5.”. Fix: Clarify the field as “Age of the person telling the story,” and either allow adult ages or explain that this field is intended for the child narrator. In this book it should say 71.
  - [H6 sev 2] **Existing title is not carried into the blank title field** - evidence: The page heading says “Grandpa’s Blue Kite,” but [64] is an empty textbox with placeholder “Grandpa’s Blue Kite.”. Fix: Populate the title field with the existing book title, or make clear that the grey text is an example and the field is intentionally blank.
  - [H1 sev 2] **The printed-book promise conflicts with the disabled order control** - evidence: [72] “Order Printed Book” is disabled, while the page also says “Printing is coming soon.”. Fix: Label the section clearly as unavailable and explain that ordering will open later, or remove the purchase panel until printing is available.
  - [CONTENT sev 2] **The pre-filled story date appears to be the current date** - evidence: [67] “Story told on” has value “2026-09-26”. Fix: Do not default a historical family memory to today's date; leave it blank or ask whether it should be the date the story was told to Oliver.
  - [H4 sev 2] **The output page still calls the book “Grandpa's Blue Kite”** - evidence: The page heading reads “Grandpa's Blue Kite” even though the title field contains “The Blue Kite”.. Fix: Update the book heading to match the personalised title, or explain clearly that the heading is the original project name and the cover title has been changed.
  - [H4 sev 2] **Personalised title is not reflected in the page heading** - evidence: The heading still says “Grandpa's Blue Kite” while the Title field and generated export use “The Blue Kite.”. Fix: Use the current personalised title for the storybook page heading as soon as the title is saved or the PDF is generated.
  - [H2 sev 2] **The label “Teller’s age” is unclear** - evidence: [78] is labelled “Teller’s age” and contains 5, although the story is for five-year-old Oliver and was told by Margaret.. Fix: Label this field “Child’s age” or “Reader’s age,” or explain precisely whose age is being requested.
  - [H4 sev 2] **The output heading does not match the personalised book** - evidence: The page still says “# Grandpa's Blue Kite” although [76] contains “The Blue Kite” and the generated export is described as having a custom title.. Fix: After personalising, update the storybook heading itself to “The Blue Kite,” or explain clearly that the heading is the original project name.
  - [H6 sev 2] **Exports are distinguished only by timestamp** - evidence: Two entries both say "pdf" and "2.4 MB" at "8:57 PM" and "8:56 PM," with no indication that the first is the corrected export.. Fix: Label exports as "Latest" and "Previous," and include the changed preview details or an explicit version note.
  - [H1 sev 1] **The cover image generation status is not clear** - evidence: Under “Cover image” the button [83] says “Generation in progress...” while the cover is shown as “Scene 8”.. Fix: Show a clear progress message such as “Preparing the PDF and cover” and explain when generation is complete.
  - [H4 sev 1] **The page heading contradicts the personalised title** - evidence: The heading says "Grandpa's Blue Kite" while the Title field says "The Blue Kite.". Fix: Use the current personalised title in the page heading, or show the original working title separately with a clear label.
- **Positives:** The progress indicator clearly shows Create and Review completed and Output as the current step.; The PDF preview is described as watermarked and as representing the exact book that could be printed.; The $59 hardcover price is visible before any order action, and I have not been asked for payment details.

### Corrected PDF title page  (step 26)
`https://93sepmzq3cnhzfe1.public.blob.vercel-storage.com/production/storybooks/0bc53638-4e6d-4682-afe2-f4bfda08a148/exports/storybook_1790456253572-t1pUY4K7ddTJgW12Vx15g9LO7MMVKf.pdf`

![screenshot](screenshots/step_26.jpg)
- **Purpose:** To open and inspect the newly regenerated 32-page storybook PDF.
- **What's happening:** The PDF viewer displays page 1 of 32. The title is “The Blue Kite,” it is “told by Margaret Ellison,” the date is September 2026, and the preview/not-for-resale watermark is visible.
- **First impression (Margaret):** "This is a much better title page. The awkward “Margaret Ellison, age 5” has disappeared, and the credit now makes it clear that I am the person telling Oliver the story."
- **Cognitive walkthrough:** Q1 Yes, I would turn through all 32 pages now to check the correction and every scene. / Q2 The page indicator “1 / 32” and the browser PDF navigation controls make it clear that this is a multipage document. / Q3 The visible title and author credit match my intended personalisation, although the PDF viewer itself offers no plainly named “next page” control.
  - [H3 sev 3] **The PDF viewer has no obvious next-page control** - evidence: Only two embedded frames are offered as controls, and the visible toolbar has no clearly labelled next-page button.. Fix: Provide clearly labelled previous and next controls in the embedded preview, and make keyboard page navigation work reliably.
  - [H1 sev 2] **The PDF review control did not page through the whole document** - evidence: flip_through reported “you paged through 1 pages” while the viewer clearly shows “1 / 32”.. Fix: Make the review action advance through all available PDF pages and clearly indicate which pages have been inspected.
  - [H2 sev 1] **Page navigation controls are not clearly labelled** - evidence: The viewer shows “1 / 32” and compact toolbar icons, but the available page controls are represented only by iframes [1] and [2] in the page description.. Fix: Give the viewer’s page controls clear text labels or tooltips such as “Previous page” and “Next page,” and state whether all 32 pages have been viewed.
  - [ACC sev 1] **Preview watermark is very faint** - evidence: The large diagonal “Our Legacy Preview” text is extremely pale against the white title page.. Fix: Use slightly darker but still unobtrusive watermark text with sufficient contrast.
- **Positives:** The regenerated PDF opened successfully.; The title is now “The Blue Kite.”; The credit correctly says “told by Margaret Ellison” and no longer attaches Oliver's age to me.; The page indicator confirms that the complete preview has 32 pages.

## Generated output assessment
*Artifact:* Website-generated personalised children's storybook and 32-page PDF

> This does not yet feel like my family story, and I would not recognise the people in it. The pictures are pretty and the blue kite is clear, but the invented Grandpa and the repeated changes from little Margaret to a boy undermine the whole keepsake. I would want the relationships, title, characters, and final PDF corrected before considering it for Oliver.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | The requested title, author details, family relationships, and character appearances are repeatedly changed or contradicted. The book invents Grandpa, changes the title to "Grandpa's Blue Kite," and often shows an older  |
| coherence | 1 | The story has a beginning, middle, and ending, but the relationships shift from Margaret and her father to an invented Grandpa and Oliver. The heading disagrees with the title field, the teller age changes from 5 to Opti |
| age fit | 3 | The simple sentences and warm kite theme are broadly suitable for a five-year-old, but the measured reading level is grade 4.3, with longer and more literary phrases such as "the best feeling in the whole world" and "mad |
| language | 2 | Many individual sentences are grammatically clear, but the text contains serious factual and relationship errors such as "Grandpa's daddy" and "Grandpa helped Oliver." There is a blank cast page, a blank page, inconsiste |
| text image fit | 1 | The kite, farmhouse, Welsh hill, and kite-flying activity are generally represented well, but many pictures contradict the intended identities and relationships. Images show a generic child, a boy, or an invented grandfa |
| character consistency | 1 | The requested child is repeatedly depicted without short silver hair, round glasses, or a blue cardigan, and sometimes changes from a girl to a boy. The father changes age and appearance, while the invented grandfather b |
| visual quality | 3 | The watercolour-style artwork is generally attractive and the blue kite is clear, but the deliverable includes preview watermarks, tiny thumbnails, blank or placeholder-like pages, and no convenient full-size page-by-pag |
| emotional resonance | 1 | The kite story could be a warm and meaningful keepsake, but the invented grandfather changes the central relationship and prevents Margaret from recognising her own memory. The later scenes do not show Margaret sharing t |

- **used correctly:** The title field was entered as "The Blue Kite."; The author name Margaret Ellison was entered.; Oliver's name and ownership were included.; The dedication names Oliver and Grandma Maggie.; The old blue shirt, blue kite, farmhouse, Welsh setting, windy hill, and kite-flying activity were retained.; The opening supplied sentence was reproduced correctly.; The warm watercolour-style visual direction was broadly followed.
- **missing:** A faithful depiction of little Margaret with short silver hair, round glasses, and a blue cardigan.; A consistent older Welsh father in the remembered scenes.; A present-day Margaret sharing the kite experience with Oliver.; A correct cast of characters.; A reliable full-size, page-by-page preview before ordering.
- **changed:** The displayed title was changed to "Grandpa's Blue Kite."; The teller age changed from 5 to Optional.; The requested father-and-daughter memory was changed into a grandfather-and-grandson story.; The child was sometimes changed from a girl to a boy.; The supplied Welsh context was inconsistently replaced by generic or contradictory family labels.; The date September 2026 was added without being supplied.
- **invented:** Grandpa.; Grandpa's daddy.; A grandfather-and-Oliver relationship.; An unspecified story date of September 2026.; A listening code page and related delivery information inside the book.

### Part by part
#### Storybook listing and cover preview
![I1](artifacts/capture_01/img_00.jpg)
> OurLegacy My Storybooks $4.00 My Storybooks 1 storybook Create New Grandpa's Blue Kite Watercolor 10 scenes
- *Picture:* A warm, softly coloured watercolor-style illustration inside a farmhouse kitchen. A brown-haired boy in a white shirt helps a brown-haired adult man attach or adjust a large blue kite. Blue pieces of cloth and lengths of string lie across the wooden floor. The man does not clearly appear to be an older Welshman, and the child is not a little Margaret with short silver hair, round glasses, and a blue cardigan. No printed title is visible on the pictured cover itself.
- *Reaction:* The farmhouse colours and blue kite are appealing, but this is not recognisably my family. Calling the book “Grandpa's Blue Kite” and showing a man with a boy instead of my father with little Margaret undermines the whole keepsake.
  - [fidelity, sev 4] The requested title was “The Blue Kite,” but the listing says “Grandpa's Blue Kite.” The preview also shows a man and a boy rather than my father and me as a little girl.
  - [coherence, sev 3] The image depicts kite-making, but its family labels contradict the story: “Grandpa” is used where the maker should be “my father.”
  - [text_image_fit, sev 3] The kite and making activity broadly match the story, but the pictured child is plainly a brown-haired boy, contradicting the repeated request to show little Margaret as a young girl.
  - [character_consistency, sev 3] Only one scene is visible, so consistency across all 10 scenes cannot be judged. In this image, the child lacks the specified short silver hair, round glasses, and blue cardigan, and the man is not clearly an older Welshman.
  - [emotional_resonance, sev 3] The gentle watercolor style has some warmth, but the invented Grandpa relationship and wrong child make it feel like someone else's family story.
- **Change I'd make:** Retitle the book “The Blue Kite.” Regenerate this cover or opening scene with my father depicted as an older Welshman making the kite with me as a little girl. I should have short silver hair, round glasses, and a blue cardigan. Do not call him Grandpa and do not show any other family members.
- **Suggested rewrite:** The Blue Kite Margaret Ellison For Oliver, with love from Grandma Maggie

#### Output page: title, preview, and printed-book offer
![I2](artifacts/capture_19/view_00.jpg)
> Grandpa's Blue Kite Make a digital PDF, a narrated video, or order a printed book. Generate Book Preview Preview A watermarked preview of the exact 32-page book you can order — personalize it below; what you preview is what gets printed. Title The Blue Kite Author Margaret Ellison Teller’s age 5 Story told on 26/09/2026 Printed Book Keepsake A real hardcover keepsake shipped to your door. Hardcover $59 Order Printed Book Printing is coming soon ✨
- *Picture:* The website interface identifies the output as “Grandpa's Blue Kite,” while its editable title is “The Blue Kite.” It offers a $59 hardcover but also says that printing is coming soon.
- *Reaction:* I would be uneasy about ordering anything here. The heading calls my father “Grandpa,” although I specifically said not to invent or show a grandfather, and the printed book is offered even though it says printing is not yet available.
  - [fidelity, sev 3] The page heading says “Grandpa's Blue Kite,” although the requested title is “The Blue Kite” and the instructions say, “Do not show any invented family members.”
  - [coherence, sev 3] The page offers “Order Printed Book” while immediately stating “Printing is coming soon ✨.”
  - [language, sev 2] The top of the page shows “$4.00,” while the hardcover is marked “$59,” without explaining whether $4.00 is a credit, a balance, or money already paid.
  - [fidelity, sev 2] The field “Story told on” has been filled with “26/09/2026,” although no story date was supplied in the inputs.
- **Change I'd make:** Change the output heading to “The Blue Kite,” remove the invented “Grandpa” wording, and either disable the printed-book button until ordering is genuinely available or explain clearly when it will open. Show the full price, currency, delivery charge, and whether the displayed $4.00 is a credit before I commit.
- **Suggested rewrite:** The Blue Kite

#### Personalization fields and generation status
![I3](artifacts/capture_19/view_01.jpg)
> Title The Blue Kite Author Margaret Ellison Teller’s age 5 Story told on 26/09/2026 Dedication For Oliver, with love from Grandma Maggie. May w This book belongs to Oliver Ellison Cover image Scene 8 Change Generation in progress... Generated Exports PDF Generating...
- *Picture:* The lower portion of the personalization panel shows the dedication and ownership fields, a small selected cover thumbnail labeled “Scene 8,” and status messages saying that both book generation and the PDF are still in progress.
- *Reaction:* The dedication and ownership details look broadly right, but I cannot judge the actual keepsake from this screen because the book itself is not open. The truncated dedication and generation messages also leave me unsure whether anything has been completed correctly.
  - [language, sev 2] The dedication field visibly ends at “For Oliver, with love from Grandma Maggie. May w,” with no indication that this is merely a horizontally clipped field rather than a truncated dedication.
  - [visual_quality, sev 2] The selected “Scene 8” cover is only a tiny thumbnail here, so facial identity, requested clothing, the Welsh farmhouse, and image artefacts cannot be checked reliably.
- **Change I'd make:** Show the entire dedication in a wrapping, readable field and provide a clearly labeled “Open full preview” button. A full-size cover preview should appear before the PDF is generated.

#### Regenerated preview header and metadata
![I4](artifacts/capture_55/view_00.jpg)
> Grandpa's Blue Kite Make a digital PDF, a narrated video, or order a printed book. Generate Book Preview Preview A watermarked preview of the exact 32-page book you can order — personalize it below; what you preview is what gets printed. Title The Blue Kite Author Margaret Ellison Teller’s age Optional Story told on 26/09/2026 Dedication For Oliver, with love from Grandma Maggie. May w This book belongs to Oliver Ellison
- *Picture:* After generation, the same output page still has the heading “Grandpa's Blue Kite,” but the teller-age field now says “Optional” rather than the previously entered value of 5.
- *Reaction:* This does not feel like a faithful final version. Although the entered title is “The Blue Kite,” the page still calls it “Grandpa's Blue Kite,” and my age setting has silently changed from 5 to “Optional.”
  - [fidelity, sev 3] The entered “Teller’s age” is visibly “5” in the earlier view but “Optional” in the final view.
  - [fidelity, sev 3] The final output heading remains “Grandpa's Blue Kite” rather than using the requested title, “The Blue Kite.”
  - [coherence, sev 3] The editable metadata and the main output heading disagree: the field says “The Blue Kite,” while the heading says “Grandpa's Blue Kite.”
- **Change I'd make:** Regenerate the output from the current fields, preserve the teller age of 5, and make every visible title update automatically. Do not present this version as final until the heading, metadata, illustrations, and PDF all agree.
- **Suggested rewrite:** The Blue Kite Teller’s age: 5

#### Cover-image gallery and generated PDF files
![I5](artifacts/capture_55/view_01.jpg)
> Cover image Scene 8 Done 1 2 3 4 5 6 7 8 9 10 Regenerate PDF Generated Exports PDF Sep 26, 2026, 8:57 PM • 2.4 MB Custom title Author: Margaret Ellison Dedication Bookplate Cover: Scene 8 Download PDF Sep 26, 2026, 8:56 PM • 2.4 MB Custom title Author: Margaret Ellison Dedication Bookplate Cover: Scene 8 Download
- *Picture:* Ten small scene thumbnails are shown, with Scene 8 outlined as the cover. The thumbnails appear to show kite-flying scenes with an adult man and a child, but they are too small here to verify the child’s identity, requested appearance, or the stated relationships. Two apparently identical PDF files are listed one minute apart.
- *Reaction:* The kite and outdoor scenes are visible, but I still cannot inspect the people closely enough to accept them as my family. Two PDFs have been created even though the website says the text did not change, and the final files are not opened for review on this page.
  - [character_consistency, sev 2] The ten thumbnails are too small to verify that little Margaret has short silver hair, round glasses, and a blue cardigan, or that the same child and father remain consistent throughout.
  - [text_image_fit, sev 2] Only thumbnail images are supplied; the associated story text and full-size page spreads are not visible, so the claim that “what you preview is what gets printed” cannot be checked.
  - [visual_quality, sev 2] The selected cover and all ten scenes are reduced to thumbnails, preventing inspection for distorted faces, extra fingers, garbled lettering, or other artefacts.
  - [coherence, sev 2] Two 2.4 MB PDFs are listed at 8:56 PM and 8:57 PM, while the note says “the text did not change.” The interface does not explain why both files were generated or which one should be used.
  - [emotional_resonance, sev 3] The gallery does not show enough of the actual book to demonstrate that the story is faithful to Margaret’s father and childhood memory.
- **Change I'd make:** Open a full-size, page-by-page preview before ordering. Check every illustration against the text, ensuring the child is clearly Margaret—a girl with short silver hair, round glasses, and a blue cardigan—and that the only family member shown is her Welsh father. Remove the duplicate PDF and label the latest verified file clearly.

#### Page 1
![I6](artifacts/capture_60/view_00.jpg)
> The Blue Kite told by Margaret Ellison September 2026
- *Picture:* A very pale title page with the navy title, a smaller byline, a September 2026 date, a large diagonal 'OurLegacy PREVIEW' watermark, and a small 'PREVIEW - NOT FOR RESALE - OURLEGACY.FAMILY' notice.
- *Reaction:* The title and name are clear, but the preview watermark and the extra date make it feel like a website proof rather than a finished keepsake. I also do not need the child's age here, but I would want the finished printed page to have no preview markings.
  - [language, sev 2] The page visibly carries a large 'OurLegacy PREVIEW' watermark and 'PREVIEW - NOT FOR RESALE - OURLEGACY.FAMILY'.
  - [visual_quality, sev 2] The page is mostly empty and the pale watermark crosses the title area.
- **Change I'd make:** Remove the watermark and preview notice from the finished copy, and keep only the title, author credit, and date unless I specifically want the date included.

#### Page 2
![I7](artifacts/capture_61/view_00.jpg)
> The Blue Kite
- *Picture:* A mostly blank pale title page with a small centered 'The Blue Kite', the diagonal preview watermark, and the preview notice at the bottom.
- *Reaction:* This repeats the title without adding a picture or useful information. It is a wasted page in a children's book and makes the opening feel padded rather than carefully made.
  - [coherence, sev 2] Page 1 already says 'The Blue Kite' and page 2 repeats only 'The Blue Kite'.
  - [visual_quality, sev 2] The page contains a large diagonal preview watermark and a small preview notice.
- **Change I'd make:** Replace this blank repeated title page with the requested cover illustration: little Margaret as a girl with short silver hair, round glasses, and a blue cardigan, beside her father and the clearly recognisable blue kite, with the farmhouse behind them.

#### Page 3
![I8](artifacts/capture_62/view_00.jpg)
> For Oliver, with love from Grandma Maggie. May we always keep the old blue kite safe.
- *Picture:* A pale dedication page with the dedication in italic type and a small blue kite illustration beneath it. The page also carries the preview watermark and notice.
- *Reaction:* The dedication is lovely and personal, and Oliver's name is exactly right. The little kite is a nice touch, although the preview markings must not appear in the final book.
  - [language, sev 1] The page visibly contains 'OurLegacy PREVIEW' and 'PREVIEW - NOT FOR RESALE - OURLEGACY.FAMILY'.
- **Change I'd make:** Keep the wording, remove the preview markings, and enlarge the small kite illustration if the final design permits.

#### Page 4
![I9](artifacts/capture_63/view_00.jpg)
> Cast of characters
- *Picture:* A nearly blank pale page with only the heading 'Cast of characters', the preview watermark, and the preview notice.
- *Reaction:* A cast page would be helpful if it actually identified the people, but this page contains no characters or descriptions at all. It is an obvious unfinished section.
  - [fidelity, sev 3] The heading promises a list of characters, but the page shows none.
  - [coherence, sev 3] The page is a placeholder-like section with no content after the heading.
- **Change I'd make:** Either remove this page or add clear short descriptions of little Margaret, her father, and Oliver, explicitly stating that there is no Grandpa character in this story.
- **Suggested rewrite:** Little Margaret — the little girl with short silver hair, round glasses, and a blue cardigan. Her father — an older Welsh man who makes the blue kite. Oliver — Margaret's grandson.

#### Page 5
![I10](artifacts/capture_64/view_00.jpg)
> This book belongs to Oliver Ellison signed
- *Picture:* A pale ownership page with a thin rectangular border, Oliver's name, a blank signing line, and the preview watermark and notice.
- *Reaction:* This is a useful and personal page, and the name is correct. The blank signing line is a sensible keepsake detail, but the preview markings should be removed.
  - [language, sev 1] The page visibly carries 'OurLegacy PREVIEW' and 'PREVIEW - NOT FOR RESALE - OURLEGACY.FAMILY'.
- **Change I'd make:** Keep the ownership page, enlarge the text slightly for comfortable reading, and remove the preview markings.

#### Page 6
![I11](artifacts/capture_65/view_00.jpg)
> One summer, my father made me something very special. He cut up an old blue shirt and made it into a kite!
- *Picture:* A pale text page with the two story sentences, a small kite illustration, the preview watermark, and the preview notice.
- *Reaction:* The opening words are exactly the memory I supplied and are simple enough for a young child. I would want the following illustration to show me as a little girl, not a boy, but this page's text itself is good.
  - [language, sev 1] The page includes the visible preview watermark and 'PREVIEW - NOT FOR RESALE - OURLEGACY.FAMILY'.
- **Change I'd make:** Keep the text, remove the preview markings, and pair it with an illustration of little Margaret clearly identifiable as a girl with short silver hair, round glasses, and a blue cardigan.

#### Page 7
![I12](artifacts/capture_66/view_00.jpg)
- *Picture:* A warm watercolor farmhouse interior showing a brown-haired little girl in ordinary clothes helping a young adult man make a kite from a blue shirt. The kite frame and fabric are clearly visible on the floor.
- *Reaction:* The picture is attractive and the making of the kite is clear, but it does not show my family as I described. The child has brown hair, no glasses, and no blue cardigan, and the man looks young rather than older; this needs correcting before I would trust it as my story.
  - [fidelity, sev 3] The picture shows a brown-haired child in a white shirt and grey shorts, not short silver hair, round glasses, and a blue cardigan.
  - [text_image_fit, sev 2] The text says 'my father made me' but the illustration does not provide the requested child appearance or clearly establish the older Welsh father.
  - [character_consistency, sev 3] The child shown here has brown hair and no glasses, unlike the requested little Margaret.
- **Change I'd make:** Regenerate the scene with little Margaret as a young girl, not a boy, with short silver hair, round glasses, and a blue cardigan, beside her older Welsh father in the warm farmhouse.

#### Page 8
![I13](artifacts/capture_67/view_00.jpg)
> The blue kite was ready! My father and I carried it up the big windy hill behind the old farmhouse.
- *Picture:* A pale text page with the story sentence, a small blue kite illustration, the preview watermark, and the preview notice.
- *Reaction:* The sentence is simple, clear, and faithful to the place and action I gave. The page should not have the preview markings in the final copy.
  - [language, sev 1] The page visibly contains 'OurLegacy PREVIEW' and 'PREVIEW - NOT FOR RESALE - OURLEGACY.FAMILY'.
- **Change I'd make:** Keep the text and remove the preview markings; enlarge the text if needed for comfortable reading.

#### Page 9
![I14](artifacts/capture_68/view_00.jpg)
- *Picture:* A watercolor landscape of a child and a young adult man walking up a green hill while carrying a blue kite, with a farmhouse in the distance. The child has brown hair and no glasses or blue cardigan; the man is not visibly older.
- *Reaction:* The hill, farmhouse, wind, and blue kite are all there, so the event is easy to follow. However, the child is not recognisably me as described, and the man does not look like the older Welsh father I asked for.
  - [fidelity, sev 3] The image shows a brown-haired child without short silver hair, round glasses, or a blue cardigan.
  - [character_consistency, sev 3] The child in this picture does not match the requested appearance of little Margaret and also appears different from the child on Page 7.
  - [text_image_fit, sev 2] The image supports the hill and kite but does not clearly match the requested identities of Margaret and her father.
- **Change I'd make:** Regenerate the image with the same little Margaret appearance on every page: short silver hair, round glasses, blue cardigan, and clearly a girl, with her older Welsh father carrying the kite beside her.

#### Page 10
![I15](artifacts/capture_69/view_00.jpg)
> Grandpa's daddy threw the kite up into the wind. Up, up, up it went — dancing in the bright blue sky!
- *Picture:* A pale text page with the story sentence, a small kite illustration, the preview watermark, and the preview notice.
- *Reaction:* This is a serious family error. My father made the kite and was with me as a child; he is not 'Grandpa's daddy', and I explicitly asked for no invented Grandpa.
  - [fidelity, sev 4] The text says "Grandpa's daddy" and substitutes an invented relationship for my father.
  - [language, sev 1] The page visibly contains the preview watermark and 'PREVIEW - NOT FOR RESALE - OURLEGACY.FAMILY'.
- **Change I'd make:** Replace the relationship with 'my father' and ensure the illustration shows my older father launching the kite with little Margaret beside him.
- **Suggested rewrite:** My father threw the kite up into the wind. Up, up, up it went — dancing in the bright blue sky!

#### Page 11
![I16](artifacts/capture_70/view_00.jpg)
- *Picture:* A watercolor sky scene showing a young adult man launching a blue kite while a child jumps beside him. The child has brown hair, no glasses, no blue cardigan, and is not clearly recognisable as little Margaret; the man is young rather than older.
- *Reaction:* The kite is beautifully visible and the excitement is clear, but the people are still wrong. It also contradicts the requested family story by presenting a young man and a generic child instead of my older Welsh father and little Margaret.
  - [fidelity, sev 4] The image shows a young man and a brown-haired child without the requested older Welsh father or little Margaret's silver hair, glasses, and blue cardigan.
  - [character_consistency, sev 4] The child and man have not retained the requested identities or appearance from the preceding scenes.
  - [text_image_fit, sev 2] The image supports the kite-launch action but does not support the corrected relationship that the man is Margaret's father.
- **Change I'd make:** Regenerate the picture with my older Welsh father launching the kite and little Margaret beside him, preserving her short silver hair, round glasses, and blue cardigan.

#### Page 12
![I17](artifacts/capture_71/view_00.jpg)
> Grandpa's daddy showed him how to hold the string. 'Let out a little more when the wind blows strong,' he said.
- *Picture:* A pale text page with the sentence, a small kite illustration, the preview watermark, and the preview notice.
- *Reaction:* This repeats the same unacceptable family mistake and also uses 'him' without clearly saying whether the child or adult is being taught. It must be rewritten before I could consider the book a faithful family keepsake.
  - [fidelity, sev 4] The text again says "Grandpa's daddy" instead of identifying the person as my father.
  - [coherence, sev 2] The phrase 'showed him how to hold the string' has an unclear pronoun after the incorrect 'Grandpa's daddy' label.
  - [language, sev 1] The page visibly contains the preview watermark and 'PREVIEW - NOT FOR RESALE - OURLEGACY.FAMILY'.
- **Change I'd make:** Identify my father directly and name me as the child being taught, for example: 'My father showed me how to hold the string. He said, “Let out a little more when the wind blows strong.”'
- **Suggested rewrite:** My father showed me how to hold the string. He said, “Let out a little more when the wind blows strong.”

#### Page 13
![I18](artifacts/capture_72/view_00.jpg)
- *Picture:* A blue kite string rises out of the picture while an older white-haired man helps a young boy hold the reel. They stand on a green hill above a farmhouse.
- *Reaction:* This is a pretty picture, but it is not my family memory. The child is a boy and the older man has been turned into Grandpa, rather than my father teaching little Margaret.
  - [fidelity, sev 4] The picture shows a young boy and an older man, although the requested memory is little Margaret with her father.
  - [text_image_fit, sev 3] The picture continues the story of the kite lesson, but it contradicts the requested identity of the child and father.
  - [character_consistency, sev 4] The child is consistently shown as a boy rather than a little girl with short silver hair, round glasses and a blue cardigan.
  - [visual_quality, sev 1] The illustration is attractive and clean, but the preview watermark says 'PREVIEW - NOT FOR RESALE'.
- **Change I'd make:** Replace the boy with little Margaret, a young girl, and show her father teaching her. Keep the hill, farmhouse and kite, but do not show Grandpa.

#### Page 14
![I19](artifacts/capture_73/view_00.jpg)
> Many, many years went by. Now Grandpa was old — and he had a grandson of his own. His name was Oliver.
- *Picture:* A white title page with a faint diagonal OurLegacy preview watermark, a small teal line above the text, and a preview notice at the bottom.
- *Reaction:* This is a serious family error. Oliver is my grandson, but he is not Grandpa's grandson, and I never asked for a character called Grandpa.
  - [fidelity, sev 4] The text says, 'Now Grandpa was old — and he had a grandson of his own.'
  - [coherence, sev 4] The text makes Margaret's narrator's family relationship change from 'my father' to 'Grandpa' without explanation.
  - [language, sev 2] The sentence is grammatically clear, but the invented family relationship makes the wording factually wrong for the requested story.
- **Change I'd make:** Remove Grandpa entirely and make the later relationship explicitly Margaret and her grandson Oliver.
- **Suggested rewrite:** Many years went by. Now I was old too. My grandson Oliver came to visit me in Wales.

#### Page 15
![I20](artifacts/capture_74/view_00.jpg)
- *Picture:* An older white-haired man sits in an armchair holding a blue kite while a curly-haired boy kneels beside him. A fire burns in the foreground, and green wellies are visible near the door.
- *Reaction:* The scene looks cosy and the kite is easy to recognise, but it is the wrong family altogether. The older man is supposed to be my father in the memory, not an invented Grandpa.
  - [fidelity, sev 4] The picture shows an elderly man with Oliver rather than my father and little Margaret, even though this is the old-memory portion of the story.
  - [text_image_fit, sev 4] The picture supports the generated 'Grandpa' text, but it does not support the family story I supplied.
  - [character_consistency, sev 4] The same older man continues to be used as Grandpa, while the requested child is repeatedly represented as a boy.
  - [visual_quality, sev 1] The watercolor-like artwork is attractive, but the preview watermark is printed across the picture.
- **Change I'd make:** Show little Margaret as a girl with short silver hair, round glasses and a blue cardigan, beside my father as he handles the kite. Do not show an elderly Grandpa.

#### Page 16
![I21](artifacts/capture_75/view_00.jpg)
> The next day, they went back to Wales! Oliver put on his green wellies and they picked up the old blue kite.
- *Picture:* A white text page with a small teal line, a faint diagonal OurLegacy preview watermark, and the preview notice at the bottom.
- *Reaction:* The sentence is easy to understand, but 'they' is vague after the invented Grandpa scene. I would want this to say plainly that Oliver and I returned to Wales.
  - [fidelity, sev 2] The text uses 'they' without making clear that the intended pair is Margaret and Oliver.
  - [coherence, sev 3] The preceding page introduced Grandpa, but this page suddenly refers to 'they' and does not repair the relationship error.
  - [age_fit, sev 1] The sentence is short and the action is clear, but 'wellies' may need explanation for a five-year-old audience unfamiliar with the British word.
- **Change I'd make:** Name Margaret and Oliver directly, and use 'boots' or explain the word wellies.
- **Suggested rewrite:** The next day, Oliver and I went back to Wales. He put on his green boots, and we picked up the old blue kite.

#### Page 17
![I22](artifacts/capture_76/view_00.jpg)
- *Picture:* An older man stands in the doorway of a stone farmhouse holding the blue kite and its string while a curly-haired boy bends down to put on green boots.
- *Reaction:* The farmhouse and Wales setting are good, but the people are still wrong. I wanted a present-day Margaret with Oliver, not an older man playing my father.
  - [fidelity, sev 4] The picture shows an older man and a boy, while the requested present-day pair is Margaret, a 71-year-old woman, and her grandson Oliver.
  - [character_consistency, sev 4] The older man has the same visual identity as the invented Grandpa, and the child remains a boy.
  - [text_image_fit, sev 3] The picture does show the kite and wellies, but it does not show the correct people named by the story.
  - [visual_quality, sev 1] The illustration is polished, although the preview watermark remains visible.
- **Change I'd make:** Show Margaret as a 71-year-old woman with short silver hair, round glasses and a blue cardigan, standing with Oliver as they leave the farmhouse.

#### Page 18
![I23](artifacts/capture_77/view_00.jpg)
> Up the big hill they climbed together. The wind was blowing just like it did long, long ago.
- *Picture:* A white text page with a small teal line, a faint diagonal OurLegacy preview watermark, and a preview notice at the bottom.
- *Reaction:* The sentence is gentle and has a nice link back to the memory, but the hidden 'they' leaves the wrong family relationship in place. I would want the names Margaret and Oliver here.
  - [fidelity, sev 3] The text says only 'they' and therefore does not identify the correct present-day pair.
  - [coherence, sev 3] The story shifts from the invented Grandpa to an unnamed pair without correcting the relationship.
  - [age_fit, sev 1] The long phrase 'just like it did long, long ago' is understandable but slightly more literary than a typical five-year-old reading level.
- **Change I'd make:** Name Margaret and Oliver and simplify the sentence slightly.
- **Suggested rewrite:** Oliver and I climbed the big hill together. The wind blew just as it had long ago.

#### Page 19
![I24](artifacts/capture_78/view_00.jpg)
- *Picture:* An older man and a curly-haired boy climb a green hillside together. The older man carries the folded blue kite, with a stone farmhouse visible in the distance.
- *Reaction:* The hill, farmhouse and kite are all right, but this is still not the family I wanted to pass on. The older man is being used where I asked for my father or present-day Margaret.
  - [fidelity, sev 4] The picture shows an older man and a boy rather than little Margaret and her father in the memory, or Margaret and Oliver in the present.
  - [text_image_fit, sev 3] The picture supports the hill-climbing action but contradicts the requested family identities.
  - [character_consistency, sev 4] The same older man and boy are repeated instead of maintaining the requested Margaret and Oliver identities.
- **Change I'd make:** For the remembered scene, show little Margaret and her father. For the later scene, show Margaret and Oliver. Keep the same hill and farmhouse.

#### Page 20
![I25](artifacts/capture_79/view_00.jpg)
> Grandpa helped Oliver hold the string. The blue kite flew up, up into the summer sky — just like before!
- *Picture:* A white text page with a small teal line, a faint diagonal OurLegacy preview watermark, and a preview notice at the bottom.
- *Reaction:* The flying kite is an important part of the memory, but the sentence invents Grandpa again. It should be Margaret helping Oliver, or my father helping little Margaret in the earlier scene.
  - [fidelity, sev 4] The text explicitly says, 'Grandpa helped Oliver hold the string.'
  - [coherence, sev 4] This repeats the incorrect family relationship introduced earlier instead of continuing the requested father-and-daughter memory.
  - [age_fit, sev 1] The repeated 'up, up' is lively and child-friendly, although the long sentence is somewhat dense for a five-year-old.
- **Change I'd make:** Change the helper to the correct person for the scene and split the sentence into two short sentences.
- **Suggested rewrite:** My father helped me hold the string. The blue kite flew up, up, into the summer sky!

#### Page 21
![I26](artifacts/capture_80/view_00.jpg)
- *Picture:* An older man helps a curly-haired boy hold a blue kite reel on a sunny hillside. The kite flies high in the sky, with a farmhouse below.
- *Reaction:* The picture is cheerful and the kite is unmistakable, but I would not recognise my family in it. My grandson should be with me, Margaret, not with an invented elderly man.
  - [fidelity, sev 4] The picture shows an older man and a boy, not Margaret and her grandson Oliver.
  - [character_consistency, sev 4] The older man has the appearance of the repeatedly invented Grandpa, while the requested child Margaret is absent.
  - [text_image_fit, sev 4] The picture matches the generated 'Grandpa helped Oliver' text, but that text itself is wrong for the supplied family story.
  - [visual_quality, sev 1] The watercolor artwork is attractive, but a preview watermark is visible.
- **Change I'd make:** Show Margaret, wearing her blue cardigan, helping Oliver hold the reel. Preserve the hill, bright sky and blue kite.

#### Page 22
![I27](artifacts/capture_81/view_00.jpg)
> Oliver laughed and laughed as the kite swooped and danced. It was the best feeling in the whole world!
- *Picture:* A white text page with a small teal line, a faint diagonal OurLegacy preview watermark, and a preview notice at the bottom.
- *Reaction:* The words sound happy and would suit a five-year-old, but they are attached to the wrong family scene. The sentence is also a little large for the requested reading age.
  - [age_fit, sev 2] The sentence contains the longer phrase 'the best feeling in the whole world' and runs on across two clauses.
  - [fidelity, sev 3] The text is about Oliver, but it follows the invented Grandpa relationship and does not identify Margaret as the person sharing the moment.
  - [coherence, sev 2] The sentence makes sense on its own but continues the unresolved Grandpa substitution.
- **Change I'd make:** Say that Oliver laughed while I helped him fly the kite, and shorten the final sentence.
- **Suggested rewrite:** Oliver laughed as the kite swooped and danced. It was the best feeling in the world!

#### Page 23
![I28](artifacts/capture_82/view_00.jpg)
- *Picture:* A curly-haired boy in a red top and green trousers laughs with his arms wide open beside an older man in a blue jacket. A blue kite is partly visible overhead.
- *Reaction:* The joy in this illustration is genuine and the colours are warm, but it again shows the wrong adult. I wanted to see myself sharing the moment with Oliver.
  - [fidelity, sev 4] The picture shows an older man with Oliver rather than Margaret with Oliver.
  - [character_consistency, sev 4] The older man continues to look like the invented Grandpa, not like the 71-year-old Margaret described in the request.
  - [text_image_fit, sev 3] The picture complements the joy of the text but does not show the correct relationship.
- **Change I'd make:** Replace the older man with Margaret, keeping Oliver, the blue kite and the happy hillside moment.

#### Page 24
![I29](artifacts/capture_83/view_00.jpg)
> They promised to keep the old blue kite safe for ever. Every time they came to Wales, they would fly it together.
- *Picture:* A white text page with a small teal line, a faint diagonal OurLegacy preview watermark, and a preview notice at the bottom.
- *Reaction:* This is a nice closing sentiment, but 'they' hides the important error. I would want the promise to belong to Margaret and Oliver, not to an invented Grandpa and Oliver.
  - [fidelity, sev 4] The text says only 'They promised' and 'they would fly it,' without correcting the invented Grandpa relationship.
  - [coherence, sev 4] The promise depends on the wrong pair of characters established earlier, so the ending does not belong to the supplied family story.
  - [language, sev 1] 'for ever' is a valid British spelling choice, but it may be unfamiliar to some readers and is less immediate than 'forever'.
- **Change I'd make:** Name Margaret and Oliver explicitly and use the more familiar spelling 'forever' unless the British spelling is intentional.
- **Suggested rewrite:** Oliver and I promised to keep the old blue kite safe forever. Every time we came to Wales, we would fly it together.

#### Page 25
![I30](artifacts/capture_84/view_00.jpg)
- *Picture:* A white blank-looking page with a faint diagonal OurLegacy preview watermark and a preview notice along the bottom edge; no substantive illustration is visible.
- *Reaction:* This page appears unfinished or accidentally blank. I would not want to pay for a keepsake with an unexplained empty page.
  - [visual_quality, sev 3] The page is essentially blank apart from the preview watermark and footer.
  - [text_image_fit, sev 3] There is no visible picture or text to connect with the kite story.
  - [language, sev 2] The page contains no story text, leaving a gap in the sequence.
- **Change I'd make:** Remove this blank page or replace it with a full-page illustration of Margaret and Oliver keeping the blue kite safe.

#### Page 26
![I31](artifacts/capture_85/view_00.jpg)
> The End Made with love, and kept forever.
- *Picture:* A white closing page with a small teal line above the text, a faint diagonal OurLegacy preview watermark, and a preview notice at the bottom.
- *Reaction:* The ending is warm and clearly marked, but it is rather generic. I would prefer a personal sign-off from Grandma Maggie to Oliver.
  - [fidelity, sev 2] The closing line, 'Made with love, and kept forever,' does not identify the people or relationship behind the keepsake.
  - [emotional_resonance, sev 2] The wording is pleasant but could have been written for almost any personalised book.
  - [language, sev 1] The page is grammatically correct, but 'kept forever' does not add a new story detail.
- **Change I'd make:** Add a personal closing line that names Oliver and Grandma Maggie and refers to their promise.
- **Suggested rewrite:** The End For Oliver, with love from Grandma Maggie. We will always remember the blue kite.

#### Page 27
![I32](artifacts/capture_86/view_00.jpg)
> The story behind these pages “The blue kite flew up, up into the summer sky — just like before!” The summer my father made me a kite out of an old blue shirt. We carried it up the windy hill behind the old farmhouse in Wales, and the bright blue kite danced high in the sky. My father taught me how to hold the string and how to let out a little more when the wind grew strong. Years later, I told the story to my grandson Oliver. Today we climb the same hill together. Oliver has brown curly hair and freckles, and he is wearing his green wellies. This time Oliver is the hero, and I help him fly Grandpa's blue kite. The kite climbs above the farmhouse and the summer clouds, and Oliver laughs as it swoops and dances. We promise to keep the old blue kite safe and to bring it whenever our family v
- *Picture:* A white text page headed 'The story behind these pages', with a long paragraph of story notes and a footer identifying Margaret Ellison, September 2026 and OurLegacy.
- *Reaction:* This page restores some of the real memory, including my father, the Welsh farmhouse and Oliver, but then it contradicts itself by saying we fly 'Grandpa's blue kite.' That one error is enough to stop me trusting the whole keepsake.
  - [fidelity, sev 4] The page says, 'I help him fly Grandpa's blue kite,' although the kite was made by my father and I asked for no Grandpa.
  - [coherence, sev 4] The first paragraph correctly says 'My father taught me,' but the next paragraph changes the kite's owner to Grandpa.
  - [character_consistency, sev 4] The story notes name Margaret, her father and Oliver, but the main pages have used an invented older man and a boy instead.
  - [age_fit, sev 1] The story-behind-the-pages text is adult-facing and contains longer sentences and vocabulary such as 'afterwards' and 'family visits.'
  - [language, sev 3] The page includes the unexplained possessive phrase 'Grandpa's blue kite,' which is a factual and grammatical relationship error in this family story.
- **Change I'd make:** Correct every reference to Grandpa, and make this page agree with the illustrations: my father made the kite, while today Margaret and Oliver fly it together.
- **Suggested rewrite:** The story behind these pages “The blue kite flew up, up into the summer sky — just like before!” One summer, my father made me a kite out of an old blue shirt. We carried it up the windy hill behind the old farmhouse in Wales, and the blue kite danced high in the sky. My father taught me how to hold the string and how to let out a little more when the wind grew strong. Years later, I told the story to my grandson Oliver. Today we climb the same hill together. Oliver has brown curly hair and freckles, and he is wearing his green wellies. This time Oliver is the hero, and I help him fly my father's blue kite. The kite climbs above the farmhouse and the summer clouds, and Oliver laughs as it swoops and dances. We promise to keep the old blue kite safe and to bring it whenever our family visits Wales. As told by Margaret Ellison · September 2026 · OurLegacy

#### Page 28
![I33](artifacts/capture_87/view_00.jpg)
> In your own words Do you remember the first time you ever watched a kite climb into a summer sky?
- *Picture:* A white activity page with a small teal line, a faint diagonal OurLegacy preview watermark, and a preview notice at the bottom.
- *Reaction:* This is a pleasant prompt for remembering, but 'the first time you ever' is a little formal for a five-year-old. It also does not ask about my actual family memory.
  - [age_fit, sev 1] The phrase 'the first time you ever watched' is longer and more formal than the simple story language elsewhere.
  - [fidelity, sev 2] The prompt asks about a generic first kite experience rather than the old blue shirt, my father or the Welsh farmhouse.
- **Change I'd make:** Ask Oliver to remember the specific blue kite and the windy hill.
- **Suggested rewrite:** In your own words Do you remember watching our old blue kite climb into the summer sky?

#### Page 29
![I34](artifacts/capture_88/view_00.jpg)
> Add your photos When you read this at sixteen, what do you think it will feel like to hold that old blue kite?
- *Picture:* A white activity page with a small teal line, a faint diagonal OurLegacy preview watermark, and a preview notice at the bottom.
- *Reaction:* The future-looking question is thoughtful, but I do not want the book to assume Oliver will read it at sixteen. That is an invented detail about him.
  - [fidelity, sev 3] The text says, 'When you read this at sixteen,' although Oliver is five and no reading age of sixteen was supplied.
  - [age_fit, sev 2] The reflective question is more mature than the rest of the five-year-old story.
  - [emotional_resonance, sev 2] The page is thoughtful, but assuming a distant future reading occasion makes it feel less personal to the present relationship.
- **Change I'd make:** Ask about reading the book now or adding a family photograph, without assigning Oliver a future age.
- **Suggested rewrite:** Add your photos What do you think it will feel like to hold our old blue kite?

#### Page 30
![I35](artifacts/capture_89/view_00.jpg)
> Notes & Memories What moment with Oliver made your heart feel fullest on that windy Welsh hill?
- *Picture:* A white notes page with a small teal line, a faint diagonal OurLegacy preview watermark, and a preview notice at the bottom.
- *Reaction:* This is a thoughtful family-memory prompt, and it is one of the better pages. I would still prefer 'you' to mean Margaret explicitly, because the current story has confused who is speaking.
  - [fidelity, sev 1] The prompt names Oliver and the windy Welsh hill, but the pronoun 'your' does not clearly identify Margaret as the intended respondent.
  - [age_fit, sev 1] The phrase 'made your heart feel fullest' is more literary than necessary for a five-year-old activity page.
- **Change I'd make:** Simplify the wording and make Margaret the intended speaker.
- **Suggested rewrite:** Notes & Memories What was your favourite moment with Oliver on the windy Welsh hill?

#### Page 31
![I36](artifacts/capture_90/view_00.jpg)
> Hear it read aloud Your private listening code  is created with your  printed book Every printed book includes a code your family can scan to hear the story read aloud.
- *Picture:* A white information page with a small teal line, a faint diagonal OurLegacy preview watermark, and a preview notice at the bottom.
- *Reaction:* This is a useful feature, but it interrupts the family story with a sales and delivery explanation. The word 'private' also needs a clear explanation of what information the code contains and how it is protected.
  - [emotional_resonance, sev 1] The page shifts suddenly from a personal keepsake to an explanation of a 'private listening code.'
  - [language, sev 2] The line breaks make 'Your private listening code is created with your printed book' look fragmented, and the privacy of the code is not explained.
  - [age_fit, sev 2] This is adult-facing explanatory copy inside a book intended for a five-year-old.
- **Change I'd make:** Move this information to the website or a separate family-information page, and explain simply what the code does and what information it stores.
- **Suggested rewrite:** Hear the story A printed book includes a code so your family can scan it and hear the story read aloud.

#### Page 32
![I37](artifacts/capture_91/view_00.jpg)
> OurLegacy Illustrated in watercolors · An OurLegacy Original Printed by OurLegacy · 2026 © 2026 Margaret Ellison. Story told by Margaret Ellison · September 2026. First printed 2026
- *Picture:* A white publication page with a small teal line, a faint diagonal OurLegacy preview watermark, a preview notice, and centred production and copyright text.
- *Reaction:* The copyright credit is clear enough, and the incorrect 'age 5' has been removed. However, 'Illustrated in watercolors' is a production claim I would want checked rather than accept without seeing the final printed quality.
  - [language, sev 2] The page says, 'Illustrated in watercolors,' although the pictures appear to be digitally rendered or reproduced rather than actual watercolors.
  - [fidelity, sev 1] The page says, 'Story told by Margaret Ellison,' but it does not correct the invented Grandpa and the wrong child shown throughout the main story.
  - [visual_quality, sev 1] The page still carries the 'PREVIEW - NOT FOR RESALE' watermark, so it is not a finished purchase-ready file.
- **Change I'd make:** Correct the main story and illustrations first, then remove the preview watermark and use accurate wording such as 'Illustrated in a watercolor style' if that is what the service actually provides.
- **Suggested rewrite:** OurLegacy Illustrated in a watercolor style · An OurLegacy Original Printed by OurLegacy · 2026 © 2026 Margaret Ellison. Story told by Margaret Ellison · September 2026. First printed 2026

#### Output review page
> OurLegacy My Storybooks $4.00 Create 2 Review 3 Output Grandpa's Blue Kite Complete Export Storybook
- *Picture:* No cover or title-page illustration is shown. This capture shows the website's navigation, price, progress labels, storybook title, completion status, and export button.
- *Reaction:* The website has called my book “Grandpa's Blue Kite,” which is not the title I gave, and I cannot see my name, dedication, or ownership details here. I also cannot tell from this page alone what the $4.00 pays for or whether another cost will appear.
  - [fidelity, sev 3] The displayed title is “Grandpa's Blue Kite,” although the title I supplied was “The Blue Kite.” The requested author name, dedication, and “This book belongs to: Oliver Ellison” are not visible in this output capture.
  - [language, sev 2] The interface uses the unexplained name “OurLegacy,” while “$4.00” and “Export Storybook” are presented without an explanation of what will be purchased or exported.
  - [visual_quality, sev 1] The review controls appear as small interface text, which is less readable for someone with mild presbyopia.
- **Change I'd make:** Restore the title to “The Blue Kite,” show “By Margaret Ellison,” include the dedication to Oliver, and state plainly what the $4.00 pays for, whether it includes printing or shipping, and whether any further charge is possible.
- **Suggested rewrite:** The Blue Kite By Margaret Ellison For Oliver, with love from Grandma Maggie. May we always keep the old blue kite safe.

#### Scene 1
![I38](artifacts/capture_93/img_00.jpg)
> One summer, my father made me something very special. He cut up an old blue shirt and made it into a kite!
- *Picture:* In a warm farmhouse room, a brown-haired adult man kneels beside a little brown-haired girl as they make a blue kite. A cut-up blue shirt and lengths of blue cloth lie on the floor.
- *Reaction:* The workshop, old shirt, and blue kite are easy to recognise, so this is a good beginning. However, the child is not the short-silver-haired girl in round glasses and a blue cardigan that I asked for, and my father does not appear to be the older Welsh man I described.
  - [fidelity, sev 3] The picture shows a short-brown-haired girl in pale clothing without round glasses or a blue cardigan, alongside a brown-haired middle-aged man rather than an older Welsh father.
  - [character_consistency, sev 3] The child and father do not match the explicit descriptions “little Margaret,” “short silver hair,” “round glasses,” “blue cardigan,” and “older Welsh man.”
- **Change I'd make:** Redraw the child as a clearly little girl with short silver hair, round glasses, and a blue cardigan. Redraw her father as an older Welsh man, while retaining the shirt, kite-making, and farmhouse setting.

#### Scene 2
![I39](artifacts/capture_93/img_01.jpg)
> The blue kite was ready! My father and I carried it up the big windy hill behind the old farmhouse.
- *Picture:* A brown-haired man and a little brown-haired girl walk beside a stone wall on a green hill. The girl holds the finished blue kite overhead, with a small farmhouse in the valley behind them.
- *Reaction:* The Welsh-looking hill, farmhouse, and blue kite are lovely and the wording now has the correct relationship. The people still are not my specified little Margaret and older Welsh father, and only Margaret appears to be carrying the kite.
  - [fidelity, sev 3] The child has brown hair, no visible round glasses, and no blue cardigan; the man also looks too young and has no clear Welsh character cues.
  - [character_consistency, sev 3] Neither figure matches the appearance established in the requested corrections.
  - [text_image_fit, sev 1] The text says “My father and I carried it,” while the picture shows the child carrying the kite and the man walking with empty hands.
- **Change I'd make:** Show the silver-haired, bespectacled little girl in a blue cardigan and the older Welsh father sharing the kite's weight as they climb together.

#### Scene 3
![I40](artifacts/capture_93/img_02.jpg)
> Grandpa's daddy threw the kite up into the wind. Up, up, up it went — dancing in the bright blue sky!
- *Picture:* A middle-aged man and a little brown-haired girl jump for joy beneath a blue kite flying high in a cloudy sky.
- *Reaction:* The flying kite and shared excitement are good, but “Grandpa's daddy” invents a grandfather who was never part of my memory. This should say that my father and I flew the kite.
  - [fidelity, sev 4] The phrase “Grandpa's daddy” introduces the grandfather whom I expressly said not to show, and the picture does not depict my specified little Margaret.
  - [coherence, sev 3] Scenes 1 and 2 establish “my father and I,” but Scene 3 abruptly changes to an unstated “Grandpa's daddy.”
  - [text_image_fit, sev 2] The text names “Grandpa's daddy,” but the picture contains only a man and a child, with no grandfather present.
  - [character_consistency, sev 3] The girl again has brown hair and lacks the specified round glasses and blue cardigan.
- **Change I'd make:** Replace “Grandpa's daddy” with “My father” and redraw little Margaret as the silver-haired girl with round glasses and a blue cardigan, flying the kite with her father.
- **Suggested rewrite:** My father threw the kite up into the wind. Up, up, up it went, dancing in the bright blue sky!

#### Scene 4
![I41](artifacts/capture_93/img_03.jpg)
> Grandpa's daddy showed him how to hold the string. 'Let out a little more when the wind blows strong,' he said.
- *Picture:* An elderly white-haired man stands behind a young brown-haired boy and helps him wind or hold a wooden kite reel. A farmhouse and rolling hills appear behind them.
- *Reaction:* This page makes the mistake even more obvious: the child has changed from a girl into a boy, and the older man has been turned into a grandfather. It is not the little girl learning from her own father.
  - [fidelity, sev 4] The text says “Grandpa's daddy” and the image shows an elderly grandfather figure with a boy, contrary to the requested father and little Margaret.
  - [coherence, sev 3] The pronoun “him” grammatically refers to Grandpa, but the picture shows him helping a young boy. The intended learner is unclear.
  - [text_image_fit, sev 3] “Grandpa's daddy showed him” does not match a picture in which an old man helps a boy rather than a grandfather.
  - [character_consistency, sev 4] The brown-haired girl in the earlier scenes has become a boy, while the father has become an elderly man.
- **Change I'd make:** Show my older Welsh father standing behind little Margaret and helping her hold the reel. Preserve her short silver hair, round glasses, and blue cardigan in every panel.
- **Suggested rewrite:** My father showed me how to hold the string. “Let out a little more when the wind blows strong,” he said.

#### Scene 5
![I42](artifacts/capture_93/img_04.jpg)
> Many, many years went by. Now Grandpa was old — and he had a grandson of his own. His name was Oliver.
- *Picture:* An elderly white-haired man sits in an armchair holding the blue kite while a curly-haired boy in a red shirt and green trousers kneels beside him in a firelit room.
- *Reaction:* Oliver has been put under an invented grandfather rather than under me, and the picture shows precisely the grandfather I asked the website not to invent. I would not recognise my family in this keepsake.
  - [fidelity, sev 4] “Now Grandpa was old — and he had a grandson of his own” directly replaces Margaret with an invented grandfather, despite the instruction “Do not show Grandpa or any invented family members.”
  - [character_consistency, sev 4] The elderly figure is male and is paired with Oliver as though he were the family member who inherited the memory.
  - [emotional_resonance, sev 4] The central relationship is changed from Margaret remembering her father to an unrelated grandfather, making the story feel generic and potentially upsetting.
- **Change I'd make:** Replace the old man with older Margaret, recognisable as short-haired, wearing round glasses and a blue cardigan, showing the kite to her grandson Oliver.
- **Suggested rewrite:** Many, many years went by. Now I was old, too — and I had a grandson named Oliver.

#### Scene 6
![I43](artifacts/capture_93/img_05.jpg)
> The next day, they went back to Wales! Oliver put on his green wellies and they picked up the old blue kite.
- *Picture:* A curly-haired boy pulls on tall green boots outside a stone building while an elderly bespectacled man stands in the doorway holding the folded blue kite.
- *Reaction:* The picture is cheerful, but it is the wrong family arrangement: an old man is preparing to fly the kite with Oliver. “The next day” also arrives without a clear present-day event having been established.
  - [fidelity, sev 4] The image again shows the prohibited grandfather rather than Margaret with Oliver, and the text leaves “they” deliberately vague.
  - [coherence, sev 2] “The next day” follows a general statement that many years went by but gives no event from which a present-day trip can clearly follow.
  - [character_consistency, sev 4] The old man remains the central adult rather than changing to Margaret; Oliver is the same curly-haired boy throughout these scenes.
- **Change I'd make:** Show older Margaret in her blue cardigan helping Oliver into his wellies and carrying the kite with him. Name Margaret in the text so there is no uncertainty.
- **Suggested rewrite:** The next day, Oliver and I went back to Wales. Together we picked up the old blue kite.

#### Scene 7
![I44](artifacts/capture_93/img_06.jpg)
> Up the big hill they climbed together. The wind was blowing just like it did long, long ago.
- *Picture:* An elderly man in a blue coat and a curly-haired boy in green trousers climb a windy hill together. A stone farmhouse is visible below.
- *Reaction:* The hill and wind recall the right family memory, but this is once again the invented grandfather and Oliver rather than Margaret and Oliver. I want my own place in the story restored.
  - [fidelity, sev 4] The picture shows an old man and Oliver, not older Margaret and her grandson.
  - [character_consistency, sev 4] The central adult remains male throughout the present-day sequence, contrary to the requested family relationships.
- **Change I'd make:** Keep the landscape but replace the old man with an older Margaret wearing round glasses and a blue cardigan, matching the established illustration style.
- **Suggested rewrite:** Oliver and I climbed the big hill together. The wind blew just as it had long, long ago.

#### Scene 8
![I45](artifacts/capture_93/img_07.jpg)
> Grandpa helped Oliver hold the string. The blue kite flew up, up into the summer sky — just like before!
- *Picture:* An elderly man stands behind Oliver and helps him hold the kite string while the blue kite flies high over the green hills and farmhouse.
- *Reaction:* The action is warm and the kite is beautifully visible, but “Grandpa” is the wrong name and the wrong person. The picture is polished; the family story is not mine.
  - [fidelity, sev 4] The sentence explicitly says “Grandpa helped Oliver,” and the illustration confirms the invented male relative.
  - [character_consistency, sev 4] The old man and curly-haired boy are consistent with the website's invented story but inconsistent with the family relationship I supplied.
- **Change I'd make:** Change the adult to older Margaret and preserve her round glasses, short silver hair, and blue cardigan as she helps Oliver hold the string.
- **Suggested rewrite:** I helped Oliver hold the string. The blue kite flew up, up into the summer sky — just like before!

#### Scene 9
![I46](artifacts/capture_93/img_08.jpg)
> Oliver laughed and laughed as the kite swooped and danced. It was the best feeling in the whole world!
- *Picture:* Oliver stands with his arms spread wide and laughs beside an elderly man. Part of the blue kite and its curling ribbon are visible above them in a golden sky.
- *Reaction:* Oliver's delight is captured well, but the scene remains generic because I am absent and an invented grandfather is standing beside him. The ending should connect his joy to my own memory of flying that kite.
  - [fidelity, sev 4] The picture shows Oliver with the invented grandfather, with no visual sign of Margaret or the Welsh father from the opening memory.
  - [emotional_resonance, sev 3] “It was the best feeling in the whole world!” is a broad generic statement rather than a specific feeling rooted in Margaret's remembered experience.
  - [age_fit, sev 1] Most of the sentence is very accessible, but “swooped” and the broad claim “the whole world” add a little unnecessary abstraction for a five-year-old listener.
- **Change I'd make:** Show older Margaret sharing Oliver's delight, and tie the moment explicitly to her memory of the kite flying with her father.
- **Suggested rewrite:** Oliver laughed as the blue kite danced in the summer sky. It felt like all those summers long ago.

#### Scene 10
![I47](artifacts/capture_93/img_09.jpg)
> They promised to keep the old blue kite safe for ever. Every time they came to Wales, they would fly it together.
- *Picture:* An elderly man places an arm around Oliver as they look across the Welsh hills. The old blue kite lies folded in the grass in the foreground.
- *Reaction:* The sunset and folded kite give the page a proper visual ending, but it ends the wrong relationship. It needs Margaret and Oliver making the promise so the book feels like my family's keepsake rather than someone else's.
  - [fidelity, sev 4] The picture again shows the explicitly prohibited invented grandfather with Oliver, and the text never names Margaret.
  - [character_consistency, sev 4] The elderly male character and curly-haired boy remain unchanged, but neither belongs to the family structure requested for the present-day scenes.
  - [emotional_resonance, sev 4] The final promise could be moving, but because it is made by the wrong adult it does not connect the kite to Margaret's memory of her father.
- **Change I'd make:** Show Margaret with her arm around Oliver, both looking across the Welsh hills, and make their promise explicitly theirs. Preserve the folded kite as the closing image.
- **Suggested rewrite:** Oliver and I promised to keep the old blue kite safe forever. Every time we came to Wales, we would fly it together.

**Top changes to the output:** 1. Remove every invented Grandpa reference and restore the relationship: Margaret's father made the kite and taught little Margaret to fly it. | 2. Regenerate every remembered-scene illustration with little Margaret clearly shown as a girl with short silver hair, round glasses, and a blue cardigan, alongside her older Welsh father. | 3. Rewrite the present-day scenes with older Margaret and Oliver flying the kite together, naming them directly and removing vague references such as "they." | 4. Use "The Blue Kite" consistently everywhere and preserve the teller age of 5. | 5. Remove the blank and placeholder pages, add or remove the cast page deliberately, and provide a full-size preview of every page before purchase. | 6. Clarify the price, currency, delivery charge, and what the $4.00 and $59 amounts represent.

## Recommendations (participant's priorities)
- **[high] Correct every scene so my father makes the kite, little Margaret is clearly the child in the childhood scenes, and present-day Margaret and Oliver are the central characters; remove all invented Grandpa references.** (Review Storybook, all scenes) - These errors change the people and relationships at the heart of the memory, so I could not give the book to Oliver.
- **[high] Make each scene's Edit Text and Edit Image controls explain what they change, and show which changes have saved successfully.** (Review Storybook) - I could not tell whether my corrections had been accepted, and I did not want to make the same mistake again.
- **[high] Add a clear warning that the generated story may contain incorrect characters or relationships and must be checked scene by scene before export.** (Review Storybook) - A beautiful-looking preview made me trust the book before I realised how much of the family story was wrong.
- **[high] Use The Blue Kite consistently in the interface, PDF cover, page heading and export screen instead of continuing to show Grandpa's Blue Kite.** (Book output and personalisation) - The contradictory title makes the finished book look careless and undermines my confidence in the personalisation.
- **[high] Correct the storyteller information so Margaret is not labelled as five years old, and clarify that Oliver is the five-year-old.** (Book output and personalisation and PDF title page) - The age mistake is a basic factual error about our family and would be embarrassing and confusing in a keepsake.
- **[high] Provide a complete final-PDF check with clearly labelled next and previous page controls, a visible page number, and a way to jump to any page.** (Corrected PDF title page) - I need to inspect all 32 pages myself before deciding whether the book is suitable for Oliver.
- **[high] Explain the $4.00 credit balance and show the cost of every image update before I click, including whether an update uses a credit and what happens if it does not work.** (My Storybooks and Review Storybook) - I want to know exactly what I am spending and avoid unexpected costs, especially on a pension.
- **[medium] Explain the image-version choices with plain labels such as Version 1, Version 2 and Latest, and show when a new image is ready.** (Review Storybook) - The words '2 versions' and the version control did not tell me which picture was newest or which one I was viewing.
- **[medium] Give the scene options meaningful names and explain which parts of the illustration can be changed, such as the child, adult, object, setting and action.** (Review Storybook) - I was trying to correct specific identities, but the site did not make clear whether those details were available to edit.
- **[medium] Give the three-dot control a visible name or replace it with a plainly labelled Options button.** (My Storybooks) - An unexplained symbol is difficult to recognise, especially when I am looking for a safe, understandable way to manage a book.
- **[medium] Explain why the printed book cannot be ordered when the order control is disabled, and state the contents, price and delivery time for the $59 option.** (Book output and personalisation) - I need to know what I am being offered before I consider paying anything.
- **[medium] Label exports with a clear version name or date such as Corrected PDF - 14 March, rather than relying only on a timestamp.** (Book output and personalisation) - I need to be certain that I am opening the latest corrected version and not an earlier PDF.
- **[low] Make the preview watermark and small text more visible, and enlarge small controls and text where possible.** (Corrected PDF title page and Review Storybook) - Very faint or tiny text is difficult for me to read and does not give me confidence that I have seen the complete book.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This is a website for turning a family memory into a personalised storybook for a child. It seems intended for parents and grandparents who want to preserve a special story as a keepsake.
- **What was the most frustrating or confusing moment, and why?** The most frustrating moment was reviewing the finished PDF and finding that later scenes still had the wrong family relationships, even after I had corrected the earlier text and pictures. I also found the page-turning controls unclear, so I was not sure I had properly checked all 32 pages at first.
- **What was the best moment?** The best moment was when the second Scene 2 version finally showed a little girl with my father, the blue kite and the Welsh hill. The artwork was attractive, and the PDF preview also let me inspect the result before ordering anything.
- **Was there any point where, in real life, you would have given up? Where and why?** I think I would seriously have given up after seeing the final book still centred on an invented Grandpa instead of Oliver and me. The work was already lengthy, and the result did not feel safe to present as our family history.
- **What did you expect to find or be able to do that wasn't there?** I expected to be able to correct every scene's wording, characters, relationships and illustrations and see the whole book update together. I also expected clear instructions about what each option changes, what the credits cost, and how to read and download the complete PDF.
- **Did you trust this website with your information (and your family's)? Why or why not?** I was willing to use the website because it explained that the PDF could be reviewed before ordering, but I did not fully trust it with our family's story. The invented characters, wrong ages and unclear saving messages made me worry that I might overlook another important error.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would pay for a finished printed keepsake if the whole book were accurate and the price and delivery were clearly explained. I would feel comfortable paying around $30 to $40 for a carefully checked personal book, but the $59 printed book would need a clear explanation of exactly what was included.
- **If the site produced something for you, how do you feel about it overall?** The pictures are warm and attractive, and the blue kite and Welsh setting are easy to recognise. However, the book still tells the wrong family story, with Grandpa, the wrong child and inconsistent characters, so it is not yet a keepsake I could give to Oliver.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | My Storybooks \| OurLegacy | reassured (1) | I can see the book I made last time, and its title is immediately recognisable. I want to open “Grandpa’s Blue Kite” to go to its final output or export step and see what can be corrected before I spend any credits or mo | click |
| 2 | Review Storybook \| OurLegacy | frustrated (-1) | I can see that my book has opened for review, but I am still disappointed by the story itself. Scene 1 says “Grandpa’s daddy” and shows a man and a child, which is not the memory I gave. Before exporting, I want to see w | click |
| 3 | Review Storybook \| OurLegacy | frustrated (-1) | I can correct the wording first. I want to change “Grandpa’s daddy” to my father, and make clear that I was the child flying the kite. I am pleased that the scene gives me both text and picture controls, although I am no | click |
| 4 | Review Storybook \| OurLegacy | reassured (1) | This is straightforward now that the text box is open. I want to remove “Grandpa’s daddy” altogether and say plainly that my father made the kite for me when I was a little girl. | type; click |
| 5 | Review Storybook \| OurLegacy | frustrated (-1) | I thought I had saved the correction, but the page still says “Grandpa’s daddy”. That is confusing and makes me wonder whether I did something wrong. I need to try again and check the picture too, because the illustratio | click |
| 6 | Review Storybook \| OurLegacy | reassured (1) | I can now see that my correction did save, although the earlier page had not made that clear. Scene 1’s picture is still wrong, so I shall choose “Edit Image” and see what control the site gives me. | click |
| 7 | Review Storybook \| OurLegacy | reassured (1) | I can see that choosing “Edit Image” has opened a simple description box, and the button is clearly greyed out until I say what should change. I shall ask for the child to be Grandma Maggie as a little girl, my father ma | type; click; wait_for_change |
| 8 | Review Storybook \| OurLegacy | reassured (1) | This is a real improvement: the picture now shows a man and a little girl making the kite, and the text says my father made it for me. Because I was the child, I would not expect my present-day silver hair, glasses, or c | click |
| 9 | Review Storybook \| OurLegacy | reassured (1) | Yes, clicking “2 versions” worked because it opened the version choices and selected Version 2. The new Scene 1 picture is an improvement, although the girl does not look specifically like five-year-old Oliver because sh | click |
| 10 | Review Storybook \| OurLegacy | reassured (1) | Yes, the click worked clearly because the two editing choices appeared beside Scene 2. I shall correct the text before the picture, because the sentence is plainly wrong: my father and I carried the kite up the windy hil | click |
| 11 | Review Storybook \| OurLegacy | reassured (1) | Yes, the “Edit Text” control has clearly opened the right box. I shall replace this sentence with the two people who really carried the kite up the hill: my father and me, when I was a little girl. | type; click |
| 12 | Review Storybook \| OurLegacy | reassured (1) | The saving worked because the new sentence is plainly visible beneath Scene 2. However, the picture still makes me uneasy: the child is a boy, so the family relationship is wrong again. I shall open Scene 2’s options and | click |
| 13 | Review Storybook \| OurLegacy | reassured (1) | The click worked clearly because the two editing choices appeared. I shall choose “Edit Image” and ask for the child to be Grandma Maggie as a little girl, with my father carrying the blue kite on the Welsh hill. | click |
| 14 | Review Storybook \| OurLegacy | reassured (1) | I can see that choosing Edit Image has opened the correct description box for Scene 2. I shall now describe the change carefully: the child must be little Margaret, with my father, carrying the blue kite on the windy hil | type; click; wait_for_change |
| 15 | Review Storybook \| OurLegacy | frustrated (-1) | The text changes have worked, and the blue kite and Welsh hill are clear in Scene 2. However, the child still looks like a boy, so the family story is not yet right. I shall correct Scene 2's picture before moving on to  | click |
| 16 | Review Storybook \| OurLegacy | frustrated (-2) | I can see that my click on “Options for Scene 2” worked because the two editing choices are open. The text is now right, but the picture still shows a boy rather than little Margaret, so I shall use “Edit Image” once mor | click |
| 17 | Review Storybook \| OurLegacy | frustrated (-1) | The box is clearly open, but the selected picture is still wrong. I shall ask for one last change: the child must be a little Margaret, a girl, and not a boy. I have $4.00 in free credits, so I can try this without payin | type; click; wait_for_change |
| 18 | Review Storybook \| OurLegacy | reassured (1) | The third Scene 2 version looks much closer to the memory: the child now appears to be a girl with my father, and the hill and blue kite are clear. I can plainly see that the regeneration worked, but Scenes 3 and 4 still | click |
| 19 | OurLegacy - Turn your family story into  | reassured (1) | I have reached the final step, and it is refreshingly clear that a PDF preview is available before ordering anything. I do not want to use the $59 printed book, but I should personalise the preview carefully and then exa | scroll |
| 20 | OurLegacy - Turn your family story into  | reassured (1) | The title “Grandpa’s Blue Kite” is not quite right for the corrected family story, so I shall personalise this properly before making the PDF. I shall call it “The Blue Kite,” credit myself as the teller of Oliver’s stor | type; type; type; type; type; click |
| 21 | OurLegacy - Turn your family story into  | reassured (1) | My title, author, dedication, and ownership details have been accepted, which is reassuring. The PDF is still generating, so I shall wait for it to finish before judging the book. I do not want to order the printed versi | wait_for_change |
| 22 | OurLegacy - Turn your family story into  | reassured (1) | The site has clearly confirmed that the PDF was made, and I can now download it so that I can inspect all 32 pages. I am a little annoyed that the heading still says “Grandpa’s Blue Kite” even though the PDF title is “Th | click |
| 23 | OurLegacy - Turn your family story into  | frustrated (-2) | The whole preview did open, so the download worked, but the finished book still does not feel like our family story. I also notice an especially important error on the title page: it says “Margaret Ellison, age 5,” altho | click |
| 24 | OurLegacy - Turn your family story into  | reassured (1) | Yes, the “Change” button has brought me back to the editable details, although it now says “Done” rather than “Change.” I can correct the age here by clearing the 5, because I am the storyteller and Oliver is the five-ye | type; click; wait_for_change |
| 25 | OurLegacy - Turn your family story into  | reassured (1) | Good, the empty age has been accepted and the newer PDF appears first, so I can tell which one is the corrected version. I need to open that newest download and inspect all 32 pages again, particularly the title page and | click |
| 26 |  | reassured (1) | Oh, the age mistake has been corrected: Margaret Ellison is now named as the teller without being made into a five-year-old. I shall now turn through all 32 pages and check the text and every picture again, especially wh | flip_through |
| 27 |  | reassured (1) | The title-page mistake has been corrected, which is a relief. However, I have not yet been allowed to inspect all 32 pages properly; the sidebar shows more pages, so I need to continue through the embedded PDF. | flip_through (FAILED) |
| 28 |  | impatient (0) | The correction has worked on this first page, which is a relief. However, the previous page-turn control failed and there is no clearly visible next-page button; I shall try the keyboard after selecting the PDF, rather t | click (FAILED) |
| 29 | OurLegacy - Turn your family story into  | frustrated (-2) | I have now inspected every page and picture, and the age error on the title page is fixed. However, the family relationships throughout much of the book are still wrong: it still treats an invented grandfather as the cen | click |
| 30 | Review Storybook \| OurLegacy | frustrated (-1) | I have now corrected what the website allowed me to correct, regenerated the PDF, and examined the finished result. The title-page age mistake is fixed, but the central family relationships are still wrong, so this is no | done |
