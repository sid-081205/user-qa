# UserQA report: Test User on http://127.0.0.1:8765/

*Persona:* **Test User** (35) - Baseline condition - a generic adult web user with no persona conditioning (ablation).  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 11 steps | *Pages reviewed:* 9 | *Issues:* 17 | *LLM calls:* 13 | *Wall time:* 242.1 s

## What the agent understood the website to be
- **what it is:** A website for generating personalised, illustrated family storybooks from supplied family details and a memory.
- **who it is for:** Families wanting a story starring their child and another loved one, apparently with a reading age suited to young children.
- **value proposition:** Turn a meaningful family memory into an illustrated storybook, with a free digital preview and an option for printed hardcovers.
- **pricing model:** The digital preview is free; printed hardcovers are available, but no actual price is shown on this page.
- **fit for me:** It sounds well suited to making a keepsake story about Sam and Grandpa Joe, provided the writing and pictures are genuinely child-friendly.
- **main tasks:** Log in, Add the child and another character, Describe a place, treasured object, and memory, Generate and read the illustrated storybook, Check the price of a printed hardcover

## Scores
- SUS: **37.5** (grade F; 68 = industry average) - inconsistent responding flagged
- UEQ-S: pragmatic 0.0, hedonic 0.0 (range -3..+3)
- Likelihood to recommend (0-10): 0
- Output keepsake-worthiness (1-5): 1
- Verdict: *"The idea is exciting, but the poor personalised output makes the service feel unreliable and completely unsuitable for paying or giving as a keepsake."*
- Would have abandoned at step 10 (127.0.0.1:8765/checkout.html \| Checkout): I would not pay because I have not requested premium gift wrap, and I will not enter card details. I will only remove the extra to establish the real cost. [self-report]

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 3 | CONTENT | Generated storybook preview | Generated title contains an obvious spelling error | The heading and cover both say “The Magical Adventrue of Sam.” | Spell-check generated titles before showing them, and let me edit the title or regenerate just that text without paying. |
| 3 | H2 | Generated storybook preview | The generated style contradicts my selected style | The page says “Illustration style: Pop-art comic,” although I selected the soft watercolour style. | Use the selected style consistently and display the exact saved choice before generation; if it cannot be honoured, explain why before payment. |
| 3 | DECEPTIVE | Hardcover checkout | Gift wrap is pre-selected without being requested | Checkbox [6] “Premium gift wrap” is checked, with “£7.99” shown. | Make optional extras unchecked by default and require an explicit choice to add them. |
| 2 | CONTENT | StoryHearth landing page | The main description uses confusing technical language | “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.” | Replace it with plain language, such as: “Turn a special family memory into a personalised, illustrated storybook starring your loved ones.” |
| 2 | ACC | StoryHearth landing page | Decorative image has no description | [image (no description) 430x440] | Add meaningful alt text describing the image, or mark it decorative with an empty alt attribute if it adds no information. |
| 2 | ACC | Log in | Login fields lack persistent visible labels | [5] and [6] are textboxes with no label; they only display the placeholders “Email” and “Password.” | Add persistent visible labels for “Email address” and “Password,” while keeping placeholders as supplementary examples. |
| 2 | H9 | My books dashboard | Technical error code shown without an explanation | “Error 0x80070057: profile sync incomplete.” | Replace the error code with a plain-language message such as “We couldn’t finish syncing your profile. You can still create a book,” and add a “Try again” button if retrying is useful. |
| 2 | H1 | My books dashboard | Error has no recovery guidance | “Error 0x80070057: profile sync incomplete.” | State whether the account is still usable and provide either an automatic retry or a clear support/retry action. |
| 2 | H2 | Reading level and illustration style | Lexile levels are unexplained jargon | “Lexile BR–200L”, “Lexile 200L–500L”, “Lexile 500L–800L”, and “Lexile 800L+” | Show a plain-language description beside each option, such as “Beginning reader (ages 4–6)” and “Early chapter-book reading (ages 7–9),” while keeping the Lexile score as secondary information. |
| 2 | ACC | Optional photo upload | File upload has no proper label | [30] file-upload (no label) | Add a visible label such as “Upload a photo of Sam” associated with the file input, including accepted file types and a maximum size. |
| 2 | CONTENT | Generated storybook preview | The cover does not reflect the supplied family memory | The cover is a generic character under a sun with “A StoryHearth original,” and no beach, Grandpa Joe, sandcastles, or yellow bucket is shown. | Use the entered people, beach setting, sandcastles, and yellow bucket in the cover, or clearly label it as a placeholder if a memory-specific cover is unavailable. |
| 2 | CONTENT | Generated storybook preview | The final sentence is grammatically incomplete | “And from that day on, whenever Sam looked up at the sky, she would always remember” | Complete the sentence with the memory Sam would always remember. |
| 2 | DECEPTIVE | Hardcover checkout | Artificial reservation countdown creates pressure | “Your price is reserved for 09:57” | Remove the countdown unless the reservation genuinely has a firm, explained deadline, and state the exact deadline and conditions. |
| 1 | ACC | My books dashboard, Story details form (x2) | Footer links are barely visible | “Privacy”, “Terms”, “Contact” and “© 2026 StoryHearth Ltd.” appear in very faint grey text. | Use a darker, higher-contrast text colour while retaining normal link affordances. |
| 1 | ACC | Generated storybook preview | Book navigation uses an unlabelled symbol | The only forward control is the button labelled “›,” with no visible “Next page” text. | Give the control an accessible name such as “Next page” and retain a visible label if space allows. |

## Page-by-page
### StoryHearth landing page  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Explain the personalised family-storybook service and direct visitors to creation, pricing, or account access.
- **What's happening:** The landing page presents the service proposition, two calls to action, a three-step overview, testimonials, FAQs, and legal/contact links. No story or other generated content is present yet.
- **First impression (Test):** "It looks warm and polished, but the main paragraph is unnecessarily technical and pretentious for what is essentially a children’s story service."
- **Cognitive walkthrough:** Q1 Yes, I want to log in and make the book. / Q2 Yes, the “Log in” button is clearly visible in the top-right corner. / Q3 Yes, “Log in” is direct and familiar.
  - [CONTENT sev 2] **The main description uses confusing technical language** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Replace it with plain language, such as: “Turn a special family memory into a personalised, illustrated storybook starring your loved ones.”
  - [ACC sev 2] **Decorative image has no description** - evidence: [image (no description) 430x440]. Fix: Add meaningful alt text describing the image, or mark it decorative with an empty alt attribute if it adds no information.
- **Positives:** The “How it works” section gives a clear three-step overview.; The call to action to get a free digital preview is reassuring.; The page has clear navigation to pricing and login.; The visual style feels warm and family-friendly.

### Log in  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** Sign in to an existing StoryHearth account.
- **What's happening:** The page presents empty email and password fields, a Log in button, and a link for people who do not yet have an account.
- **First impression (Test):** "It looks calm, simple, and trustworthy. The login form is immediately visible without clutter."
- **Cognitive walkthrough:** Q1 Yes, I would enter my account details now. / Q2 Yes, the two fields and the orange “Log in” button are prominent. / Q3 Yes. The “Email,” “Password,” and “Log in” wording all match what I want to do.
  - [ACC sev 2] **Login fields lack persistent visible labels** - evidence: [5] and [6] are textboxes with no label; they only display the placeholders “Email” and “Password.”. Fix: Add persistent visible labels for “Email address” and “Password,” while keeping placeholders as supplementary examples.
- **Positives:** The page is uncluttered and the main form is easy to find.; The Log in button has strong visual prominence.; The “Create an account” link makes it clear how new users should proceed.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** Show the books in my account and provide a way to create a new one.
- **What's happening:** After login, the page says “Welcome back, Demo” and “You have no books yet.” A prominent button offers to create a new book, while a technical error alert reports that profile sync is incomplete.
- **First impression (Test):** "The page is simple and the next step is easy to find, but the error code at the top looks like something has gone wrong and gives me no idea whether it matters."
- **Cognitive walkthrough:** Q1 Yes, I would try creating the new book because this is exactly what I came to do. / Q2 Yes, the orange “+ Create a new book” button is prominent and easy to notice. / Q3 Yes, “Create a new book” clearly matches what I want to do.
  - [H9 sev 2] **Technical error code shown without an explanation** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the error code with a plain-language message such as “We couldn’t finish syncing your profile. You can still create a book,” and add a “Try again” button if retrying is useful.
  - [H1 sev 2] **Error has no recovery guidance** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: State whether the account is still usable and provide either an automatic retry or a clear support/retry action.
  - [ACC sev 1] **Footer links are barely visible** - evidence: “Privacy”, “Terms”, “Contact” and “© 2026 StoryHearth Ltd.” appear in very faint grey text.. Fix: Use a darker, higher-contrast text colour while retaining normal link affordances.
- **Positives:** The page clearly confirms that I am logged in with “Welcome back, Demo.”; The empty-book state is concise and easy to understand.; The primary “+ Create a new book” action is visually prominent and clearly labelled.

### Book details form  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Collect the main child and secondary character's details before creating a personalised storybook.
- **What's happening:** The page presents six inputs for describing the star of the story and someone else in the story. The relationship is already set to Grandparent, matching the family memory I want to use, and the Next button is available.
- **First impression (Test):** "This looks neat, calm, and easy to understand. The headings "Who's the star of the story?" and "Who else is in the story?" make the form feel personal and guide me through the task."
- **Cognitive walkthrough:** Q1 Yes, I would fill this in now because it is the necessary next step in making the book. / Q2 Yes, the visible labels, example placeholders, dropdowns, and orange Next button are all easy to notice. / Q3 Yes. I can enter Sam as the star, add Grandpa Joe, and the labels for age, pronouns, appearance, and relationship match what I want to provide.
- **Positives:** The form is organised into clear, relevant groups.; The labels are visible rather than relying only on placeholder text.; The examples, such as "e.g. Grandma Rose" and "e.g. curly red hair, green wellies", help explain what to enter.; The relationship already defaults to Grandparent, which is correct for my memory.

### Story details form  (step 5)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_05.jpg)
- **Purpose:** Collect the setting, a meaningful object, and the family memory that will guide creation of the personalised book.
- **What's happening:** The form displays three empty fields for the story location, special object, and memory or idea, with “Back” and “Next” controls below them.
- **First impression (Test):** "This looks calm, tidy, and straightforward. The examples help without getting in the way, although the footer links are extremely faint."
- **Cognitive walkthrough:** Q1 Yes, I can fill in the memory details immediately. / Q2 Yes, the three fields are prominent and the orange “Next” button is easy to find. / Q3 Yes. “Where does the story happen?”, “A special object”, and “Tell us the memory or idea behind your story” closely match what I want to enter.
  - [ACC sev 1] **Footer text has very low contrast** - evidence: The footer items “Privacy”, “Terms”, “Contact”, and “© 2026 StoryHearth Ltd.” are extremely pale against the background.. Fix: Use a darker text colour with at least WCAG AA contrast, and make the links look visibly clickable.
- **Positives:** The heading “Your story” clearly communicates the purpose of the step.; Each field has a visible, descriptive label.; The placeholder examples make it easy to understand the expected kind of answer.; The large “Next” button has a clear visual emphasis, while “Back” gives me control.

### Reading level and illustration style  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** To let the user choose how difficult the story text should be and what the illustrations should look like before generating the book.
- **What's happening:** The form shows reading-level radio buttons and illustration-style radio buttons. One option in each group is selected, and the user can go back or continue to the next step.
- **First impression (Test):** "It looks clean and easy to scan. The illustration descriptions are friendly, but the Lexile labels make me pause because I don’t know what they mean."
- **Cognitive walkthrough:** Q1 Yes, I would choose a reading level and illustration style here so the book suits Sam. / Q2 Yes, the reading-level and illustration-style radio buttons are clearly visible, as is the Next button. / Q3 The illustration labels match what I want, but the Lexile labels do not clearly explain which level is right for a five-year-old.
  - [H2 sev 2] **Lexile levels are unexplained jargon** - evidence: “Lexile BR–200L”, “Lexile 200L–500L”, “Lexile 500L–800L”, and “Lexile 800L+”. Fix: Show a plain-language description beside each option, such as “Beginning reader (ages 4–6)” and “Early chapter-book reading (ages 7–9),” while keeping the Lexile score as secondary information.
- **Positives:** The page is visually clean and the options are grouped clearly.; The illustration-style descriptions are understandable and appealing.; Back and Next controls are clearly visible.

### Optional photo upload  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Let the user optionally add a photo of the child before generating the personalised book.
- **What's happening:** The page offers an image file upload, explains that a clear photo of the child's face may help the illustrations resemble them, and shows Back and Create my book buttons. The upload currently has no file selected.
- **First impression (Test):** "This looks straightforward and I understand that the photo is optional. The green “Create my book” button is obvious, though the file chooser itself is a bit bare."
- **Cognitive walkthrough:** Q1 Yes, because I want to finish creating the book and I do not need to upload a photo. / Q2 Yes, I notice the “Choose file” control near the top of the form. / Q3 Mostly. “Choose file” makes sense, but it does not clearly say whether this should be a photo of Sam or the child in the story.
  - [ACC sev 2] **File upload has no proper label** - evidence: [30] file-upload (no label). Fix: Add a visible label such as “Upload a photo of Sam” associated with the file input, including accepted file types and a maximum size.
- **Positives:** The heading clearly says “Add a photo (optional).”; The explanation tells me what kind of photo could help.; The “Create my book” button is prominent and easy to find.

### Generated storybook preview  (step 8)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_08.jpg)
- **Purpose:** Preview the newly generated nine-page personalised storybook and offer regeneration and hardcover ordering.
- **What's happening:** The first of nine pages is displayed as a book cover. The story is titled “The Magical Adventrue of Sam,” and the output claims a Pop-art comic illustration style. A next arrow is available, while regeneration and ordering controls are below the fold.
- **First impression (Test):** "The book appeared and the cover is readable, but the misspelled title immediately makes it feel unfinished. The style also does not match the watercolour choice I made, and the generic sun-and-character image is disappointing for a family memory."
- **Cognitive walkthrough:** Q1 Yes, I need to read all nine pages carefully before deciding whether the result is good enough to order. / Q2 Yes, the right arrow labelled “›” is visible beneath the cover and the page indicator says 1 / 9. / Q3 Partly. The arrow indicates moving to the next page, but it is a symbol rather than a clearly written “Next page” control.
  - [CONTENT sev 3] **Generated title contains an obvious spelling error** - evidence: The heading and cover both say “The Magical Adventrue of Sam.”. Fix: Spell-check generated titles before showing them, and let me edit the title or regenerate just that text without paying.
  - [H2 sev 3] **The generated style contradicts my selected style** - evidence: The page says “Illustration style: Pop-art comic,” although I selected the soft watercolour style.. Fix: Use the selected style consistently and display the exact saved choice before generation; if it cannot be honoured, explain why before payment.
  - [CONTENT sev 2] **The cover does not reflect the supplied family memory** - evidence: The cover is a generic character under a sun with “A StoryHearth original,” and no beach, Grandpa Joe, sandcastles, or yellow bucket is shown.. Fix: Use the entered people, beach setting, sandcastles, and yellow bucket in the cover, or clearly label it as a placeholder if a memory-specific cover is unavailable.
  - [CONTENT sev 2] **The final sentence is grammatically incomplete** - evidence: “And from that day on, whenever Sam looked up at the sky, she would always remember”. Fix: Complete the sentence with the memory Sam would always remember.
  - [ACC sev 1] **Book navigation uses an unlabelled symbol** - evidence: The only forward control is the button labelled “›,” with no visible “Next page” text.. Fix: Give the control an accessible name such as “Next page” and retain a visible label if space allows.
- **Positives:** The creation result is unmistakable, with a title, cover, and 1 / 9 page indicator.; The generated cover and title are large and easy to see.; The page counter helps me understand that there are eight more pages to read.

### Hardcover checkout  (step 10)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_10.jpg)
- **Purpose:** To show the cost of ordering the generated book as a hardcover and collect delivery and payment information.
- **What's happening:** The checkout prices The Magical Adventrue of Sam at £24.99, adds £12.99 shipping, and pre-selects £7.99 premium gift wrap, making the current total £45.97. The page also shows a 09:57 price-reservation countdown, address fields, card fields, and a Pay now button below the fold.
- **First impression (Test):** "The order summary is easy to read, but the pre-ticked gift wrap feels sneaky because it adds £7.99 without me asking. The countdown also feels like unnecessary pressure."
- **Cognitive walkthrough:** Q1 Yes, I would untick “Premium gift wrap” to find the actual cost of the hardcover without the unwanted extra. / Q2 Yes, the checked “Premium gift wrap” checkbox with [6] is visible beside the £7.99 charge. / Q3 Yes, “Premium gift wrap” clearly identifies the extra, although the fact that it is pre-selected does not match what I want.
  - [DECEPTIVE sev 3] **Gift wrap is pre-selected without being requested** - evidence: Checkbox [6] “Premium gift wrap” is checked, with “£7.99” shown.. Fix: Make optional extras unchecked by default and require an explicit choice to add them.
  - [DECEPTIVE sev 2] **Artificial reservation countdown creates pressure** - evidence: “Your price is reserved for 09:57”. Fix: Remove the countdown unless the reservation genuinely has a firm, explained deadline, and state the exact deadline and conditions.
  - [H3 sev 1] **The purchase is not framed as clearly optional** - evidence: [11] button “Pay now” appears below the fold after the address and card fields.. Fix: Place an obvious cancel or return-to-preview link beside Pay now and preserve the book preview.
- **Positives:** The £24.99 hardcover price is shown plainly.; Shipping is shown separately as £12.99.; The total includes every currently selected charge.
- **Would abandon here:** I would not pay because I have not requested premium gift wrap, and I will not enter card details. I will only remove the extra to establish the real cost.

## Generated output assessment
*Artifact:* A nine-page personalized illustrated children's storybook preview with a cover, unfinished dedication page, website viewer screenshot, and eight visible story/end pages.

> I am disappointed and suspicious of the result. It mentions Sam, the beach, and the yellow bucket, but it ignores Grandpa Joe, sandcastles, the requested reading level, and the cheerful family memory. The spelling mistakes, broken placeholders, pronoun reversal, unrelated scary plot, and incomplete ending make this look like an unfinished template rather than a personalized book. I also notice that the reaction mentions a watercolour choice, but no watercolour style was actually present in the supplied inputs.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | The story uses Sam's name, age five, she/her pronouns in several passages, and mentions a yellow bucket. However, Grandpa Joe appears zero times, no sandcastles are mentioned or shown, brown hair is inconsistent, the bea |
| coherence | 1 | The narrative jumps from a beach opening to an unexplained evening, rain, a stranger in the woods, a repeated opening sentence, and an unfinished final thought. The line “Sam, follow me!” followed by “and he followed him |
| age fit | 1 | The measured grade level is 6.5, above the requested age-five level, and page four contains terms such as “ephemeral,” “crepuscular,” “ineffable,” and “existential.” The threatening line that no one would ever find Sam i |
| language | 1 | The title misspells “Adventure” as “Adventrue,” Sam is misspelled as “Samn,” “in the beach” is ungrammatical, the actor is reversed in the Uncle Bartholomew sentence, unresolved template variables are printed, an opening |
| text image fit | 1 | Several pages contradict their prose. I5 shows sunshine instead of pouring rain and omits the hood, puddles, running, and yellow bucket. I8 shows Sam standing still rather than skipping home. I3 lacks sand, a bucket, Gra |
| character consistency | 2 | Most images use the same basic figure, but Sam's visible brown hair and green clothing are not maintained in I6, where the figure appears bald or light-haired and differently dressed. Labels identify the characters, but  |
| visual quality | 2 | The artwork is clean enough that there are no obvious garbled faces or extra limbs, but it is extremely sparse and repetitive. Several pages reuse nearly the same composition, the image is not meaningfully connected to t |
| emotional resonance | 1 | The result ignores the defining people and event in my memory—Grandpa Joe and building sandcastles—and substitutes a generic, somewhat frightening adventure. The unfinished placeholders and incomplete ending make it unsu |

- **used correctly:** The child's first name, Sam, is used frequently.; The age five is stated explicitly.; She/her pronouns are used in several passages.; The yellow bucket is named in the opening and rain scenes.; The beach is named in the opening and repeated template sentence.
- **missing:** Grandpa Joe never appears.; The central event of building sandcastles never appears.; Brown hair is not consistently depicted.; The beach is not clearly or accurately illustrated.; The requested BR–200L reading level is not met.; No premium gift-wrap result is shown in the captured book preview.
- **changed:** A cheerful beach memory with Grandpa Joe was changed into an unrelated storm-and-woods adventure.; The requested relationship, Grandpa, was changed to an uncle.; The setting was moved from the beach into a dark forest and winding-path sequence.; The story added rain and a red balloon.; Sam's consistent she/her identity is contradicted by “he followed him.”; The intended sandcastle event was replaced with a generic journey home.
- **invented:** Uncle Bartholomew; A lantern; Heavy rain and puddles; A winding path through woods; Toothy whispering shadows; A shiny red balloon; An existential and frightening danger that no one would find Sam; A repeated opening sentence

### Part by part
#### Cover
![I1](artifacts/capture_01/img_00.jpg)
> A StoryHearth original Illustration style: Pop-art comic The Magical Adventrue of Sam Sam
- *Picture:* A very simple pop-art-style illustration of a small brown-haired figure labelled “Sam,” standing between a green strip and a blue strip beneath a large sun and yellow star. There is no beach activity, sandcastle, bucket, or Grandpa Joe.
- *Reaction:* The cover is generic and the misspelling “Adventrue” is immediately visible. It does not make me feel that this is Sam's beach memory with Grandpa Joe.
  - [language, sev 3] The title says “The Magical Adventrue of Sam”; “Adventure” is misspelled.
  - [fidelity, sev 3] The cover shows neither Grandpa Joe nor sandcastles, and no yellow bucket is visible.
  - [visual_quality, sev 2] The figure is extremely generic, the scene is mostly empty, and the name “Sam” is placed awkwardly across the ground.
- **Change I'd make:** Correct the title and redesign the cover around Sam, Grandpa Joe, the yellow bucket, and a recognizable sandcastle at the beach.
- **Suggested rewrite:** The Magical Beach Day with Sam and Grandpa Joe

#### Dedication page
![I2](artifacts/capture_03/view_00.jpg)
> For {{recipient_name}}, with love from {{sender_name}}
- *Picture:* A screenshot of the StoryHearth book viewer showing the unfinished dedication inside a large white panel. It includes navigation controls, page number 2/9, a regeneration button priced at $4.99, and an order button.
- *Reaction:* This looks broken and unfinished, not like a polished keepsake. The raw template placeholders are particularly disappointing on a paid personalized book.
  - [language, sev 4] The page visibly prints “For {{recipient_name}}, with love from {{sender_name}}”.
  - [fidelity, sev 4] No recipient or sender information was supplied, but the site still presents unresolved personalization fields as book content.
  - [visual_quality, sev 3] The book page is visually empty apart from the placeholder sentence and contains no story illustration.
- **Change I'd make:** Do not print unresolved variables. If no names are available, use a neutral dedication or omit this page and include an illustration of Sam and Grandpa Joe.
- **Suggested rewrite:** For my wonderful Sam, with love.

#### Page 3 — story opening
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in the beach, there lived a curious child named Sam. Sam was 5 years old and loved nothing more than a yellow bucket.
- *Picture:* Sam stands alone in a minimal scene with a sun, star, green ground, and blue foreground. Despite the alt text “Sam at the beach,” there is no visible sandcastle, shoreline detail, Grandpa Joe, or yellow bucket.
- *Reaction:* Sam's name and age are used, but “in the beach” is wrong and the promised beach setup is missing. The yellow bucket is especially important and should not disappear.
  - [language, sev 2] “Once upon a time, in the beach, there lived” is ungrammatical; the sentence should use “at the beach” or simply “there lived.”
  - [fidelity, sev 3] The text mentions the yellow bucket, but I3 does not show it; Grandpa Joe and the requested sandcastle-building memory are absent.
  - [text_image_fit, sev 3] The image is labelled as being at the beach but provides no sand, sea, shoreline, bucket, sandcastle, or Grandpa Joe.
- **Change I'd make:** Correct the grammar and show Sam and Grandpa Joe beginning to build a sandcastle with the yellow bucket.
- **Suggested rewrite:** Sam was five years old. On a sunny beach day, she and Grandpa Joe packed their yellow bucket. They were going to build the biggest sandcastle they could!

#### Page 4 — evening sky
![I4](artifacts/capture_05/img_00.jpg)
> One evening Sam gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* Sam stands beneath a purple and pink evening sky with a few white stars. The character is broadly consistent with the earlier figure.
- *Reaction:* The picture is calm, but the prose is far beyond a five-year-old's reading level. Words such as “ephemeral,” “crepuscular,” and “existential” make the story feel literary rather than personal.
  - [age_fit, sev 4] The sentence uses “ephemeral luminescence,” “crepuscular firmament,” “ineffable,” “juxtaposing,” and “existential trepidation.” The measured grade level is 6.5 rather than the requested age-five level.
  - [fidelity, sev 2] This invented evening mood has no connection to the supplied memory of a cheerful day building sandcastles with Grandpa Joe.
- **Change I'd make:** Replace the advanced sentence with one or two short, concrete sentences about the sunset, and keep Grandpa Joe beside Sam.
- **Suggested rewrite:** Sam looked up at the orange and pink sky. Grandpa Joe stood beside her and smiled.

#### Page 5 — rain and shelter
![I5](artifacts/capture_06/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Samn pulled up her hood and ran for shelter, holding a yellow bucket tight.
- *Picture:* The picture repeats the bright daytime cover scene with a blue sky, sun, star, and Sam standing still. It shows no rain, puddles, hood, running movement, or yellow bucket.
- *Reaction:* This is a direct mismatch between words and pictures. It also misspells Sam as “Samn” and introduces rain that was not part of my memory.
  - [language, sev 3] Sam's name is misspelled as “Samn.”
  - [text_image_fit, sev 4] The text describes heavy rain, puddles, a hood, running, and a yellow bucket, while I5 shows sunshine and a motionless figure with none of those objects.
  - [fidelity, sev 3] The invented rain scene replaces the requested sandcastle-building event and omits Grandpa Joe.
- **Change I'd make:** Remove the unnecessary storm, restore the spelling of Sam, and illustrate the actual memory of her carrying the yellow bucket with Grandpa Joe.
- **Suggested rewrite:** Sam picked up her yellow bucket. Grandpa Joe helped her carry it to the wet sand, where they could build together.

#### Page 6 — Uncle Bartholomew
![I6](artifacts/capture_07/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Sam, follow me!" he called, and he followed him along the winding path.
- *Picture:* Two labelled figures stand in a dark, flat setting. “Uncle Bartholomew” is a tall figure holding a small yellow rectangle, while Sam appears smaller, bald or light-haired, and dressed differently from earlier pages. No winding path is shown.
- *Reaction:* This is a major error: I asked for Grandpa Joe, and the site invented Uncle Bartholomew. The last sentence also changes Sam into “he” and makes the uncle follow himself.
  - [fidelity, sev 4] The requested person, “Grandpa Joe,” is absent and is replaced by the invented “Uncle Bartholomew.”
  - [language, sev 4] “Sam, follow me!” is followed by “and he followed him,” which reverses the intended action and incorrectly makes Sam male.
  - [character_consistency, sev 3] Sam in I6 appears bald or light-haired and has lost the visible brown hair and green clothing used on most other pages.
  - [text_image_fit, sev 3] The text mentions a winding path and lantern journey, but the image shows both characters standing still in an indistinct flat setting.
- **Change I'd make:** Replace Uncle Bartholomew with Grandpa Joe throughout and redraw Sam with the same brown hair, clothing, and proportions as the previous pages.
- **Suggested rewrite:** “Come with me, Sam,” said Grandpa Joe. Sam followed him down the sandy path, carrying her yellow bucket.

#### Page 7 — dark woods
![I7](artifacts/capture_08/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Sam again. Sam clutched a shiny red balloon and trembled in the dark.
- *Picture:* Sam stands at night near a crescent moon, a red balloon, and several simple trees. The balloon is visible, but Sam is not shown trembling, the trees do not have teeth, and no whispering shadows are depicted.
- *Reaction:* This feels like an unrelated dark fantasy chapter rather than a beach memory. The threatening line about never being found is also unsettling for a five-year-old.
  - [fidelity, sev 4] The woods, threatening shadows, and red balloon were all invented, while the beach, Grandpa Joe, and sandcastles disappear.
  - [age_fit, sev 4] “the shadows grew teeth and whispered that no one would ever find Sam again” introduces frightening existential danger that is not suitable for the requested gentle memory.
  - [text_image_fit, sev 3] The red balloon appears, but toothy shadows, whispering, and Sam's trembling are absent; the picture is much calmer than the prose.
- **Change I'd make:** Replace this page with a cheerful sandcastle-building scene featuring Sam and Grandpa Joe, and remove the threatening language and invented balloon.
- **Suggested rewrite:** Sam and Grandpa Joe dug deep in the wet sand. Soon, a tall castle began to grow.

#### Page 8 — return home
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in the beach, there lived a curious child named Sam. At last the sun came out, and Sam skipped all the way home, happier than ever.
- *Picture:* A nearly identical bright daytime scene shows Sam standing still. There is no visible skipping, path home, beach activity, Grandpa Joe, bucket, or completed sandcastle.
- *Reaction:* The repeated opening sentence feels like a template error, and the picture does not show Sam doing anything. The ending is generic rather than tied to the memory I supplied.
  - [language, sev 3] “Once upon a time, in the beach, there lived a curious child named Sam.” repeats the opening almost word for word and still contains the ungrammatical phrase “in the beach.”
  - [coherence, sev 3] The sun is said to come out, but the preceding page had no meaningful sun-and-rain setup, and the woods story has not been connected to the beach or Grandpa Joe.
  - [text_image_fit, sev 3] The text says Sam skipped all the way home, but I8 shows her standing still in a generic landscape.
  - [fidelity, sev 3] The page fails to conclude the requested memory of building sandcastles with Grandpa Joe.
- **Change I'd make:** End the requested memory directly: show Sam and Grandpa Joe beside their completed sandcastle, then walking home together.
- **Suggested rewrite:** Sam and Grandpa Joe looked at their tall sandcastle and smiled. It was not the biggest castle on the beach, but it was their favorite one. Then they walked home together.

#### Page 9 — ending
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Sam looked up at the sky, she would always remember The End
- *Picture:* An orange page displays “The End” twice and shows Sam standing still with the same simple green clothing used on many pages. The final memory sentence is not shown graphically or completed.
- *Reaction:* This is visibly unfinished. “The End” is duplicated, the last sentence has no ending or punctuation, and there is no personal memory to close the story.
  - [language, sev 4] “And from that day on, whenever Sam looked up at the sky, she would always remember” is incomplete and lacks final punctuation; “The End” appears twice.
  - [coherence, sev 4] The final sentence never identifies what Sam remembered or connects the ending to building sandcastles with Grandpa Joe.
  - [visual_quality, sev 3] The large orange field is mostly empty, and the duplicated “The End” makes the page look like an unresolved template or rendering error.
- **Change I'd make:** Complete the final memory in simple language, show only one “The End,” and use a warm image of Sam and Grandpa Joe beside their sandcastle.
- **Suggested rewrite:** From then on, Sam always remembered that beach day with Grandpa Joe, her yellow bucket, and their wonderful sandcastle.  The End

**Top changes to the output:** 1. Rebuild the entire story around the supplied memory: Sam builds sandcastles at the beach with Grandpa Joe and her yellow bucket. | 2. Replace Uncle Bartholomew, the dark woods, the red balloon, and the threatening language with simple age-appropriate family interactions. | 3. Correct “Adventrue,” “Samn,” “in the beach,” the reversed pronouns, the repeated opening, the incomplete ending, and all template placeholders. | 4. Rewrite the prose to approximately BR–200L, using short sentences, common vocabulary, and a clear beginning, middle, and end. | 5. Redraw every beach page with sand, water, Grandpa Joe, Sam's yellow bucket, and a developing sandcastle. | 6. Keep Sam visually consistent with brown hair and the same clothing across every page, and show Grandpa Joe consistently as well. | 7. Remove the repeated generic illustrations and ensure each picture visibly matches its page text.

## Recommendations (participant's priorities)
- **[high] Rebuild the story around the supplied family memory, including Grandpa Joe, the sandcastles, the beach, and the yellow bucket, instead of inventing an unrelated adventure.** (Generated storybook preview) - Personalisation is the entire purpose of the product, and the current result does not capture the keepsake I entered.
- **[high] Ensure the generated illustration style always matches the style selected during setup, and replace contradictory or generic artwork with relevant beach scenes.** (Reading level and illustration style / Generated storybook preview) - Choosing a style and seeing a completely different result makes the service feel unreliable and dishonest.
- **[high] Correct spelling and grammar errors, remove unresolved placeholders and repeated text, fix character names and pronouns, and complete the final sentence.** (Generated storybook preview) - The obvious errors make the book look unfinished and unsuitable for a child or a gift.
- **[high] Rewrite the text at the requested beginner reading level with short sentences, common vocabulary, a clear beginning, middle, and end, and no frightening or age-inappropriate language.** (Generated storybook preview) - A personalised children's book must be readable for the selected age and emotionally suitable for the child.
- **[high] Make the purchase clearly optional, show the basic delivered price prominently, do not preselect extras, and remove artificial reservation pressure.** (Hardcover checkout) - I nearly believed the full price included an unwanted gift-wrap charge, and the countdown felt like pressure rather than helpful information.
- **[high] Replace the technical dashboard error with a plain-language explanation and give users a clear recovery action.** (My books dashboard) - An unexplained error code is worrying and makes me doubt whether the account or my data is safe.
- **[medium] Explain Lexile levels in ordinary language and recommend an option based on the child's age.** (Reading level and illustration style) - I had to guess what BR–200L meant, which adds unnecessary jargon to an otherwise straightforward form.
- **[medium] Add persistent visible labels to the login fields and a proper label to the photo upload explaining whose photo it is and what it is used for.** (Log in / Optional photo upload) - Placeholders disappear while typing, and the file control did not make clear what photo was being requested.
- **[medium] Simplify the landing-page language, describe the product in concrete terms, and add a description for the decorative image.** (StoryHearth landing page) - Phrases such as “multimodal generative narrative engine” sound needlessly technical for creating a bedtime story, and the missing image description reduces accessibility.
- **[low] Increase the contrast of footer text and links, and label the book-navigation symbol clearly.** (Story details form / Generated storybook preview) - Low-contrast text and an unlabelled control made otherwise easy pages harder to read and navigate.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** StoryHearth is for creating personalised digital storybooks that feature a child and a meaningful family memory. It appears aimed at parents or family members wanting a personalised keepsake for a child.
- **What was the most frustrating or confusing moment, and why?** The most frustrating moment was seeing the generated book: it misspelled the title, ignored Grandpa Joe and the sandcastles, contradicted the selected watercolour style, and ended with an incomplete sentence. I also nearly felt pressured by the checkout because gift wrap was already selected and there was an artificial countdown.
- **What was the best moment?** The best moment was entering the beach memory and yellow bucket because the three questions and examples made that part of the process clear and encouraging. Untickling the gift wrap was also reassuring because the total immediately became clear.
- **Was there any point where, in real life, you would have given up? Where and why?** I would probably have abandoned the service at the book preview rather than pay for the hardcover. At that point the result looked unfinished and clearly did not represent the family memory I entered.
- **What did you expect to find or be able to do that wasn't there?** I expected a complete, age-appropriate story about Sam, Grandpa Joe, the beach, the yellow bucket, and the sandcastles, with illustrations that matched those details. I also expected a properly labelled photo upload, a clear reading-level explanation, and an obviously optional purchase with the real cost visible before any extras are added.
- **Did you trust this website with your information (and your family's)? Why or why not?** I was willing to type basic account details, but I would not trust the site with more sensitive family information unless it explained how the data was used and stored. The mismatched output made me suspicious that my inputs were not being handled reliably.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would not pay for this version. A fair price might be around £10 to £15 for a good digital book, or roughly £20 to £25 for a genuinely well-produced hardcover; I would pay more only if the story and artwork were personalised, polished, and clearly matched the requested memory.
- **If the site produced something for you, how do you feel about it overall?** I am disappointed and suspicious. It looks like an unfinished generic template rather than a personalised keepsake, and I would not be comfortable giving it as a gift.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | This looks relevant to me, although “multimodal generative narrative engine” and “lived-experience corpus” sound far more technical and grand than making a bedtime story. The simple three steps and mention of a free digi | click |
| 2 | Log in – StoryHearth | reassured (1) | This is clear and easy to understand. I can tell exactly where to enter my details, although the fields only have placeholder text rather than proper visible labels. | type; type; click |
| 3 | My books – StoryHearth | confused (0) | I’m logged in, but that error message looks technical and slightly worrying. It doesn’t seem to stop me here, and the “Create a new book” button is obvious. | click |
| 4 | Create your book – StoryHearth | reassured (1) | This is a straightforward form, and I can see everything without hunting around. I’ll fill in Sam and Grandpa Joe, choose the right age and pronouns, and include the appearance details so the story feels personal. | type; select; select; type; type; click |
| 5 | Create your book – StoryHearth | reassured (2) | This step is much clearer than the previous error message. The three questions give me helpful structure, and the examples make it easy to understand what each box wants. I’ll enter our beach memory and the yellow bucket | type; type; type; click |
| 6 | Create your book – StoryHearth | reassured (1) | This is a tidy-looking choice page, but “Lexile” is jargon I don’t understand. Since Sam is five and is the hero, I’m going to choose the easiest-looking beginning-reading option, “Lexile BR–200L,” and keep the soft wate | click; click |
| 7 | Create your book – StoryHearth | reassured (1) | This is a simple final setup step. I don't have a photo ready, and the upload is optional, so I'll leave it blank and create the book. The upload control says “Choose file,” but it would be clearer if it had a proper lab | click; wait_for_change |
| 8 | Your storybook – StoryHearth | confused (-1) | It did generate the book, so that worked, but the title has a typo: “Adventrue.” I also asked for the soft watercolour style, yet the page says “Illustration style: Pop-art comic” and the cover is extremely plain rather  | flip_through |
| 9 | Your storybook – StoryHearth | frustrated (-1) | I’ve now seen the whole book, and the ending feels incomplete: “she would always remember” doesn’t say what she remembered. I want to see the real hardcover cost, so I’ll use “Order hardcover,” but I won’t pay or enter a | click |
| 10 | Checkout – StoryHearth | annoyed (-1) | The basic hardcover costs £24.99, but I nearly assumed the full price was £45.97 because “Premium gift wrap” is already ticked. I don’t want that extra, so I’ll untick it and see the real total before stopping without pa | click |
| 11 | Checkout – StoryHearth | reassured (1) | Good, unticking the gift wrap clearly removed the £7.99 charge and brought the total down to £37.98. That gives me the real delivered cost, so I’ll stop here without entering payment details or paying. | done |
