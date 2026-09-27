# UserQA report: Test User on http://127.0.0.1:8765/

*Persona:* **Test User** (35) - Baseline condition - a generic adult web user with no persona conditioning (ablation).  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 11 steps | *Pages reviewed:* 9 | *Issues:* 22 | *LLM calls:* 13 | *Wall time:* 237.7 s

## What the agent understood the website to be
- **what it is:** A website for creating personalised, illustrated family storybooks from family members and a remembered event.
- **who it is for:** Families who want a made-to-order story featuring their child and another family member.
- **value proposition:** Turn a family memory into a storybook preview that can be read together and optionally printed as a hardcover.
- **pricing model:** A free digital preview is advertised, while printed hardcovers are sold and shipped across the UK; no actual price is shown here.
- **fit for me:** It sounds very relevant because I want a story starring my five-year-old daughter, Sam, and her Grandpa Joe, based on a beach memory.
- **main tasks:** Log in, Add a child and another character, Describe a family memory, place, and treasured object, Generate and read an illustrated preview, Check the price of a printed hardcover

## Scores
- SUS: **35.0** (grade F; 68 = industry average) - inconsistent responding flagged
- UEQ-S: pragmatic -1.5, hedonic -0.25 (range -3..+3)
- Likelihood to recommend (0-10): 0
- Output keepsake-worthiness (1-5): 1
- Verdict: *"The setup was promising, but the broken, inaccurate book and misleading checkout made me distrust the site and reject the result."*
- Would have abandoned at step 11 (127.0.0.1:8765/checkout.html \| Checkout): I would stop here because I do not want to pay, and the pre-checked £7.99 gift wrap makes me uncomfortable about the £45.97 total. [self-report]

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 3 | CONTENT | Generated storybook preview (x2) | The final sentence is incomplete | “And from that day on, whenever Sam looked up at the sky, she would always remember” | Finish the thought, for example: “...she would always remember the sandcastles she had built with Grandpa Joe.” Check the generated text for complete sentences before showing the finished preview. |
| 3 | H9 | My books dashboard | Unexplained technical error | “Error 0x80070057: profile sync incomplete.” | Replace the raw code with a plain-language message such as “We could not finish syncing your profile. Your account is secure; retry or continue without syncing,” and provide a Retry button or link to  |
| 3 | H2 | Generated storybook preview | Generated style does not match my selection | I selected “soft Watercolour,” but the preview says “Illustration style: Pop-art comic.” | Use the selected style when generating the book, and display a confirmation or warning if that style cannot be honoured. |
| 3 | VALUE | Generated storybook preview | Paid regeneration may be shown despite an unusable ending | “Regenerate entire book – $4.99” directly below the incomplete final page | Automatically correct the incomplete sentence at no charge, or allow individual free text editing before offering whole-book regeneration. |
| 3 | DECEPTIVE | Checkout | Premium gift wrap is pre-selected | [6] checkbox "Premium gift wrap" (checked), £7.99 | Leave optional extras unchecked by default and show the updated total immediately when the checkbox changes. |
| 2 | ACC | My books dashboard, Book setup form, Optional photo upload (x3) | Footer links and copyright have very low contrast | “Privacy”, “Terms”, “Contact”, and “© 2026 StoryHearth Ltd.” appear extremely faint. | Use a darker text colour that meets WCAG contrast requirements, while retaining the existing layout. |
| 2 | CONTENT | StoryHearth homepage | Overly technical wording in the main description | “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.” | Replace this with plain wording such as: “Turn a treasured family memory into a personalised illustrated storybook starring your loved ones.” |
| 2 | ACC | StoryHearth homepage | Image has no description | [image (no description) 430x440] | Provide a concise alt description of the illustrated personalised storybook scene. |
| 2 | ACC | Log in | Email and password fields have no permanent labels | [5] textbox (no label) placeholder “Email” and [6] textbox (no label) placeholder “Password” | Add visible labels above both fields and keep the placeholder text only as supplementary guidance. |
| 2 | H9 | My books dashboard | Warning provides no recovery path | The error banner contains no visible retry, dismiss, or help control. | Add “Retry sync,” “Continue anyway,” and “Get help” actions, with an explanation of what each will do. |
| 2 | H2 | Choose the look & feel | Reading-level default may be too advanced | [22] "Lexile 200L–500L" is checked by default even though Sam is age 5. | Recommend or select the band appropriate to the entered age, and show plain-language help such as “Beginning reader (about ages 4–7)” alongside the Lexile range. |
| 2 | ACC | Optional photo upload | Photo upload has no accessible label | [30] file-upload (no label) | Add a visible or programmatic label such as “Choose a photo of Sam” connected to the file input. |
| 2 | CONTENT | Generated storybook preview | Title is misspelled | The title reads “The Magical Adventrue of Sam” both above and on the cover. | Spell-check generated titles and either correct obvious typos automatically or show them for editing before ordering. |
| 2 | H3 | Generated storybook preview | No obvious edit control for the generated title | The preview shows the title and page controls, but no control to edit the title is visible. | Provide an Edit title or Edit book option, with undo and a warning if edits will affect the price. |
| 2 | VALUE | Checkout | The total is not easy to understand before ordering | “Hardcover: The Magical Adventrue of Sam £24.99”, “Premium gift wrap £7.99”, “Shipping & handling £12.99”, “Total £45.97” | Show a clear “book total”, “shipping”, and “optional extras” summary, with the total updating when optional items are changed. |

## Page-by-page
### StoryHearth homepage  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Explain the personalised storybook service and let visitors start creating, view pricing, or log in.
- **What's happening:** The landing page presents the service, its main “Proceed” and “See pricing” calls to action, a three-step explanation, customer quotations, and footer links.
- **First impression (Test):** "The page looks calm and attractive, and the three simple steps make the idea easy to understand. The main paragraph is much too technical and does not sound like language meant for an ordinary parent."
- **Cognitive walkthrough:** Q1 Yes, after logging in I would be ready to start making the story. / Q2 Yes, the “Log in” control is prominent in the top-right corner. / Q3 Yes, “Log in” clearly matches what I want and is easier to understand than “Proceed.”
  - [CONTENT sev 2] **Overly technical wording in the main description** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Replace this with plain wording such as: “Turn a treasured family memory into a personalised illustrated storybook starring your loved ones.”
  - [ACC sev 2] **Image has no description** - evidence: [image (no description) 430x440]. Fix: Provide a concise alt description of the illustrated personalised storybook scene.
  - [H2 sev 1] **Main Proceed action is ambiguous** - evidence: [5] is labelled only “Proceed →” while the account login control [4] is separately labelled “Log in.”. Fix: Label the button “Create your story” or explain whether it continues to sign-in when an account is required.
- **Positives:** The main service proposition is clear from the headline.; The three-step process is easy to scan.; The free-preview and UK-delivery information is visible without clicking elsewhere.; Login, pricing, privacy, terms, and contact routes are present.

### Log in  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** Allow an existing StoryHearth customer to access their account.
- **What's happening:** The page presents empty Email and Password fields, a Log in button, and a Create an account link.
- **First impression (Test):** "The form is simple and easy to understand, and the main button stands out clearly."
- **Cognitive walkthrough:** Q1 Yes, I want to log in so I can create the personalised book. / Q2 Yes, the Email and Password fields and the Log in button are immediately visible. / Q3 Yes, the placeholders and button clearly describe what is needed and what will happen.
  - [ACC sev 2] **Email and password fields have no permanent labels** - evidence: [5] textbox (no label) placeholder “Email” and [6] textbox (no label) placeholder “Password”. Fix: Add visible labels above both fields and keep the placeholder text only as supplementary guidance.
- **Positives:** The form is uncluttered and easy to scan.; The Log in button is large and clearly styled.; The Create an account link is available for new customers.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** Show the signed-in user's book library and provide a way to create a new personalised book.
- **What's happening:** The dashboard welcomes the user, reports that there are no books, and offers a button to create one. A prominent technical error states that profile sync is incomplete.
- **First impression (Test):** "The page is clean and the next step is obvious, but the raw error code and “profile sync incomplete” warning make the site feel unreliable before I have started."
- **Cognitive walkthrough:** Q1 Yes, I would try creating a book to find out whether the profile warning actually affects me. / Q2 Yes, the orange “+ Create a new book” button is prominent and easy to notice. / Q3 Yes, “Create a new book” clearly matches what I want to do.
  - [H9 sev 3] **Unexplained technical error** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the raw code with a plain-language message such as “We could not finish syncing your profile. Your account is secure; retry or continue without syncing,” and provide a Retry button or link to help.
  - [H9 sev 2] **Warning provides no recovery path** - evidence: The error banner contains no visible retry, dismiss, or help control.. Fix: Add “Retry sync,” “Continue anyway,” and “Get help” actions, with an explanation of what each will do.
  - [ACC sev 2] **Footer links and copyright have very low contrast** - evidence: “Privacy”, “Terms”, “Contact”, and “© 2026 StoryHearth Ltd.” appear extremely faint.. Fix: Use a darker text colour that meets WCAG contrast requirements, while retaining the existing layout.
- **Positives:** Login success is confirmed by reaching the account dashboard and seeing “Log out.”; The empty-library state is clearly stated: “You have no books yet.”; The main call to action is visually prominent and clearly labelled.

### Book setup form  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Collect the main child and another person who will appear in the personalised story.
- **What's happening:** The page presents fields for the child's first name, age, pronouns, appearance, the other character's name, and their relationship. All fields are initially blank or set to a generic selection, with “Grandparent” already selected as the relationship.
- **First impression (Test):** "This looks neat and easy to understand. The orange Next button stands out, and I can see all the information needed to begin."
- **Cognitive walkthrough:** Q1 Yes, I would fill this in now because this clearly comes before choosing the memory and creating the story. / Q2 Yes, the labelled textboxes, dropdowns, and the orange Next button are easy to notice. / Q3 Yes. “Who's the star of the story?” and “Who else is in the story?” clearly match what I want, although “Relationship” is slightly generic without the name beside it.
  - [ACC sev 1] **Very faint footer text** - evidence: The footer links “Privacy”, “Terms”, and “Contact” appear extremely pale against the background.. Fix: Use a darker footer text colour with stronger contrast.
  - [H2 sev 1] **Other character’s relationship label lacks context** - evidence: The dropdown [11] is labelled only “Relationship”, while the character name is in separate control [10].. Fix: Rename the field to “Relationship to the child” or “Grandpa Joe’s relationship to Sam”.
- **Positives:** The form has a clear progression with one prominent Next button.; The age and pronouns dropdowns limit free-form answers and are easy to use.; The optional appearance field is clearly marked as optional.

### Story details form  (step 5)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_05.jpg)
- **Purpose:** Collect the setting, an important object, and the personal memory that will be used to create the storybook.
- **What's happening:** The page presents three empty fields under “Your story”: “Where does the story happen?”, “A special object”, and “Tell us the memory or idea behind your story”. “Back” and “Next” are available.
- **First impression (Test):** "This is straightforward and reassuring. The labels and example prompts tell me exactly what to put in each box."
- **Cognitive walkthrough:** Q1 Yes, I would fill in these details now because this is exactly the information needed to create the memory story. / Q2 Yes, I can see the three labelled text fields and the “Next” button. / Q3 Yes. “Where does the story happen?” matches the setting, “A special object” matches the bucket, and the final question asks for the family memory.
- **Positives:** The fields are clearly labelled.; The placeholders provide useful examples without making the form feel complicated.; The large story field gives enough room to describe the memory.; The page is visually clean and the next action is easy to find.

### Choose the look & feel  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** Choose an appropriate reading difficulty and illustration style for the personalised children's book.
- **What's happening:** The form offers four Lexile reading bands and three illustration styles. A middle reading band and the Watercolour style are selected, and I can go back or continue.
- **First impression (Test):** "The choices are neatly presented and easy to scan, but the default “Lexile 200L–500L” does not seem right for a five-year-old."
- **Cognitive walkthrough:** Q1 Yes, I would change the reading level to the lowest band because Sam reads at about age five. / Q2 Yes, the four reading-level radio buttons and their selected states are visible. / Q3 The labels describe reading levels, but Lexile terminology is unfamiliar; “beginning reader, suitable for ages 4–5” would match my goal more directly.
  - [H2 sev 2] **Reading-level default may be too advanced** - evidence: [22] "Lexile 200L–500L" is checked by default even though Sam is age 5.. Fix: Recommend or select the band appropriate to the entered age, and show plain-language help such as “Beginning reader (about ages 4–7)” alongside the Lexile range.
- **Positives:** The current selections are clearly marked.; The illustration descriptions help me understand what each style means.; The large options and clear Next button make this step quick.

### Optional photo upload  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Offer an optional child photo before generating the personalised book.
- **What's happening:** The page asks for a clear photo of the child's face, provides a file upload, and offers Back and Create my book controls.
- **First impression (Test):** "Clear and uncomplicated. I can skip the photo and finish creating the book."
- **Cognitive walkthrough:** Q1 Yes, I want to finish the book and this is the final step. / Q2 Yes, the green “Create my book” button is prominent. / Q3 Yes, “Create my book” clearly describes the final action.
  - [ACC sev 2] **Photo upload has no accessible label** - evidence: [30] file-upload (no label). Fix: Add a visible or programmatic label such as “Choose a photo of Sam” connected to the file input.
  - [ACC sev 1] **Footer text has very low contrast** - evidence: “Privacy Terms Contact © 2026 StoryHearth Ltd.” appears extremely faint. Fix: Use a darker text colour that meets WCAG contrast requirements.
- **Positives:** The photo is clearly marked optional.; The explanation says why a photo would be useful.; Both Back and Create my book are visible together.; The main action is visually prominent.

### Generated storybook preview  (step 8)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_08.jpg)
- **Purpose:** Preview the newly generated personalised storybook and proceed to ordering a hardcover.
- **What's happening:** The site displays the first of nine generated pages, with a cover, page navigation, and offscreen controls for regenerating the book or ordering a hardcover.
- **First impression (Test):** "The cover is simple and child-friendly, but “Adventrue” looks like a spelling mistake and the stated Pop-art style does not match the soft Watercolour style I selected."
- **Cognitive walkthrough:** Q1 Yes, because I need to read the complete generated book before checking the hardcover cost. / Q2 Yes, the right-arrow button [7] below the preview looks like the next-page control. / Q3 The arrow does indicate going forward, although a label such as “Next page” would be clearer.
  - [H2 sev 3] **Generated style does not match my selection** - evidence: I selected “soft Watercolour,” but the preview says “Illustration style: Pop-art comic.”. Fix: Use the selected style when generating the book, and display a confirmation or warning if that style cannot be honoured.
  - [CONTENT sev 3] **The final sentence is incomplete** - evidence: “And from that day on, whenever Sam looked up at the sky, she would always remember”. Fix: Finish the thought, for example: “...she would always remember the sandcastles she had built with Grandpa Joe.” Check the generated text for complete sentences before showing the finished preview.
  - [CONTENT sev 3] **Generated ending has no complete thought** - evidence: “And from that day on, whenever Sam looked up at the sky, she would always remember”. Fix: Validate generated sentences before presenting the book and provide a free direct edit or regeneration option for incomplete text.
  - [VALUE sev 3] **Paid regeneration may be shown despite an unusable ending** - evidence: “Regenerate entire book – $4.99” directly below the incomplete final page. Fix: Automatically correct the incomplete sentence at no charge, or allow individual free text editing before offering whole-book regeneration.
  - [CONTENT sev 2] **Title is misspelled** - evidence: The title reads “The Magical Adventrue of Sam” both above and on the cover.. Fix: Spell-check generated titles and either correct obvious typos automatically or show them for editing before ordering.
  - [H3 sev 2] **No obvious edit control for the generated title** - evidence: The preview shows the title and page controls, but no control to edit the title is visible.. Fix: Provide an Edit title or Edit book option, with undo and a warning if edits will affect the price.
- **Positives:** The page clearly says it is a nine-page preview.; The page counter shows “1 / 9,” so I know I still have eight pages to inspect.; The next-page arrow is visible directly beneath the preview.

### Checkout  (step 11)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_11.jpg)
- **Purpose:** To collect delivery and payment information and place an order for the hardcover book.
- **What's happening:** The page displays a price reservation timer, the hardcover price, shipping and handling, a checked Premium gift wrap option, and a total. Empty address and payment fields are provided, with the Pay now button further down the page.
- **First impression (Test):** "I can quickly find the total, but the checked gift wrap makes the checkout feel misleading. I would not trust the total until I know exactly what is included and what happens if I uncheck it."
- **Cognitive walkthrough:** Q1 Yes, I would look at the checkout to find out the real cost, but I would stop before entering payment details because I do not want to pay. / Q2 Yes, the “Premium gift wrap” checkbox and the total are easy to notice. / Q3 The price labels are understandable, but the pre-checked “Premium gift wrap” does not match what I asked for and makes the total unclear.
  - [DECEPTIVE sev 3] **Premium gift wrap is pre-selected** - evidence: [6] checkbox "Premium gift wrap" (checked), £7.99. Fix: Leave optional extras unchecked by default and show the updated total immediately when the checkbox changes.
  - [VALUE sev 2] **The total is not easy to understand before ordering** - evidence: “Hardcover: The Magical Adventrue of Sam £24.99”, “Premium gift wrap £7.99”, “Shipping & handling £12.99”, “Total £45.97”. Fix: Show a clear “book total”, “shipping”, and “optional extras” summary, with the total updating when optional items are changed.
  - [H1 sev 1] **Reservation timer adds pressure** - evidence: “Your price is reserved for 09:57”. Fix: Use neutral wording such as “Price held for 10 minutes” and explain what happens when the timer expires.
  - [H8 sev 1] **Payment button is hidden below the fold** - evidence: [11] button "Pay now" (offscreen). Fix: Keep the order summary and the final payment action visible or provide a clear sticky total and checkout button.
- **Positives:** The book title and hardcover price are shown clearly.; Shipping and handling are itemised rather than hidden.; The total is shown before any payment fields are completed.; Privacy, Terms, and Contact links are available below the fold.
- **Would abandon here:** I would stop here because I do not want to pay, and the pre-checked £7.99 gift wrap makes me uncomfortable about the £45.97 total.

## Generated output assessment
*Artifact:* Nine-page personalized children's storybook preview

> I read all nine pages, and this does not feel like the story I asked for. Grandpa Joe and the sandcastle memory are missing, while serious vocabulary, a scary invented adventure, spelling errors, placeholders, and an unfinished ending make the result feel unreliable. The flat pictures also do not match the Watercolour style I selected.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | The output correctly uses Sam, age 5, she/her, brown hair in the simple drawings, the beach, and the yellow bucket. However, Grandpa Joe appears zero times, sandcastle building is omitted, the original memory is replaced |
| coherence | 2 | There is an opening and a nominal ending, but the plot jumps from a beach to an unexplained evening, heavy rain, a lantern, a winding path, dark woods, threatening shadows, sunshine, and home. The opening sentence is rep |
| age fit | 1 | The passage 'The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation' is unsuitable for age five. Automatic measurement als |
| language | 1 | Visible errors include 'Adventrue,' 'Samn,' 'in the beach,' unresolved '{{recipient_name}}' and '{{sender_name}}' placeholders, a duplicated 'The End,' and the unfinished sentence 'she would always remember.' |
| text image fit | 1 | The pictures are often generic or contradictory: Page 5 shows sun and no rain, bucket, puddles, or hood; Page 6 omits the winding path and does not clearly show a lantern; Page 7 shows ordinary trees rather than shadows  |
| character consistency | 4 | Sam generally retains the same round face, short brown hair, green shirt, dark trousers, and label across the pictures. There is some drift in proportions and no strong visual indication that Sam is a girl, but no outrig |
| visual quality | 1 | The artwork is extremely basic, with flat geometric shapes, minimal detail, repeated scenery, and labels under characters. The output explicitly says 'Illustration style: Pop-art comic' despite the selected Watercolour s |
| emotional resonance | 1 | The story does not develop the supplied memory with Grandpa Joe and does not feel like a personal keepsake. Broken placeholders, the wrong style, invented frightening characters, and an unfinished final sentence make the |

- **used correctly:** Sam's first name is generally spelled correctly except for the single typo 'Samn.'; The age five is stated correctly.; The pronoun 'her' is used for Sam.; The drawings depict Sam with short brown hair.; The beach is repeatedly used as the setting.; The yellow bucket is named in the text.
- **missing:** Grandpa Joe never appears.; Building sandcastles is omitted from the actual story and pictures.; The requested personal memory does not form the plot.; The intended Watercolour style is not used.
- **changed:** A cheerful sandcastle-building day with Grandpa Joe was replaced with a dark fantasy adventure.; The requested relationship with Grandpa Joe was changed to an invented Uncle Bartholomew.; The special yellow object remains in the prose but is repeatedly absent from the illustrations.
- **invented:** A magical adventure.; Uncle Bartholomew.; Evening existential melancholy.; Heavy rain and puddles.; A lantern and winding path.; Dark woods with shadows that grow teeth.; A threat that no one will ever find Sam.; A shiny red balloon.; A trip home.

### Part by part
#### Cover / Title page
![I1](artifacts/capture_01/img_00.jpg)
> A StoryHearth original Illustration style: Pop-art comic
- *Picture:* A very basic flat-color drawing of a small child labeled Sam, with short brown hair and a green shirt, standing between blue water, a strip of green land, a yellow star, and a large sun. The title is printed above the child.
- *Reaction:* The misspelling 'Adventrue' immediately makes the cover look careless. The picture is also far too generic and flat for the soft Watercolour style I selected.
  - [language, sev 3] The title reads 'The Magical Adventrue of Sam.'
  - [visual_quality, sev 3] The cover is labeled 'Illustration style: Pop-art comic' and consists of plain geometric shapes rather than Watercolour artwork.
  - [character_consistency, sev 1] Sam has short brown hair, but the drawing gives no other clear features that establish the requested appearance.
- **Change I'd make:** Correct the title to 'The Magical Adventure of Sam' and replace the generic flat drawing with a soft Watercolour cover showing Sam with brown hair, Grandpa Joe, a yellow bucket, and a sandcastle at the beach.
- **Suggested rewrite:** The Magical Beach Adventure of Sam

#### Page 2
![I2](artifacts/capture_03/view_00.jpg)
> For {{recipient_name}}, with love from {{sender_name}}
- *Picture:* The website preview frame is visible around a mostly blank white page containing the unresolved dedication in the center.
- *Reaction:* I would not accept unresolved template brackets on a finished keepsake. This looks like a preview error rather than intentional personalization.
  - [language, sev 4] The page displays 'For {{recipient_name}}, with love from {{sender_name}}' with both template placeholders still visible.
  - [emotional_resonance, sev 3] An unresolved generic dedication does not feel personally made.
- **Change I'd make:** Ask for the intended recipient and sender names, populate the fields, and remove all braces before generating the book.

#### Page 3
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in the beach, there lived a curious child named Sam. Sam was 5 years old and loved nothing more than a yellow bucket.
- *Picture:* Sam stands in a simple seaside scene with blue water, a green shoreline, a yellow star, and a bright sun. There is no yellow bucket, Grandpa Joe, sandcastle, shovel, or visible beach activity.
- *Reaction:* The story starts naming the right age and object, but the grammar is poor and the picture leaves out almost everything that made the requested beach memory special.
  - [language, sev 2] The phrase 'in the beach' should be 'at the beach.'
  - [fidelity, sev 3] The text says Sam loves a yellow bucket, but the picture does not contain one and neither Grandpa Joe nor the requested sandcastle-building event appears.
  - [text_image_fit, sev 3] The image shows only Sam near water and omits the yellow bucket central to this page.
- **Change I'd make:** Rewrite this as a direct scene of Sam and Grandpa Joe building a sandcastle together, and make sure the image clearly shows both characters, the yellow bucket, and a shovel.
- **Suggested rewrite:** Sam and Grandpa Joe went to the beach to build a sandcastle. Sam carried her favorite yellow bucket, and Grandpa Joe brought a small shovel.

#### Page 4
![I4](artifacts/capture_05/img_00.jpg)
> One evening Sam gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* Sam stands beneath a purple and pink evening sky dotted with a few stars, while the same blue water and green shoreline remain below.
- *Reaction:* This sentence is far too advanced and abstract for a five-year-old. It is also disconnected from a cheerful day of building sandcastles with Grandpa Joe.
  - [age_fit, sev 4] The sentence uses words such as 'ephemeral,' 'crepuscular,' 'engendered,' 'juxtaposing,' 'ineffable,' and 'existential trepidation.' The measured reading level is grade 6.5, not BR-200L.
  - [coherence, sev 3] The story abruptly changes from Sam loving a yellow bucket to an unexplained evening meditation with no beach activity or Grandpa Joe.
  - [emotional_resonance, sev 3] The obscure melancholy and existential language makes the requested happy family memory feel cold and impersonal.
- **Change I'd make:** Replace the sentence with short, concrete language about Sam and Grandpa Joe noticing the evening sky after building their sandcastle.
- **Suggested rewrite:** When the sky grew dark, Sam and Grandpa Joe stopped to look at the first stars. Sam smiled because their sandcastle was still standing by the sea.

#### Page 5
![I5](artifacts/capture_06/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Samn pulled up her hood and ran for shelter, holding a yellow bucket tight.
- *Picture:* The picture is almost identical to the sunny cover: Sam stands near blue water and green land beneath a bright yellow sun and beside a yellow star. There are no raindrops, puddles, hood, or bucket.
- *Reaction:* 
  - [language, sev 3] Sam's name is misspelled as 'Samn.'
  - [text_image_fit, sev 4] The text describes pouring rain, grey drops, puddles, a hood, and a yellow bucket, while the image shows sunshine, a star, no rain, and no bucket.
  - [fidelity, sev 2] The rain and shelter are invented events, and Grandpa Joe is inexplicably absent.
- **Change I'd make:** Remove the invented rain sequence or redraw it accurately. For this beach memory, a better page would continue the sandcastle activity with Sam and Grandpa Joe.
- **Suggested rewrite:** A big wave splashed near their sandcastle. Sam laughed and held her yellow bucket tightly while Grandpa Joe helped her rebuild the castle.

#### Page 6
![I6](artifacts/capture_07/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Sam, follow me!" he called, and he followed him along the winding path.
- *Picture:* Sam stands beside a taller figure labeled 'Uncle Bartholomew' in a muted outdoor scene. A small yellow rectangle appears beside the taller figure, but there is no visible lantern, winding path, beach, or Grandpa Joe.
- *Reaction:* This introduces someone I never mentioned and removes the grandfather who was central to the memory. The pronoun sentence is also confusing.
  - [fidelity, sev 4] The page invents 'Uncle Bartholomew' while omitting Grandpa Joe, whom I explicitly included.
  - [language, sev 2] 'He called, and he followed him' does not clearly establish who follows whom.
  - [coherence, sev 3] A lantern and winding path appear without explanation after Sam has supposedly run away from rain at the beach.
  - [text_image_fit, sev 2] The image labels Uncle Bartholomew but does not clearly depict the promised lantern or winding path.
- **Change I'd make:** Delete Uncle Bartholomew and replace him with Grandpa Joe. Make Grandpa Joe the person helping Sam at the beach, and remove the unexplained path and lantern.
- **Suggested rewrite:** "Look, Grandpa Joe! I made a castle!" Sam called. Grandpa Joe smiled and helped her pat the sand into a tall tower.

#### Page 7
![I7](artifacts/capture_08/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Sam again. Sam clutched a shiny red balloon and trembled in the dark.
- *Picture:* Sam stands beside a red balloon near a few simple trees under a crescent moon and starry sky. The trees have rounded canopies without visible teeth.
- *Reaction:* This is a sudden, frightening detour that does not belong in the requested beach memory. For an early-reader story, the threat of never being found is more alarming than the supplied idea requires.
  - [fidelity, sev 4] The dark woods, threatening shadows, lost-forever threat, and red balloon are all invented and replace the requested sandcastle outing.
  - [coherence, sev 4] The story moves from a beach and winding path to 'Deep in the woods' without explaining how Sam got there or why.
  - [age_fit, sev 3] The shadows 'grew teeth' and whisper that no one will ever find Sam, creating avoidable fear for a five-year-old.
  - [text_image_fit, sev 3] The picture shows ordinary rounded trees and does not show shadows with teeth, whispering figures, trembling, or Sam being lost.
- **Change I'd make:** Remove the threatening forest scene entirely and keep the action at the beach with Sam and Grandpa Joe.
- **Suggested rewrite:** Sam and Grandpa Joe found one smooth shell near the water. Sam put it in her yellow bucket to add to her beach treasures.

#### Page 8
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in the beach, there lived a curious child named Sam. At last the sun came out, and Sam skipped all the way home, happier than ever.
- *Picture:* Sam stands alone in another generic sunny seaside image with blue water, green land, a yellow star, and a large sun. There is no visible path home, sandcastle, Grandpa Joe, bucket, or home.
- *Reaction:* Repeating the opening almost word for word makes the ending feel like a reset rather than a conclusion. The image also fails to show the promised trip home.
  - [coherence, sev 3] The sentence 'Once upon a time, in the beach, there lived a curious child named Sam' repeats the opening instead of advancing the story.
  - [language, sev 2] 'In the beach' is repeated and should be 'at the beach.'
  - [fidelity, sev 4] Sam skips home alone even though the requested memory was a day at the beach building sandcastles with Grandpa Joe.
  - [text_image_fit, sev 3] The text says Sam skipped all the way home, but the image shows her standing in the same seaside setting with no movement or destination.
- **Change I'd make:** End the actual beach-day sequence with Sam and Grandpa Joe saying goodbye after completing the sandcastle, and show them together in the image.
- **Suggested rewrite:** Sam and Grandpa Joe packed their shovel after one last look at the sandcastle. Sam waved goodbye, carrying her yellow bucket as they walked home.

#### Page 9
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Sam looked up at the sky, she would always remember The End
- *Picture:* Sam stands alone against a flat orange background with 'The End' printed above her. The beach, Grandpa Joe, yellow bucket, and sandcastle are absent.
- *Reaction:* The last thought stops in the middle of a sentence, and 'The End' is duplicated. This is not a finished keepsake.
  - [language, sev 4] 'she would always remember' is an unfinished sentence, and 'The End' appears twice.
  - [emotional_resonance, sev 4] The intended final memory never identifies what Sam remembered, so the ending does not complete the personal story.
  - [text_image_fit, sev 3] The page says Sam would remember something when looking at the sky, but the picture has no sky and does not show what she remembers.
- **Change I'd make:** Complete the final sentence, print 'The End' only once, and either add a relevant image or turn the page into a clean closing page featuring Sam's sandcastle.
- **Suggested rewrite:** The End From then on, whenever Sam saw a sandy castle, she remembered the happy day she built one with Grandpa Joe.

**Top changes to the output:** 1. Rebuild the story around Sam and Grandpa Joe building sandcastles together at the beach; remove Uncle Bartholomew and the dark-woods adventure. | 2. Fix every production error: 'Adventure,' 'Sam,' 'at the beach,' remove unresolved template placeholders, complete the final sentence, and print 'The End' only once. | 3. Replace the advanced sentence with BR-200L-appropriate vocabulary and short, concrete sentences for a five-year-old. | 4. Use soft Watercolour illustrations and ensure every image includes the correct characters, setting, actions, yellow bucket, and sandcastle. | 5. End with a complete, personal thought about Sam remembering her day with Grandpa Joe.

## Recommendations (participant's priorities)
- **[high] Make the generated story faithfully include the named characters, relationship, setting, objects, and supplied memory, especially Sam and Grandpa Joe building sandcastles.** (Generated storybook preview) - The personalisation is the main reason to use the site, and omitting the most important people and memory makes the result worthless as a keepsake.
- **[high] Fix the story before showing paid regeneration: spell the title and names correctly, remove unresolved placeholders, remove duplicated text, and complete the final sentence.** (Generated storybook preview) - Obvious errors made the book look unfinished and made me unwilling to spend even £4.99 to try to improve it.
- **[high] Use age-appropriate vocabulary, shorter concrete sentences, and a complete, positive ending for the selected reading level.** (Choose the look & feel / Generated storybook preview) - Sam is five, and the advanced vocabulary, frightening shadows, and incomplete ending were not suitable for her.
- **[high] Apply the selected Watercolour style consistently and make each illustration match the text, characters, beach, yellow bucket, sandcastles, and action on that page.** (Generated storybook preview) - The output said it used Pop-art comic despite my Watercolour selection, and mismatched pictures further reduced my trust.
- **[high] Do not preselect paid gift wrap, and show a clear breakdown of the item, gift wrap, shipping, and total before the user reaches checkout.** (Checkout) - The £45.97 total was much higher than the initial £4.99 regeneration price, and the already-selected gift wrap felt misleading.
- **[high] Add a clear free correction or regeneration path for factual mistakes, spelling errors, missing requested details, and incomplete text.** (Generated storybook preview) - I need control over errors that are clearly the website's fault before being asked to pay for another version.
- **[medium] Replace the unexplained dashboard error with a plain-language explanation and give me a useful recovery action.** (My books dashboard) - The error code told me nothing about what was wrong or whether my account and saved data were safe.
- **[medium] Provide permanent, accessible labels for the email, password, and photo-upload fields.** (Log in / Optional photo upload) - Clear labels would make the forms easier to understand and use with assistive technology.
- **[medium] Replace technical homepage wording with simple language and make the primary action clearly say that it leads to logging in.** (StoryHearth homepage) - The wording sounded aimed at specialists rather than ordinary parents and the initial action was not completely obvious.
- **[medium] Increase the contrast of footer text and links and add a descriptive alternative text or description for the main image.** (Homepage / My books dashboard / Book setup form / Optional photo upload) - The low-contrast text was difficult to read and the missing image description reduced accessibility.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This website is for creating personalised storybooks featuring a child and people or memories important to them. It seems aimed at parents or family members wanting a keepsake story about a child.
- **What was the most frustrating or confusing moment, and why?** The most frustrating moment was seeing the completed book ignore Grandpa Joe and the sandcastle memory, use the wrong illustration style, contain spelling mistakes and placeholders, and end with an unfinished sentence. The preselected gift wrap at checkout also felt like a trap.
- **What was the best moment?** The book setup form was fairly clear and reassuring. I liked that I could enter Sam's details, describe the memory, choose a reading level, and select an illustration style without much difficulty.
- **Was there any point where, in real life, you would have given up? Where and why?** Yes. I would probably have abandoned the site after reading the generated story, especially once I saw that it was not about the memory I entered and could not repair the ending. I also would not have continued to payment after seeing the £45.97 total with gift wrap preselected.
- **What did you expect to find or be able to do that wasn't there?** I expected the story to be about Sam and Grandpa Joe building sandcastles at the beach, with the yellow bucket included. I also expected an obvious way to edit or regenerate the title and story for free, and I did not see a way to fix the incomplete ending before paying.
- **Did you trust this website with your information (and your family's)? Why or why not?** I would be cautious about entering family information after seeing the unexplained technical error and the generated story include unresolved template placeholders. The wrong style and missing family member made me doubt whether the site handled my information and instructions reliably.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would not pay £4.99 to regenerate this result, and I would not pay £45.97 for a hardcover with these problems. If the story were accurate, polished, clearly illustrated, and suitable for a five-year-old, a lower-cost digital version might be worth paying for; I would consider more for a genuinely well-made physical keepsake.
- **If the site produced something for you, how do you feel about it overall?** I would reject this book. It does not feel personal or reliable because the key people and memory are missing, the language is too advanced and frightening for Sam, the illustrations are generic and wrong for the chosen style, and the text contains serious production errors.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | This looks relevant to what I want, although “multimodal generative narrative engine” and “lived-experience corpus” sound much more technical than I need. I can see how it works at a glance, so I’ll use the clear “Log in | click |
| 2 | Log in – StoryHearth | reassured (1) | This is straightforward. I can see exactly where to enter my account details, so I’ll fill them in and log in. | type; type; click |
| 3 | My books – StoryHearth | hesitant (-1) | I got into my account, so that worked, but the error code immediately makes me a bit uneasy because it tells me almost nothing. The orange “Create a new book” button is easy to spot, so I’ll try it and see whether I can  | click |
| 4 | Create your book – StoryHearth | reassured (2) | This is straightforward. I can fill in Sam's name, age, pronouns, and appearance, then add Grandpa Joe as the other character. I don't need to change the relationship because Grandparent is already selected. | type; select; select; type; type; click |
| 5 | Create your book – StoryHearth | reassured (2) | This is clear enough to fill in. I’ll enter the beach, my yellow bucket, and the memory about Sam and Grandpa Joe building sandcastles. The form has kept my earlier character details, so I’m ready to continue. | type; type; type; click |
| 6 | Create your book – StoryHearth | reassured (1) | This is clear, but “Lexile 200L–500L” is too advanced for Sam, who is only five. I’ll choose “Lexile BR–200L”; I’m happy to keep the soft watercolour look and continue. | click; click |
| 7 | Create your book – StoryHearth | reassured (1) | This is simple and I don't have a suitable photo to upload here, so I'll leave it optional. The “Create my book” button is obvious. | click; wait_for_change |
| 8 | Your storybook – StoryHearth | suspicious (-1) | It worked and my book is here, but I’m already suspicious. I chose soft Watercolour, yet it says “Pop-art comic,” and “Adventrue” is misspelled. I’ll still read all nine pages carefully before deciding whether to order i | flip_through |
| 9 | Your storybook – StoryHearth | suspicious (-1) | I’ve now looked at all nine pages, but the ending text feels unfinished: “she would always remember” doesn’t say what she would remember. I’m still uncomfortable that the simple illustrations do not resemble the soft Wat | scroll |
| 10 | Your storybook – StoryHearth | frustrated (-1) | I can now see the ordering controls, and the $4.99 regeneration price is explicit, but I would not spend that because the book has several problems. I want to click “Order hardcover” to check the real cost and delivery d | click |
| 11 | Checkout – StoryHearth | frustrated (-1) | I can see the real checkout cost now: £24.99 for the hardcover, plus £7.99 gift wrap and £12.99 shipping, making £45.97. The gift wrap was already checked, which feels like a trap, and I will not enter any payment detail | scroll |
