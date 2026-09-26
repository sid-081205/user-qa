# UserQA report: Priya Nair on http://127.0.0.1:8765/

*Persona:* **Priya Nair** (36) - Shift-working nurse and mum of two who does everything on her phone in stolen minutes.  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 12 steps | *Pages reviewed:* 9 | *Issues:* 29 | *LLM calls:* 15 | *Wall time:* 349.4 s

## What the agent understood the website to be
- **what it is:** A website that generates illustrated personalised family storybooks.
- **who it is for:** Families wanting a custom story featuring their children and other loved ones.
- **value proposition:** Turns a family memory into a fully illustrated book preview, with printed hardcovers available.
- **pricing model:** A free digital preview is advertised; the actual hardcover price is not yet shown.
- **fit for me:** Very relevant for a personalised fifth-birthday present for Aarav, provided creation is quick and the delivered hardcover price is clear.
- **main tasks:** Log in, Add family characters and a shared memory, Generate and read the storybook preview, Check the price of a printed hardcover

## Scores
- SUS: **52.5** (grade D; 68 = industry average)
- UEQ-S: pragmatic -0.25, hedonic 0.25 (range -3..+3)
- Likelihood to recommend (0-10): 2
- Output keepsake-worthiness (1-5): 1
- Verdict: *"Quick to start, but the wrong story, broken output and sneaky checkout extras mean I would not pay or recommend it."*

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 3 | CONTENT | Generated storybook preview, Hardcover checkout (x2) | Generated title contains a spelling error | The heading and cover say “The Magical Adventrue of Aarav.” | Correct the title to “Adventure” and provide an edit control before ordering. |
| 3 | H9 | My books dashboard | Raw technical sync error | “Error 0x80070057: profile sync incomplete.” | Replace the error code with plain language such as “Some saved profile details couldn’t be loaded. You can still create a book, or retry your profile.” Include a clear Retry option if action is needed |
| 3 | H2 | Generated storybook preview | Generated style does not match my selected style | I selected “Watercolour,” but the page says “Illustration style: Pop-art comic”. | Apply the selected Watercolour style and show a confirmation beside the style, such as “Watercolour selected.” |
| 3 | VALUE | Generated storybook preview | Regeneration fee uses unexplained dollar pricing | “Regenerate entire book – $4.99” | Show the fee in GBP, clarify that it is one-off, and ask for confirmation before charging. |
| 3 | DECEPTIVE | Hardcover checkout | Premium gift wrap is pre-selected | [6] checkbox "Premium gift wrap" (checked), £7.99 | Make optional extras unchecked by default, show the resulting total immediately, and require an explicit choice. |
| 2 | ACC | Login form, My books dashboard, Story details form (x3) | Footer text has very low contrast | The pale footer links “Privacy”, “Terms”, and “Contact” sit on a very light background. | Use a darker text colour with at least WCAG AA contrast against the footer background. |
| 2 | H8 | Story details form, My books dashboard (x2) | Desktop navigation breaks into awkward fragments | The header visibly shows “How it works,” “StoryHearth,” “Pricing,” “My books,” and “Log out” squeezed across multiple lines, with “How it works” wrapping into “ | Use a compact menu button on small screens, or prevent navigation labels from wrapping and keep the logo and menu in separate rows. |
| 2 | CONTENT | StoryHearth homepage | Corporate jargon in the main description | Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus. | Replace it with a short plain-English line such as 'Turn a family memory into a one-of-a-kind illustrated storybook starring your child.' |
| 2 | ACC | StoryHearth homepage | Hero image lacks a useful description | [image (no description) 342x440] | Add concise alt text describing the book or family-story product shown. |
| 2 | VALUE | StoryHearth homepage | Printed-book price is not visible on the homepage | Only 'See pricing' and 'Free digital preview · Printed hardcovers shipped across the UK' are shown. | Show a clear starting price for a hardcover, and clarify whether delivery is included. |
| 2 | ACC | Login form | Login fields have placeholder-only labels | [5] textbox (no label) placeholder "Email" and [6] textbox (no label) placeholder "Password" | Give both textboxes persistent visible labels and programmatic label associations rather than relying only on placeholders. |
| 2 | H5 | Create your book – characters | Relationship defaults to Grandparent | Control [11] displays “Grandparent” even though control [10], “Who else is in the story?”, is empty. | Default the Relationship dropdown to “Select relationship” or leave it blank, and require an explicit choice before continuing. |
| 2 | H5 | Create your book – characters | The companion character only asks for a name and relationship | “Who else is in the story?” has only a textbox and “Relationship”; there are no fields for Meera’s appearance, age or pronouns. | Add optional fields for the companion’s age, pronouns and appearance, or explain on the next step that they can be included later. |
| 2 | H2 | Choose the look & feel | Reading-level options use unfamiliar jargon | "Lexile BR–200L" and "Lexile 200L–500L" | Add a plain-English description such as “Easiest — ages 4–6” and “Easy — ages 6–8,” while retaining the Lexile range as secondary information. |
| 2 | H3 | Generated storybook preview | No visible edit or save control for the generated book | The only visible book controls are “‹,” “›,” “Regenerate entire book – $4.99,” and “Order hardcover.” | Add clear “Edit details,” “Edit page,” and “Save” controls, and explain whether edits are free. |

## Page-by-page
### StoryHearth homepage  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Explain the personalised storybook service and let visitors begin creation, view prices, or log in.
- **What's happening:** The homepage is open on a phone-sized screen. It contains a large hero message, two prominent action buttons, pricing and login links, a three-step summary, testimonials, and footer information.
- **First impression (Priya):** "The offer sounds lovely, and 'Proceed' is obvious. The first paragraph is jargon-heavy and takes up a lot of space, while the top links are squeezed awkwardly on my phone."
- **Cognitive walkthrough:** Q1 Yes, I want to log in and start making Aarav's book. / Q2 Yes, the 'Log in' button at the top is visible. / Q3 Yes, 'Log in' clearly means signing into my account.
  - [CONTENT sev 2] **Corporate jargon in the main description** - evidence: Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.. Fix: Replace it with a short plain-English line such as 'Turn a family memory into a one-of-a-kind illustrated storybook starring your child.'
  - [ACC sev 2] **Hero image lacks a useful description** - evidence: [image (no description) 342x440]. Fix: Add concise alt text describing the book or family-story product shown.
  - [VALUE sev 2] **Printed-book price is not visible on the homepage** - evidence: Only 'See pricing' and 'Free digital preview · Printed hardcovers shipped across the UK' are shown.. Fix: Show a clear starting price for a hardcover, and clarify whether delivery is included.
  - [H8 sev 1] **Top navigation is cramped on mobile** - evidence: 'How it works' wraps onto two lines and crowds the StoryHearth, Pricing, and Log in controls.. Fix: Use a compact mobile menu with adequately sized tap targets, or shorten the link to 'How it works' in a single line.
- **Positives:** The orange 'Proceed' button is highly visible.; The three-step process makes the basic service understandable.; The free digital preview makes trying the service feel low risk.

### Login form  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** Allow an existing customer to access their StoryHearth account.
- **What's happening:** The page asks for an email address and password, then offers a large “Log in” button. It also provides links to account registration, privacy, terms, and contact.
- **First impression (Priya):** "Simple and recognisable. The big button is easy to use with one thumb, although the fields have no permanent visible labels."
- **Cognitive walkthrough:** Q1 Yes, I would enter my account details now. / Q2 Yes, the two input boxes and the large orange “Log in” button are immediately visible. / Q3 Yes. The placeholders “Email” and “Password” and the button “Log in” match what I want to do, though the textbox controls themselves technically have no labels.
  - [ACC sev 2] **Login fields have placeholder-only labels** - evidence: [5] textbox (no label) placeholder "Email" and [6] textbox (no label) placeholder "Password". Fix: Give both textboxes persistent visible labels and programmatic label associations rather than relying only on placeholders.
  - [ACC sev 2] **Footer text has very low contrast** - evidence: The pale footer links “Privacy”, “Terms”, and “Contact” sit on a very light background.. Fix: Use a darker text colour with at least WCAG AA contrast against the footer background.
  - [H8 sev 1] **Navigation wraps awkwardly on the narrow phone screen** - evidence: The screenshot shows “How it works” split over two lines around the StoryHearth heading.. Fix: Use a compact mobile header with a menu icon, or keep navigation labels on one line without wrapping.
- **Positives:** The orange “Log in” button is prominent and easy to tap.; The form is short, with only two fields.; The page clearly says “Welcome back” and explains that I am logging in.; Privacy, terms, and contact links are available.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** Show the books attached to my account and provide a way to create another one.
- **What's happening:** After a successful login, the dashboard greets me, says that I have no books yet, and displays a warning that profile synchronisation is incomplete. The main available action is “+ Create a new book.”
- **First impression (Priya):** "The big orange button is easy to spot and the page is mostly uncluttered, but that raw error message makes me wonder whether the book will miss my family details."
- **Cognitive walkthrough:** Q1 Yes. I want to start the birthday book now, and the large orange button appears to be the main action. / Q2 Yes. “+ Create a new book” is immediately visible below the message that I have no books yet. / Q3 Yes. It clearly says I can create a new book, which is exactly what I need.
  - [H9 sev 3] **Raw technical sync error** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the error code with plain language such as “Some saved profile details couldn’t be loaded. You can still create a book, or retry your profile.” Include a clear Retry option if action is needed.
  - [ACC sev 2] **Footer text has very low contrast** - evidence: “Privacy,” “Terms,” “Contact,” and “© 2026 StoryHearth Ltd.” appear extremely faint.. Fix: Darken the footer text to meet WCAG contrast requirements and keep visible links distinguishable from non-link copyright text.
  - [H8 sev 1] **Navigation wraps awkwardly on a phone** - evidence: The header labels wrap into “How it works,” “My books,” and separate “Log out” lines.. Fix: Use a compact mobile header with a menu icon, or shorten the labels and lay them out in a clean single row with adequate spacing.
- **Positives:** The successful login is confirmed by “Welcome back, Demo.”; The empty state clearly says, “You have no books yet.”; The large orange “+ Create a new book” button makes the next step obvious.

### Create your book – characters  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Collect basic details about the child who will star in the story and another character in it.
- **What's happening:** The form is ready for character details. The child's name and appearance boxes are empty, the age and pronouns still say Select…, and the other-character relationship defaults to Grandparent despite nobody having entered a name.
- **First impression (Priya):** "It looks straightforward on my phone and I can see everything I need without reading much. The default “Grandparent” is a bit odd, but easy to spot and change."
- **Cognitive walkthrough:** Q1 Yes, I would fill this in now because it is directly on the way to creating Aarav's birthday book. / Q2 Yes, the labelled name, age and pronoun fields, followed by the second-character name and relationship field, are prominent and easy to notice. / Q3 Yes. “Who's the star of the story?” and “Who else is in the story?” clearly match what I want; the single “Relationship” label is less explicit but still understandable in context.
  - [H5 sev 2] **Relationship defaults to Grandparent** - evidence: Control [11] displays “Grandparent” even though control [10], “Who else is in the story?”, is empty.. Fix: Default the Relationship dropdown to “Select relationship” or leave it blank, and require an explicit choice before continuing.
  - [H5 sev 2] **The companion character only asks for a name and relationship** - evidence: “Who else is in the story?” has only a textbox and “Relationship”; there are no fields for Meera’s appearance, age or pronouns.. Fix: Add optional fields for the companion’s age, pronouns and appearance, or explain on the next step that they can be included later.
  - [H2 sev 1] **Second-character relationship is not clearly scoped** - evidence: The standalone label “Relationship” appears directly below “Who else is in the story?”.. Fix: Rename the label to “Relationship to [child]” or show it as a grouped question once the second character's name is entered.
- **Positives:** The main purpose is obvious from the heading “Who's the star of the story?”.; The fields are large enough to tap comfortably on a phone.; Optional appearance details are clearly marked optional.; The form avoids requesting a long block of information at this step.

### Story details form  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** Collect the setting, meaningful object, and central family memory that the personalised book should include.
- **What's happening:** The form has three empty fields labelled for where the story happens, a special object, and the memory or idea behind the story. Back and Next controls are visible.
- **First impression (Priya):** "Straightforward and much better than a long form. I can do this quickly on my phone."
- **Cognitive walkthrough:** Q1 Yes, this is exactly the information I came here to add. / Q2 Yes, the three large text boxes are immediately visible. / Q3 Yes. 'Tell us the memory or idea behind your story' clearly matches what I want to write.
  - [H8 sev 2] **Desktop navigation breaks into awkward fragments** - evidence: The header visibly shows “How it works,” “StoryHearth,” “Pricing,” “My books,” and “Log out” squeezed across multiple lines, with “How it works” wrapping into “How it works.”. Fix: Use a compact menu button on small screens, or prevent navigation labels from wrapping and keep the logo and menu in separate rows.
  - [ACC sev 2] **Footer links have very low contrast** - evidence: “Privacy,” “Terms,” and “Contact” are extremely pale against the footer background.. Fix: Use a darker, WCAG-compliant text colour and maintain at least a 4.5:1 contrast ratio.
- **Positives:** There are only three relevant fields, so this suits my limited time.; Field labels and placeholders are specific and easy to scan.; Back and Next buttons are large and visually distinct.; The previous character details appear to have been accepted because the flow advanced to this step.

### Choose the look & feel  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Choose the reading difficulty and visual style used to generate the personalised storybook.
- **What's happening:** I can select one reading level and one illustration style. The current selections are Lexile 200L–500L and “Watercolour — soft and dreamy,” with a large Next button.
- **First impression (Priya):** "It looks neat and easy to scan, and the large choices work well on my phone. I’m not going to stop over the style, but “Lexile” is a bit technical for me."
- **Cognitive walkthrough:** Q1 Yes, I want Aarav’s book to suit a five-year-old and I’m ready to choose the easiest reading level. / Q2 Yes, the four reading-level radio buttons and three illustration-style buttons are immediately visible. / Q3 Partly. The illustration labels clearly match what I want, but “Lexile BR–200L” does not plainly tell me that this is easiest or best for a five-year-old.
  - [H2 sev 2] **Reading-level options use unfamiliar jargon** - evidence: "Lexile BR–200L" and "Lexile 200L–500L". Fix: Add a plain-English description such as “Easiest — ages 4–6” and “Easy — ages 6–8,” while retaining the Lexile range as secondary information.
- **Positives:** The two decisions are clearly separated.; Large radio controls are easy to tap with one thumb.; The selected state is visible.; Watercolour is already selected, so there is no need to make another decision.

### Optional photo upload  (step 8)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_08.jpg)
- **Purpose:** Allow the customer to add a child’s photo before generating the personalised storybook.
- **What's happening:** This is the last step before generation. A photo can be uploaded, or the customer can continue without one using “Create my book.”
- **First impression (Priya):** "Simple and quick. I can easily skip the photo, though the navigation is squashed and the upload control itself looks like an old desktop-style file picker."
- **Cognitive walkthrough:** Q1 Yes, I would try creating the book now because I have entered all the story details. / Q2 Yes, the large teal “Create my book” button stands out immediately. / Q3 Yes, “Create my book” clearly says that it will generate the birthday book.
  - [H8 sev 1] **Navigation is cramped on a phone** - evidence: The top links “How it works,” “Pricing,” “My books,” and “Log out” wrap into an uneven multi-line layout.. Fix: Use a compact mobile header with a menu button, or shorten and align the links on one row.
  - [ACC sev 1] **Upload control is visually dated and lacks a nearby field label** - evidence: [30] is shown as “Choose file” and “No file chosen,” with no separate visible label attached to the control.. Fix: Use a large, labelled mobile upload button and add accessible file-state and validation text.
- **Positives:** The heading clearly says “Add a photo (optional),” so I know I can continue without one.; The “Create my book” button is large, prominent, and clearly labelled.; A Back button is available, giving me some control before generating the book.

### Generated storybook preview  (step 9)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_09.jpg)
- **Purpose:** Preview the complete generated picture book and choose whether to regenerate it or order a printed hardcover.
- **What's happening:** A nine-page book titled “The Magical Adventrue of Aarav” has been generated. Page 1 is displayed with next-page, regeneration, and hardcover-order controls.
- **First impression (Priya):** "The cover is bright and simple enough for Aarav, but the title has an obvious typo and the style is “Pop-art comic” when I selected Watercolour, which makes me doubt the rest of the book."
- **Cognitive walkthrough:** Q1 Yes, I want to read all nine pages because this is meant to be Aarav’s birthday present. / Q2 Yes, the right-arrow button and “1 / 9” make the page navigation obvious. / Q3 The arrow is understandable, though a clearer “Next page” label would be better on a phone.
  - [H2 sev 3] **Generated style does not match my selected style** - evidence: I selected “Watercolour,” but the page says “Illustration style: Pop-art comic”.. Fix: Apply the selected Watercolour style and show a confirmation beside the style, such as “Watercolour selected.”
  - [CONTENT sev 3] **Generated title contains a spelling error** - evidence: The heading and cover say “The Magical Adventrue of Aarav.”. Fix: Correct the title to “Adventure” and provide an edit control before ordering.
  - [VALUE sev 3] **Regeneration fee uses unexplained dollar pricing** - evidence: “Regenerate entire book – $4.99”. Fix: Show the fee in GBP, clarify that it is one-off, and ask for confirmation before charging.
  - [H3 sev 2] **No visible edit or save control for the generated book** - evidence: The only visible book controls are “‹,” “›,” “Regenerate entire book – $4.99,” and “Order hardcover.”. Fix: Add clear “Edit details,” “Edit page,” and “Save” controls, and explain whether edits are free.
  - [ACC sev 2] **Small page-navigation buttons on a phone** - evidence: The controls shown as [6] and [7] are compact arrow buttons beneath the book.. Fix: Use at least 44 by 44 pixel targets and label them “Previous page” and “Next page.”
- **Positives:** The “1 / 9” counter makes the preview length clear.; The next-page arrow is visible without hunting through the page.; The cover is colourful, simple, and suitable-looking for a young child.

### Hardcover checkout  (step 11)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_11.jpg)
- **Purpose:** Show the complete hardcover cost and collect delivery and payment information.
- **What's happening:** The generated book is selected as a £24.99 hardcover. Premium gift wrap is pre-selected for £7.99, shipping and handling is £12.99, and the resulting total is £45.97. A price-reservation countdown is active, and empty delivery and card fields lead toward payment.
- **First impression (Priya):** "I can finally see the real total, but £45.97 feels steep and the pre-ticked £7.99 gift wrap immediately makes me wary. The narrow layout also makes the header wrap awkwardly."
- **Cognitive walkthrough:** Q1 Yes, I would uncheck the gift wrap to establish the price I actually want, but I would not proceed to payment yet. / Q2 Yes, the checked “Premium gift wrap” box is very noticeable directly beneath the book price. / Q3 The label and separate £7.99 price are clear, but it should not have been selected by default.
  - [DECEPTIVE sev 3] **Premium gift wrap is pre-selected** - evidence: [6] checkbox "Premium gift wrap" (checked), £7.99. Fix: Make optional extras unchecked by default, show the resulting total immediately, and require an explicit choice.
  - [DECEPTIVE sev 2] **Artificial reservation countdown adds pressure** - evidence: “Your price is reserved for 09:57”. Fix: Remove the countdown unless there is a genuine, documented reservation policy, and explain precisely what expires.
  - [ACC sev 2] **Navigation is cramped on mobile** - evidence: The header visibly wraps “How it works,” “Pricing,” “My books,” and “Log out” across multiple uneven lines.. Fix: Use a compact mobile navigation menu or stack the links into clean full-width rows with adequately sized tap targets.
  - [VALUE sev 2] **Delivery charge is not explained before checkout** - evidence: “Shipping & handling £12.99” with no destination, timing, or service explanation nearby.. Fix: Label the service and estimated delivery time, and make clear whether the charge varies by destination.
  - [VALUE sev 2] **Unchecked gift wrap still shows a £7.99 charge** - evidence: The checkbox for "Premium gift wrap" is unchecked, but the line still displays "£7.99".. Fix: Show the gift-wrap line as £0.00 when unchecked, or remove the charge line and clearly state that it is not included.
  - [CONTENT sev 1] **The hardcover title contains a spelling error** - evidence: The checkout heading says "Hardcover: The Magical Adventrue of Aarav".. Fix: Allow the title to be edited before checkout and correct the spelling before presenting the order summary.
- **Positives:** The full total is displayed before payment.; The hardcover price and each charge are shown as separate amounts.; The gift-wrap price is visible beside its checkbox, so the added cost is not hidden once I notice it.

## Generated output assessment
*Artifact:* A nine-page personalised digital children's storybook preview with an ordering page for a hardcover edition

> I can see that it used Aarav's name, our park and Rory, but it has missed the actual present I wanted: a five-year-old hero teaching his little sister Meera to find cloud shapes on his birthday. I would not keep this version with the spelling error, raw placeholders, wrong pronouns, repeated scenes, adult vocabulary, invented uncle and Meera completely missing.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | The output correctly uses Aarav, age 5, Abbey Park in Leicester and the name Rory. However, Meera appears nowhere, the sibling relationship and fifth-birthday cloud-finding memory are omitted, Aarav's appearance is not f |
| coherence | 1 | The narrative jumps from an unexplained melancholy sky to rain, an invented uncle, threatening woods and a repeated opening sentence. It also changes Aarav to “she,” repeats page 1 at page 6, and ends with an unfinished  |
| age fit | 1 | The measured grade 7.7 reading level is too difficult for a five-year-old, and the prose actively uses adult words such as “ephemeral,” “crepuscular,” “juxtaposing” and “existential trepidation.” The threatening “shadows |
| language | 1 | There are raw template placeholders, the title is misspelled “Adventrue,” Aarav becomes “Aara,” a male character is referred to as “she,” the opening is duplicated, and the last sentence has no completion or final punctu |
| text image fit | 2 | Several images broadly support their pages, such as the evening sky and the red balloon, but the rain page shows sunshine, the uncle page omits the described path and shelter, the woods do not show threatening shadows, a |
| character consistency | 2 | Aarav's face and body remain broadly similar, but his clothing consistently ignores the supplied red dinosaur T-shirt and short black hair. Character labels are baked into the artwork, the uncle is an unsupported additio |
| visual quality | 2 | The colours are clean and the mobile pages are uncluttered, but the artwork is very basic, repeats the same park scene, does not follow the chosen Watercolour style, includes diagram-like name labels, misspells the title |
| emotional resonance | 1 | Aarav's name and local park provide a small amount of personalisation, but the central sibling memory, birthday atmosphere and warmth are absent. The threatening adventure, invented uncle, placeholder dedication and inco |

- **used correctly:** Aarav's first name; Aarav's age of 5; Aarav's male pronouns in much of the story; Abbey Park in Leicester; Rory's name; A birthday-adjacent magical adventure framing
- **missing:** Meera's name; Meera's role as Aarav's younger sister; The fifth-birthday setting; Aarav teaching Meera to find shapes in clouds; The park memory near the family home; Aarav being the hero through his teaching; Short black hair; Big brown eyes; Red dinosaur T-shirt; A proper sender and recipient dedication; Evidence that the premium gift-wrap selection was applied; A clear total price including delivery
- **changed:** The gentle sibling cloud game became a dark and threatening adventure.; Rory was replaced by a red balloon during the main action.; The requested character appearance was changed to a plain teal top.; The selected Watercolour style was changed to Pop-art comic.; The intended birthday present became a generic story opening and ending
- **invented:** Uncle Bartholomew; A lantern; A dark forest with threatening shadows; A red balloon; Rain and puddles; Mean's; A large share link and referral credit claim; A generic adventure story structure

### Part by part
#### Cover / Title page
![I1](artifacts/capture_01/img_00.jpg)
> A StoryHearth original Illustration style: Pop-art comic The Magical Adventrue of Aarav Aarav
- *Picture:* A simple flat-colour illustration of a small boy in a teal top standing beside a red toy-like shape, three trees and a bright sun. The title is printed across the sky, and “Aarav” is printed below the child.
- *Reaction:* It is bright and easy to recognise, but “Adventrue” immediately makes it look careless. I also asked for Watercolour, not “Pop-art comic,” and Aarav is not wearing the red dinosaur T-shirt I described.
  - [language, sev 3] The title says “Adventrue” rather than “Adventure”.
  - [fidelity, sev 3] The caption says “Illustration style: Pop-art comic,” although the chosen Watercolour style was ignored.
  - [character_consistency, sev 3] Aarav is drawn in a plain teal top rather than the supplied “red dinosaur t-shirt.”
  - [text_image_fit, sev 2] The red object beside Aarav is an ambiguous animal-like shape rather than a clearly recognisable toy dinosaur called Rory.
  - [visual_quality, sev 2] The picture is very generic, uses placeholder-like labels under the character, and does not resemble a Watercolour illustration.
- **Change I'd make:** Correct the title, label the chosen style accurately, and redraw Aarav with short black hair, big brown eyes and a red dinosaur T-shirt while holding a clearly identifiable Rory.
- **Suggested rewrite:** The Magical Adventure of Aarav A StoryHearth original Illustration style: Watercolour For Aarav's fifth birthday

#### Dedication page
![I2](artifacts/capture_03/view_00.jpg)
> For {{recipient_name}}, with love from {{sender_name}}
- *Picture:* A mobile screenshot of the StoryHearth preview page. Inside a large cream frame, unprocessed template placeholders are displayed above the page navigation. The surrounding interface includes “How it works,” “Pricing,” “My books,” “Log out,” a regeneration price and an “Order hardcover” button.
- *Reaction:* Leaving raw placeholders on a birthday present is unacceptable. On my phone, the page is also surrounded by a lot of website clutter, but I can see the big order button.
  - [language, sev 4] The displayed dedication still contains “{{recipient_name}}” and “{{sender_name}}”.
  - [fidelity, sev 3] Neither the recipient nor the sender has been filled in, despite the book being personalised.
  - [visual_quality, sev 3] The unfinished template text is shown inside the book preview, and the phone view includes the full website interface.
- **Change I'd make:** Replace both template variables with real values before rendering and previewing the page.
- **Suggested rewrite:** For Aarav, with love from Priya Happy fifth birthday!

#### Page 1
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in Abbey Park in Leicester, there lived a curious child named Aarav. Aarav was 5 years old and loved nothing more than Aarav's red toy dinosaur called Rory. Aarav
- *Picture:* Aarav stands in a generic green park with three round trees, a bright sun and a red animal-like shape. There are no visible paths, benches, clouds, sister, birthday details or clear dinosaur features.
- *Reaction:* It uses our park and Rory's name, but the picture is just a repeated template-like park scene. Saying “Aarav's” in the third person is clunky rather than a loving detail.
  - [language, sev 2] “Loved nothing more than Aarav's red toy dinosaur” refers back to the subject by name instead of using “his.”
  - [fidelity, sev 3] The supplied details “short black hair, big brown eyes” and “red dinosaur t-shirt” are not shown, and the birthday or cloud-finding premise has not begun.
  - [text_image_fit, sev 3] The image is a generic park and does not clearly show a red toy dinosaur, Abbey Park, Leicester or anything tying the scene to Aarav's birthday.
  - [visual_quality, sev 2] The printed label “Aarav” beneath the character looks like a diagram label rather than finished story artwork.
- **Change I'd make:** Show Aarav recognisably on his fifth birthday at Abbey Park, wearing his dinosaur T-shirt and holding Rory, while beginning the cloud-game premise.
- **Suggested rewrite:** It was Aarav's fifth birthday. He wore his red dinosaur T-shirt and put Rory, his favourite toy dinosaur, in his pocket. “Come on, Meera,” he called. “Let's find shapes in the clouds!”

#### Page 2
![I4](artifacts/capture_05/img_00.jpg)
> One evening Aarav gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation. Aarav
- *Picture:* Aarav stands beneath a purple and pink evening sky with several small white stars or cloud-like dots, beside three round trees.
- *Reaction:* This is completely beyond a five-year-old, and I would not expect Aarav to know words like “ephemeral.” The lovely idea of looking for shapes should be here instead.
  - [age_fit, sev 4] The sentence uses “ephemeral luminescence,” “crepuscular firmament,” “engendered,” “ineffable,” “juxtaposing” and “existential trepidation.”
  - [fidelity, sev 4] The requested memory of Aarav teaching Meera to find shapes in the clouds is absent.
  - [coherence, sev 3] The difficult sentence gives no simple reason for the story's action and creates melancholy without a child-friendly setup.
  - [visual_quality, sev 2] The character is again labelled “Aarav,” and the image remains a simplistic template rather than Watercolour artwork.
- **Change I'd make:** Replace the advanced sentence with simple language and show distinct cloud shapes, with Aarav pointing one out to Meera.
- **Suggested rewrite:** Aarav looked up at the sky. “That cloud looks like a dinosaur,” he said. “Can you find one that looks like a rabbit, Meera?”

#### Page 3
![I5](artifacts/capture_06/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Aara pulled up his hood and ran for shelter, holding Aarav's red toy dinosaur called Rory tight. Aarav
- *Picture:* The same bright daytime park scene reappears, with a large sun, green ground, three trees, Aarav and the ambiguous red object. There is no rain, puddles, hood or visible running.
- *Reaction:* The text and picture tell different stories: it says heavy rain, but the sun is shining. “Aara” is not Aarav, and the possessive wording is awkward.
  - [language, sev 3] Aarav is misspelled as “Aara” and “Aarav's red toy dinosaur” is used in a third-person possessive construction.
  - [coherence, sev 3] The sudden rain and run for shelter are not connected to the birthday cloud game, and no cause or consequence is developed.
  - [text_image_fit, sev 4] The prose says rain poured into puddles, but the image shows bright sunshine and no rain or puddles.
  - [character_consistency, sev 2] The image does not show the hood, movement or dinosaur T-shirt described in the supplied character details.
- **Change I'd make:** Either remove the invented storm or illustrate it consistently. It would be better to keep the real family memory and make the cloud shapes the focus.
- **Suggested rewrite:** Meera spotted a long cloud. “That's Rory!” she cried. Aarav smiled. “Good looking, Meera!” he said.

#### Page 4
![I6](artifacts/capture_07/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Aarav, follow me!" he called, and she followed him along the winding path. Uncle Bartholomew Aarav
- *Picture:* A taller figure in blue holding a small yellow rectangle stands beside Aarav in a dark, muted park. Both are labelled beneath the image.
- *Reaction:* I never mentioned Uncle Bartholomew, and “she followed him” is wrong for Aarav. It feels as though a different story has been pasted over mine.
  - [fidelity, sev 4] “Uncle Bartholomew” is an invented important character who was not supplied in the family details.
  - [coherence, sev 4] Although Aarav is addressed with male pronouns elsewhere, “she followed him” contradicts the requested “he / him” pronouns.
  - [character_consistency, sev 3] Aarav is still shown in his plain teal top rather than his red dinosaur T-shirt, and the image has no sister, cloud activity or birthday context.
  - [text_image_fit, sev 2] The picture roughly shows two figures, but there is no clear winding path, lantern light, shelter or meaningful interaction with Meera.
  - [visual_quality, sev 2] The labels “Uncle Bartholomew” and “Aarav” are baked into the image, making the scene look unfinished.
- **Change I'd make:** Delete Uncle Bartholomew and replace him with Meera. Correct Aarav's pronoun and show a warm sibling interaction in the park.
- **Suggested rewrite:** Meera looked at the next cloud. “I found a heart!” she said. Aarav took Rory's tiny hand. “That's my clever sister!”

#### Page 5
![I7](artifacts/capture_08/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Aarav again. Aarav clutched a shiny red balloon and trembled in the dark. Aarav
- *Picture:* Aarav stands in a dark green field beneath a starry sky and crescent moon, beside a floating red balloon and three trees.
- *Reaction:* This is frightening and does not belong in the gentle birthday memory I supplied. The red balloon has also replaced the special toy dinosaur in the key action.
  - [fidelity, sev 4] The story abruptly moves into woods and introduces a red balloon even though the special object was Rory, Aarav's red toy dinosaur.
  - [age_fit, sev 4] “The shadows grew teeth and whispered that no one would ever find Aarav again” introduces a serious abandonment threat.
  - [coherence, sev 4] The woods, threatening shadows and balloon appear without explanation and do not resolve the cloud-finding activity.
  - [text_image_fit, sev 3] The image shows a red balloon, but it does not show deep woods, teeth in the shadows, whispering or fear.
  - [character_consistency, sev 2] Aarav remains in the same teal top instead of the specified red dinosaur T-shirt.
- **Change I'd make:** Remove the threatening sequence. Return to the park and use Rory positively, perhaps helping the cloud shapes connect to the sibling memory.
- **Suggested rewrite:** Aarav held up Rory. The red dinosaur pointed towards a cloud shaped like a dragon. “That one is Rory too!” said Meera.

#### Page 6
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in Abbey Park in Leicester, there lived a curious child named Aarav. At last the sun came out, and Aarav skipped all the way home, happier than ever. Aarav
- *Picture:* Aarav stands still in a generic sunny park beside the same three trees. There is no visible route home, skipping, sister, dinosaur, cloud shapes or park landmark.
- *Reaction:* This repeats the opening as though nothing happened, then rushes Aarav home without saying what he and Meera learned. It feels pasted together rather than carefully made.
  - [coherence, sev 4] “Once upon a time, in Abbey Park in Leicester, there lived a curious child named Aarav” repeats the opening inside the story rather than advancing the plot.
  - [fidelity, sev 4] The birthday present, cloud-shape game, sibling bond and the requested scene of Aarav teaching Meera receive no proper conclusion.
  - [text_image_fit, sev 3] The text says Aarav skipped all the way home, but the picture shows him standing in the same generic park with no path or home.
  - [visual_quality, sev 2] This is essentially the cover image repeated, with the label “Aarav” still visible.
- **Change I'd make:** Replace the repeated opening with a clear resolution to the sibling cloud game and show the relevant actions and characters.
- **Suggested rewrite:** Aarav and Meera counted seven cloud shapes before it was time to go home. “Best birthday ever,” Meera said, hugging Rory.

#### Page 7 / Closing page
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Aarav looked up at the sky, he would always remember The End Aarav
- *Picture:* An orange sunset background with the printed words “The End,” Aarav standing beside three trees, and “Aarav” printed below him. Meera, Rory, the cloud activity and a distinct park setting are absent.
- *Reaction:* The sentence stops after “remember,” so it is not a proper keepsake ending. I wanted the ending to celebrate Aarav teaching Meera, not leave her and Rory out of the final memory.
  - [language, sev 4] “He would always remember” ends without an object or final punctuation, and “The End” appears twice.
  - [fidelity, sev 4] Meera, her sibling relationship and the cloud-shape birthday memory are absent from the closing page.
  - [coherence, sev 4] The final recollection is incomplete and does not resolve the earlier cloud game or threats.
  - [text_image_fit, sev 3] The image does not show Aarav looking at the sky with Meera or Rory, despite the closing text referring to looking at the sky and remembering.
  - [emotional_resonance, sev 4] The final page omits the family bond and birthday memory that would make the gift personal.
- **Change I'd make:** Complete one short sentence, remove the duplicate “The End,” and illustrate Aarav and Meera together with Rory under the cloud-shaped sky.
- **Suggested rewrite:** From then on, whenever Aarav and Meera looked at the sky, they smiled and searched for more shapes together. The End

**Top changes to the output:** 1. Rebuild the entire story around Aarav teaching Meera to find shapes in clouds at Abbey Park on his fifth birthday, with Meera present from beginning to end. | 2. Fix the title, complete the dedication, remove every template placeholder, correct “Aara” to “Aarav,” restore “he/him,” remove the repeated opening and finish the final sentence. | 3. Replace the advanced vocabulary and threatening forest sequence with short, warm, child-friendly sentences at approximately ages 5–7. | 4. Redraw every page in the chosen Watercolour style with consistent short black hair, big brown eyes and a red dinosaur T-shirt, and make Rory clearly recognisable. | 5. Create genuine illustrations for each event, especially the cloud game, sibling interaction, park, Rory and closing memory, rather than reusing generic park templates. | 6. Show the full price, delivery charge and any gift-wrap cost before checkout so there are no surprises.

## Recommendations (participant's priorities)
- **[high] Rebuild the story around the requested memory: Aarav teaching Meera to find shapes in the clouds at Abbey Park on his fifth birthday, with both children present from beginning to end.** (Generated storybook preview) - The current book misses the central sibling memory and does not feel personal enough to give as a keepsake.
- **[high] Fix the title and all language errors, including the misspelling, the wrong name, the incorrect pronouns, the repeated opening, the template placeholders and the unfinished final sentence.** (Generated storybook preview) - These mistakes make the book look broken and immediately unsuitable as a birthday present.
- **[high] Use short, warm, age-appropriate language for a five-year-old and remove the threatening forest passage and difficult vocabulary.** (Choose the look and feel / Generated storybook preview) - I need a gentle bedtime story that Aarav can actually understand and enjoy.
- **[high] Match the generated illustrations to the selected Watercolour style and keep Aarav's appearance, clothing, Rory and the important story events consistent across the pages.** (Generated storybook preview) - The output ignored the chosen style and did not visually represent the family memory I entered.
- **[high] Show the book price, delivery charge and gift-wrap cost clearly before checkout, and make every optional extra unselected by default.** (Homepage and checkout) - I need to know the full cost upfront and do not want to pay for things I did not ask for.
- **[high] Add clear Edit and Regenerate controls, and explain any regeneration charge in pounds before I choose it.** (Generated storybook preview) - I need a way to fix a story that is not right without feeling trapped or pressured into paying.
- **[medium] Make the relationship field apply clearly to each child and provide sensible options, with 'Sibling' available for Meera.** (Create your book – characters) - The default 'Grandparent' was confusing and made me question whether the rest of the family details would be correct.
- **[medium] Replace Lexile with plain-language reading levels such as 'Best for ages 4–6' and explain them in one short line.** (Choose the look and feel) - I do not know what Lexile means and just want to choose a suitable story for a five-year-old quickly.
- **[medium] Replace the technical sync error with a clear message that says whether my details were saved and what to do if they were not.** (My books dashboard) - The raw error made me worry that my family's information might disappear before I had even created the book.
- **[medium] Improve the mobile navigation, form labels, page buttons and low-contrast footer text.** (Throughout the website) - I am using this on a small phone with one free hand, so cramped navigation and tiny controls make it harder to use.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This is for making personalised birthday storybooks for children, with the child and their family appearing in the story. It is aimed at parents looking for a keepsake or present, especially people who want to choose the characters, memory and artwork themselves.
- **What was the most frustrating or confusing moment, and why?** The worst moment was seeing the finished book: it left out Meera and the cloud-shape memory, used the wrong style, called Aarav by the wrong name, changed his pronouns and had a spelling error. I also felt suspicious at checkout because gift wrap was preselected and the full cost was not obvious from the start.
- **What was the best moment?** The best moment was entering Aarav, Meera, Abbey Park and Rory into the short forms. Those steps were quick and easy, and it felt like I was building something personal rather than filling in a long generic questionnaire.
- **Was there any point where, in real life, you would have given up? Where and why?** Yes, I would probably have given up before entering payment details. The preview made the book clearly unsuitable, and the £45.97 starting total with £7.99 gift wrap and £12.99 delivery felt too much for a present I was not happy with.
- **What did you expect to find or be able to do that wasn't there?** I expected a story about Aarav teaching Meera to find shapes in the clouds at Abbey Park on his fifth birthday, with both children present throughout. I also expected the chosen watercolour style to be followed, a clear edit or regenerate option, and the full delivered price shown before checkout.
- **Did you trust this website with your information (and your family's)? Why or why not?** Only to a limited extent. I was happy to type in the children's names and story details, but the raw sync error made me wary, and I would not have trusted the site with payment while the title, characters, style and story content were clearly wrong.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I might pay around £20 to £30 for a good quality personalised hardcover if the story was accurate and the delivered price was completely clear. I would pay more for genuinely lovely, consistent artwork and a properly finished story, but not for gift wrap or a regeneration charge that was not explained.
- **If the site produced something for you, how do you feel about it overall?** I would not keep this version or give it to Aarav. It used a few details correctly, such as his name, age, park and Rory, but missed the actual present I wanted and had enough spelling, wording, character and artwork problems to make it feel unfinished.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | This looks relevant straight away—I could make a birthday book starring Aarav. The first paragraph is far too corporate, but the three steps look simple. I need to log in first before I make it. | click |
| 2 | Log in – StoryHearth | neutral (1) | Straightforward enough. I can see the two boxes straight away, though the labels disappear when I tap them. I’ll use my account details and get straight on with the book. | type; type; click |
| 3 | My books – StoryHearth | confused (0) | I’m in, and the big orange button is obvious. That profile sync error makes me a bit wary, though—does that mean my details won’t come through? I’ll try creating the book first. | click |
| 4 | Create your book – StoryHearth | neutral (1) | This is quick and easy to scan. I can put Aarav in and add Meera as his little sister, but the relationship box already says “Grandparent,” so I definitely need to change that. | type; select; select; type; type; select |
| 5 | Create your book – StoryHearth | reassured (1) | Good, Meera's in and it's saved as his sibling. The description is cut off visually, but I know the full text I entered. I'll press Next. | click |
| 6 | Create your book – StoryHearth | reassured (1) | Good, this is quick—just three boxes. I’ll add Abbey Park, Rory, and the cloud-shape memory, then tap Next. | type; type; type; click |
| 7 | Create your book – StoryHearth | reassured (1) | These choices are clear, but “Lexile” is jargon I don’t understand. For a five-year-old, I’d choose the easiest range, and the watercolour style looks lovely, so I’ll keep that and press Next. | click; click |
| 8 | Create your book – StoryHearth | reassured (1) | I’ll skip the photo because I don’t have a suitable one on this phone and I don’t want to delay his present. The big “Create my book” button is clear, although the navigation at the top looks cramped. | click; wait_for_change |
| 9 | Your storybook – StoryHearth | confused (0) | It’s worked, and the cover is cute, but it says “Adventrue” and “Pop-art comic” even though I chose Watercolour. I need to read every page before deciding whether this is suitable for Aarav. | flip_through |
| 10 | Your storybook – StoryHearth | disappointed (-1) | I’ve looked through all nine pages. The ending feels very plain and Aarav is alone, even though the story was about teaching Meera at the park. I won’t pay the regeneration charge; I need to check the actual hardcover to | click |
| 11 | Checkout – StoryHearth | suspicious (-2) | There it is: £45.97 before I’ve even entered an address. I didn’t ask for premium gift wrap, but it’s already ticked, so I’m unchecking that now. I won’t enter any payment details. | click |
| 12 | Checkout – StoryHearth | reassured (1) | Good, the total has dropped to £37.98 after I removed the gift wrap. That’s still quite a lot for a birthday present, especially with £12.99 shipping, but at least I can see the full cost now. I won’t enter any payment d | done |
