# UserQA report: Harold Brooks on http://127.0.0.1:8765/

*Persona:* **Harold Brooks** (78) - Retired carpenter with macular degeneration who browses at 200% zoom.  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 13 steps | *Pages reviewed:* 9 | *Issues:* 32 | *LLM calls:* 16 | *Wall time:* 315.1 s

## What the agent understood the website to be
- **what it is:** A website for making personalised illustrated family storybooks from supplied family memories.
- **who it is for:** Families wanting stories featuring their children and other family members or pets.
- **value proposition:** Turn a family memory into an illustrated book, with a free digital preview and an optional printed hardcover.
- **pricing model:** A free digital preview is advertised; printed hardcovers are available, but no price is shown on this page.
- **fit for me:** It could help me make a book about Conker for Lily and read it with her, but I need clearer, plainer wording and more readable text.
- **main tasks:** Log in, Add a child and another character, Describe a memory, treasured object, and place, Generate and read a storybook preview, Check and order a printed hardcover

## Scores
- SUS: **45.0** (grade F; 68 = industry average) - inconsistent responding flagged
- UEQ-S: pragmatic -0.5, hedonic -0.5 (range -3..+3)
- Likelihood to recommend (0-10): 3
- Output keepsake-worthiness (1-5): 1
- Verdict: *"The site took my details and made a book, but the result was more like a rough plank with the nails showing than a keepsake I would be proud to give Lily."*

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 3 | ACC | Home page, My books dashboard, Story details, Log in form (x4) | Footer text is too faint and small to read | Some text is too faint, including “Privacy”, “Terms”, “Contact”, and “© 2026 StoryHearth Ltd.” | Use larger, dark, high-contrast footer text and descriptive labels for every link. |
| 3 | ACC | Hardcover checkout, Create your book, Optional photo upload (x3) | Footer links are faint and too small to read | [12], [13], [14] are marked “faint/small text you cannot make out” | Use dark, high-contrast text at least 16 CSS pixels before zoom, with descriptive link labels and comfortable spacing. |
| 3 | CONTENT | Generated storybook preview, Hardcover checkout (x2) | Spelling error in the generated title | “The Magical Adventrue of Lily” | Provide an obvious edit control for the title and run a spelling check before showing the final preview. |
| 3 | ACC | Home page | Supporting text has weak contrast | “Leverage our multimodal generative narrative engine…” and “Free digital preview · Printed hardcovers shipped across the UK” are shown in pale grey or beige. | Use near-black body text on white or another strongly contrasting background, and maintain at least WCAG AA contrast. |
| 3 | H9 | My books dashboard | Error message gives no useful explanation or recovery | “Error 0x80070057: profile sync incomplete.” | Replace the code with plain wording such as “Some of your profile details have not loaded. You can continue, but your book may not include them,” and provide a clear “Try again” or “Continue without p |
| 3 | H5 | Choose the look & feel | The story field silently cut off the end of my memory | The action result says, “typed 300 characters … but the box now only shows 200 characters; the end of what you typed was cut off: ...'aginary gallop across the  | Do not let typed text disappear. Provide enough room or allow 300 characters, and show a persistent character count with a clear warning before proceeding. Preserve the entire text until I explicitly  |
| 3 | H2 | Generated storybook preview | The generated illustration style does not match my choice | I selected “Storybook classic — timeless ink and colour,” but the page says “Illustration style: Pop-art comic”. | Use the selected style in the generated book, or clearly explain that the requested style is unavailable and ask me to choose an alternative. |
| 3 | ACC | Generated storybook preview | Page navigation uses tiny icon-only controls | [6] button “‹” and [7] button “›” | Use large, clearly labelled buttons such as “Previous page” and “Next page,” with adequate spacing and strong contrast. |
| 3 | CONTENT | Generated storybook preview | The final sentence of the story is incomplete | “And from that day on, whenever Lily looked up at the sky, she would always remember” followed immediately by “The End” | Check the generated final paragraph and ensure every sentence ends grammatically, with a complete thought before displaying “The End.” |
| 3 | ACC | Generated storybook preview | The page-turn buttons are too small for comfortable use | [6] and [7] are shown as small arrow-only controls | Make the controls at least 44 by 44 pixels and label them “Previous page” and “Next page,” while keeping the arrows as supplementary symbols. |
| 3 | DECEPTIVE | Hardcover checkout | Gift wrap is pre-selected without being requested | [6] checkbox "Premium gift wrap" (checked); £7.99 | Make every optional extra unchecked by default and show the total again immediately before and after the box is selected. |
| 2 | H2 | Home page | The opening explanation is written in needlessly technical language | “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.” | Replace it with plain language, such as: “Turn a special family memory into a personalised illustrated storybook featuring your own family.” |
| 2 | ACC | Home page | Main image has no useful description | [image (no description) 577x440] | Give the image meaningful alternative text, or mark it decorative if it conveys no information. |
| 2 | ACC | Log in form | Login fields are not visibly labelled | [5] textbox (no label) placeholder "Email"; [6] textbox (no label) placeholder "Password" | Put permanent, high-contrast labels such as 'Email address' above the fields, and keep visible text inside each field when something is typed. |
| 2 | H1 | My books dashboard | Profile sync failure is presented without reassurance | “Error 0x80070057: profile sync incomplete.” | Show whether the account is usable and explain the next step, rather than displaying only a technical error. |

## Page-by-page
### Home page  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Explain the service and let me start creating a story, log in, or view pricing.
- **What's happening:** I have arrived at the public home page. The service description, two main calls to action, a three-step explanation, customer quotations, and frequently asked questions are visible at different scroll positions.
- **First impression (Harold):** "The heading and big buttons are clear enough, but the main description uses ridiculous jargon and much of the supporting writing is pale and difficult for my eyes."
- **Cognitive walkthrough:** Q1 Yes, once I get past the need to log in; this is the service my friend mentioned. / Q2 Yes, the dark “Log in” button is prominent at the top right, and the orange “Proceed” button is also visible. / Q3 “Log in” is clear for signing into my account, while “Proceed” is less explicit but reasonable once I know I am starting a story.
  - [ACC sev 3] **Supporting text has weak contrast** - evidence: “Leverage our multimodal generative narrative engine…” and “Free digital preview · Printed hardcovers shipped across the UK” are shown in pale grey or beige.. Fix: Use near-black body text on white or another strongly contrasting background, and maintain at least WCAG AA contrast.
  - [ACC sev 3] **Footer text is too faint and small to read** - evidence: Some text is too faint, including “Privacy”, “Terms”, “Contact”, and “© 2026 StoryHearth Ltd.”. Fix: Use larger, dark, high-contrast footer text and descriptive labels for every link.
  - [H2 sev 2] **The opening explanation is written in needlessly technical language** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Replace it with plain language, such as: “Turn a special family memory into a personalised illustrated storybook featuring your own family.”
  - [ACC sev 2] **Main image has no useful description** - evidence: [image (no description) 577x440]. Fix: Give the image meaningful alternative text, or mark it decorative if it conveys no information.
  - [H2 sev 1] **Primary action is vague** - evidence: [5] link "Proceed →". Fix: Label the button “Create your storybook” and explain that I will be asked a few simple questions.
- **Positives:** The large heading clearly states that this is about family stories.; The three-step explanation is broken into plain, understandable stages below the jargon.; The “Log in” button is prominent and clearly labelled.; The page says the digital preview is free and delivery is available across the UK.

### Log in form  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** Let an existing StoryHearth customer sign in to create and use a family storybook.
- **What's happening:** The page presents two empty sign-in fields and a large Log in button, with a link for people creating an account. The privacy, terms, contact, and copyright links are below the visible area.
- **First impression (Harold):** "The main login job is clear and the button is large, but the pale placeholder text is difficult for my eyes. I feel more confident once I look at the overall arrangement rather than reading every faint detail."
- **Cognitive walkthrough:** Q1 Yes, this is exactly what I expected the Log in link to do. / Q2 Yes, the two large fields and the orange 'Log in' button are easy to notice. / Q3 The button clearly says 'Log in', and the placeholders 'Email' and 'Password' tell me what to put in them, though permanent field labels would be better.
  - [ACC sev 2] **Login fields are not visibly labelled** - evidence: [5] textbox (no label) placeholder "Email"; [6] textbox (no label) placeholder "Password". Fix: Put permanent, high-contrast labels such as 'Email address' above the fields, and keep visible text inside each field when something is typed.
  - [ACC sev 1] **Footer links are too faint and small** - evidence: Privacy; Terms; Contact; and © 2026 StoryHearth Ltd. are marked faint/small text I cannot make out. Fix: Use darker, larger footer text with a contrast ratio that remains readable at 200% zoom.
- **Positives:** The 'Welcome back' heading is large and reassuring.; The orange 'Log in' button is large, clearly named, and easy to see.; The email and password boxes are large enough to target comfortably.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** Shows the books in the account and provides a way to create a new book.
- **What's happening:** The account has no existing books, so the page presents “+ Create a new book.” A profile sync error is visible above the welcome message.
- **First impression (Harold):** "The layout is uncluttered and the main button is easy to spot. I’m put off by the error code, which looks more like a workshop error message than a helpful explanation."
- **Cognitive walkthrough:** Q1 Yes, I would try creating the book because that is exactly what I came here to do. / Q2 Yes, the large orange “+ Create a new book” button stands out. / Q3 Yes. “Create a new book” plainly tells me it will start a book.
  - [H9 sev 3] **Error message gives no useful explanation or recovery** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the code with plain wording such as “Some of your profile details have not loaded. You can continue, but your book may not include them,” and provide a clear “Try again” or “Continue without profile details” button.
  - [H1 sev 2] **Profile sync failure is presented without reassurance** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Show whether the account is usable and explain the next step, rather than displaying only a technical error.
  - [ACC sev 2] **Footer text is too faint to read** - evidence: The visible notes say “Privacy”, “Terms”, “Contact”, and “© 2026 StoryHearth Ltd.” are faint/small and cannot be read.. Fix: Use darker, larger text and larger link targets for the footer.
- **Positives:** The “+ Create a new book” button is large, clearly labelled, and easy to notice.; The page says plainly that there are no books yet, so I know I am not overlooking something.; The main navigation labels are written in ordinary language.

### Create your book  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Collect basic details about the child who will star in a personalised storybook and another character in the story.
- **What's happening:** The form begins with a child's first-name box, an age menu, and a pronouns menu. Further fields and the Next button require scrolling.
- **First impression (Harold):** "The heading and labels are large and plainly worded, so I know what is wanted. At this zoom I must keep scrolling, but I don't feel lost."
- **Cognitive walkthrough:** Q1 Yes, I can fill in Lily's name, age, and pronouns now. / Q2 Yes, the matching textbox and menus are clearly visible. / Q3 Yes, “Child's first name,” “Age,” and “Pronouns” say exactly what I need to provide.
  - [ACC sev 2] **Important fields and Next button are below the fold** - evidence: The page says “everything below needs scrolling,” and [12] “Next” is offscreen.. Fix: Keep each question and its control in a compact, clearly separated group, provide a visible progress indicator, and ensure the Next control remains easy to find after scrolling.
  - [ACC sev 2] **Footer links are too faint to read** - evidence: [13], [14], and [15] are faint/small, and the footer text cannot be read.. Fix: Use dark, full-opacity text with adequate size and a readable text label for every link, including Privacy, Terms, and Contact.
- **Positives:** The page heading clearly explains the purpose of the form.; The visible field labels use ordinary words and are easy to match to the task.; The name, age, and pronoun controls are large enough to see and distinguish.

### Story details  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** Collect the setting, a special object, and the memory that will guide creation of Lily's personalised storybook.
- **What's happening:** Three empty fields request the story location, a special object, and details of the family memory. Back and Next are available below the fold.
- **First impression (Harold):** "This is straightforward and uses clear headings. The large fields are easy to see, although I need to scroll to reach the Next button."
- **Cognitive walkthrough:** Q1 Yes, I know the family memory and can describe it clearly. / Q2 Yes, the three large boxes are obvious, and the Next button is named clearly after scrolling down. / Q3 Yes. The place, object, and memory correspond exactly to what I want in the book.
  - [ACC sev 2] **Example text is pale and low contrast** - evidence: Placeholder text such as "e.g. the beach at Grandma's" and "e.g. a yellow bucket" is very light grey.. Fix: Use dark, high-contrast placeholder text at a readable size and retain permanent visible field labels.
  - [ACC sev 2] **Footer links are too small and faint to read** - evidence: The Privacy, Terms, and Contact links are described as faint or small, and the copyright text is unreadable.. Fix: Use larger, high-contrast footer links and copyright text that remain readable at 200% zoom.
  - [H7 sev 1] **The Next button is below the visible area** - evidence: [19] button "Back" (offscreen); [20] button "Next" (offscreen). Fix: Keep a large Back and Next action bar visible as a sticky footer, or make the step advance automatically only after clear confirmation.
- **Positives:** The headings clearly describe the information needed.; The input boxes are large and easy to distinguish.; The labels use ordinary family-memory language rather than technical wording.; The page provides clear Back and Next controls.

### Choose the look & feel  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Choose the reading difficulty and visual style for Lily's personalised book.
- **What's happening:** The page presents four reading-level radio buttons and three illustration-style radio buttons. The middle reading level and watercolour style are selected, with Back and Next controls below.
- **First impression (Harold):** "This is fairly straightforward and the large choices are easy to see. Lexile is not a word I know, though, so I need to rely on the sensible default that has already been ticked for a four-year-old."
- **Cognitive walkthrough:** Q1 Yes, I would accept the reading level and choose an illustration style. / Q2 Yes, the clearly labelled illustration radio buttons are visible after scrolling, although the first two controls are off-screen at my current zoom. / Q3 Partly. The illustration labels match my choice well, but the Lexile labels do not plainly explain which level is best for a four-year-old.
  - [H5 sev 3] **The story field silently cut off the end of my memory** - evidence: The action result says, “typed 300 characters … but the box now only shows 200 characters; the end of what you typed was cut off: ...'aginary gallop across the Norfolk fields. It matters because'”.. Fix: Do not let typed text disappear. Provide enough room or allow 300 characters, and show a persistent character count with a clear warning before proceeding. Preserve the entire text until I explicitly remove it.
  - [H2 sev 2] **Reading-level choices use unexplained jargon** - evidence: The heading is “Reading level”, followed only by “Lexile BR–200L”, “Lexile 200L–500L”, “Lexile 500L–800L”, and “Lexile 800L+”.. Fix: Give each option a plain-English age description, such as “Age 4–6 — Lily can read independently” or “Age 6–8 — Lily and an adult can read together”, with Lexile details shown as secondary information.
  - [ACC sev 2] **Footer links are effectively invisible at this zoom** - evidence: The links labelled with faint, unreadable text lead to “/privacy.html”, “/privacy.html#terms”, and “mailto:hello@storyhearth.test”.. Fix: Use dark, high-contrast text at a readable size, and enlarge the click targets to at least 44 by 44 pixels.
  - [H6 sev 1] **The preselected reading level is not explained** - evidence: “Lexile 200L–500L” is checked without any visible explanation of why that was selected.. Fix: State plainly, for example, “Recommended for a 4-year-old, based on the age you entered”.
- **Positives:** The page heading and group labels are large and readable.; The selected radio button is visible, so I can tell that a choice has been made.; The illustration choices are described in friendly, concrete words.; There is a clear Back button and a Next button.

### Optional photo upload  (step 9)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_09.jpg)
- **Purpose:** To let the user add a photo of the child before generating the personalised book.
- **What's happening:** The form presents a photo upload area, explains that a clear photo can help the illustrations resemble the child, and offers Back or Create my book. The upload is not required.
- **First impression (Harold):** "Straightforward enough. The optional wording reassures me, and the final button is large and clearly labelled. I do not have a suitable photo to add now."
- **Cognitive walkthrough:** Q1 Yes, I would try creating the book without a photo because the form says the photo is optional. / Q2 Yes, I noticed the large "Create my book" button at the bottom of the form. / Q3 Yes, "Create my book" clearly describes the next action and matches my goal of making Lily's book.
  - [ACC sev 2] **Photo upload control has no visible label** - evidence: [30] file-upload (no label); the screen only shows the native "Choose file" and "No file chosen" text. Fix: Give the upload control an explicit label such as "Choose a photo of Lily" and provide a large, keyboard-friendly upload button.
  - [ACC sev 2] **Footer links are too faint to read** - evidence: [13], [14], and [15] are shown as faint/small text I cannot make out; the screen also shows faint copyright text. Fix: Use dark, high-contrast footer text at a readable size and ensure the links remain visible and legible at 200% zoom.
- **Positives:** The heading and explanation are large and easy to understand.; The photo is clearly marked optional, so I do not feel trapped into providing one.; The "Create my book" button is large, high-contrast, and clearly labelled.; There is a visible Back control, giving me a way to return to the previous step.

### Generated storybook preview  (step 10)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_10.jpg)
- **Purpose:** To preview the generated nine-page personalised storybook and provide options to regenerate it or order a hardcover.
- **What's happening:** The first of nine generated pages is displayed with a cover image and navigation controls. A regeneration control carries a $4.99 charge, and an Order hardcover link leads to checkout.
- **First impression (Harold):** "The book is there, so the main job was done, but the misspelt title and unexpected Pop-art style make me mistrust the result. The arrows are small and partly out of sight, which is awkward at this zoom."
- **Cognitive walkthrough:** Q1 Yes, I want to read through every page carefully. / Q2 I can see the “›” next-page arrow, but it is small and off to the side rather than plainly presenting “Read next page.” / Q3 The arrow is understandable, but the words “Next page” would match what I want much better.
  - [CONTENT sev 3] **Spelling error in the generated title** - evidence: “The Magical Adventrue of Lily”. Fix: Provide an obvious edit control for the title and run a spelling check before showing the final preview.
  - [H2 sev 3] **The generated illustration style does not match my choice** - evidence: I selected “Storybook classic — timeless ink and colour,” but the page says “Illustration style: Pop-art comic”.. Fix: Use the selected style in the generated book, or clearly explain that the requested style is unavailable and ask me to choose an alternative.
  - [ACC sev 3] **Page navigation uses tiny icon-only controls** - evidence: [6] button “‹” and [7] button “›”. Fix: Use large, clearly labelled buttons such as “Previous page” and “Next page,” with adequate spacing and strong contrast.
  - [CONTENT sev 3] **The final sentence of the story is incomplete** - evidence: “And from that day on, whenever Lily looked up at the sky, she would always remember” followed immediately by “The End”. Fix: Check the generated final paragraph and ensure every sentence ends grammatically, with a complete thought before displaying “The End.”
  - [ACC sev 3] **The page-turn buttons are too small for comfortable use** - evidence: [6] and [7] are shown as small arrow-only controls. Fix: Make the controls at least 44 by 44 pixels and label them “Previous page” and “Next page,” while keeping the arrows as supplementary symbols.
  - [H7 sev 2] **Important controls are shown below the fold** - evidence: [8] button “Regenerate entire book – $4.99” and [9] link “Order hardcover” are marked offscreen.. Fix: Place page navigation, pricing information, and the order action in a fixed or clearly visible area, while ensuring they work at 200% zoom.
- **Positives:** The site clearly shows the book title, cover, and that there are 9 pages.; The preview separates the current page number from the total page count.; The regeneration price is shown directly on the button rather than hidden until later.

### Hardcover checkout  (step 12)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_12.jpg)
- **Purpose:** Show the delivery and payment costs and collect the information needed to order a printed hardcover.
- **What's happening:** The chosen hardcover is £24.99. Premium gift wrap is already checked for £7.99, shipping and handling is £12.99, and the displayed total is £45.97. Address and payment fields appear below, along with a Pay now button.
- **First impression (Harold):** "The basic price is plain enough, but the pre-ticked gift wrap and countdown make me wary before I have even reached the delivery details."
- **Cognitive walkthrough:** Q1 Yes, I would try to remove the unwanted gift wrap and work out the true cost, but I would not proceed to payment today. / Q2 Yes, the checked “Premium gift wrap” box is clearly visible and appears easy to untick. / Q3 Mostly. The item and charges are labelled clearly, but I have to remove “Premium gift wrap” to learn the cost without an extra service.
  - [DECEPTIVE sev 3] **Gift wrap is pre-selected without being requested** - evidence: [6] checkbox "Premium gift wrap" (checked); £7.99. Fix: Make every optional extra unchecked by default and show the total again immediately before and after the box is selected.
  - [ACC sev 3] **Footer links are faint and too small to read** - evidence: [12], [13], [14] are marked “faint/small text you cannot make out”. Fix: Use dark, high-contrast text at least 16 CSS pixels before zoom, with descriptive link labels and comfortable spacing.
  - [DECEPTIVE sev 2] **Countdown creates pressure at checkout** - evidence: “Your price is reserved for 09:57”. Fix: Remove the countdown, or state plainly what happens when it expires and whether the price truly changes.
  - [VALUE sev 2] **Shipping is a substantial charge that needs clearer context** - evidence: “Shipping & handling £12.99”. Fix: Explain what the charge includes and let me confirm whether it changes after entering a delivery address.
  - [CONTENT sev 2] **The misspelled book title is carried into the purchase** - evidence: “Hardcover: The Magical Adventrue of Lily”. Fix: Allow the title to be corrected before checkout and confirm the corrected wording in the order summary.
- **Positives:** The hardcover, gift-wrap and shipping charges are shown as separate lines.; The total of £45.97 is visible without requiring a calculation.; The gift-wrap checkbox has a written label rather than an icon alone.

## Generated output assessment
*Artifact:* Nine-page generated personalised storybook preview displayed on a website

> I can see the colours and the large headings, but this is not the book I asked for. It spells my great-granddaughter's title wrongly, leaves out the horse I made, introduces a family member I never mentioned, and ends before finishing its thought. At 200% zoom I can manage most labels, but the tiny arrows and pale footer still make the site tiring to use.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 2 | The output correctly retains Lily, age four, Harold, the workshop shed, Norfolk and the name Conker, but it omits the carving, the Christmas gift, the relationship as her great-grandfather, the imaginary gallop and the k |
| coherence | 2 | There is a nominal beginning, middle and end, but the story abruptly introduces Uncle Bartholomew and dark woods. The sentence “and he followed him” is incoherent, page 8 repeats the opening, and the final sentence stops |
| age fit | 1 | The measured reading level is grade 7.6 for a requested age of four. Words such as “ephemeral”, “luminescence”, “crepuscular”, “ineffable”, “juxtaposing” and “existential trepidation” are far beyond the audience, while “ |
| language | 1 | There are major defects: “Adventrue”, “Lil”, visible template placeholders, “he followed him”, “all way home”, duplicated “The End”, an exact repeated opening and an unfinished final sentence with no punctuation. |
| text image fit | 1 | Conker is absent from every image despite being the central object. The rain page has no rain, the lantern page has no visible path, the dark-woods page is not a recognisable wood with toothed shadows, and the homecoming |
| character consistency | 2 | The same simplified blond figure is generally reused for Lily, but she has neither the supplied strawberry-blonde bob nor pink wellies and appears bald. Harold never appears despite being central, while the invented Uncl |
| visual quality | 2 | The artwork is clean enough to understand and uses large dark labels, but it is very sparse, does not follow the selected classic ink-and-colour style, repeatedly reuses the same scene, omits Conker, and includes low-con |
| emotional resonance | 1 | The book does not show Harold carving or giving Conker and never completes the final memory. Its invented frightening adventure feels generic rather than like a loving keepsake from a grandfather to his great-granddaught |

- **used correctly:** Lily's first name; Lily's age of four; The relationship category involving Grandpa Harold; Harold's name; Harold's workshop shed; The Norfolk fields; The special object's name, Conker; The fact that Conker is a hand-carved wooden rocking horse
- **missing:** The fact that Harold is Lily's great-grandfather and Grandpa; Harold carving Conker in the workshop; Harold giving Conker to Lily at Christmas; Lily riding Conker on an imaginary gallop across the Norfolk fields; Conker being a family keepsake made by hand; The love with which the object was passed down; Evidence that the selected premium gift wrap was applied
- **changed:** Lily's strawberry-blonde bob and pink wellies were replaced by a bald, plain, gender-neutral figure in ordinary dark trousers; A gentle family keepsake memory was changed into a dark adventure involving rain, woods, threatening shadows and an invented uncle; The selected Classic illustration style was replaced by a declared Pop-art comic style
- **invented:** Uncle Bartholomew; A lantern; A threatening dark wood with shadows that grow teeth; A shiny red balloon; The claim that no one would ever find Lily

### Part by part
#### Cover / Page 1
![I1](artifacts/capture_01/img_00.jpg)
> A StoryHearth original Illustration style: Pop-art comic
- *Picture:* A simple flat-colour illustration of a small blond child labelled “Lily”, standing between a workshop-like building and three trees. There is no rocking horse, no pink wellies and no bob hairstyle. The sun partly overlaps the title.
- *Reaction:* I can read the large, dark title at my zoom, but “Adventrue” is plainly wrong. I was promised a classic storybook, not this flat comic look, and the cover fails to show the very horse that matters.
  - [language, sev 4] The title says “The Magical Adventrue of Lily”; “Adventrue” should be “Adventure”.
  - [fidelity, sev 3] The cover does not show Conker and does not show Lily's stated “strawberry-blonde bob, pink wellies”.
  - [visual_quality, sev 3] The selected style was “Classic — timeless ink and colour”, but the page says “Illustration style: Pop-art comic” and uses a sparse flat graphic style.
- **Change I'd make:** Correct the title, use the selected classic ink-and-colour style, and put Lily in her strawberry-blonde bob and pink wellies beside a clearly visible wooden rocking horse named Conker.
- **Suggested rewrite:** The Magical Adventure of Conker and Lily

#### Page 2 — Dedication
![I2](artifacts/capture_03/view_00.jpg)
> For {{recipient_name}}, with love from {{sender_name}}
- *Picture:* The captured viewport shows the StoryHearth navigation bar, a mostly blank preview panel marked “2 / 9”, small arrow buttons, a regenerate button, an order button, and a very pale footer. No book illustration is visible in this capture.
- *Reaction:* The unfinished name brackets are worse than useless in a gift. I can see the large order button, but the tiny arrow controls and almost invisible footer text would be troublesome with my eyesight.
  - [language, sev 4] The dedication still contains the template markers “{{recipient_name}}” and “{{sender_name}}”.
  - [fidelity, sev 3] The supplied names Lily and Grandpa Harold were available but were not inserted into the dedication.
  - [visual_quality, sev 3] The page-number arrows are small, the footer text “Privacy Terms Contact © 2026 StoryHearth Ltd.” is extremely pale, and the captured book panel is blank.
- **Change I'd make:** Replace the template markers with the supplied names and show a clear, unclipped book page. Enlarge and label the navigation controls and increase footer contrast.
- **Suggested rewrite:** For Lily, with love from Grandpa Harold

#### Page 3
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in Harold's workshop shed and the Norfolk fields, there lived a curious child named Lily. Lily was 4 years old and loved nothing more than Conker, the hand-carved wooden rocking horse.
- *Picture:* The same basic child stands outside the small building near trees and a sun. The image repeats the cover scene and does not show Harold, woodworking tools, Norfolk fields, Conker, Lily's bob or her wellies.
- *Reaction:* This names Lily, Harold's shed, Norfolk and Conker, but it merely says the horse exists instead of showing our family making and giving it. The picture does not show the special object at all.
  - [fidelity, sev 3] The key supplied events—Grandpa Harold carving Conker, giving him to Lily at Christmas, and Lily's later imaginary gallop—are absent.
  - [text_image_fit, sev 3] The text centres on Conker in “Harold's workshop shed and the Norfolk fields”, while the picture shows neither Conker nor Harold nor clear fields.
  - [coherence, sev 2] “in Harold's workshop shed and the Norfolk fields, there lived a curious child” treats two locations as if they were one combined home.
- **Change I'd make:** Begin with the Christmas presentation of Conker, show the carving in the shed, and use clear pictures of Harold, Lily and the wooden horse.
- **Suggested rewrite:** On Christmas morning, Grandpa Harold gave Lily a surprise. It was Conker, a little wooden rocking horse he had carved by hand.

#### Page 4
![I4](artifacts/capture_05/img_00.jpg)
> One evening Lily gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* Lily stands front-facing under a purple evening sky with stars. She is not visibly looking upward, and Conker is absent.
- *Reaction:* I have spent fifty years using plain words, and I would not read that sentence aloud to a four-year-old. It sounds like a college lesson, not a bedtime story about my great-granddaughter.
  - [age_fit, sev 4] The measured prose is at Flesch-Kincaid grade 7.6 for a requested reading age of four, and this sentence uses “ephemeral”, “luminescence”, “crepuscular”, “engendered”, “melancholy”, “juxtaposing”, “ineffable” and “existential trepidation”.
  - [emotional_resonance, sev 3] “engendered an inexplicable melancholy” and “existential trepidation” introduce sombre abstract emotions unrelated to Harold carving a beloved keepsake.
  - [text_image_fit, sev 2] The text says Lily “gazed upward”, but the image shows her face and eyes looking straight ahead.
  - [text_image_fit, sev 3] Conker is central to the story but is missing from the picture.
- **Change I'd make:** Replace the sentence with simple language about Lily seeing the evening sky and the stars, and show her actually looking up while holding Conker.
- **Suggested rewrite:** The sun went down, and the first stars appeared. Lily looked up at the dark blue sky.

#### Page 5
![I5](artifacts/capture_06/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Lil pulled up her hood and ran for shelter, holding Conker, the hand-carved wooden rocking horse tight.
- *Picture:* A bright sunny daytime scene is repeated, with Lily standing still. There is no rain, puddle, hood, running movement or Conker.
- *Reaction:* This page says several things that the picture plainly does not show. I noticed the missing rain immediately, and “Lil” is another name error that would be spotted by Lily herself.
  - [language, sev 4] Lily's name is misspelled as “Lil”.
  - [language, sev 2] “holding Conker, the hand-carved wooden rocking horse tight” awkwardly places “tight” after the long object phrase instead of saying “holding Conker tightly”.
  - [text_image_fit, sev 4] The text says rain, puddles, a hood and running, while the image shows sun, no rain and a stationary child.
  - [character_consistency, sev 2] Lily is described as pulling up a hood, but no hood is shown.
- **Change I'd make:** Use Lily's full name, make the sentence natural, and either illustrate the rain and shelter or remove the rain from the story. Show Conker clearly in Lily's arms.
- **Suggested rewrite:** Then the rain began to fall. Lily held Conker tightly as she ran back to the workshop.

#### Page 6
![I6](artifacts/capture_07/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Lily, follow me!" he called, and he followed him along the winding path.
- *Picture:* An adult man labelled “Uncle Bartholomew” stands with a small yellow rectangle resembling a lantern beside Lily. The same workshop, trees and child are shown, with no winding path and no Conker.
- *Reaction:* I never mentioned an Uncle Bartholomew, and suddenly he has walked into our family story. The sentence also says Lily called “follow me” and then that “he followed him”, which makes no sense.
  - [fidelity, sev 4] “Uncle Bartholomew” and his lantern are invented and replace the supplied central relationship with Grandpa Harold.
  - [coherence, sev 4] “Lily, follow me!” is followed by “and he followed him”, with two uses of “he” and no clear subject.
  - [text_image_fit, sev 3] The text describes a winding path, but the image contains no path; Conker is also missing.
  - [character_consistency, sev 4] Uncle Bartholomew appears abruptly in the text and picture despite never being established or supplied.
- **Change I'd make:** Remove the invented uncle and put Grandpa Harold in this page, showing him taking Lily and Conker along a clear path.
- **Suggested rewrite:** Grandpa Harold came along with his lantern. “Come with me, Lily,” he said, and together they followed the path across the fields.

#### Page 7
![I7](artifacts/capture_08/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Lily again. Lily clutched a shiny red balloon and trembled in the dark.
- *Picture:* Lily stands under a crescent moon beside a red balloon and a few trees. The scene is dark, but it is not recognisably a wood, there are no toothed shadows, and Conker is absent.
- *Reaction:* This is the wrong story for a four-year-old to hear before bed, with shadows growing teeth and the claim that nobody will find her. The red balloon appears in the picture but has no explained place in our memory.
  - [age_fit, sev 4] “the shadows grew teeth and whispered that no one would ever find Lily again” introduces loss anxiety and a frightening threat to a four-year-old.
  - [fidelity, sev 3] The deep dark wood, threatening shadows and shiny red balloon are invented and disconnected from the supplied family keepsake memory.
  - [text_image_fit, sev 3] The picture shows an open grassy area with only three trees rather than “deep in the woods”, and it does not show teeth or whispering shadows.
  - [emotional_resonance, sev 3] Lily is trembling and apparently lost, replacing the warmth of a handmade present passed down with love.
- **Change I'd make:** Remove the frightening episode and the unexplained balloon. Show Lily safely riding Conker through the Norfolk fields with Grandpa Harold.
- **Suggested rewrite:** Lily climbed onto Conker and pretended they were galloping across the Norfolk fields. Grandpa Harold walked beside her and laughed as she raced over the grass.

#### Page 8
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in Harold's workshop shed and the Norfolk fields, there lived a curious child named Lily. At last the sun came out, and Lily skipped all way home, happier than ever.
- *Picture:* The basic sunny cover image returns. Lily is standing rather than skipping, no home or route is shown, and neither Conker nor Harold is present.
- *Reaction:* This is almost the cover copied into the ending, and it starts again as though a new tale has begun. The words also say “all way home”, which is another simple but visible error.
  - [coherence, sev 3] The opening sentence on page 3 is repeated exactly on page 8: “Once upon a time, in Harold's workshop shed and the Norfolk fields, there lived a curious child named Lily.”
  - [language, sev 2] “skipped all way home” is missing the word “the” and should be “skipped all the way home”.
  - [text_image_fit, sev 3] The text says Lily skipped home, but the image shows her standing still in the same generic daytime setting; no destination, Conker or Harold is shown.
  - [visual_quality, sev 3] The picture is essentially a repeat of the cover rather than a new illustration for the resolution.
- **Change I'd make:** Remove the repeated opening, correct the grammar, and make a genuinely new return-home picture showing Lily, Conker and Grandpa Harold together.
- **Suggested rewrite:** When the sun came out, Lily rode Conker back to the workshop. She laughed because the gallop across the fields had been every bit as wonderful as she had imagined.

#### Page 9
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Lily looked up at the sky, she would always remember The End
- *Picture:* An orange-sky version of the generic building, child and trees appears with “The End” printed above. Conker, Harold, the workshop activity and the family memory are absent.
- *Reaction:* The last thought stops in the middle, so the book ends before telling me what Lily would remember. Printing “The End” twice makes it look unfinished rather than special.
  - [language, sev 4] The sentence “she would always remember” has no object and ends without punctuation.
  - [language, sev 3] “The End” appears twice on the same page.
  - [emotional_resonance, sev 4] The incomplete final thought never says that Lily will remember Grandpa Harold carving Conker for her and the love behind the keepsake.
  - [text_image_fit, sev 3] The closing memory concerns looking at the sky, but the picture contains no visible sky detail and none of the people or objects needed to carry the family memory.
- **Change I'd make:** Complete the final thought with one reference to Harold, the carving and Conker, print “The End” only once, and show Lily keeping the horse as a family keepsake.
- **Suggested rewrite:** And Lily always remembered the day Grandpa Harold gave her Conker. The little wooden horse was not just a toy. It was a present made by hand and filled with love.  The End

**Top changes to the output:** 1. Rewrite the entire story as a short, simple first-person or direct family memory centred on Harold carving Conker, giving it to Lily at Christmas, and their imaginary gallop across Norfolk. | 2. Remove Uncle Bartholomew, the threatening woods, the toothed shadows, the unexplained balloon and the possible-loss language. | 3. Correct “Adventrue”, “Lil” and “all way home”; replace both name placeholders; complete the final sentence; remove repeated text and the duplicated “The End”. | 4. Redraw Lily with her strawberry-blonde bob and pink wellies, and show Harold and Conker consistently on every page where they belong. | 5. Use the requested classic ink-and-colour style rather than the stated Pop-art comic style, with distinctive pictures rather than repeated generic scenes. | 6. Ensure the preview uses high-contrast text, large labelled controls and no tiny icon-only page arrows so the book can be checked comfortably at 200% zoom.

## Recommendations (participant's priorities)
- **[high] Rewrite the story as a short, simple memory about Harold carving Conker, giving it to Lily at Christmas and taking her on an imaginary gallop across the Norfolk fields.** (Generated storybook preview) - The story must sound like my family memory and be suitable for a four-year-old, not a frightening generic adventure full of grandadventure words.
- **[high] Correct “Adventrue”, “Lil”, “all way home” and every other visible spelling or template error, complete the final sentence and remove repeated text and the duplicated “The End”.** (Generated storybook preview) - A keepsake with obvious mistakes would be embarrassing to hand to Lily and would make me doubt the whole book.
- **[high] Redraw Lily with her strawberry-blonde bob and pink wellies, and show Harold and Conker consistently in the relevant pictures.** (Generated storybook preview) - The people and the hand-carved horse are the heart of the story. Conker being absent from the pictures makes the book miss its purpose.
- **[high] Use the requested classic ink-and-colour storybook style instead of changing it to Pop-art comic, and check that each picture matches the words on its page.** (Choose the look & feel / Generated storybook preview) - I selected a particular style, and I need to know the finished book looks like the one I ordered.
- **[high] Replace tiny icon-only page arrows and other small controls with large, clearly labelled buttons such as “Previous page” and “Next page”.** (Generated storybook preview) - At 200% zoom the arrows were hard to see and difficult to hit. I should be able to inspect all nine pages independently.
- **[high] Make all text and important instructions high contrast, especially the home page explanation, form examples and footer links.** (Home page / Create your book / all pages) - Pale grey writing is effectively invisible to me and turns ordinary reading into a struggle.
- **[high] Remove the countdown and do not preselect paid gift wrap or any other extra that I did not request.** (Hardcover checkout) - A countdown makes a straightforward purchase feel hurried, and the unexpected £7.99 made me suspicious of the total.
- **[medium] Explain the reading-level choices in plain English and state why a level was selected for a four-year-old.** (Choose the look & feel) - “Lexile 200L–500L” is workshop jargon to me, and I should understand an important choice before I make it.
- **[medium] Explain the dashboard error and profile-sync problem, with a clear way to recover without making me think I have done something wrong.** (My books) - The unexplained error worried me and made the account seem unreliable.
- **[medium] Keep important fields and the Next button visible where possible, with proper visible labels for login fields and the photo upload.** (Log in / Create your book / Optional photo upload) - I should not have to hunt for the next action or guess what an empty box means, especially at high zoom.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This is for making a personalised storybook featuring a child and the people and memories that matter to them. It is especially for parents or relatives who want to keep a story for a child.
- **What was the most frustrating or confusing moment, and why?** The finished book was the worst moment. The title was misspelt, the pictures were in the wrong style, Conker was missing and the story ended in the middle of a sentence. I could not give that to Lily as a proper keepsake.
- **What was the best moment?** The best moment was entering the memory in my own words and choosing the classic storybook pictures. The steps felt reassuringly simple once the questions were clear.
- **Was there any point where, in real life, you would have given up? Where and why?** I would probably have given up when the book came out with the wrong title, wrong style, missing Conker and an unfinished ending. At 200% zoom, the tiny page arrows would also have made me stop if I could not read or hit them.
- **What did you expect to find or be able to do that wasn't there?** I expected a simple story about me carving Conker, giving it to Lily at Christmas and riding it with her across the Norfolk fields. I also expected to edit the story, see every page comfortably, and check that the pictures and words matched before paying.
- **Did you trust this website with your information (and your family's)? Why or why not?** I would be careful about entering family information until I knew the site would keep it safe and use it properly. I was particularly wary of the preselected £7.99 gift wrap and the countdown pressuring me at checkout.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would pay about £10 for a proper digital storybook if it were correct, and perhaps £15 to £20 for a nicely printed copy. I would pay more only after seeing the corrected title, complete story, correct pictures and clear total price with no surprise extras.
- **If the site produced something for you, how do you feel about it overall?** I was disappointed and frustrated. It was not the loving book I wanted for Lily, and I would not trust it as a keepsake without a great deal of checking and correcting.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | This sounds very relevant, and the three steps are easy to understand. But that first explanatory paragraph is full of “multimodal generative narrative engine” and “lived-experience corpus”—that’s workshop language nobod | click |
| 2 | Log in – StoryHearth | reassured (1) | Well, this looks straightforward enough. I can see the email box, password box and a big Log in button, though the boxes rely on pale placeholder writing rather than proper labels. I have my account details, so I'll fill | type; type; click |
| 3 | My books – StoryHearth | confused (0) | I can see the large orange “Create a new book” button clearly enough, which is the right next step. The error message worries me, though—I’m not sure whether my account is properly set up, but the page still lets me carr | click |
| 4 | Create your book – StoryHearth | reassured (1) | This is a plain form and I can manage it, measure it like timber first. I know Lily is four and she/her, so I'll fill in what I know before going farther down the page. | type; select; select; scroll |
| 5 | Create your book – StoryHearth | reassured (1) | Right, I can manage these last pieces. Lily has a strawberry-blonde bob and wears pink wellies; Grandpa Harold is the other person, and Grandparent is already the right relationship. I’ll fill in what I know and move on. | type; type; select; click |
| 6 | Create your book – StoryHearth | reassured (2) | This asks sensible questions, and I know the answers. The place is my workshop shed and the Norfolk fields, the special object is Conker, and I can give the whole Christmas memory in my own words. | type; type; type; click |
| 7 | Create your book – StoryHearth | reassured (1) | Well, it has saved my story and brought me to the look-and-feel choices. “Lexile 200L–500L” sounds like workshop jargon to me, but since Lily is only four, the site seems to have made that choice for her; the watercolour | click; scroll |
| 8 | Create your book – StoryHearth | reassured (2) | That’s the style I want—proper storybook pictures rather than crayon scribbles. The selected dot is clear, and the Next button is large enough that I won’t have to chase a tiny target. | click |
| 9 | Create your book – StoryHearth | reassured (1) | This is the last bit before making the book. I do not have a suitable photo of Lily ready, and the word "optional" tells me I can leave it blank. The big button is easy to see, so I will click it. | click; wait_for_change |
| 10 | Your storybook – StoryHearth | frustrated (-1) | The book has been made, but I’m not happy with the title: “Adventrue” is misspelt. The cover also says “Pop-art comic,” although I chose “Storybook classic,” so something has gone wrong. I need to read all nine pages bef | flip_through |
| 11 | Your storybook – StoryHearth | frustrated (-1) | I’ve now looked through all nine pages, and this last sentence feels unfinished—as though I’ve reached the end of a plank before it’s been joined properly. I won’t pay the $4.99 to regenerate it, but I will use “Order ha | click |
| 12 | Checkout – StoryHearth | suspicious (-1) | There it is, but I’m suspicious of that gift wrap being already ticked. That is £7.99 I never asked for, and the countdown is making a nuisance of a plain purchase. I’ll untick the gift wrap and look down the page carefu | click; scroll; read_page |
| 13 | Checkout – StoryHearth | reassured (1) | Good, unticking “Premium gift wrap” brought the total down to £37.98, and the page showed that change clearly. That tells me the real cost of one hardcover with delivery is £37.98, excluding gift wrap. I have found out w | done |
