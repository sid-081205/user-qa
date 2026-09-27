# UserQA report: Test User on http://127.0.0.1:8765/

*Persona:* **Test User** (35) - Baseline condition - a generic adult web user with no persona conditioning (ablation).  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 14 steps | *Pages reviewed:* 10 | *Issues:* 23 | *LLM calls:* 18 | *Wall time:* 328.9 s

## What the agent understood the website to be
- **what it is:** A website that turns family details and a remembered event into a personalised illustrated storybook.
- **who it is for:** Families wanting a story featuring their child and another favourite person.
- **value proposition:** Create a bespoke family memory story, preview it digitally, and optionally have it printed as a hardcover.
- **pricing model:** A free digital preview is advertised; the cost of printed hardcovers is not yet shown, though a Pricing link is available.
- **fit for me:** It sounds well suited to preserving a memory involving Sam and Grandpa Joe, especially because I can preview the story before deciding on printing.
- **main tasks:** Log in, Add family characters, Describe a memory, Generate and read a storybook, Check and potentially order a printed hardcover

## Scores
- SUS: **40.0** (grade F; 68 = industry average)
- UEQ-S: pragmatic -1.25, hedonic 1.25 (range -3..+3)
- Likelihood to recommend (0-10): 1
- Output keepsake-worthiness (1-5): 1
- Verdict: *"Easy enough to fill in, but the final book was so inaccurate, frightening, unfinished, and expensive that I would not use it or recommend it."*

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 3 | H9 | My books dashboard | Unexplained technical sync error | “Error 0x80070057: profile sync incomplete.” | Replace the code with a plain-language message such as “Some profile details may not have loaded. You can still create a book, or try again,” and provide a visible Retry option. |
| 3 | H2 | Generated storybook preview | Selected illustration style appears not to have been applied | The page says “Illustration style: Pop-art comic,” although the story setup said “soft watercolour illustrations.” | Apply the selected soft watercolour style, and clearly show which style was used or offer a correction option. |
| 3 | CONTENT | Generated storybook preview | Cover illustration may not reflect the supplied character details | The cover shows a generic child labelled “Sam,” with no visible brown hair or connection to Grandpa Joe or the beach memory. | Use the entered character details and memory in the generated cover, or clearly explain what personalisation is included and let me regenerate or edit it. |
| 3 | DECEPTIVE | Hardcover checkout | Premium gift wrap is pre-selected without being requested | [6] checkbox “Premium gift wrap” (checked) and “£7.99” | Default the optional gift-wrap checkbox to unchecked and show exactly what it adds to the total when selected. |
| 2 | ACC | Optional photo upload, Create your book – characters (x2) | Footer text has very low contrast | The footer links “Privacy”, “Terms”, and “Contact” and the copyright line are extremely pale against the background. | Use a darker text colour with sufficient contrast and keep it visually readable on hover and focus. |
| 2 | CONTENT | Generated storybook preview, Hardcover checkout (x2) | Typo in generated title | “The Magical Adventrue of Sam” | Correct the title to “The Magical Adventure of Sam” and provide a way to edit the title before ordering. |
| 2 | H2 | StoryHearth homepage | Unnecessarily technical product language | Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus. | Replace this with plain language such as: 'Turn a family member and a treasured memory into a personalised illustrated storybook.' |
| 2 | ACC | Log in | Email and password fields have no persistent labels | [5] and [6] are listed as “textbox (no label)” and rely only on the placeholders “Email” and “Password”. | Add visible labels such as “Email address” and “Password” associated with each input, rather than using placeholders as the only labels. |
| 2 | H1 | My books dashboard | Error gives no recovery action | “Error 0x80070057: profile sync incomplete.” with no visible retry or help control | Include a “Try again” button and a “Continue anyway” option if book creation is still available. |
| 2 | ACC | Optional photo upload | File upload has no programmatic label | [30] file-upload (no label) shows only the browser text “Choose file” and “No file chosen”. | Add a visible and programmatic label such as “Child’s photo (optional)” associated with the file input. |
| 2 | H1 | Creating book | Loading state has no explanation | The central panel contains only a loading spinner and no status text. | Add accessible visible text such as “Creating your book…” and, if possible, show a progress indicator or estimated time. |
| 2 | VALUE | Generated storybook preview | Hardcover price is not shown before ordering | [9] link "Order hardcover" and [8] button "Regenerate entire book – $4.99"; no hardcover price is visible beside the order link. | Display the hardcover price clearly next to the “Order hardcover” control, including any shipping or tax information before checkout. |
| 2 | DECEPTIVE | Generated storybook preview | Paid regeneration control is prominent beside ordering | [8] button "Regenerate entire book – $4.99" appears immediately beside the orange “Order hardcover” link. | Move regeneration into a clearly labelled secondary section, require confirmation before charging, and explain what will change. |
| 2 | VALUE | Hardcover checkout | The final cost may be difficult to understand at a glance | “Hardcover: The Magical Adventrue of Sam £24.99”, “Premium gift wrap £7.99”, “Shipping & handling £12.99”, and “Total £45.97” | Show a clear delivery estimate and explain whether shipping varies, while keeping every required and optional charge visibly itemised. |
| 2 | DECEPTIVE | Hardcover checkout | Countdown-style price reservation may create unnecessary urgency | "Your price is reserved for 09:40" | Explain whether the price is genuinely fixed and what happens at the deadline, or remove the countdown if it is only decorative. |

## Page-by-page
### StoryHearth homepage  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Explain the family storybook service and direct visitors to pricing, login, or the story creation process.
- **What's happening:** The page displays a warm family-oriented hero area, an illustrative book image, a three-step explanation, testimonials, and frequently asked questions below the fold.
- **First impression (Test):** "Attractive and relevant, though the main paragraph sounds unnecessarily technical and makes the service feel less approachable."
- **Cognitive walkthrough:** Q1 Yes, I would try logging in and creating the Sam and Grandpa Joe story. / Q2 Yes, the dark 'Log in' button at the top right is immediately noticeable. / Q3 Yes, 'Log in' clearly matches what I need to do.
  - [H2 sev 2] **Unnecessarily technical product language** - evidence: Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.. Fix: Replace this with plain language such as: 'Turn a family member and a treasured memory into a personalised illustrated storybook.'
  - [TRUST sev 1] **Testimonials provide few trust details** - evidence: “My daughter asks for ‘her’ book every single night.” — Hannah, Leeds. Fix: Mark testimonials as verified customer reviews and show fuller reviewer details or link them to independent reviews.
- **Positives:** The warm illustration makes the product feel child-friendly.; The three process steps clearly explain the basic workflow.; 'Free digital preview · Printed hardcovers shipped across the UK' is useful and easy to understand.; The prominent login and proceed controls are easy to find.

### Log in  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** This page lets an existing StoryHearth customer sign in to their account.
- **What's happening:** The page displays two empty credential fields, a “Log in” button, and a link to create an account. The navigation also offers “How it works” and “Pricing.”
- **First impression (Test):** "It looks calm, simple, and easy to understand. I can immediately see what I need to do."
- **Cognitive walkthrough:** Q1 Yes, I want to log in so I can create the storybook. / Q2 Yes, the two large input boxes and the orange “Log in” button are immediately noticeable. / Q3 Yes. The “Email” and “Password” placeholders and “Log in” button match what I want to do.
  - [ACC sev 2] **Email and password fields have no persistent labels** - evidence: [5] and [6] are listed as “textbox (no label)” and rely only on the placeholders “Email” and “Password”.. Fix: Add visible labels such as “Email address” and “Password” associated with each input, rather than using placeholders as the only labels.
- **Positives:** The form is uncluttered and the main action is visually prominent.; The wording is familiar and easy to understand.; There is a clear route to create an account for anyone who is new.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** Show the signed-in user’s saved books and provide a way to create another book.
- **What's happening:** The site has logged in the Demo account and presents an empty book library with a creation button. A prominent error banner reports that profile synchronization is incomplete.
- **First impression (Test):** "The page is simple and the next action is obvious, but the technical error makes me question whether my account information has loaded correctly."
- **Cognitive walkthrough:** Q1 Yes, I would try creating a book because that is my next step. / Q2 Yes, the orange “+ Create a new book” button stands out immediately. / Q3 Yes, “Create a new book” clearly matches what I want to do.
  - [H9 sev 3] **Unexplained technical sync error** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the code with a plain-language message such as “Some profile details may not have loaded. You can still create a book, or try again,” and provide a visible Retry option.
  - [H1 sev 2] **Error gives no recovery action** - evidence: “Error 0x80070057: profile sync incomplete.” with no visible retry or help control. Fix: Include a “Try again” button and a “Continue anyway” option if book creation is still available.
  - [H2 sev 1] **Generic account greeting** - evidence: “Welcome back, Demo”. Fix: Personalize the dashboard with the user’s name or email identifier where appropriate.
- **Positives:** The successful login destination is easy to recognize as the dashboard.; The empty-library message is concise and easy to understand.; The main action is clearly visible and clearly labelled.

### Create your book – characters  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Collect the details of the child and the other person who will appear in a personalised story.
- **What's happening:** I am logged in and viewing empty character fields with a Next button. The form starts with Sam's name, age, pronouns, and optional appearance, followed by Grandpa Joe's name and relationship.
- **First impression (Test):** "It looks tidy and easy to scan. “Who's the star of the story?” makes the purpose friendly, although “Who else is in the story?” sounds as though I might be able to add more than one person even though there is only one name field."
- **Cognitive walkthrough:** Q1 Yes, I can fill in the known details and continue. / Q2 Yes, the fields, dropdowns, and orange Next button are all visible without needing to search. / Q3 Mostly. The labels match what I want to enter, but “Who else is in the story?” implies multiple additional characters while the form only provides one name field.
  - [H2 sev 1] **Singular character field contradicts plural wording** - evidence: The heading says “Who else is in the story?” but there is only [10] “Who else is in the story?” textbox.. Fix: Change the label to “Who is the other person in the story?” if only one person is supported, or add a clear “Add another person” control if multiple people are allowed.
  - [CONTENT sev 1] **Optional appearance field may be too restrictive for the planned memory** - evidence: [9] “What do they look like? (optional)” has placeholder “e.g. curly red hair, green welllies” and there is no field for Grandpa Joe's grey hair.. Fix: Allow appearance details for the additional character too, or clarify that this description applies to both characters.
  - [ACC sev 1] **Footer text has very low contrast** - evidence: The footer links and copyright text, including “Privacy”, “Terms”, and “Contact”, appear extremely faint against the background.. Fix: Use a darker footer text colour with sufficient WCAG contrast.
- **Positives:** The main action is an obvious orange “Next” button.; Required character information is grouped logically on one screen.; The age and pronouns dropdowns reduce the chance of entering inconsistent wording.

### Story details form  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** Collect the setting, special object, and family memory needed to generate the personalised storybook.
- **What's happening:** The form contains empty fields for the story location, a special object, and the memory or idea behind the story, with a Back button and a prominent Next button.
- **First impression (Test):** "This looks straightforward and uncluttered. The labels and examples tell me what kind of details to provide, and the orange Next button is obvious."
- **Cognitive walkthrough:** Q1 Yes, I would try this now because it is clearly the next step in creating the book. / Q2 Yes, I noticed the three text fields and the orange Next button. / Q3 Yes. “Where does the story happen?” matches the setting, “A special object” matches the bucket, and the final prompt asks for the memory.
- **Positives:** The form is focused on only the details needed for this step.; The placeholder examples make the expected kind of information easy to understand.; The Back button provides a way to return without losing my place.; Next is visually prominent.

### Choose the look & feel  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Choose the reading difficulty and visual illustration style for the personalised book.
- **What's happening:** The form shows four reading-level radio buttons and three illustration-style options. Lexile 200L–500L and Watercolour are selected, and the user can continue with Next.
- **First impression (Test):** "The page is tidy and easy to scan. I like the watercolour description, and the default reading range seems suitable."
- **Cognitive walkthrough:** Q1 Yes, I would accept the current reading level and watercolour style and continue. / Q2 Yes, the selected radio buttons and the orange “Next” button are obvious. / Q3 Yes. “Reading level” and “Illustration style” clearly match what I want to choose, though the Lexile ranges do not directly mention an age.
  - [H2 sev 1] **Reading level is labelled with Lexile rather than a child’s age** - evidence: “Lexile BR–200L,” “Lexile 200L–500L,” “Lexile 500L–800L,” and “Lexile 800L+”. Fix: Show approximate age guidance beside each range, such as “ages 4–6,” while retaining the Lexile label.
- **Positives:** The selected states are clearly visible.; The illustration descriptions are friendly and help me understand the style.; Back and Next give me clear control over moving through the process.

### Optional photo upload  (step 8)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_08.jpg)
- **Purpose:** Offer an optional photo of the child for use in the personalised illustrations, then let the user create the book.
- **What's happening:** The page shows an optional image upload, a Back button, and the final “Create my book” button. The upload is empty and the user is ready to generate the personalised book.
- **First impression (Test):** "This is a simple final step. The fact that the photo is optional means I can comfortably continue without one."
- **Cognitive walkthrough:** Q1 Yes, I would click “Create my book” because I have no suitable photo to add and the upload is optional. / Q2 Yes, the teal “Create my book” button is prominent on the right. / Q3 Yes, “Create my book” clearly says that this will make or generate the book.
  - [ACC sev 2] **File upload has no programmatic label** - evidence: [30] file-upload (no label) shows only the browser text “Choose file” and “No file chosen”.. Fix: Add a visible and programmatic label such as “Child’s photo (optional)” associated with the file input.
  - [ACC sev 2] **Footer text has very low contrast** - evidence: The footer links “Privacy”, “Terms”, and “Contact” and the copyright line are extremely pale against the background.. Fix: Use a darker text colour with sufficient contrast and keep it visually readable on hover and focus.
- **Positives:** The heading and explanation clearly identify the upload as optional.; The final “Create my book” button is prominent and clearly labelled.; A Back control is available, so I do not feel trapped on this step.

### Creating book  (step 9)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_09.jpg)
- **Purpose:** Submit the entered story details and generate the personalised book preview.
- **What's happening:** A central loading spinner is displayed after the book creation button was pressed. No generated story or preview is visible yet, and there is no status text, estimated time, or progress detail.
- **First impression (Test):** "The spinner tells me the site is busy, but the blank screen feels unfinished and a little confusing. I would prefer a clear message such as “Creating your book…” rather than having to infer what is happening."
- **Cognitive walkthrough:** Q1 Yes, I would wait because the spinner suggests that my book is being created. / Q2 There is no control needed at this moment; the loading spinner is the only visible status indicator. / Q3 The spinner is understandable as a loading symbol, but it has no text label explaining the current step.
  - [H1 sev 2] **Loading state has no explanation** - evidence: The central panel contains only a loading spinner and no status text.. Fix: Add accessible visible text such as “Creating your book…” and, if possible, show a progress indicator or estimated time.
- **Positives:** The spinner provides a clear visual indication that the site is working.; The navigation remains available while the book is being created.

### Generated storybook preview  (step 10)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_10.jpg)
- **Purpose:** To preview the completed personalised storybook and provide access to further pages and hardcover ordering.
- **What's happening:** A 9-page preview is displayed with the cover of “The Magical Adventrue of Sam.” The cover is labelled “A StoryHearth original” and “Illustration style: Pop-art comic.” A disabled previous arrow, page indicator 1 / 9, next-page button, regenerate control, and order-hardcover link are present, with some controls below the fold.
- **First impression (Test):** "The book is there, but the typo in “Adventrue” makes it look unfinished. I also notice that the stated Pop-art comic style does not match the soft watercolour style I selected."
- **Cognitive walkthrough:** Q1 Yes, I would try to read through the book because that is the main purpose of this page. / Q2 Yes, I noticed the “›” next-page button and the 1 / 9 page indicator, although the order-hardcover link is below the fold. / Q3 Partly. “›” indicates that I can continue reading, but there is no clear “Read next page” wording and the book controls require some guessing.
  - [H2 sev 3] **Selected illustration style appears not to have been applied** - evidence: The page says “Illustration style: Pop-art comic,” although the story setup said “soft watercolour illustrations.”. Fix: Apply the selected soft watercolour style, and clearly show which style was used or offer a correction option.
  - [CONTENT sev 3] **Cover illustration may not reflect the supplied character details** - evidence: The cover shows a generic child labelled “Sam,” with no visible brown hair or connection to Grandpa Joe or the beach memory.. Fix: Use the entered character details and memory in the generated cover, or clearly explain what personalisation is included and let me regenerate or edit it.
  - [CONTENT sev 2] **Typo in generated title** - evidence: “The Magical Adventrue of Sam”. Fix: Correct the title to “The Magical Adventure of Sam” and provide a way to edit the title before ordering.
  - [VALUE sev 2] **Hardcover price is not shown before ordering** - evidence: [9] link "Order hardcover" and [8] button "Regenerate entire book – $4.99"; no hardcover price is visible beside the order link.. Fix: Display the hardcover price clearly next to the “Order hardcover” control, including any shipping or tax information before checkout.
  - [DECEPTIVE sev 2] **Paid regeneration control is prominent beside ordering** - evidence: [8] button "Regenerate entire book – $4.99" appears immediately beside the orange “Order hardcover” link.. Fix: Move regeneration into a clearly labelled secondary section, require confirmation before charging, and explain what will change.
  - [H1 sev 1] **Ordering control is below the fold** - evidence: [9] link “Order hardcover” is marked offscreen.. Fix: Keep a visible “Order hardcover” button near the book controls, or make the available actions clear at the top.
- **Positives:** The book title and page count are clearly displayed.; The page indicator “1 / 9” tells me how long the preview is.; The next-page button is visible and easy to find.; The preview is clearly separated as a generated result rather than another setup form.

### Hardcover checkout  (step 13)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_13.jpg)
- **Purpose:** Review the hardcover order price, delivery and payment requirements before purchasing.
- **What's happening:** The selected hardcover is shown with itemised pricing. A premium gift-wrap add-on is checked by default, increasing the total, and empty delivery and payment fields are presented. The order is not yet submitted.
- **First impression (Test):** "The main price is visible, but £45.97 feels high and the pre-ticked £7.99 gift wrap immediately looks like a sneaky add-on."
- **Cognitive walkthrough:** Q1 I would try to inspect and remove the gift wrap, but I would not proceed with payment. / Q2 Yes, I noticed the checked “Premium gift wrap” checkbox, but it was easy to overlook because it appears as a compact row in the price breakdown. / Q3 The labels identify the hardcover, gift wrap, shipping and total clearly, but “Premium gift wrap” does not make clear that it is an optional extra I had not requested.
  - [DECEPTIVE sev 3] **Premium gift wrap is pre-selected without being requested** - evidence: [6] checkbox “Premium gift wrap” (checked) and “£7.99”. Fix: Default the optional gift-wrap checkbox to unchecked and show exactly what it adds to the total when selected.
  - [VALUE sev 2] **The final cost may be difficult to understand at a glance** - evidence: “Hardcover: The Magical Adventrue of Sam £24.99”, “Premium gift wrap £7.99”, “Shipping & handling £12.99”, and “Total £45.97”. Fix: Show a clear delivery estimate and explain whether shipping varies, while keeping every required and optional charge visibly itemised.
  - [CONTENT sev 2] **The generated title contains a spelling error** - evidence: “Hardcover: The Magical Adventrue of Sam”. Fix: Correct the title to “Adventure” and allow the customer to edit or confirm the title before checkout.
  - [DECEPTIVE sev 2] **Countdown-style price reservation may create unnecessary urgency** - evidence: "Your price is reserved for 09:40". Fix: Explain whether the price is genuinely fixed and what happens at the deadline, or remove the countdown if it is only decorative.
- **Positives:** The hardcover price, shipping, add-on and total are shown as separate lines.; The delivery and payment sections are clearly labelled.; No payment has been submitted yet.

## Generated output assessment
*Artifact:* AI-generated personalized children's storybook preview with checkout flow

> I am very disappointed. It fails to tell the family memory I supplied, replaces Grandpa Joe with an invented uncle, uses unsuitable language and frightening material, and looks visually generic and unfinished. I would not accept this proof or pay for it.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | The output uses Sam's name and age, broadly suggests a beach, mentions a yellow bucket, and includes brown hair in some illustrations. However, Grandpa Joe never appears, the sandcastle-building memory is not depicted or |
| coherence | 1 | The narrative jumps from a beach to unexplained rain, a winding path, dark woods, and Sam going home alone. It repeats the opening almost verbatim, uses ambiguous pronouns with Uncle Bartholomew, and ends with an unfinis |
| age fit | 1 | Although Sam is five, the prose is measured at grade 7.0 and includes words such as "ephemeral," "crepuscular," "ineffable," and "existential trepidation." The threatening forest sequence is also frightening and emotiona |
| language | 1 | There are numerous serious errors: "Adventrue," "Samn," "in the beach," ambiguous pronouns, a repeated opening, duplicate "The End," unresolved template placeholders, and a final sentence with no completion or punctuatio |
| text image fit | 1 | Several pictures directly contradict their text: rain is paired with a sunny sky, a yellow bucket is represented by a yellow star, shadows with teeth are absent from a calm woodland image, and the conclusion shows neithe |
| character consistency | 2 | Sam has a broadly similar simple brown-haired appearance, but is not consistently presented as a five-year-old girl and her clothing changes. More importantly, the requested character Grandpa Joe is absent and replaced b |
| visual quality | 1 | The illustrations are sparse and generic, use the wrong visual style, omit important requested details, and include a plain final page. They do not provide the warm, polished watercolour quality expected from a paid keep |
| emotional resonance | 1 | The book fails to preserve the warm memory of Sam building sandcastles with Grandpa Joe. Generic imagery, an invented threatening plot, a missing relationship, and an unfinished ending make the result impersonal and unsu |

- **used correctly:** Sam's first name; Sam's age of five; The broad beach setting in some text and illustrations; Brown hair in some illustrations; She/her pronouns in parts of the prose; The yellow bucket in one story page; The premium gift-wrap selection at checkout
- **missing:** Grandpa Joe; The grandparent relationship; Building sandcastles together; The yellow bucket in the cover and most relevant illustrations; The soft watercolour style; A complete, explicit celebration of the family memory; A delivery estimate; A clear shipping-cost explanation
- **changed:** The requested watercolour style became a sparse pop-art comic style; The central sandcastle-building activity became unrelated fantasy and horror events; The yellow bucket was frequently represented as a yellow star; Sam was not clearly visualized as a five-year-old girl; The conclusion had Sam leaving alone rather than saying goodbye to Grandpa Joe
- **invented:** Uncle Bartholomew; A lantern; A winding path; A threatening dark forest; A red balloon; Sudden rain and a storm; Abstract melancholy and existential fear; Bartholomew and other unrelated capitalized names

### Part by part
#### Cover / Title page
![I1](artifacts/capture_01/img_00.jpg)
> A StoryHearth original Illustration style: Pop-art comic
- *Picture:* A very simple flat illustration of a small brown-haired figure labelled “Sam,” standing beside a yellow star, with a large sun overhead and bands of blue and green behind him. There is no beach detail, sandcastle, yellow bucket, or Grandpa Joe.
- *Reaction:* The misspelling “Adventrue” immediately makes the cover look unfinished. I also asked for a soft watercolour look, not a plain pop-art graphic, and this image does not communicate the family beach memory I entered.
  - [language, sev 3] The title reads “The Magical Adventrue of Sam.”
  - [fidelity, sev 3] The cover shows a generic figure, star, and sun but omits the beach, sandcastles, yellow bucket, brown-haired five-year-old girl, and Grandpa Joe.
  - [visual_quality, sev 3] The picture is a sparse geometric graphic labelled “Pop-art comic,” not the requested soft watercolour style, and the generated “Sam” label overlaps the ground.
  - [character_consistency, sev 2] Sam is presented as an androgynous figure in a green top with short brown hair, with no clear visual indication that she is a five-year-old girl.
  - [emotional_resonance, sev 3] Nothing in the image represents the specific memory of building sandcastles with Grandpa Joe.
- **Change I'd make:** Correct “Adventrue” to “Adventure” and replace the generic cover with a soft watercolour beach scene showing five-year-old Sam with brown hair, Grandpa Joe, a yellow bucket, and their sandcastle.
- **Suggested rewrite:** A StoryHearth original Illustration style: Soft watercolour The Magical Adventure of Sam and Grandpa Joe

#### Page 1 / Opening page
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in the beach, there lived a curious child named Sam. Sam was 5 years old and loved nothing more than a yellow bucket.
- *Picture:* The same extremely simple brown-haired figure stands under a large sun beside a yellow star, with flat blue and green bands suggesting water and land. There is no visible sandcastle, bucket, or Grandpa Joe.
- *Reaction:* This does not look like the opening to my requested memory. The yellow object is a star rather than my yellow bucket, and the promised sandcastle day with Grandpa Joe never starts.
  - [fidelity, sev 4] The supplied memory was “A day at the beach building sandcastles with Grandpa Joe,” but Grandpa Joe and the sandcastle-building event are absent.
  - [language, sev 2] “Once upon a time, in the beach” uses the wrong construction; this should be “at the beach.”
  - [text_image_fit, sev 3] The text says Sam loves a yellow bucket, while the picture contains a yellow star and no bucket.
  - [character_consistency, sev 2] The simple figure has short brown hair, but nothing in the drawing clearly establishes Sam as a five-year-old girl.
  - [emotional_resonance, sev 3] The opening uses stock fantasy phrasing and does not introduce the warm grandfather-child relationship that made the memory special.
- **Change I'd make:** Open directly at the beach with Sam and Grandpa Joe building sandcastles, and show the yellow bucket clearly in Sam's hands.
- **Suggested rewrite:** Sam was five years old, and she loved the beach. On one special day, Sam went to the shore with Grandpa Joe. They carried Grandpa Joe's old yellow bucket and set out to build the biggest sandcastle they could.

#### Page 2
![I4](artifacts/capture_05/img_00.jpg)
![I2](artifacts/capture_03/view_00.jpg)
> One evening Sam gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* Sam stands under a purple-to-pink evening sky with a few white stars. The scene is calm and visually simple, with no Grandpa Joe, sandcastle, or yellow bucket.
- *Reaction:* This sentence is far too advanced and emotionally heavy for a five-year-old. Words such as “ephemeral,” “melancholy,” and “existential trepidation” sound like an adult literary essay, not a bedtime story.
  - [age_fit, sev 4] “The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy” contains vocabulary far beyond a five-year-old's reading level.
  - [language, sev 3] Although grammatically elaborate, the sentence is wildly unsuitable for the requested age; the automatic measurement also gives the prose a grade 7.0 level.
  - [coherence, sev 3] The sudden shift to evening and abstract melancholy is not connected to the requested beach memory or any action involving Grandpa Joe.
  - [fidelity, sev 3] This invented melancholy scene has no basis in the supplied memory and displaces the sandcastle activity.
  - [text_image_fit, sev 2] The picture captures evening and stars, but it cannot convey the advanced emotions or elaborate wording in the text.
- **Change I'd make:** Replace the sentence with simple language about Sam watching clouds over the beach, and keep the focus on her shared day with Grandpa Joe.
- **Suggested rewrite:** Sam looked up at the sky. The clouds were white and soft, and one looked just like a rabbit. Grandpa Joe stood beside her and said, “That one is our sandcastle cloud.”

#### Page 3
![I5](artifacts/capture_06/img_00.jpg)
![I3](artifacts/capture_04/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Samn pulled up her hood and ran for shelter, holding a yellow bucket tight.
- *Picture:* The image is bright and sunny, with a large sun, blue sky, the same green-shirted figure, and the yellow star. There are no raindrops, puddles, hood, beach activity, or yellow bucket.
- *Reaction:* The story says it is pouring rain, but the picture looks sunny. I also notice “Samn” immediately, which is a serious mistake in a personalized book.
  - [text_image_fit, sev 4] The text describes pouring rain, grey drops, puddles, and a hood, while the picture shows a bright sun and clear blue sky.
  - [language, sev 3] The child's name is incorrectly rendered as “Samn.”
  - [character_consistency, sev 3] Samn is not the supplied name, and the image still shows the original figure without a hood or rain protection.
  - [fidelity, sev 2] The yellow star in the image does not match the yellow bucket described in the text.
  - [coherence, sev 3] The sudden storm is introduced without setup and does not lead into the requested sandcastle memory with Grandpa Joe.
- **Change I'd make:** Correct “Samn” to “Sam,” show actual rain, and make the weather part of a problem that Sam and Grandpa Joe solve together at the beach.
- **Suggested rewrite:** Then the sky turned grey, and rain began to fall. Sam pulled her coat over her head and held her yellow bucket tight. “Our sandcastle!” she called. “Come on, Sam,” said Grandpa Joe. “We can keep building under my umbrella.”

#### Page 4
![I6](artifacts/capture_07/img_00.jpg)
![I4](artifacts/capture_05/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Sam, follow me!" he called, and he followed him along the winding path.
- *Picture:* Two simple labelled figures, “Uncle Bartholomew” and “Sam,” stand against a dark gradient sky above the same blue-and-green bands. Bartholomew has a small yellow rectangle beside him that may represent the lantern.
- *Reaction:* I never supplied an uncle named Bartholomew; Grandpa Joe has been replaced by a stranger. The pronouns are also wrong: after Bartholomew speaks to Sam, the story says “he followed him,” leaving the actors unclear.
  - [fidelity, sev 4] The user specified “Grandpa Joe” with the relationship “Grandparent,” but the output invents “Uncle Bartholomew” and omits Grandpa Joe.
  - [language, sev 3] “He called, and he followed him” makes the pronouns and direction of action ambiguous.
  - [coherence, sev 3] A lantern-bearing uncle suddenly appears, but there is no setup for why he is there or how the story moved from the beach to “the winding path.”
  - [text_image_fit, sev 2] The image shows the two figures and a possible lantern, but no visible winding path and no transition from the beach.
  - [character_consistency, sev 3] Sam is drawn with the same short brown hair, but the invented uncle is given a full appearance and label that was never requested.
- **Change I'd make:** Remove Uncle Bartholomew, restore Grandpa Joe, and show Grandpa Joe helping Sam build or protect the sandcastle at the beach.
- **Suggested rewrite:** “Sam, what shall we build next?” asked Grandpa Joe. Sam pointed to a wide patch of wet sand. “Let's make a castle with four strong towers!” Grandpa Joe laughed. “Then we will need your yellow bucket.”

#### Page 5
![I7](artifacts/capture_08/img_00.jpg)
![I5](artifacts/capture_06/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Sam again. Sam clutched a shiny red balloon and trembled in the dark.
- *Picture:* Sam stands at night near three simple trees, a crescent moon, stars, and a floating red balloon. The trees are rounded rather than menacing, and no teeth or frightening shadows are visible.
- *Reaction:* This is a sudden horror detour involving being lost in dark woods, not a gentle family beach memory. It is also harsher and more frightening than I would choose for Sam at five.
  - [fidelity, sev 4] The supplied event was building sandcastles with Grandpa Joe at the beach; the story instead invents a lost-child sequence in the woods with a red balloon.
  - [coherence, sev 4] The story jumps from Grandpa Joe's beach outing to Sam being alone in deep woods without explaining how she got there.
  - [age_fit, sev 4] “The shadows grew teeth and whispered that no one would ever find Sam again” is frightening and emotionally unsuitable for the requested gentle age-five beach story.
  - [text_image_fit, sev 3] The text describes shadows with teeth and whispering danger, but the picture shows harmless round trees and a calm moonlit scene.
  - [character_consistency, sev 2] Sam's shirt changes from green in earlier pages to teal here, and the picture does not show Grandpa Joe beside her.
  - [emotional_resonance, sev 4] The threatening separation is not based on my memory and makes the keepsake feel upsetting rather than affectionate.
- **Change I'd make:** Remove the frightening woods and red balloon. Return to the beach, where Sam and Grandpa Joe work through a small problem and finish their sandcastle together.
- **Suggested rewrite:** A big wave splashed near their castle and washed away one corner. Sam looked worried, but Grandpa Joe said, “We can build it again.” Together they pressed the wet sand into a strong new wall. The yellow bucket made a perfect castle gate.

#### Page 6
![I8](artifacts/capture_09/img_00.jpg)
![I6](artifacts/capture_07/img_00.jpg)
> Once upon a time, in the beach, there lived a curious child named Sam. At last the sun came out, and Sam skipped all the way home, happier than ever.
- *Picture:* Sam again stands beneath a large sun in a sparse blue-and-green scene. There is no path home, no beach activity, no yellow bucket, no sandcastle, and no Grandpa Joe.
- *Reaction:* The opening sentence has been repeated almost word for word, and Sam leaves alone. This should be the warm conclusion to her day with Grandpa Joe, not the start of another story.
  - [fidelity, sev 4] The memory called for Sam and Grandpa Joe to build sandcastles together, but the conclusion says only that “Sam skipped all the way home.”
  - [coherence, sev 4] “Once upon a time, in the beach, there lived a curious child named Sam” repeats the opening almost exactly after the intervening events.
  - [language, sev 2] “Once upon a time, in the beach” is an incorrect and awkward construction.
  - [text_image_fit, sev 3] The text describes skipping all the way home, but the picture shows Sam standing still with no home, path, or movement.
  - [character_consistency, sev 2] Sam's basic design remains similar, but she is again alone and Grandpa Joe is absent.
- **Change I'd make:** End the active story with Sam and Grandpa Joe admiring their finished sandcastle, then show them waving goodbye. Do not repeat the opening sentence.
- **Suggested rewrite:** At last, Sam and Grandpa Joe had built a wide castle with tall towers and a deep moat. Grandpa Joe helped Sam place the last shell on top. Sam smiled. “We made it together,” she said.

#### Page 7 / Closing page
![I9](artifacts/capture_10/img_00.jpg)
![I7](artifacts/capture_08/img_00.jpg)
> The End And from that day on, whenever Sam looked up at the sky, she would always remember The End
- *Picture:* A plain orange page with “The End” at the top, the same small figure labelled “Sam” in the middle, and the familiar blue and green bands below. There is no Grandpa Joe, sandcastle, bucket, or completed final memory.
- *Reaction:* The last sentence does not finish, and “The End” appears twice. This is not a polished keepsake, especially for a paid personalized book.
  - [language, sev 4] “And from that day on, whenever Sam looked up at the sky, she would always remember” ends without saying what she remembered.
  - [language, sev 3] “The End” is printed twice in the text.
  - [fidelity, sev 4] The final memory never explicitly recalls building sandcastles with Grandpa Joe, and the yellow bucket is absent.
  - [text_image_fit, sev 3] The picture only shows Sam and “The End”; it does not depict the sky, the completed memory, Grandpa Joe, the sandcastle, or the bucket.
  - [emotional_resonance, sev 4] The unfinished sentence and plain final illustration prevent the book from feeling like a meaningful family keepsake.
  - [visual_quality, sev 3] The large empty orange field and generic repeated figure make the concluding page visually plain.
- **Change I'd make:** Complete the final thought, print “The End” only once, and use a warm watercolour image of Sam and Grandpa Joe beside their finished sandcastle and yellow bucket.
- **Suggested rewrite:** The End From that day on, whenever Sam saw a sandcastle, she would smile and remember the day she built one with Grandpa Joe.

#### Checkout — gift wrap selected, upper section
![I10](artifacts/capture_13/view_00.jpg)
> StoryHearth How it works Pricing My books Log out Checkout Your price is reserved for 09:44 Hardcover: The Magical Adventrue of Sam    £24.99  Premium gift wrap    £7.99 Shipping & handling    £12.99 Total    £45.97 Delivery Address Payment Card number Expiry CVC
- *Picture:* The upper checkout page shows the product summary, a checked premium-gift-wrap box, the price breakdown, and the beginning of blank address and payment fields.
- *Reaction:* The misspelled title is still present at the point where I am expected to pay £45.97. The selected gift wrap is honored, but seeing the error repeated in checkout makes me less confident that the printed book would be carefully checked.
  - [language, sev 3] The checkout product name repeats “The Magical Adventrue of Sam.”
  - [emotional_resonance, sev 3] The most obvious customer-facing product name remains misspelled after the preview, reducing confidence in a £45.97 keepsake purchase.
- **Change I'd make:** Correct “Adventrue” everywhere before checkout, verify the final book proof, and add a clear delivery estimate or shipping explanation before payment.
- **Suggested rewrite:** Hardcover: The Magical Adventure of Sam — £24.99 Premium gift wrap — £7.99 Shipping & handling — £12.99 Total — £45.97

#### Checkout — gift wrap selected, lower section
![I11](artifacts/capture_13/view_01.jpg)
> Premium gift wrap    £7.99 Shipping & handling    £12.99 Total    £45.97 Delivery Address Payment Card number Expiry CVC Pay now
- *Picture:* The lower checkout page repeats the price summary and shows blank address, card number, expiry, and CVC fields, followed by a prominent “Pay now” button.
- *Reaction:* The form is understandable, but I would want the corrected title and a delivery estimate before entering payment details. Paying £45.97 for this flawed preview would feel risky.
  - [emotional_resonance, sev 3] The purchase is presented for payment despite the misspelled title, missing requested family content, frightening detour, and unfinished ending.
- **Change I'd make:** Do not present payment as final until a corrected proof has been approved; display the delivery timeframe and final corrected title beside the payment button.
- **Suggested rewrite:** Review corrected proof Delivery estimate: shown clearly before payment Pay £45.97 now

#### Checkout — gift wrap removed, upper section
![I12](artifacts/capture_14/view_00.jpg)
> StoryHearth How it works Pricing My books Log out Checkout Your price is reserved for 09:30 Hardcover: The Magical Adventrue of Sam    £24.99  Premium gift wrap    £7.99 Shipping & handling    £12.99 Total    £37.98 Delivery Address Payment Card number Expiry CVC
- *Picture:* The checkout page now has an unchecked premium-gift-wrap box. A £7.99 gift-wrap line is still visible, shipping is £12.99, and the total is £37.98.
- *Reaction:* The total correctly falls by £7.99 when I uncheck the box, but the gift-wrap line still shows £7.99 even though it is not selected. That makes the price breakdown unnecessarily confusing.
  - [language, sev 3] The checkout title still reads “The Magical Adventrue of Sam.”
  - [visual_quality, sev 2] The unchecked “Premium gift wrap” row still displays “£7.99” rather than “Not selected” or “£0.00,” even though the total has been reduced.
  - [emotional_resonance, sev 3] At £37.98, the checkout still asks for payment on a book that has repeatedly misspelled the title and failed to preserve the supplied family story.
- **Change I'd make:** Change the unchecked row to “Premium gift wrap — Not selected — £0.00,” correct the title everywhere, and provide delivery timing before payment.
- **Suggested rewrite:** Hardcover: The Magical Adventure of Sam — £24.99 Premium gift wrap — Not selected — £0.00 Shipping & handling — £12.99 Total — £37.98

#### Page 8
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in the beach, there lived a curious child named Sam. At last the sun came out, and Sam skipped all the way home, happier than ever.
- *Picture:* A brighter illustration showing Sam going home after the sun comes out.
- *Reaction:* The repeated opening makes it feel like a template error, and Sam goes home alone instead of finishing the memory with Grandpa Joe.
  - [language, sev 3] The opening sentence is repeated almost exactly: “Once upon a time, in the beach, there lived a curious child named Sam.”
  - [language, sev 2] “In the beach” is again grammatically incorrect.
  - [fidelity, sev 3] The central memory of building sandcastles with Grandpa Joe is not resolved; Sam simply goes home.
- **Change I'd make:** Remove the repeated sentence and explicitly conclude the shared activity and Grandpa Joe relationship.
- **Suggested rewrite:** When they finished, Sam and Grandpa Joe admired their sandcastle together. It was not the biggest castle, but it was their special one.

#### Page 9
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Sam looked up at the sky, she would always remember The End
- *Picture:* A simple closing-page illustration with the unfinished sentence and duplicated “The End.”
- *Reaction:* The ending is visibly unfinished, repeats “The End,” and never names the family memory or Grandpa Joe. The final illustration is too plain to feel like a keepsake.
  - [language, sev 4] The sentence ends after “remember” with no object or punctuation.
  - [coherence, sev 3] “The End” appears both before and after the unfinished sentence.
  - [fidelity, sev 4] The closing does not mention Grandpa Joe, sandcastles, or the special family memory.
  - [visual_quality, sev 3] The final image is described as very plain and does not provide a satisfying visual conclusion.
  - [emotional_resonance, sev 4] The page feels incomplete and does not provide a meaningful keepsake ending.
- **Change I'd make:** Finish the sentence once, remove the duplicate ending, and close on the shared sandcastle memory with a warm illustration.
- **Suggested rewrite:** From that day on, whenever Sam saw a sandy beach, she remembered building sandcastles with Grandpa Joe. The End

#### Checkout — gift wrap removed, lower section
![I13](artifacts/capture_14/view_01.jpg)
> Delivery Address Payment Card number Expiry CVC Pay now
- *Picture:* The lower checkout area shows empty address, card number, expiry, and CVC fields, with an orange “Pay now” button. The page footer is visible below.
- *Reaction:* The layout is clear, but I would not pay until the book’s obvious errors were fixed and the shipping cost was explained.
  - [emotional_resonance, sev 3] The final payment step follows a product with unresolved placeholders, misspellings, invented characters, frightening material, and an unfinished sentence.
- **Change I'd make:** Add a final review link or correction notice before payment, and state the delivery timeframe and return policy.

**Top changes to the output:** 1. Rewrite the entire story around Sam and Grandpa Joe building sandcastles together at the beach, ending with an explicit reflection on that special family memory. | 2. Replace the frightening and advanced material with simple, warm prose suitable for a five-year-old. | 3. Correct all errors, including "Adventrue," "Samn," "in the beach," pronoun ambiguity, duplicate text, repeated scenes, template placeholders, and the unfinished final sentence. | 4. Use consistent soft watercolour illustrations showing five-year-old Sam with brown hair, Grandpa Joe, the yellow bucket, and their completed sandcastle in every key scene. | 5. Require image-text alignment and an explicit final proof check before checkout, including corrected product naming and a clear breakdown of shipping and delivery.

## Recommendations (participant's priorities)
- **[high] Rewrite the story around the supplied memory, keeping the requested people, relationship, place, object, and main event, with a clear and emotionally satisfying ending.** (Generated storybook preview) - The most important purpose of the product is to preserve a personal family memory, and this output failed at that basic purpose.
- **[high] Apply the selected illustration style consistently and require the images to match the text and the supplied character details.** (Generated storybook preview) - Paying for a keepsake would be pointless if the pictures do not represent the selected style or the people in the story.
- **[high] Use simple, warm, age-appropriate language for a five-year-old and remove frightening, advanced, or unfinished material.** (Generated storybook preview) - The story should be engaging and comforting for Sam, not confusing, threatening, or written at an unexpectedly advanced level.
- **[high] Run an automatic final check for spelling, grammar, repeated text, unresolved placeholders, incomplete sentences, and character consistency before showing the book.** (Generated storybook preview) - Typos, awkward sentences, and unfinished output make the book look careless and undermine confidence in the product.
- **[high] Show the full hardcover price, shipping, delivery details, and any optional extras before the user clicks Order hardcover.** (Generated storybook preview) - I should not discover the final cost only after starting checkout.
- **[high] Do not preselect premium gift wrap or any other paid extra.** (Hardcover checkout) - I felt annoyed because I had not requested gift wrap and did not expect it to increase the total.
- **[high] Make the total, shipping charge, delivery information, and optional charges understandable at a glance.** (Hardcover checkout) - The final cost was not clear enough, and the countdown-style reservation added unnecessary pressure.
- **[medium] Replace technical homepage phrases such as “multimodal generative narrative engine” and “lived-experience corpus” with plain explanations.** (StoryHearth homepage) - The technical wording sounds more complicated than the family activity needs to be.
- **[medium] Replace the unexplained technical sync error with a clear, reassuring message and a recovery action.** (My books dashboard) - The error made me wonder whether my details were safe and whether I could continue using the account.
- **[medium] Explain what is happening during the creation loading state and indicate that the book is being generated and saved.** (Create your book – Creating book) - The spinner alone did not tell me whether the process was still working or had encountered a problem.
- **[medium] Use persistent, accessible labels for the login fields and file upload, and improve the low-contrast footer text.** (Log in and Optional photo upload) - Clear labels and readable text would make these parts easier and more reassuring to use, especially for less technical users.
- **[low] Make the ordering control visible earlier and keep the paid regeneration option less prominent than the option to review or edit the book.** (Generated storybook preview) - The most important action was below the fold, while an extra paid action was too prominent.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This is a website for creating personalised storybooks starring children and important people in their lives, then optionally ordering a printed keepsake. It seems aimed at parents and families who want to turn a personal memory into a children's book.
- **What was the most frustrating or confusing moment, and why?** The most frustrating moment was seeing the finished preview: it replaced Grandpa Joe with an invented uncle, used frightening and advanced material for a five-year-old, contained serious language errors, and used pop-art images instead of the soft watercolour style I selected. The default premium gift wrap at checkout made the purchase feel deceptive as well.
- **What was the best moment?** The best moment was entering the beach memory through the clear creation form. The questions about the people, place, object, and memory made it easy to explain what I wanted the story to include.
- **Was there any point where, in real life, you would have given up? Where and why?** I would probably have given up when I saw the generated book, because it did not represent the family memory I supplied. If I had continued to checkout, the unexpected price and preselected gift wrap would have been another strong reason to stop.
- **What did you expect to find or be able to do that wasn't there?** I expected the book to show Sam and Grandpa Joe building sandcastles together at the beach, using the yellow bucket and soft watercolour illustrations. I also expected to see the full price, shipping, delivery information, and any optional charges clearly before choosing to order.
- **Did you trust this website with your information (and your family's)? Why or why not?** I was willing to enter the story details, but the unexplained profile sync error made me hesitate about how my information was being handled. The mismatch between the requested content and the output also made me trust the site less with a family keepsake.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would not pay for this result. Even for a good version, a fair price would probably be around £20-£25 including ordinary shipping; I would pay more only if the story accurately captured the requested characters and memory, the illustrations were consistently high quality, and all costs were transparent. I would not pay extra for gift wrap unless I actively selected it.
- **If the site produced something for you, how do you feel about it overall?** I am very disappointed. The output does not tell the family memory I supplied, replaces Grandpa Joe with an invented uncle, includes unsuitable language and frightening material, and looks generic and unfinished. I would not accept it as proof or pay for it.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | This looks relevant to me because I would like a story about Sam and Grandpa Joe at the beach. The illustration is appealing, but words like 'multimodal generative narrative engine' and 'lived-experience corpus' sound fa | click |
| 2 | Log in – StoryHearth | reassured (1) | This is straightforward. The placeholders tell me which details belong in each box, and the orange button makes the main action obvious. | type; type; click |
| 3 | My books – StoryHearth | hesitant (0) | I’m logged in, which is clear enough, but that profile sync error makes me hesitate because it looks technical and doesn’t explain whether my details are safe. The orange “+ Create a new book” button is obvious, so I’ll  | click |
| 4 | Create your book – StoryHearth | neutral (1) | This form is clear enough, and the orange “Next” button stands out. It asks about the people first, but I still need to get to a place where I can enter our memory at the beach. | type; select; select; type; type; select |
| 5 | Create your book – StoryHearth | reassured (2) | Yes, this all looks right. I’ll click “Next” to continue with our beach memory. | click |
| 6 | Create your book – StoryHearth | reassured (2) | This is clear and easy to follow. I can put the beach as the place, the yellow bucket as the special object, and explain that Sam and Grandpa Joe built sandcastles together. The wording “Tell us the memory or idea behind | type; type; type; click |
| 7 | Create your book – StoryHearth | reassured (1) | This is a simple style choice. The selected reading level sounds right for Sam at five, and the soft watercolour pictures appeal to me, so I’ll keep both and continue. | click |
| 8 | Create your book – StoryHearth | reassured (1) | I don't have a photo to upload here, and it says “optional,” so I'll leave it empty. “Create my book” clearly tells me this is the final action. | click |
| 9 | Create your book – StoryHearth | neutral (0) | I can tell something is happening because the spinner is moving, but I’m not sure whether it is creating the book, saving it, or still processing. I’ll wait for it to finish. | wait_for_change |
| 10 | Your storybook – StoryHearth | hesitant (-1) | The book was created, but the title has a clear typo, and it says “Pop-art comic” even though I chose soft watercolour illustrations. The cover also looks quite simple rather than like the style I selected. I need to rea | flip_through |
| 11 | Your storybook – StoryHearth | frustrated (-1) | I’ve reached the end and the preview says 9 pages, so I did look through the whole thing. The ending feels a little disconnected from the beach-and-sandcastles memory, and the title typo and mismatched style still bother | scroll |
| 12 | Your storybook – StoryHearth | frustrated (-1) | I’ve seen the ending now, and the story still doesn’t feel like the beach memory I entered, especially the line about looking up at the sky. I’m going to click “Order hardcover” to find out what it really costs, but I wi | click |
| 13 | Checkout – StoryHearth | annoyed (-2) | That is more expensive than I expected, and I’m annoyed that premium gift wrap was selected by default. I would not have asked for it, so I’m going to uncheck it and look at the full checkout details. I will not enter ca | click; scroll; read_page |
| 14 | Checkout – StoryHearth | annoyed (-1) | Good, unchecking “Premium gift wrap” worked and the total dropped to £37.98. That is still quite a lot for one book once £12.99 shipping is included. I have found out what I needed to know, and I’m stopping here without  | done |
