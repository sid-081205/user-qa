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
*Artifact:* Personalized illustrated digital storybook and printable keepsake preview

> The pictures are pretty and the blue kite, Welsh hill and Oliver's details are warm, but I cannot accept this as our family book while my father is turned into Grandpa and I am replaced by an elderly man. The loving words and gentle story are not enough to overcome such a central mistake, and I would need every relevant scene and relationship checked and corrected before trusting it.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | The book preserves many supplied details, including the blue kite, old blue shirt, Welsh farmhouse, windy hill, Oliver's curls, freckles and green wellies, the dedication, and the childhood kite-flying memory. However, i |
| coherence | 1 | The story has a recognizable beginning, middle and end, but the family relationships change abruptly. The father becomes "Grandpa's daddy," little Margaret becomes a boy, and Oliver is presented as the grandson of an inv |
| age fit | 3 | The sentences are mostly short, gentle and emotionally suitable for a five-year-old, with no frightening or inappropriate content. The automatic reading level is grade 4.3 despite the requested reading age of five, so so |
| language | 2 | The prose is generally clear and readable, and the dedication is warmly expressed. There are important presentation and clarity problems: the heading does not match the entered title, the $4.00 charge is unexplained, the |
| text image fit | 2 | Many watercolor images beautifully establish the blue kite, Welsh hill, farmhouse and kite flight. Nevertheless, many pictures contradict their text: the text calls the adult Margaret's father while the image shows an el |
| character consistency | 1 | Oliver is reasonably consistent in the later scenes, with brown curly hair, freckles and green wellies. The other characters are not: the child changes from a girl to a boy and loses the specified short silver hair, roun |
| visual quality | 3 | The watercolor illustrations are attractive, warm and generally clear, especially the countryside, farmhouse and kite scenes. The finished book feels unfinished because of the blank cover and duplicate title pages, empty |
| emotional resonance | 2 | The book has real emotional potential because it uses Margaret's family memory, Oliver's appearance, the Welsh setting, the blue kite and the loving dedication. At present, however, the invented grandfather and the repea |

- **used correctly:** The blue kite made from an old blue shirt; Margaret's father making the kite and teaching her to fly it; The windy hill behind the old farmhouse in Wales; Oliver's brown curly hair, freckles and green wellies; The intended present-day relationship in which Oliver is the hero and Margaret helps him fly the kite; The title input "The Blue Kite" in the title field; The author name Margaret Ellison; The dedication to Oliver; The ownership name Oliver Ellison; The watercolor style and reading-age request
- **missing:** A consistent visual identity for little Margaret with short silver hair, round glasses and a blue cardigan; A consistent present-day depiction of Margaret as Oliver's grandmother; A clear cover showing Oliver and Margaret with the kite; A real cast-of-characters page; A clear explanation of what the $4.00 charge includes; A clear explanation of the hardcover price and its current availability; A full-size way to inspect and correct every scene before choosing the final PDF
- **changed:** The entered title "The Blue Kite" is replaced by the displayed heading "Grandpa's Blue Kite"; Margaret's father is changed into an invented Grandpa or "Grandpa's daddy"; Little Margaret is changed into a generic brown-haired girl and later a boy; Margaret is replaced in the present-day scenes by an elderly silver-haired man; Oliver is made the grandson of the invented Grandpa rather than Margaret's grandson; The original "today" visit is changed into an invented "next day" trip back to Wales; The joint promise between Margaret and Oliver is weakened into an unnamed "they"
- **invented:** An invented Grandpa character; The relationship "Grandpa's daddy"; A story in which Oliver is Grandpa's grandson; An automatic story date that was not supplied; A story in which the present-day adult is an elderly man rather than Margaret

### Part by part
#### Storybook cover/listing
![I1](artifacts/capture_01/img_00.jpg)
> My Storybooks $4.00 My Storybooks 1 storybook Create New Grandpa's Blue Kite Watercolor \| 10 scenes 22 minutes ago
- *Picture:* A warm watercolor-style picture set in a farmhouse kitchen. An adult man and a brown-haired boy are making or repairing a large blue kite from pieces of blue fabric. The kite is clearly visible, but the child is a boy rather than little Margaret.
- *Reaction:* The picture is pretty and the blue kite is easy to recognise, but I would not recognise my family in it. My father made the kite with me when I was a little girl, not with a boy called Grandpa.
  - [fidelity, sev 4] The listing calls the book "Grandpa's Blue Kite," although my chosen title was "The Blue Kite" and my corrected family story identifies the kite-maker as my father.
  - [fidelity, sev 4] The picture shows an adult man and a boy in a kitchen, rather than my father and little Margaret carrying the finished kite on the windy Welsh hill. This contradicts my later corrections, which explicitly said, "Replace the boy with little Margaret, a young girl."
  - [character_consistency, sev 3] The child has short brown hair and no visible round glasses or blue cardigan, so he does not match the requested depiction of little Margaret.
  - [text_image_fit, sev 3] The blue kite matches the central object, but the image does not show the corrected event or setting: Margaret and her father carrying it up the windy hill behind the old farmhouse in Wales.
  - [emotional_resonance, sev 4] The attractive picture feels like a pleasant generic kite story, but calling my father "Grandpa" and showing a boy instead of me would make this unsuitable as a personal family keepsake.
- **Change I'd make:** Change the title to "The Blue Kite" and replace this picture with a clear watercolor scene of my father, an older Welsh man, making or carrying the kite with little Margaret. Margaret should be recognisably a young girl, with short silver hair, round glasses, and a blue cardigan, on the windy hill behind the old farmhouse in Wales. Do not show Oliver, Grandpa, or any invented relative.
- **Suggested rewrite:** The Blue Kite

#### Export page header and purchase options
![I2](artifacts/capture_19/view_00.jpg)
![I4](artifacts/capture_55/view_00.jpg)
> OurLegacy My Storybooks $4.00 Create Review 3 Output Back to review Grandpa's Blue Kite Make a digital PDF, a narrated video, or order a printed book. Generate Book Preview Preview A watermarked preview of the exact 32-page book you can order — personalize it below; what you preview is what gets printed. Title The Blue Kite Author Margaret Ellison Teller’s age 5 Story told on 26/09/2026 Printed Book Keepsake A real hardcover keepsake shipped to your door. Hardcover $59 Order Printed Book Printing is coming soon ✨
- *Picture:* A clean export page headed “Grandpa’s Blue Kite.” Below it are a book-preview panel and a printed-book panel. The $59 hardcover button is pale and unavailable, with “Printing is coming soon” underneath.
- *Reaction:* I can see the price, but the $4.00 in the navigation has no explanation, and I still cannot order the $59 book. More importantly, the heading says “Grandpa’s Blue Kite” even though the field beneath correctly says “The Blue Kite.”
  - [fidelity, sev 3] The page heading says “Grandpa's Blue Kite,” although the Title field says “The Blue Kite.”
  - [language, sev 2] The page shows “$4.00” at the top and “Hardcover $59” without explaining whether the $4.00 is a charge, a credit, or something else.
  - [language, sev 2] “Make a digital PDF, a narrated video, or order a printed book” promises a narrated-video option, but no narration control is shown in this capture.
  - [visual_quality, sev 1] The explanatory text and some controls are small and grey, making them harder to read.
- **Change I'd make:** Change the page heading and filename description to “The Blue Kite,” explain exactly what the $4.00 charge covers, and label the hardcover as “$59 — not yet available to order.” I would also show a clear narration option if one is actually offered.
- **Suggested rewrite:** The Blue Kite Create a preview and choose a download or printed-book option. Hardcover: $59. Printed books are not yet available to order.

#### Preview settings and cover
![I3](artifacts/capture_19/view_01.jpg)
> Title The Blue Kite Author Margaret Ellison Teller’s age 5 Story told on 26/09/2026 Dedication For Oliver, with love from Grandma Maggie. May w This book belongs to Oliver Ellison Cover image Scene 8 Change Generation in progress... Generated Exports PDF Generating...
- *Picture:* The lower portion of the preview panel shows the dedication and ownership fields. A small watercolor cover thumbnail labelled “Scene 8” depicts a blue kite above an adult man and a child standing outdoors. A generation message and a generating PDF status appear below.
- *Reaction:* The blue kite is easy to recognise, but the cover does not show the present-day relationship I wanted between Oliver and his grandmother. I cannot tell from this thumbnail whether it has also confused the child as a boy.
  - [fidelity, sev 3] The cover thumbnail shows an adult man and a child, rather than five-year-old Oliver with his grandmother as in the family story’s present-day ending.
  - [text_image_fit, sev 3] The cover is labelled “Scene 8,” but the selected picture does not visibly present the relationship emphasized in my original ending, where Oliver is the hero and I help him fly the kite.
  - [fidelity, sev 2] The dedication is visibly cut off after “For Oliver, with love from Grandma Maggie. May w,” so the full wording cannot be checked here.
- **Change I'd make:** Use a cover showing five-year-old Oliver in green wellies flying the blue kite with his grandmother, rather than an adult man and a child. Display the dedication across enough space to show the whole sentence, and let me enlarge the cover before accepting it.
- **Suggested rewrite:** For Oliver, with love from Grandma Maggie. May we always keep the old blue kite safe.

#### Final export settings after generation
![I4](artifacts/capture_55/view_00.jpg)
> OurLegacy My Storybooks $4.00 Create Review 3 Output Back to review Grandpa's Blue Kite Make a digital PDF, a narrated video, or order a printed book. Generate Book Preview Preview A watermarked preview of the exact 32-page book you can order — personalize it below; what you preview is what gets printed. Title The Blue Kite Author Margaret Ellison Teller’s age Optional Story told on 26/09/2026 Dedication For Oliver, with love from Grandma Maggie. May w Printed Book Keepsake A real hardcover keepsake shipped to your door. Hardcover $59 Order Printed Book Printing is coming soon ✨
- *Picture:* This is the same export page after generation. The teller’s age field now reads “Optional,” while the cover gallery is lower on the page. The printed-book button remains unavailable.
- *Reaction:* “Optional” is not a mistake: I deliberately cleared the teller’s age on my last visit. The unresolved “Grandpa’s Blue Kite” heading and the unexplained date “26/09/2026” still need attention.
  - [fidelity, sev 3] The final page still says “Grandpa's Blue Kite” even though my submitted title was “The Blue Kite.”
  - [fidelity, sev 2] “Story told on 26/09/2026” is displayed even though I did not enter a story date in the information provided.
  - [language, sev 2] The label “Story told on” does not explain whether the date means when the memory happened, when I told the story, or when the file was created.
- **Change I'd make:** Synchronize the heading with the accepted title, and do not insert a date automatically. Ask me to choose “No story date” or clearly label an automatically added date as the file-generation date.
- **Suggested rewrite:** The Blue Kite Teller’s age: Optional Story date: Not supplied

#### Final cover gallery and PDF downloads
![I5](artifacts/capture_55/view_01.jpg)
> Cover image Scene 8 Done 1 2 3 4 5 6 7 8 9 10 Regenerate PDF Generated Exports PDF Sep 26, 2026, 8:57 PM 2.4 MB Custom title Author: Margaret Ellison Dedication Bookplate Cover: Scene 8 Download PDF Sep 26, 2026, 8:56 PM 2.4 MB Custom title Author: Margaret Ellison Dedication Bookplate Cover: Scene 8 Download
- *Picture:* A gallery of ten small watercolor scene thumbnails is shown, with Scene 8 outlined as the cover. Several thumbnails appear to show a taller dark-haired male figure with a child, while others show kite-making or kite-flying scenes. Two PDF entries, one minute apart, are listed with Download buttons.
- *Reaction:* The pictures are attractive as small thumbnails, but they still do not make me recognise my family; the child and relationships need careful checking at full size. I also cannot tell which of the two nearly identical PDFs is the final one.
  - [fidelity, sev 3] Several thumbnails show a taller male figure with a child, rather than clearly showing little Margaret as a silver-haired girl in a blue cardigan or the intended present-day pairing of Margaret and Oliver.
  - [character_consistency, sev 3] The gallery thumbnails do not consistently make the intended child and adult characters recognisable; the cover and several scenes appear to use a generic man-and-child pairing.
  - [emotional_resonance, sev 3] The selected cover is described in the interface only as “Scene 8” and, at the thumbnail size shown, does not convey the personal relationship that would make this a family keepsake.
  - [language, sev 2] The two downloads are distinguished only by timestamps, “Sep 26, 2026, 8:57 PM” and “Sep 26, 2026, 8:56 PM”; neither is marked “Latest” or “Earlier version.”
  - [visual_quality, sev 1] The thumbnails are too small in this view to inspect faces, hands, clothing, or the kite construction properly.
- **Change I'd make:** Let me open each scene at a large size and correct the characters before regenerating the PDF. Mark the 8:57 file as “Latest PDF” and the 8:56 file as “Earlier version,” and make the selected cover show Oliver and his grandmother with the blue kite if that is the ending I am keeping.
- **Suggested rewrite:** Latest PDF — Sep 26, 2026, 8:57 PM Earlier version — Sep 26, 2026, 8:56 PM

#### Cover / Title page / Page 1
![I6](artifacts/capture_60/view_00.jpg)
> The Blue Kite told by Margaret Ellison September 2026
- *Picture:* A plain white title page with the navy title, a small author line, a date, a large pale 'OurLegacy PREVIEW' watermark, and small preview text at the bottom. There is no actual cover illustration.
- *Reaction:* The title and author are clear, but this does not look like an attractive keepsake cover, and I would be disappointed to see a preview watermark across a family book.
  - [visual_quality, sev 3] The page is almost entirely blank, with 'OurLegacy PREVIEW' and 'PREVIEW · NOT FOR RESALE' visible.
  - [fidelity, sev 2] The page says 'told by Margaret Ellison' correctly, but there is no cover image showing the blue kite, Wales, or the family.
  - [language, sev 1] The date 'September 2026' was not part of my supplied story details and appears to have been added by the website.
- **Change I'd make:** Use a real watercolor cover showing the old blue kite flying above the Welsh farmhouse, with Margaret and Oliver clearly identifiable, and remove the preview watermark from the final file.

#### Title page / Page 2
![I7](artifacts/capture_61/view_00.jpg)
> The Blue Kite
- *Picture:* Another almost blank white page with the title repeated and the pale 'OurLegacy PREVIEW' watermark.
- *Reaction:* Repeating the title on an empty page makes the book feel unfinished rather than special.
  - [visual_quality, sev 3] The page contains no illustration and is dominated by the 'OurLegacy PREVIEW' watermark.
  - [emotional_resonance, sev 2] The second title page adds no family picture or meaningful introduction.
- **Change I'd make:** Replace this duplicate blank page with a warm watercolor family scene or remove it and begin the story on this page.

#### Dedication / Page 3
![I8](artifacts/capture_62/view_00.jpg)
> For Oliver, with love from Grandma Maggie. May we always keep the old blue kite safe.
- *Picture:* A white dedication page with italic text and a very small blue kite illustration beneath it, partly obscured by the pale preview watermark.
- *Reaction:* The words are loving and exactly reflect my intention, but the little kite is too small to give the page warmth.
  - [visual_quality, sev 2] The kite illustration is tiny and faint, while the large watermark cuts across the page.
  - [emotional_resonance, sev 1] The personal dedication is strong, but the page does not show Margaret and Oliver or their relationship.
- **Change I'd make:** Keep the dedication but add a gentle watercolor of Oliver holding the kite with Margaret, and remove the watermark.

#### Cast of characters / Page 4
![I9](artifacts/capture_63/view_00.jpg)
> Cast of characters
- *Picture:* A blank white page with only the heading 'Cast of characters' and the preview watermark.
- *Reaction:* I would expect this page to tell me who is in our story, but nobody is actually introduced.
  - [fidelity, sev 2] The page lists no characters despite the story needing Margaret as a child, her father, and Oliver.
  - [language, sev 2] The heading promises a cast list, but no names or descriptions follow.
  - [visual_quality, sev 3] The page is empty apart from the heading and watermark.
- **Change I'd make:** Add a short illustrated cast list: little Margaret, her father, and Oliver, with the relationships clearly stated.
- **Suggested rewrite:** This is our family: Margaret, who made this kite when she was a little girl. Her father, who taught her how to fly it. Oliver, Margaret's grandson and the hero of our story.

#### This book belongs to / Page 5
![I10](artifacts/capture_64/view_00.jpg)
> This book belongs to Oliver Ellison signed
- *Picture:* A simple ownership page with Oliver Ellison's name inside a pale rectangular box and a signing line.
- *Reaction:* This is a nice personal touch, and Oliver's name is correct, though the page is very plain.
  - [visual_quality, sev 1] The ownership page is plain and the preview watermark crosses the page.
- **Change I'd make:** Keep the ownership wording, perhaps with a small watercolor kite in the corner and no watermark.

#### Story opening / Page 6
![I11](artifacts/capture_65/view_00.jpg)
> One summer, my father made me something very special. He cut up an old blue shirt and made it into a kite!
- *Picture:* A white text page with the sentence centered in dark blue type. A very small kite illustration appears below, partly covered by the watermark.
- *Reaction:* This is a clear and faithful beginning, with short sentences that a five-year-old could follow.
  - [text_image_fit, sev 1] The tiny kite is decorative, but it does not show my father making the kite from the old blue shirt.
  - [visual_quality, sev 2] The pale preview watermark and very small illustration make the page look like a draft rather than a finished keepsake.
- **Change I'd make:** Use a full-page watercolor of my father making the kite while I watch, clearly showing the old blue shirt and the kite frame.

#### Making the kite / Page 7
![I12](artifacts/capture_66/view_00.jpg)
- *Picture:* A watercolor scene inside a farmhouse kitchen. A young girl with brown hair kneels beside a man who is attaching spars and string to a blue kite made from fabric; scraps of blue shirt and ribbon lie on the floor.
- *Reaction:* The picture is attractive and the making of the kite is easy to understand, but the child looks like an ordinary brown-haired girl rather than the specified little Margaret with short silver hair, round glasses, and a blue cardigan.
  - [character_consistency, sev 3] The girl has long brown hair, no visible round glasses, and no blue cardigan; the instructions specifically requested short silver hair, round glasses, and a blue cardigan.
  - [fidelity, sev 2] The man is shown making the kite with a child, but the picture does not clearly identify the child as Margaret.
  - [character_consistency, sev 1] The man's appearance here must remain consistent with the later hill and kite-flying scenes.
- **Change I'd make:** Regenerate the image with a little Margaret who has short silver hair, round glasses, and a blue cardigan, and show my father, an older Welsh man, making the kite from the old blue shirt.

#### Walking up the hill / Page 8
![I13](artifacts/capture_67/view_00.jpg)
> The blue kite was ready! My father and I carried it up the big windy hill behind the old farmhouse.
- *Picture:* A white text page with the sentence centered in dark blue type. A tiny kite illustration is visible below the text beneath the watermark.
- *Reaction:* The sentence is easy to understand and follows the memory, but the small image does not show the walk.
  - [text_image_fit, sev 2] The page says my father and I carried the kite up the hill, but the tiny decorative image does not depict either of us or the farmhouse.
  - [fidelity, sev 1] Wales is not named in this page's text, although it is part of the memory and appears elsewhere.
- **Change I'd make:** Replace the tiny decoration with a full-page watercolor of little Margaret and her father carrying the kite up the hill behind the old farmhouse in Wales.
- **Suggested rewrite:** The blue kite was ready! My father and I carried it up the big, windy hill behind the old farmhouse in Wales.

#### Hill scene / Page 9
![I14](artifacts/capture_68/view_00.jpg)
- *Picture:* A broad watercolor landscape shows a man and a child carrying a blue kite up a green hill, with a stone wall, countryside, and an old farmhouse in the distance.
- *Reaction:* This is a lovely picture of the hill and the kite, but the child is shown as a boy with short brown hair, not as little Margaret.
  - [character_consistency, sev 3] The child appears to be a boy; the requested character was little Margaret, a young girl, with short silver hair, round glasses, and a blue cardigan.
  - [fidelity, sev 2] The picture does not visibly establish that the child is my father's daughter or that she is Margaret.
  - [text_image_fit, sev 2] The image complements the hill scene, although the identity of the child is wrong.
- **Change I'd make:** Regenerate the image with little Margaret, clearly a girl with short silver hair, round glasses, and a blue cardigan, walking beside her father.

#### First kite flight / Page 10
![I15](artifacts/capture_69/view_00.jpg)
> Grandpa's daddy threw the kite up into the wind. Up, up, up it went — dancing in the bright blue sky!
- *Picture:* A white text page with the sentence centered in dark blue type and a tiny kite illustration below it beneath the watermark.
- *Reaction:* This is where the story goes seriously wrong: my father has been changed into 'Grandpa's daddy,' and the page does not show the first kite flight.
  - [fidelity, sev 4] The text says "Grandpa's daddy" although the person making and flying the kite is my father, not an invented grandfather.
  - [coherence, sev 4] The relationship suddenly changes from 'my father' to 'Grandpa's daddy' without any explanation.
  - [text_image_fit, sev 2] The page describes the kite going up, but the visible image is only a tiny decorative kite.
- **Change I'd make:** Replace the relationship with 'my father' and use the full-page watercolor of my father helping little Margaret launch the kite.
- **Suggested rewrite:** My father threw the kite up into the wind. Up, up, up it went, dancing in the bright blue sky!

#### Flying the kite / Page 11
![I16](artifacts/capture_70/view_00.jpg)
- *Picture:* A watercolor scene shows an older man and a boy flying a blue kite high in a cloudy sky. The boy is jumping with both arms raised.
- *Reaction:* The kite and sky are lovely, but this is not our family: the child is a boy and the man has been presented as an invented grandfather rather than my father and little Margaret.
  - [character_consistency, sev 4] The child is visibly a boy with short hair, not little Margaret in a blue cardigan and round glasses.
  - [fidelity, sev 4] The picture shows the wrong generation and relationships, matching the invented 'Grandpa's daddy' in the preceding text.
  - [text_image_fit, sev 2] The image shows a kite flying upward, but it does not show the requested father and daughter launching it.
- **Change I'd make:** Regenerate the scene with my father and little Margaret flying the kite together, keeping the same Welsh hill and sky.

#### Teaching Margaret / Page 12
![I17](artifacts/capture_71/view_00.jpg)
> Grandpa's daddy showed him how to hold the string. 'Let out a little more when the wind blows strong,' he said.
- *Picture:* A white text page with the sentence centered in dark blue type and a small kite illustration below it beneath the watermark.
- *Reaction:* The advice itself is warm and close to my memory, but the words have changed the people and gender of the story, and the picture does not show the lesson.
  - [fidelity, sev 4] The text says "Grandpa's daddy showed him" even though my father taught me, a girl, how to hold the string.
  - [coherence, sev 4] The pronoun 'him' conflicts with the earlier first-person memory and the requested child Margaret.
  - [text_image_fit, sev 2] The page describes teaching someone to hold the string, but the visible image is only a tiny kite.
  - [age_fit, sev 3] The dialogue is understandable, but the incorrect family language makes the page confusing rather than comforting for a five-year-old.
- **Change I'd make:** Correct the relationship and pronoun, and illustrate my father showing little Margaret how to hold the string on the windy hill.
- **Suggested rewrite:** My father showed me how to hold the string. 'Let out a little more when the wind blows strong,' he said.

#### Page 13
![I18](artifacts/capture_72/view_00.jpg)
- *Picture:* A watercolor landscape shows an elderly silver-haired man helping a small fair-haired boy hold a kite reel on the windy Welsh hillside, with the farmhouse below.
- *Reaction:* The picture is attractive and the kite and hill are easy to recognise, but the people are wrong. This is supposed to show my father teaching little Margaret, not an old man and a boy.
  - [fidelity, sev 4] The image shows an elderly man and a small boy where the story requires my father and his young daughter, Margaret.
  - [text_image_fit, sev 3] The illustration continues the book's invented 'Grandpa' story and does not support the preceding instruction that my father showed me how to hold the string.
  - [character_consistency, sev 4] The child is a fair-haired boy in a white shirt and shorts, not little Margaret as explicitly requested.
- **Change I'd make:** Redraw this as little Margaret as a clearly female five-year-old child with short silver hair, round glasses, and a blue cardigan, holding the reel while my older Welsh father helps her.

#### Page 14
![I19](artifacts/capture_73/view_00.jpg)
> Many, many years went by. Now Grandpa was old — and he had a grandson of his own. His name was Oliver.
- *Picture:* A white text page with a pale diagonal 'OurLegacy PREVIEW' watermark, a short green rule, and a small decorative blue kite-like flourish.
- *Reaction:* This sentence is plainly wrong: Oliver is my grandson, not the grandson of an invented Grandpa. The layout is calm and readable, but the family history at its heart is untrue.
  - [fidelity, sev 4] The text says, 'Grandpa was old — and he had a grandson of his own,' contradicting my input that Oliver is my grandson and my narrator's grandson.
  - [coherence, sev 4] The subject changes from the remembered Margaret-and-father story to an old man named Grandpa, even though I specifically requested, 'Do not show Grandpa or any invented family members.'
  - [character_consistency, sev 4] The new central character is 'Grandpa,' who was never part of the requested family story.
- **Change I'd make:** Replace the invented Grandpa with the true relationship: years later, Margaret has a grandson named Oliver, whom she has told the story.
- **Suggested rewrite:** Many years later, I told my grandson Oliver about the day my father and I flew the blue kite.

#### Page 15
![I20](artifacts/capture_74/view_00.jpg)
- *Picture:* Indoors, an elderly silver-haired man sits by a fire holding the folded blue kite while a curly-haired, freckled five-year-old boy in a red top and green trousers kneels beside him. Green wellies stand near the door.
- *Reaction:* Oliver's curls, freckles, and green wellies are recognisable, but the adult must be me, his grandmother. Instead, the picture makes the old man my grandfather and us a different family pair.
  - [fidelity, sev 4] The picture shows Oliver with an elderly man and the kite indoors, rather than with his grandmother Margaret after she has told him the family story.
  - [text_image_fit, sev 3] This image follows the wrong claim that Oliver is the grandson of an old man named Grandpa.
  - [character_consistency, sev 4] The adult is consistently wrong: he has been generated as my father, then as an invented Grandpa, rather than distinguishing me as an older woman and my father as the kite-maker.
- **Change I'd make:** Show Margaret at 71, with short silver hair, round glasses, and a blue cardigan, showing or retelling the story to Oliver. Do not add a grandfather.

#### Page 16
![I21](artifacts/capture_75/view_00.jpg)
> The next day, they went back to Wales! Oliver put on his green wellies and they picked up the old blue kite.
- *Picture:* A white text page with a pale diagonal preview watermark, a green rule, and a small blue decorative mark.
- *Reaction:* The green wellies and blue kite come from my own memory, but 'the next day' and going back to Wales have been invented. My memory said that today we climb the same hill together; it did not say we had just returned the previous day.
  - [fidelity, sev 2] The text invents 'The next day, they went back to Wales,' while my input said, 'Today we climb the same hill together.'
  - [fidelity, sev 4] The word 'they' avoids naming the adult, leaving the companion to be understood as the invented Grandpa from the previous page.
  - [coherence, sev 2] No earlier supplied event says that Oliver and Margaret had travelled to Wales and then gone back the next day.
- **Change I'd make:** Name Margaret explicitly and remove the invented travel schedule. State that Oliver and Margaret are going to fly the kite on the Welsh hill that day.
- **Suggested rewrite:** Oliver put on his green wellies. Then we picked up the old blue kite and went out together.

#### Page 17
![I22](artifacts/capture_76/view_00.jpg)
- *Picture:* Outside a stone farmhouse, an elderly silver-haired man carries the blue kite and string while a curly-haired, freckled boy pulls on one green welling boot.
- *Reaction:* The farmhouse, wellies, and kite are welcome, but I am not in this picture at all. The adult has again been made into my male partner or grandfather rather than me, Margaret.
  - [fidelity, sev 4] Margaret is absent; the visible adult is an elderly man who has repeatedly replaced the correct family member.
  - [text_image_fit, sev 1] The text says Oliver puts on 'his green wellies,' but the image shows him pulling on only one boot while the other green wellie is absent from his feet.
  - [character_consistency, sev 4] The recurring adult is wrong, and no short-haired, glasses-wearing older Margaret is kept consistent across the present-day scenes.
- **Change I'd make:** Replace the elderly man with Margaret, described as 71 with short silver hair, round glasses, and a blue cardigan. Show Oliver pulling on both green wellies while Margaret holds the kite.

#### Page 18
![I23](artifacts/capture_77/view_00.jpg)
> Up the big hill they climbed together. The wind was blowing just like it did long, long ago.
- *Picture:* A white text page with a pale diagonal 'OurLegacy PREVIEW' watermark, a short green rule, and a small decorative flourish.
- *Reaction:* The sentence itself is gentle and preserves the windy hill, but 'they' again refers to Margaret and the wrong elderly man. That vague phrasing hides rather than fixes the relationship error.
  - [fidelity, sev 4] The unnamed 'they' follows the previous page's elderly man, although the remembered pair who climbed the hill was Margaret and her father, and the present pair should be Margaret and Oliver.
  - [coherence, sev 3] The transition is smooth, but its characters are inconsistent with the requested family relationships and even with the truthful source story.
- **Change I'd make:** Name Oliver and Margaret so that the relationship is unambiguous and separate the childhood climb from the present-day climb.
- **Suggested rewrite:** Oliver and I climbed the big hill together. The wind blew just as it had when I was little.

#### Page 19
![I24](artifacts/capture_78/view_00.jpg)
- *Picture:* An elderly silver-haired man and a curly-haired, freckled boy climb a green hillside together. The man carries the folded blue kite, with a farmhouse and valley far below.
- *Reaction:* This is a lovely watercolor of the right hill and kite, but it is the wrong family. I should be climbing beside Oliver as his 71-year-old grandmother, not as an elderly male grandfather.
  - [fidelity, sev 4] The adult companion is an elderly man, while the present-day adult in my memory is Margaret, Oliver's grandmother.
  - [text_image_fit, sev 2] The illustration generally matches 'they climbed together,' but visually confirms the incorrect identity concealed by the pronoun.
  - [character_consistency, sev 4] The same incorrect elderly man is reused from page to page instead of preserving the specified appearance of Margaret.
- **Change I'd make:** Redraw Margaret and Oliver climbing the hill together, with Margaret carrying the kite and using the specified short silver hair, round glasses, and blue cardigan.

#### Page 20
![I25](artifacts/capture_79/view_00.jpg)
> Grandpa helped Oliver hold the string. The blue kite flew up, up into the summer sky — just like before!
- *Picture:* A white text page with a pale preview watermark, a short green rule, and a small blue decorative flourish.
- *Reaction:* The flying-kite image and repeated upward movement are appropriate, but 'Grandpa' is an invented and incorrect relationship. This is the central error I would not allow in a family keepsake.
  - [fidelity, sev 4] The text says, 'Grandpa helped Oliver hold the string,' but I am Oliver's grandmother, and I specifically asked not to show an invented grandfather.
  - [coherence, sev 4] This continues the website's invented Grandpa storyline instead of returning to the true present-day relationship in the source narrative.
- **Change I'd make:** Replace Grandpa with Grandma Margaret and identify Oliver as the hero holding the string.
- **Suggested rewrite:** I helped Oliver hold the string. Up, up went the blue kite into the summer sky!

#### Page 21
![I26](artifacts/capture_80/view_00.jpg)
- *Picture:* A curly-haired, freckled boy in a red top, green trousers, and green wellies laughs while holding the kite reel. An elderly silver-haired man stands closely behind him as the blue kite flies high in a cloudy sky.
- *Reaction:* The joy is warm and Oliver looks appealing, but the person helping him should be me. This attractive picture would be much more personal with my own silver hair, glasses, and blue cardigan beside him.
  - [fidelity, sev 4] The elderly man replaces Margaret and is presented as the family member helping Oliver fly the kite.
  - [character_consistency, sev 4] Margaret is still absent and does not match the requested present-day description of a 71-year-old woman with short silver hair, round glasses, and a blue cardigan.
- **Change I'd make:** Show Oliver holding the reel while Margaret stands beside him in her blue cardigan, with a warm but age-appropriate expression.

#### Page 22
![I27](artifacts/capture_81/view_00.jpg)
> Oliver laughed and laughed as the kite swooped and danced. It was the best feeling in the whole world!
- *Picture:* A white text page with a pale diagonal preview watermark, a green rule, and a small decorative flourish.
- *Reaction:* This is a warm, simple ending to the flight, and 'the kite swooped and danced' is close to the wording in my own memory. I do not object to the flourish 'the best feeling in the whole world.'
  - [fidelity, sev 2] This text does not identify the incorrect adult, but it depends on the preceding page where Oliver was wrongly shown with an invented Grandpa.
- **Change I'd make:** Retain the wording if the preceding image and relationship are corrected; no substantial text change is needed.

#### Page 23
![I28](artifacts/capture_82/view_00.jpg)
- *Picture:* The curly-haired boy spreads his arms and laughs beneath the partly visible blue kite. The same elderly silver-haired man stands beside him on the sunny hillside.
- *Reaction:* It is a cheerful illustration, and Oliver's appearance is consistent, but the wrong elderly man again displaces me. I would treasure this picture much more if it showed my actual relationship with him.
  - [fidelity, sev 4] Margaret is missing from the central present-day memory, replaced throughout by an invented elderly male relative.
  - [text_image_fit, sev 2] The image complements Oliver laughing after the kite swoops and dances, but it also reinforces the wrong family pairing.
  - [character_consistency, sev 4] Oliver remains broadly consistent, but the adult's identity has remained consistently incorrect throughout the present-day sequence.
- **Change I'd make:** Replace the elderly man with Margaret while preserving Oliver's joyful pose. Keep Oliver's brown curly hair, freckles, red top, green trousers, and green wellies.

#### Page 24
![I29](artifacts/capture_83/view_00.jpg)
> They promised to keep the old blue kite safe for ever. Every time they came to Wales, they would fly it together.
- *Picture:* A white text page with a pale diagonal 'OurLegacy PREVIEW' watermark, a short green rule, and a small blue decorative flourish.
- *Reaction:* This is a proper closing thought, but it is spoiled by 'they.' I had promised with Oliver to keep the old blue kite safe and bring it whenever our family visited Wales.
  - [fidelity, sev 3] The text changes my joint promise with Oliver into a vague promise by an unspecified 'they,' following the invented Grandpa storyline.
  - [fidelity, sev 2] The input said, 'We promise to keep the old blue kite safe and to bring it whenever our family visits Wales,' but the output has shifted the focus to 'they would fly it together.'
  - [coherence, sev 3] The pronoun is unclear after the previous page's incorrect pairing of Oliver with an elderly man.
- **Change I'd make:** Name Oliver and Margaret and restore the promise to keep the kite safe and bring it on family visits to Wales.
- **Suggested rewrite:** Oliver and I promised to keep the old blue kite safe. Whenever our family visited Wales, we would bring it out again.

#### Page 25
![I30](artifacts/capture_84/view_00.jpg)
- *Picture:* A watercolor-style view from a grassy hill above a Welsh-looking farmhouse at sunset. Oliver, with brown curly hair, freckles, a red top, green trousers, and green wellies, stands beside an elderly silver-haired man in a blue jacket. The man has one arm around Oliver. A blue kite with crossed spars and long trailing ribbons lies in the foreground.
- *Reaction:* The countryside and Oliver look warm and attractive, but I cannot accept this picture as our family memory. The man is presented as Grandpa, although the present-day person with Oliver should be me, Margaret.
  - [fidelity, sev 4] The picture shows Oliver with an elderly silver-haired man, although my input says, "Today we climb the same hill together" and Oliver is my grandson.
  - [character_consistency, sev 4] Margaret does not appear at all; the site replaces her with an unnamed elderly man.
  - [text_image_fit, sev 4] This is the illustration following the promise that they would always fly the kite together, but it contradicts the supplied relationship by showing the wrong adult.
  - [emotional_resonance, sev 4] The tender hilltop pose is moving, but it is not my relationship with Oliver and therefore is not a faithful keepsake for me.
- **Change I'd make:** Redraw the scene with Margaret Ellison, not an elderly man. Show Margaret as a 71-year-old woman with short silver hair, round glasses, and a blue cardigan, standing or crouching beside Oliver while he holds the kite string. Keep Oliver's brown curly hair, freckles, green wellies, the farmhouse, and the blue kite.

#### Page 26
![I31](artifacts/capture_85/view_00.jpg)
> The End Made with love, and kept forever.
- *Picture:* A softly painted closing scene with the blue kite resting beside a stone wall and an old stone farmhouse, surrounded by grass and wildflowers in warm evening light. The words “The End” and “Made with love, and kept forever.” are placed over the picture. A diagonal OurLegacy preview watermark and a small “PREVIEW · NOT FOR RESALE · OURLEGACY FAMILY” label are visible.
- *Reaction:* This is a proper, quiet ending, and the saved kite beside the farmhouse suits the promise in our story. The lettering is clear, although I would not want the preview watermarks in a purchased copy.
  - [visual_quality, sev 1] A large diagonal “OurLegacy PREVIEW” watermark and a “PREVIEW · NOT FOR RESALE” label cross the picture.
- **Change I'd make:** Remove all preview watermarks and labels from the purchased version. Otherwise, retain the simple final wording and closing illustration.

#### Page 27
![I32](artifacts/capture_86/view_00.jpg)
![I34](artifacts/capture_88/view_00.jpg)
> The story behind these pages “The blue kite flew up, up into the summer sky — just like before!” The summer my father made me a kite out of an old blue shirt. We carried it up the windy hill behind the old farmhouse in Wales, and the bright blue kite danced high in the sky. My father taught me how to hold the string and how to let out a little more when the wind grew strong. Years later, I told the story to my grandson Oliver. Today we climb the same hill together. Oliver has brown curly hair and freckles, and he is wearing his green wellies. This time Oliver is the hero, and I help him fly Grandpa's blue kite. The kite climbs above the farmhouse and the summer clouds, and Oliver laughs as it swoops and dances. We promise to keep the old blue kite safe and to bring it whenever our family v
- *Picture:* A white reference page headed “The story behind these pages.” It reproduces the supplied family narrative in a long paragraph, with a large, faint diagonal OurLegacy preview watermark and small footer text.
- *Reaction:* This page faithfully reproduces what I entered, including the phrase “Grandpa's blue kite,” so that wording came from me rather than being invented here. I can recognise my memory in it, though it does not repair the different family story printed in the main tale.
  - [coherence, sev 3] This reference account says, "Today we climb the same hill together" and Oliver is my grandson, while the illustrated story has treated Oliver as Grandpa's grandson and paired him with an elderly man.
  - [visual_quality, sev 1] A large diagonal “OurLegacy PREVIEW” watermark crosses the otherwise plain reference page.
- **Change I'd make:** Keep this page as the source record, but remove the preview watermark and ensure the main story follows the same relationships. If “Grandpa's blue kite” means Oliver's grandfather, retain it here because that phrase came from my input; otherwise change it consistently throughout.

#### Page 28
![I33](artifacts/capture_87/view_00.jpg)
> In your own words Do you remember the first time you ever watched a kite climb into a summer sky?
- *Picture:* A white writing page with a bold heading, one italic question, and nine pale ruled lines for a reply. A large diagonal preview watermark crosses the page.
- *Reaction:* This gives Oliver room to say what the story means to him and is a thoughtful addition. The question and the writing lines are rather small, so I would enlarge them for comfortable reading and writing.
  - [visual_quality, sev 2] The italic question and ruled lines are small and pale against the white page.
  - [visual_quality, sev 1] A large diagonal “OurLegacy PREVIEW” watermark covers the writing area.
- **Change I'd make:** Enlarge the question and increase the contrast and spacing of the writing lines. Remove the preview watermark from the purchased copy.
- **Suggested rewrite:** What is your favourite moment from flying the blue kite?

#### Page 30
![I35](artifacts/capture_89/view_00.jpg)
> Notes & Memories What moment with Oliver made your heart feel fullest on that windy Welsh hill?
- *Picture:* A white notes page with a bold heading, one italic question, and nine pale horizontal writing lines. A diagonal preview watermark crosses the page.
- *Reaction:* This is a thoughtful place for me to add the particular moment I want Oliver to remember. The question is rather small and abstract for a five-year-old, although it is meant for an adult writing in the keepsake.
  - [visual_quality, sev 2] The question and writing lines are small and low-contrast.
  - [age_fit, sev 1] "What moment with Oliver made your heart feel fullest" uses an abstract expression that is less direct for a child beginning to read.
  - [visual_quality, sev 1] A large diagonal “OurLegacy PREVIEW” watermark covers part of the notes page.
- **Change I'd make:** Enlarge the question and ruled lines, remove the preview watermark, and use plainer wording suitable for Margaret to read comfortably.
- **Suggested rewrite:** Notes & Memories What was the happiest moment you and Oliver shared on the windy hill in Wales?

#### Page 31
![I36](artifacts/capture_90/view_00.jpg)
> Hear it read aloud Your private listening code is created with your printed book Every printed book includes a code your family can scan to hear the story read aloud.
- *Picture:* A mostly white information page headed “Hear it read aloud.” An empty outlined square in the centre contains the message about a listening code, with a short explanation below. A diagonal preview watermark crosses the page.
- *Reaction:* I understand that the code is supplied with the printed book rather than with this PDF, and an audio version could be useful. In the preview the key information is very small, and “private” should be explained more clearly before I trust it with a family code.
  - [language, sev 2] "Your private listening code is created with your printed book" does not say whether the code is unique, whether it expires, or whether accessing the recording requires an account.
  - [visual_quality, sev 2] The central code message and lower explanatory sentence are very small, with a large diagonal preview watermark across the page.
- **Change I'd make:** Use larger type and explain the privacy and access terms plainly. State whether the code is unique to our order, whether anyone with it can hear the recording, and whether an account or further payment is required.
- **Suggested rewrite:** Hear the story aloud Your printed book will include a private listening code. Scan the code with a phone or tablet to hear The Blue Kite read aloud. No extra account is needed. Keep the code private because other people may be able to use it to hear the recording.

#### Page 32
![I37](artifacts/capture_91/view_00.jpg)
> OurLegacy Illustrated in watercolors · An OurLegacy Original Printed by OurLegacy · 2026 © 2026 Margaret Ellison. Story told by Margaret Ellison · September 2026. First printed 2026
- *Picture:* A restrained white publication page with the OurLegacy name centred above small publication and copyright details. A large, faint diagonal preview watermark crosses the page.
- *Reaction:* This is orderly and the erroneous “age 5” has been removed, which is an improvement. I would still want “Printed by OurLegacy” confirmed if that is meant literally as the printer, rather than simply the company that produced the book.
  - [language, sev 1] "Printed by OurLegacy" may misleadingly claim that OurLegacy is the physical printer when it may only be the book-making platform.
  - [visual_quality, sev 1] A large diagonal “OurLegacy PREVIEW” watermark crosses the publication page.
- **Change I'd make:** Remove the preview watermark. Confirm who physically printed the book, and change the line to “Published by OurLegacy” if OurLegacy did not print it. Retain the corrected attribution without “age 5.”
- **Suggested rewrite:** OurLegacy Illustrated in watercolors · An OurLegacy Original Published by OurLegacy · 2026 © 2026 Margaret Ellison. Story told by Margaret Ellison. First published September 2026.

#### Output page / title and controls
> OurLegacy My Storybooks $4.00 Create 2 Review 3 Output Grandpa's Blue Kite Complete Export Storybook
- *Picture:* No separate cover or title-page picture is included in the supplied pictures; this is the website's output-review interface with the story title, price and export control.
- *Reaction:* The title is not the one I entered, and calling it “Grandpa's Blue Kite” confirms the relationship mistake before I have even opened the scenes. The £4.00 figure is clear, but this capture does not explain what buying it includes.
  - [fidelity, sev 3] The page calls the book “Grandpa's Blue Kite,” although my entered title was “The Blue Kite.”
  - [emotional_resonance, sev 3] The displayed title makes the book about a grandfather, although the real relationship is my daughter’s son Oliver and his grandmother.
- **Change I'd make:** Change the title to “The Blue Kite” and retain “Author: Margaret Ellison,” “For Oliver” and the entered dedication. Before payment, show plainly what the $4.00 charge includes, whether it is a charge per book, and whether any shipping or additional exports cost extra.
- **Suggested rewrite:** The Blue Kite

#### Scene 1
![I38](artifacts/capture_93/img_00.jpg)
> One summer, my father made me something very special. He cut up an old blue shirt and made it into a kite!
- *Picture:* In a warm watercolor farmhouse room, a dark-haired adult man kneels beside a young brown-haired girl as they make a kite from a blue shirt. The man has dark hair, while the girl has no visible glasses or blue cardigan.
- *Reaction:* The first sentence now says “my father” and “me,” so that important correction has come from my own revised input. The picture is warm and clearly shows the shirt and kite, but the child does not look like the little Margaret I specifically requested.
  - [character_consistency, sev 3] The requested little Margaret has short silver hair, round glasses and a blue cardigan, but I38 shows a brown-haired girl in a pale top and grey skirt or shorts.
  - [fidelity, sev 2] I38 broadly matches “my father made me a kite,” but omits the three identifying features entered for Margaret.
- **Change I'd make:** Redraw the child as little Margaret with short silver hair, round glasses and a blue cardigan, while keeping the father, shirt, kite and farmhouse. Make it unmistakable that the adult is her father.

#### Scene 2
![I39](artifacts/capture_93/img_01.jpg)
> The blue kite was ready! My father and I carried it up the big windy hill behind the old farmhouse.
- *Picture:* A dark-haired man and a young brown-haired girl climb a green hill together. The girl holds the blue kite above her head, and an old farmhouse appears in the distance.
- *Reaction:* The Welsh hill, old farmhouse and shared journey are easy to see. However, I still do not recognise myself as the child, because the requested silver hair, glasses and blue cardigan are missing.
  - [character_consistency, sev 3] I39 again shows a brown-haired girl without glasses or a blue cardigan, unlike the supplied description of little Margaret.
  - [fidelity, sev 2] The text and setting match the supplied memory, but Margaret's requested identifying appearance is absent from the picture.
  - [emotional_resonance, sev 2] Although the hill and kite are personal, the missing visual details of Margaret weaken the family resemblance.
- **Change I'd make:** Keep the composition but redraw little Margaret with short silver hair, round glasses and a blue cardigan. Keep the father recognisably the same man shown in Scene 1.

#### Scene 3
![I40](artifacts/capture_93/img_02.jpg)
> Grandpa's daddy threw the kite up into the wind. Up, up, up it went — dancing in the bright blue sky!
- *Picture:* A dark-haired man and a young girl stand on a windy hill beneath a blue kite. The girl has both arms raised, while the man appears to hold the string.
- *Reaction:* This sentence has replaced my father with “Grandpa's daddy,” which is not something I entered. The picture is lively, but it cannot repair the wrong family relationship in the text.
  - [fidelity, sev 4] The text says “Grandpa's daddy,” but the entered memory says “my father,” and I was expressly instructed to show my father making and flying the kite.
  - [coherence, sev 4] Scenes 1 and 2 use “my father and I,” but Scene 3 abruptly changes to “Grandpa's daddy” without establishing a new narrator or relationship.
  - [character_consistency, sev 3] The little girl in I40 has short brown hair and no glasses or blue cardigan, and the adult no longer matches the clearly dark-haired father in I38–I39.
  - [text_image_fit, sev 2] The picture shows a man and child beneath a rising kite, but it is unclear which person has just thrown it because the man remains with the string while the child raises both arms.
- **Change I'd make:** Replace the relationship wording and redraw the same father and little Margaret from Scene 2. Show my father releasing the line while Margaret watches.
- **Suggested rewrite:** My father let out the string. Up, up, up went the blue kite! It danced in the bright blue sky.

#### Scene 4
![I41](artifacts/capture_93/img_03.jpg)
> Grandpa's daddy showed him how to hold the string. 'Let out a little more when the wind blows strong,' he said.
- *Picture:* An elderly white-haired man stands behind a young brown-haired boy and helps him hold a kite string. The farmhouse and hills are visible in the background.
- *Reaction:* This is plainly the wrong family scene: the child has become a boy and my father has become an old grandfather. I would not want Oliver to inherit this relationship error in our family book.
  - [fidelity, sev 4] The entered instruction was “My father and I” and “little Margaret, a young girl, clearly not a boy,” but the text says “Grandpa's daddy” and “him.”
  - [text_image_fit, sev 4] I41 shows an elderly man teaching a boy, which supports the wrong wording but contradicts the corrected family story in Scenes 1 and 2.
  - [character_consistency, sev 4] The brown-haired girl from I39–I40 becomes a brown-haired boy, and the dark-haired father becomes an elderly man.
  - [coherence, sev 4] The child changes sex and the adult changes identity across successive memories without any explanation.
- **Change I'd make:** Replace both sentences and redraw my father teaching little Margaret, with the same short silver hair, round glasses and blue cardigan shown consistently. Do not show an elderly grandfather.
- **Suggested rewrite:** My father showed me how to hold the string. “Let out a little more when the wind grows strong,” he said.

#### Scene 5
![I42](artifacts/capture_93/img_04.jpg)
> Many, many years went by. Now Grandpa was old — and he had a grandson of his own. His name was Oliver.
- *Picture:* A silver-haired elderly man sits beside a curly-haired boy in a red jumper and green trousers. They hold a blue kite together in a living room with a fire.
- *Reaction:* Oliver is drawn warmly, but the story has made him the grandson of the wrong man. It is my memory, my father’s kite, and Oliver’s relationship is with me, his grandmother.
  - [fidelity, sev 4] The text says “Grandpa was old — and he had a grandson of his own,” but the entered story says Oliver is my grandson and that I tell him my father’s story.
  - [coherence, sev 4] The narration shifts from Margaret's first-person memory to an unexplained third-person account of Grandpa and Oliver.
  - [text_image_fit, sev 4] I42 does show an old man and curly-haired boy with the kite, but it therefore illustrates the invented relationship rather than the requested one.
  - [emotional_resonance, sev 4] The image is affectionate, but it presents Margaret's memory as Grandpa and Oliver's shared story.
- **Change I'd make:** Redraw the scene with me as an older Margaret sharing the kite story with Oliver. I should have short silver hair, round glasses and a blue cardigan, and Oliver should be recognisably the same curly-haired boy.
- **Suggested rewrite:** Many years went by. Now I was older. I told my grandson Oliver the story of the blue kite my father made.

#### Scene 6
![I43](artifacts/capture_93/img_05.jpg)
> The next day, they went back to Wales! Oliver put on his green wellies and they picked up the old blue kite.
- *Picture:* Outside a stone farmhouse, a curly-haired boy pulls on green wellies while an elderly silver-haired man holds the blue kite.
- *Reaction:* The green wellies and Welsh farmhouse are good details, but I can see at once that the adult is an old man rather than me. Calling this “the next day” also feels vague after the time jump in the previous scene.
  - [fidelity, sev 4] The entered story says that today Oliver and I climb the same hill and that I help him fly Grandpa's blue kite; the text and I43 instead pair Oliver with an unnamed elderly man.
  - [character_consistency, sev 4] The silver-haired man in I43 is presented as Oliver's companion, but the supplied character description identifies short silver hair, round glasses and a blue cardigan as Grandma Margaret.
  - [text_image_fit, sev 3] The picture supports the wellies, kite and departure from a farmhouse, but supports the wrong adult companion.
  - [coherence, sev 2] “The next day” has no clearly established trip or plan in the preceding scene.
- **Change I'd make:** Replace the elderly man with Grandma Maggie, wearing her blue cardigan and round glasses, and say why Oliver and Margaret are going to Wales. Keep the green wellies and old kite.
- **Suggested rewrite:** One day, Oliver and I took the old blue kite back to Wales. Oliver put on his green wellies, and we set off together.

#### Scene 7
![I44](artifacts/capture_93/img_06.jpg)
> Up the big hill they climbed together. The wind was blowing just like it did long, long ago.
- *Picture:* A curly-haired boy in a red jumper climbs ahead of an elderly silver-haired man on a green hill. The man carries the folded blue kite, with a winding road and old farmhouse below.
- *Reaction:* The hill and farmhouse are recognisable, and the boy is lively, but this is another picture of Oliver with his grandfather rather than with me. I would need the whole scene redrawn.
  - [fidelity, sev 4] The supplied story places Oliver and Margaret on the hill together; I44 substitutes an elderly man for Margaret.
  - [text_image_fit, sev 4] The picture does show two people climbing a hill, but its adult figure contradicts the intended identity of the person in the entered story.
  - [character_consistency, sev 4] I44 continues the invented silver-haired male grandfather rather than depicting short silver-haired, bespectacled Grandma Maggie in a blue cardigan.
- **Change I'd make:** Redraw the pair as Oliver and Grandma Maggie. Show Maggie in round glasses and a blue cardigan, with the same kite and farmhouse, and preserve Oliver's curly hair, red jumper and green trousers.

#### Scene 8
![I45](artifacts/capture_93/img_07.jpg)
> Grandpa helped Oliver hold the string. The blue kite flew up, up into the summer sky — just like before!
- *Picture:* An elderly silver-haired man helps a curly-haired boy hold a kite string while a blue kite flies over the green hills and distant farmhouse.
- *Reaction:* The flying kite and the link between the present and my childhood are lovely, but the central relationship is wrong. Oliver should be flying his grandmother's kite with me beside him.
  - [fidelity, sev 4] The entered story says “I help him fly Grandpa's blue kite,” but the output says “Grandpa helped Oliver.”
  - [text_image_fit, sev 4] I45 directly illustrates an elderly man helping Oliver, so the picture reinforces the invented relationship rather than the corrected one.
  - [character_consistency, sev 4] The adult has the wrong identity and lacks the entered blue cardigan; no round glasses are visible.
  - [emotional_resonance, sev 4] The affectionate shared action could be meaningful, but it belongs to Oliver and his grandfather rather than Oliver and his grandmother.
- **Change I'd make:** Change “Grandpa” to “Grandma” or “I,” and redraw the helper as Grandma Maggie with short silver hair, round glasses and a blue cardigan. Keep Oliver's pose and the kite's flight.
- **Suggested rewrite:** I helped Oliver hold the string. Up, up went the blue kite into the summer sky, just like before!

#### Scene 9
![I46](artifacts/capture_93/img_08.jpg)
> Oliver laughed and laughed as the kite swooped and danced. It was the best feeling in the whole world!
- *Picture:* Oliver laughs with his arms open beside an elderly silver-haired man. Only the lower edge of the blue kite and its ribbon are visible at the top of the picture.
- *Reaction:* Oliver's joy is warm and genuine, but the adult is still the wrong person and most of the kite has been cropped out. I would prefer a picture that shows both Oliver's face and the kite dancing in the sky.
  - [fidelity, sev 4] I46 shows Oliver celebrating with an elderly man rather than with his grandmother.
  - [text_image_fit, sev 3] The text says the kite “swooped and danced,” but only a small part of the kite is visible at the top edge, so that important action is not shown clearly.
  - [character_consistency, sev 4] The adult is the same invented old man and does not match Grandma Maggie's entered appearance.
  - [visual_quality, sev 2] The accidental cropping of the kite weakens an otherwise attractive illustration.
- **Change I'd make:** Redraw Grandma Maggie beside Oliver in her blue cardigan and glasses, while including the complete kite swooping above them. Keep Oliver's joyful expression.

#### Scene 10
![I47](artifacts/capture_93/img_09.jpg)
> They promised to keep the old blue kite safe for ever. Every time they came to Wales, they would fly it together.
- *Picture:* At sunset, an elderly silver-haired man places an arm around Oliver. The blue kite lies folded on the grass in the foreground, with the old farmhouse and hills behind them.
- *Reaction:* This makes a gentle ending, and the kite is safely kept, but it belongs to Oliver and his grandfather rather than Oliver and me. Because the kite is lying on the ground, the picture also does not fully show the promised future flights.
  - [fidelity, sev 4] The entered dedication and ending are about “we” — Margaret and Oliver — but the text and I47 leave the pair as an unnamed “they” and depict an elderly man.
  - [text_image_fit, sev 2] The sentence says they would fly the kite together, while I47 shows the kite resting on the ground and the characters embracing.
  - [character_consistency, sev 4] The ending continues the invented grandfather instead of showing short silver-haired, bespectacled Grandma Maggie in a blue cardigan.
  - [emotional_resonance, sev 4] The sunset embrace is touching, but the wrong relationship makes this particular family keepsake unacceptable without redrawing.
- **Change I'd make:** Redraw the ending with Oliver and Grandma Maggie, keeping her short silver hair, round glasses and blue cardigan. Make the language name the pair directly, and either show the kite flying in the distance or make clear that it is being carefully put away after their flight.
- **Suggested rewrite:** Oliver and I promised to keep the old blue kite safe. Whenever we visited Wales, we would take it out and fly it together.

**Top changes to the output:** 1. Correct the entire story so the kite-maker is Margaret's father, the childhood child is clearly little Margaret, and the present-day pair is Margaret and Oliver; remove every invented Grandpa reference. | 2. Regenerate the illustrations with consistent character identities: little Margaret as a girl with short silver hair, round glasses and a blue cardigan, and present-day Margaret as a 71-year-old woman with short silver hair, round glasses and a blue cardigan. | 3. Restore the entered title "The Blue Kite" everywhere and remove the unexplained automatic story date. | 4. Use a proper cover and meaningful cast page showing the blue kite, the Welsh farmhouse, Margaret and Oliver, rather than blank pages or an unrelated man-and-child scene. | 5. Show the complete kite and the relevant action on each illustrated page, and provide large, easily inspected scene previews with clear labels for the latest PDF. | 6. Explain exactly what the $4.00 charge covers, whether any shipping or export costs are extra, and that the $59 hardcover is unavailable rather than presenting an unexplained or disabled purchase option. | 7. Remove preview watermarks and labels from the purchased file, enlarge small grey text and writing lines, and keep the simple, warm ending and dedication.

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
