# UserQA report: Priya Nair on http://127.0.0.1:8765/

*Persona:* **Priya Nair** (36) - Shift-working nurse and mum of two who does everything on her phone in stolen minutes.  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 12 steps | *Pages reviewed:* 9 | *Issues:* 25 | *LLM calls:* 15 | *Wall time:* 300.5 s

## What the agent understood the website to be
- **what it is:** A service that turns family details and a shared memory into a personalised illustrated storybook.
- **who it is for:** Families wanting a story featuring their children and other relatives, friends, or pets.
- **value proposition:** Create a bespoke family story and digital preview, with printed hardcovers available.
- **pricing model:** The digital preview is described as free. Printed hardcovers are offered, but no price is shown here.
- **fit for me:** Very relevant because I want a quick birthday book starring Aarav, with Meera included, and the site says the preview is free.
- **main tasks:** Log in, Add characters, Describe a family memory, Generate and read the storybook preview, Check hardcopy pricing and ordering

## Scores
- SUS: **45.0** (grade F; 68 = industry average)
- UEQ-S: pragmatic -1.0, hedonic 1.0 (range -3..+3)
- Likelihood to recommend (0-10): 1
- Output keepsake-worthiness (1-5): 1
- Verdict: *"Quick to start and full of promise, but the unfinished, inaccurate story and sneaky checkout mean I would not give this to Aarav."*

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 3 | CONTENT | Generated storybook preview (x2) | Generated title contains a spelling error | The cover and page heading both say “The Magical Adventrue of Aarav.” | Add title proofreading or spelling correction before showing the generated book as ready to order. |
| 3 | H1 | Generated storybook preview | Generated style does not match the selected style | The selection screen showed “Crayon — like a child drew it,” but the generated cover says “Illustration style: Pop-art comic.” | Apply the selected style consistently, or clearly report that the requested style was unavailable and require confirmation before charging for regeneration. |
| 3 | CONTENT | Generated storybook preview | The final story sentence is incomplete | “And from that day on, whenever Aarav looked up at the sky, he would always remember” | Complete the sentence in the generated story and include a clear ending, then check all final-page text for truncation before saving the book. |
| 3 | DECEPTIVE | Hardcover checkout | Premium gift wrap is pre-selected | [6] checkbox "Premium gift wrap" (checked) — £7.99 | Default the gift-wrap checkbox to unchecked and require an explicit choice to add it. |
| 2 | ACC | Optional photo upload, My books dashboard, Generated storybook preview, Hardcover checkout (x4) | Header navigation wraps and reads as broken sentences | The top shows “How it StoryHearth works,” “Pricing,” “My books,” and “Log out” on separate, awkwardly aligned lines. | Use a compact mobile menu or stack the navigation neatly with consistent spacing and full, readable link labels. |
| 2 | CONTENT | Home page | Opening copy uses unexplained jargon | “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.” | Replace it with plain language, for example: “Turn a family memory into a beautifully illustrated story starring your child.” |
| 2 | VALUE | Home page | Printed price is not visible before creation | The page says “Printed hardcovers shipped across the UK” and offers “See pricing,” but shows no actual hardback price. | Show at least the starting hardback price on the home page and make clear whether delivery is included. |
| 2 | ACC | Home page | Phone navigation is cramped | “How it works,” “Pricing,” and “Log in” are squeezed across the top of the narrow screen, with “How it works” wrapping onto two lines. | Use a compact mobile header with larger tap targets, such as logo plus a menu, or keep short labels on one line. |
| 2 | H9 | My books dashboard | Unexplained technical error on a successful login | “Error 0x80070057: profile sync incomplete.” | Replace the error code with plain language, such as “Some profile details may not have loaded. You can still create a book,” and provide a Retry details button if needed. |
| 2 | H5 | Create book details | Relationship is preselected before a character is entered | [11] Relationship is selected: “Grandparent” while [10] “Who else is in the story?” is empty | Start Relationship at “Select relationship” and require a choice after someone is entered. |
| 2 | H7 | Create book details | Only one other-character appearance field is provided | [10] “Who else is in the story?” has no matching appearance field, while [9] asks “What do they look like?” only for the child | After naming the other character, ask for their relationship and optional appearance in a compact repeating character section. |
| 2 | H2 | Reading level and illustration | Lexile labels need plain-language help | “Lexile BR–200L” | Add a short age guide, such as “Beginner — roughly ages 4–7”, to every reading-level option. |
| 2 | ACC | Optional photo upload | Footer text is very faint | “Privacy Terms Contact © 2026 StoryHearth Ltd.” appears in extremely light grey on the pale background. | Use a much darker footer text colour with sufficient contrast and enlarge the tap targets. |
| 2 | TRUST | Optional photo upload | Photo upload gives no privacy reassurance | The page asks for “a clear photo of your child's face” but gives no nearby explanation of how the image is stored, used, or deleted. | Add a short note beside the uploader explaining retention, model use, deletion, and linking it to the full privacy policy. |
| 2 | VALUE | Generated storybook preview | Paid regeneration is prominent without clarifying what changes | [8] “Regenerate entire book – $4.99” | Label it as a one-time charge and explain what gets regenerated; put it behind a confirmation step showing the amount before tapping. |

## Page-by-page
### Home page  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Introduce the personalised storybook service and direct visitors to sign in, start creating, or view pricing.
- **What's happening:** The page shows the service proposition, primary calls to action, a short explanation of how it works, customer quotes, and FAQ/footer links. No content has yet been generated for me.
- **First impression (Priya):** "The warm colours and big buttons feel friendly, but the opening explanation is far too technical for someone scanning quickly on a phone."
- **Cognitive walkthrough:** Q1 Yes, I would log in and try making Aarav’s book because the headline and process match what I want. / Q2 Yes, the dark “Log in” button is visible at the top and easy to tap. / Q3 Yes. “Log in” clearly means signing into my existing account.
  - [CONTENT sev 2] **Opening copy uses unexplained jargon** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Replace it with plain language, for example: “Turn a family memory into a beautifully illustrated story starring your child.”
  - [VALUE sev 2] **Printed price is not visible before creation** - evidence: The page says “Printed hardcovers shipped across the UK” and offers “See pricing,” but shows no actual hardback price.. Fix: Show at least the starting hardback price on the home page and make clear whether delivery is included.
  - [ACC sev 2] **Phone navigation is cramped** - evidence: “How it works,” “Pricing,” and “Log in” are squeezed across the top of the narrow screen, with “How it works” wrapping onto two lines.. Fix: Use a compact mobile header with larger tap targets, such as logo plus a menu, or keep short labels on one line.
- **Positives:** The primary “Proceed” and “Log in” buttons are prominent.; The three-step explanation is short and task-focused.; It clearly says the digital preview is free.; The page looks warm and family-friendly without being cluttered.

### Log in form  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** Sign in to an existing StoryHearth account.
- **What's happening:** The page displays a welcome-back login form with empty Email and Password fields, plus account and support links.
- **First impression (Priya):** "This looks quick and simple. The large Log in button is easy to spot, although the fields only have placeholder text rather than visible labels."
- **Cognitive walkthrough:** Q1 Yes, I would try this immediately because I already have an account and need to get to the book. / Q2 Yes, the Email and Password fields and the Log in button are all visible. / Q3 Yes, the placeholders say Email and Password, and the button says Log in, so the wording matches what I want to do.
  - [ACC sev 1] **Fields have no visible labels** - evidence: [5] textbox (no label) placeholder "Email"; [6] textbox (no label) placeholder "Password". Fix: Add visible labels such as Email address and Password above the fields, and keep the placeholders only as supplementary hints.
- **Positives:** The login form is short and does not require unnecessary fields.; The large orange Log in button is easy to tap on a phone.; The page clearly says Welcome back and provides a Create an account link.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** Show the signed-in user's saved storybooks and let them begin a new book.
- **What's happening:** The account is logged in successfully. The page says “You have no books yet” and offers one prominent creation control, while also displaying a profile sync error.
- **First impression (Priya):** "The creation button is obvious and easy to use on my phone, but that technical error makes me wonder if something is wrong with my account."
- **Cognitive walkthrough:** Q1 Yes. I need to create a new birthday book now. / Q2 Yes. The large orange “+ Create a new book” button is impossible to miss. / Q3 Yes. “Create a new book” clearly says what tapping it will do.
  - [H9 sev 2] **Unexplained technical error on a successful login** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the error code with plain language, such as “Some profile details may not have loaded. You can still create a book,” and provide a Retry details button if needed.
  - [ACC sev 1] **Navigation wraps awkwardly on a phone** - evidence: The links “How it works”, “My books”, and “Log out” are split across multiple lines and visually crowded.. Fix: Use a compact mobile header with a menu button, or keep each navigation label on one line with adequate spacing.
- **Positives:** Login success is clear from the welcome message and the empty-books status.; The “+ Create a new book” button is prominent and clearly labelled.; The page is uncluttered and requires no reading before taking the main action.

### Create book details  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Collect the main child and second character who will appear in the personalised story.
- **What's happening:** A short form is open for entering the star child’s details, appearance, and one other person with a relationship type. A large orange Next button is visible.
- **First impression (Priya):** "It’s straightforward and the boxes are big enough for my phone, though the preselected “Grandparent” relationship is a bit misleading."
- **Cognitive walkthrough:** Q1 Yes, I want to make Aarav the hero and include Meera, so this is the form I need. / Q2 Yes, I can immediately see the name, age, pronouns, appearance, other-character and relationship controls. / Q3 Mostly. “Who else is in the story?” is a bit broad, and I have to use Relationship for Meera’s “little sister” connection, but “Sibling” makes sense.
  - [H5 sev 2] **Relationship is preselected before a character is entered** - evidence: [11] Relationship is selected: “Grandparent” while [10] “Who else is in the story?” is empty. Fix: Start Relationship at “Select relationship” and require a choice after someone is entered.
  - [H7 sev 2] **Only one other-character appearance field is provided** - evidence: [10] “Who else is in the story?” has no matching appearance field, while [9] asks “What do they look like?” only for the child. Fix: After naming the other character, ask for their relationship and optional appearance in a compact repeating character section.
- **Positives:** The large orange Next button is obvious.; The form is short and uses plain labels.; The appearance field is clearly marked optional.; Controls are large enough to tap with one thumb.

### Story details form  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** Collect the setting, special object, and memory or idea that will be used to generate the personalised storybook.
- **What's happening:** The user is on the story-details step after entering the main character and sibling. The form contains three empty fields for the location, a special object, and the story memory, with navigation buttons.
- **First impression (Priya):** "This looks quick and manageable. I can see the fields straight away, and they match the details I need to provide."
- **Cognitive walkthrough:** Q1 Yes, I would try this now because there are only three relevant fields and I already know the answers. / Q2 Yes, the labelled textboxes and examples are immediately visible. / Q3 Yes. The labels clearly ask for the place, object, and memory needed for Aarav’s story.
- **Positives:** The form is short and focused on the information needed.; The labels are clear and the placeholders provide useful examples.; The Next button is prominent and easy to reach on a phone.

### Reading level and illustration  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Choose how difficult the book should be and which artistic style it should use.
- **What's happening:** The story details have been completed. The page now offers four Lexile reading levels and three illustration styles, with sensible choices already selected and a prominent Next button.
- **First impression (Priya):** "This is quick and much less effort than a form. I can see both choices clearly, although the navigation at the top has wrapped into several lines."
- **Cognitive walkthrough:** Q1 Yes, I would choose the beginner range because this is for Aarav at age five. / Q2 Yes, the four large reading-level radio buttons are immediately visible. / Q3 Mostly. The Lexile ranges identify reading difficulty, but plain labels such as “Age 4–7” would be easier for me than expecting me to know Lexile.
  - [H2 sev 2] **Lexile labels need plain-language help** - evidence: “Lexile BR–200L”. Fix: Add a short age guide, such as “Beginner — roughly ages 4–7”, to every reading-level option.
  - [H8 sev 1] **Mobile navigation wraps into separate lines** - evidence: The top navigation visibly shows “How it works”, “Pricing”, “My books”, and “Log out” across crowded lines.. Fix: Use a compact mobile menu with clear spacing and keep the StoryHearth brand on one line.
- **Positives:** The selected options are visible immediately.; The large radio targets are easy to tap one-handed.; There is a clear Back button and a prominent Next button.; Only two simple decisions are required.

### Optional photo upload  (step 8)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_08.jpg)
- **Purpose:** Let the user optionally add a child's photo before generating the personalised book.
- **What's happening:** This is the last setup screen. No photo has been chosen, and both Back and Create my book are available.
- **First impression (Priya):** "Quick and understandable. I can skip the upload and create the book, though the navigation at the top looks badly wrapped on my phone."
- **Cognitive walkthrough:** Q1 Yes, I would skip it because a clear photo is not essential and I'd rather not upload my child's picture here. / Q2 Yes, the “Choose file” control and the large “Create my book” button are both obvious. / Q3 Yes. “Create my book” clearly says what will happen next.
  - [ACC sev 2] **Header navigation wraps and reads as broken sentences** - evidence: The top shows “How it StoryHearth works,” “Pricing,” “My books,” and “Log out” on separate, awkwardly aligned lines.. Fix: Use a compact mobile menu or stack the navigation neatly with consistent spacing and full, readable link labels.
  - [ACC sev 2] **Footer text is very faint** - evidence: “Privacy Terms Contact © 2026 StoryHearth Ltd.” appears in extremely light grey on the pale background.. Fix: Use a much darker footer text colour with sufficient contrast and enlarge the tap targets.
  - [TRUST sev 2] **Photo upload gives no privacy reassurance** - evidence: The page asks for “a clear photo of your child's face” but gives no nearby explanation of how the image is stored, used, or deleted.. Fix: Add a short note beside the uploader explaining retention, model use, deletion, and linking it to the full privacy policy.
- **Positives:** The photo is clearly marked optional.; The large “Create my book” button is easy to tap.; A Back button gives me a way to revise my earlier choices.; The step contains no required form fields.

### Generated storybook preview  (step 9)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_09.jpg)
- **Purpose:** Preview the generated family story, navigate its pages, optionally regenerate it, and start a hardcover order.
- **What's happening:** A generated nine-page book titled “The Magical Adventrue of Aarav” is displayed at page 1 of 9. The cover labels the style as “Pop-art comic” despite crayon having been selected, and paid regeneration and hardcover-order controls appear below the preview.
- **First impression (Priya):** "The book is there and the big Order button is obvious, but the misspelled title and unexpected Pop-art style feel disappointing for a £4.99 personalisation-adjacent product."
- **Cognitive walkthrough:** Q1 Yes, I would tap the next arrow because I need to read every page. / Q2 Yes, the right-arrow button marked “›” is visible beneath the cover. / Q3 Partly—the arrow clearly means next page, but the tiny arrow icon alone is less obvious than a labelled “Next page” button.
  - [H1 sev 3] **Generated style does not match the selected style** - evidence: The selection screen showed “Crayon — like a child drew it,” but the generated cover says “Illustration style: Pop-art comic.”. Fix: Apply the selected style consistently, or clearly report that the requested style was unavailable and require confirmation before charging for regeneration.
  - [CONTENT sev 3] **Generated title contains a spelling error** - evidence: The cover and page heading both say “The Magical Adventrue of Aarav.”. Fix: Add title proofreading or spelling correction before showing the generated book as ready to order.
  - [CONTENT sev 3] **The final story sentence is incomplete** - evidence: “And from that day on, whenever Aarav looked up at the sky, he would always remember”. Fix: Complete the sentence in the generated story and include a clear ending, then check all final-page text for truncation before saving the book.
  - [VALUE sev 2] **Paid regeneration is prominent without clarifying what changes** - evidence: [8] “Regenerate entire book – $4.99”. Fix: Label it as a one-time charge and explain what gets regenerated; put it behind a confirmation step showing the amount before tapping.
  - [CONTENT sev 2] **Generated title contains a spelling error** - evidence: “The Magical Adventrue of Aarav”. Fix: Add spelling and title-quality checks to generation, and let the user edit the title before ordering.
  - [H2 sev 1] **Next-page control lacks a text label** - evidence: [7] button “›”. Fix: Use a labelled “Next page” button and a larger touch target, while keeping the arrow as supporting text.
  - [ACC sev 1] **Top navigation wraps awkwardly on a phone** - evidence: The header visibly breaks “How it works” and “My books” across lines and overlaps the StoryHearth wordmark area.. Fix: Use a compact mobile navigation menu or a single-row layout with smaller spacing and touch targets.
- **Positives:** The preview clearly states “Preview · 9 pages” and “1 / 9.”; The cover is visible immediately without entering the book text.; The “Order hardcover” action is large, prominent, and easy to find.; The previous-page button is correctly disabled on page 1.

### Hardcover checkout  (step 11)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_11.jpg)
- **Purpose:** Show the complete cost of ordering the generated story as a hardcover and collect delivery and payment details.
- **What's happening:** The checkout lists the hardcover, a pre-selected premium gift-wrap add-on, shipping and handling, and the total. A countdown says the price is reserved, while address and payment forms continue below.
- **First impression (Priya):** "At least the delivery cost and total are shown, but £45.97 is higher than I expected. The already-ticked gift wrap immediately makes me wary of being upsold without being asked."
- **Cognitive walkthrough:** Q1 Yes, I want to remove the gift wrap and compare the total. / Q2 Yes, the checked box beside “Premium gift wrap” is visible. / Q3 Yes, the label clearly identifies the extra charge, although it should have been opt-in rather than pre-selected.
  - [DECEPTIVE sev 3] **Premium gift wrap is pre-selected** - evidence: [6] checkbox "Premium gift wrap" (checked) — £7.99. Fix: Default the gift-wrap checkbox to unchecked and require an explicit choice to add it.
  - [DECEPTIVE sev 2] **Artificial reservation countdown** - evidence: Your price is reserved for 09:57. Fix: Remove the countdown unless a real price guarantee is documented, and state clearly whether the price can change.
  - [H2 sev 2] **Gift-wrap checkbox is detached from its label** - evidence: The empty checkbox for [6] appears by itself above “Premium gift wrap” and “£7.99”.. Fix: Put the checkbox directly beside the gift-wrap label and make the entire labelled row a clearly styled tap target.
  - [H2 sev 2] **The price-reservation message is ambiguous** - evidence: “Your price is reserved for 09:45” is shown without explaining whether that is a countdown, a clock time, or how long the price is held.. Fix: Say plainly, “We’ll hold this price for 09:45 remaining,” and use a live countdown with an accessible text alternative.
  - [ACC sev 1] **Navigation wraps awkwardly on a phone** - evidence: The header visibly splits “How it works,” “My books,” and “Log out” across awkward lines.. Fix: Use a compact mobile header with a menu, or stack each navigation item cleanly without breaking its label.
- **Positives:** The hardcover price, delivery charge, and total are all visible before payment.; The total correctly adds to £45.97.; The order title confirms which book is being purchased.

## Generated output assessment
*Artifact:* Nine-page personalised children's hardcover book preview with checkout page

> This is recognisably about Aarav in a park, but it leaves out the most important person and memory: Meera learning to spot shapes in the clouds. The misspelled title, unresolved names, wrong pronouns, frightened plot, plain artwork, and unfinished ending make it feel like an unproofed draft. I would be too disappointed to give this as Aarav's birthday present.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | Aarav, age five, Abbey Park, Leicester, and Rory are present, but Meera never appears; the requested fifth-birthday cloud-shape lesson is omitted; the red dinosaur T-shirt and crayon style are not used; and Uncle Barthol |
| coherence | 1 | The story jumps from a park to unexplained evening sadness, rain, an invented uncle, frightening woods, and a repeated opening. Page 6 changes Aarav to "she", and page 9 ends mid-sentence after duplicating "The End". |
| age fit | 1 | The measured grade level is 8.2 for a requested five-year-old audience, and the prose includes "ephemeral", "crepuscular", "ineffable", "existential", and "trepidation". The threatening "shadows grew teeth" passage may a |
| language | 1 | There is a misspelled title, the near-miss "Aara", incorrect possessives, a pronoun error, repeated opening and ending, exposed placeholders, and an unfinished final sentence. |
| text image fit | 2 | Some broad settings match, including the evening sky and red balloon, but the rain page has a bright sun and no rain, the uncle page does not show movement along a path, the woods lack toothy shadows, and the final image |
| character consistency | 2 | Aarav's basic cartoon face and teal clothing remain fairly consistent, but he does not match the supplied short black hair, big brown eyes, and red dinosaur T-shirt. Meera is absent, Rory is usually not recognisable, and |
| visual quality | 2 | The images are clean enough and contain no obvious distorted faces, extra fingers, or garbled artwork, but they are very plain vector scenes rather than the requested crayon style. Several pages repeat nearly identical c |
| emotional resonance | 1 | Although the story starts with Aarav in a park, it omits the family-specific birthday memory, never includes Meera, introduces an unrelated uncle and frightening plot, and ends unfinished. It would not feel like a keepsa |

- **used correctly:** Aarav's first name; Aarav's age of five; Abbey Park in Leicester; The name Rory; The description of Rory as a red toy dinosaur; Male reference in much of the story; The selected premium gift wrap in the checkout total
- **missing:** Meera; Meera's relationship to Aarav as his little sister; Aarav teaching Meera to find shapes in the clouds; The fifth-birthday occasion; Short black hair; Big brown eyes; Red dinosaur T-shirt; Crayon illustration style; BR-200L reading level
- **changed:** The personal family memory was replaced with a generic magical adventure; Aarav's pronoun changes from he/him to "she" on page 6; Rory is described in the introduction but disappears from most illustrations and is replaced by a balloon; The requested sibling activity is replaced by invented rain, woods, shadows, and an uncle
- **invented:** Uncle Bartholomew; A rainstorm and puddles; A winding path; Toothy shadows in the woods; A red balloon; Existential sadness; A repeated statement that no one would find Aarav

### Part by part
#### Cover / Title page
![I1](artifacts/capture_01/img_00.jpg)
> A StoryHearth original Illustration style: Pop-art comic
- *Picture:* A plain vector-style boy labelled Aarav stands in a generic park with green trees, a bench-like red shape, and a large sun. He has very little or no visible black hair, wears a teal top rather than a red dinosaur T-shirt, and has no dinosaur called Rory.
- *Reaction:* Aarav's name is there, but 'Adventrue' immediately makes this look unfinished. The picture is not the crayon style I chose and does not look like the little boy I described.
  - [language, sev 3] The title shown on the cover is "The Magical Adventrue of Aarav"; "Adventrue" is misspelled.
  - [visual_quality, sev 3] The page says "Illustration style: Pop-art comic" even though I selected "Crayon".
  - [character_consistency, sev 3] The illustrated Aarav has little or no black hair and wears a teal top, rather than short black hair, big brown eyes, and a red dinosaur T-shirt.
  - [text_image_fit, sev 2] The cover promises a magical Aarav story, but Rory is absent and the red object beside the bench does not clearly depict a toy dinosaur.
- **Change I'd make:** Correct the title, generate every illustration in the requested crayon style, and show Aarav with short black hair, big brown eyes, a red dinosaur T-shirt, and Rory clearly visible.
- **Suggested rewrite:** Aarav and Rory Find Shapes in the Clouds A StoryHearth original Illustration style: Crayon

#### Page 2
![I2](artifacts/capture_03/view_00.jpg)
> For {{recipient_name}}, with love from {{sender_name}}
- *Picture:* A mobile preview page headed "The Magical Adventrue of Aarav" shows a large cream dedication card containing unresolved template placeholders, with page navigation and ordering controls below it.
- *Reaction:* This is clearly not ready to give away: my names have not even been inserted. Seeing the raw placeholders on the page feels like a broken proof rather than a personal birthday message.
  - [language, sev 4] "For {{recipient_name}}, with love from {{sender_name}}" exposes unresolved template code.
  - [emotional_resonance, sev 3] The intended personal dedication is replaced by generic unresolved variables, so the page does not feel made for Aarav or from me.
- **Change I'd make:** Populate the fields with Aarav and Priya before publishing and add a brief, affectionate dedication.
- **Suggested rewrite:** For Aarav, with love from Mum

#### Page 3
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in Abbey Park in Leicester, there lived a curious child named Aarav. Aarav was 5 years old and loved nothing more than Aarav's red toy dinosaur called Rory.
- *Picture:* Aarav stands in a very simple generic park beside trees and a red animal-like shape. There are no visible signs naming Abbey Park or Leicester, and the illustration does not establish the requested birthday outing or Meera.
- *Reaction:* The place, age, and dinosaur are mentioned, which is a decent start. The awkward repeated name and lack of any birthday or family context make it feel generated from a checklist.
  - [language, sev 2] "loved nothing more than Aarav's red toy dinosaur called Rory" incorrectly uses Aarav's in place of the possessive form his.
  - [fidelity, sev 3] Although Aarav, his age, Rory, Abbey Park, and Leicester appear, the supplied fifth-birthday outing, Meera, sibling relationship, and cloud-shape game are absent.
  - [text_image_fit, sev 2] The text locates the story specifically in "Abbey Park in Leicester," but the picture is a generic park with no identifying features.
  - [character_consistency, sev 3] Aarav has little or no visible short black hair and wears teal instead of the specified red dinosaur T-shirt.
- **Change I'd make:** Rewrite this as the actual birthday outing with Mum, Aarav, Meera, and Rory, and add recognisable crayon-style details that establish the park and characters.
- **Suggested rewrite:** On Aarav's fifth birthday, Mum took Aarav and his little sister, Meera, to Abbey Park in Leicester. Aarav brought his red toy dinosaur, Rory. He could not wait to show Meera the shapes he could see in the clouds.

#### Page 4
![I4](artifacts/capture_05/img_00.jpg)
> One evening Aarav gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* Aarav stands beneath a purple and pink evening sky with a few simple stars and trees. The image does not show cloud shapes, Meera, or the birthday activity.
- *Reaction:* I could see that he was looking at the evening sky, but I would not read this to a five-year-old. The long, difficult words sound like a machine produced them rather than a bedtime story.
  - [age_fit, sev 4] "The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation" uses vocabulary far beyond a five-year-old's reading level.
  - [fidelity, sev 4] The requested memory was Aarav teaching Meera to find shapes in the clouds, but neither Meera nor a shape-finding game appears.
  - [text_image_fit, sev 2] The text describes a profound emotional response to the sky, while the picture only shows a passive figure under a generic evening sky.
- **Change I'd make:** Replace the abstract prose with short spoken sentences and use the scene to begin the cloud-shape game between Aarav and Meera.
- **Suggested rewrite:** Aarav looked up at the sky. "Meera, what can you see?" he asked. Meera pointed to the clouds. "That cloud looks like a big rabbit!"

#### Page 5
![I5](artifacts/capture_06/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Aara pulled up his hood and ran for shelter, holding Aarav's red toy dinosaur called Rory tight.
- *Picture:* The picture repeats the basic daytime park scene with a bright sun, green trees, Aarav, and the same ambiguous red shape. There is no rain, puddle, hood, running movement, or clearly visible Rory.
- *Reaction:* I noticed the wrong spelling straight away, and the picture still looks sunny while the story says it is pouring with rain. This part is a clear mismatch between words and pictures.
  - [language, sev 3] Aarav is suddenly called "Aara", and "Aarav's red toy dinosaur" again uses the wrong possessive form.
  - [fidelity, sev 3] Rain, puddles, a hood, and running for shelter were invented and replace the requested fifth-birthday cloud activity with Meera.
  - [text_image_fit, sev 3] The text says "the rain began to pour" and "Big grey drops splashed into the puddles", but the image has a bright sun, no rain, and no puddles.
  - [text_image_fit, sev 3] The text requires a running child wearing a hood, while the pictured Aarav stands still in the same basic pose used earlier.
- **Change I'd make:** Remove the invented storm episode or regenerate the image with visible rain, puddles, a hood, running movement, and a clearly recognisable Rory; preserve the spelling Aarav.
- **Suggested rewrite:** A raindrop landed on Rory's nose. "Quick!" said Aarav. He tucked Rory under his red dinosaur T-shirt and ran with Meera to the big oak tree until the shower passed.

#### Page 6
![I6](artifacts/capture_07/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Aarav, follow me!" he called, and she followed him along the winding path.
- *Picture:* A simple adult figure labelled "Uncle Bartholomew" stands beside Aarav in a dim outdoor scene and carries a small yellow rectangle resembling a lantern. Meera is absent.
- *Reaction:* Nobody named Uncle Bartholomew is in our family memory, so introducing him feels intrusive. More importantly, Aarav is called 'she' immediately after being called 'he'.
  - [character_consistency, sev 4] "Aarav, follow me!" is followed by "and she followed him", contradicting the supplied pronouns he/him and the story's use of Aarav as a boy.
  - [fidelity, sev 3] "Uncle Bartholomew" was not supplied and Meera, the person who was supposed to be in the memory, is absent.
  - [coherence, sev 3] The story abruptly changes from Aarav running in rain to an invented uncle leading an unidentified 'she' along a path, with no explanation of who follows whom or why.
  - [text_image_fit, sev 2] The image depicts Aarav standing beside Uncle Bartholomew, not Aarav following him along a winding path, and the setting does not show the rain described on the previous page.
- **Change I'd make:** Delete the invented uncle, keep Aarav consistently male, and use this page to show Meera playing the cloud-shape game with him.
- **Suggested rewrite:** "Aarav, that cloud looks like Rory!" said Meera. Aarav smiled. Rory had a long neck, two small arms, and a tail. "Show me one more," said Aarav.

#### Page 7
![I7](artifacts/capture_08/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Aarav again. Aarav clutched a shiny red balloon and trembled in the dark.
- *Picture:* Aarav stands at night near trees, a crescent moon, and a floating red balloon. Rory is not shown, and the shadows do not visibly have teeth.
- *Reaction:* The red balloon is easy to see, but Rory has mysteriously vanished and Aarav is alone in a frightening story instead of being with Meera. The threat about never being found is too dark for this birthday bedtime book.
  - [age_fit, sev 3] "the shadows grew teeth and whispered that no one would ever find Aarav again" introduces frightening threat language for a five-year-old bedtime story.
  - [fidelity, sev 3] The woods, threatening shadows, balloon, and separation from Meera are invented, while the supplied sibling cloud-game memory is still missing.
  - [text_image_fit, sev 2] The picture shows a red balloon, but not the threatening toothy shadows central to the text or any woods deep enough to explain the danger.
  - [text_image_fit, sev 3] Rory is no longer visible despite being the supplied special object that Aarav brought to the park.
- **Change I'd make:** Replace the threatening scene with a gentle cloud-game development, show Meera and Rory together, and retain only a simple visual change in the cloud shapes.
- **Suggested rewrite:** The wind moved the clouds together. Meera spotted a long shape with a tail. "It's Rory!" she cried. Aarav held up his toy, and they both laughed because the real Rory was safe in his hand.

#### Page 8
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in Abbey Park in Leicester, there lived a curious child named Aarav. At last the sun came out, and Aarav skipped all the way home, happier than ever.
- *Picture:* Aarav stands in a simple sunny park with green trees. He is not shown skipping, going home, or accompanied by Meera, and the picture closely repeats earlier daytime scenes.
- *Reaction:* The opening sentence has simply been pasted in again, so the ending feels accidental. The picture also misses the family walk home that would make the ending warm and personal.
  - [coherence, sev 3] "Once upon a time, in Abbey Park in Leicester, there lived a curious child named Aarav" repeats the opening almost word for word instead of resolving the story.
  - [fidelity, sev 4] Meera is still absent from the ending, and the promised shared memory of teaching her to find cloud shapes has never happened.
  - [text_image_fit, sev 3] The text says Aarav "skipped all the way home", but he is shown standing in a generic park with no path-home action, Meera, or Mum.
- **Change I'd make:** Replace the repeated opening with a clear resolution in which Aarav and Meera finish their cloud game and walk home together.
- **Suggested rewrite:** Aarav and Meera found one last shape: a big smiling cloud that looked just like their dad. Then they gave Rory a birthday hug and walked home together, still laughing.

#### Page 9
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Aarav looked up at the sky, he would always remember The End
- *Picture:* An orange gradient end page shows "The End" above the same basic standing Aarav and trees. Meera, Rory, the park outing, and the cloud shapes are absent.
- *Reaction:* There are two "The End" lines, and the actual closing thought stops in the middle. This is the most obvious sign that I would be paying for an unfinished proof.
  - [language, sev 4] "whenever Aarav looked up at the sky, he would always remember" ends without punctuation or a completed thought, and "The End" is duplicated.
  - [coherence, sev 4] The final memory is unfinished, so the story has no completed emotional resolution.
  - [emotional_resonance, sev 4] The ending does not mention the birthday memory, teaching Meera, or the shared laugh, leaving it generic and incomplete.
  - [text_image_fit, sev 2] The final picture is a generic repeat of Aarav standing near trees and does not visually represent the unfinished memory sentence.
- **Change I'd make:** Complete one short closing sentence, remove the duplicate ending, and illustrate Aarav and Meera smiling at the cloud shapes while holding Rory.
- **Suggested rewrite:** The End From that day on, whenever Aarav looked at the clouds, he smiled because they always reminded him of the fun birthday game he had played with Meera.

#### Checkout
![I10](artifacts/capture_12/view_00.jpg)
![I11](artifacts/capture_12/view_01.jpg)
> Checkout Your price is reserved for 09:35 Hardcover: The Magical Adventrue of Aarav	£24.99  Premium gift wrap	£7.99 Shipping & handling	£12.99 Total	£37.98 Delivery Address Payment Card number Expiry CVC Pay now
- *Picture:* A mobile checkout page itemises the £24.99 hardcover, £7.99 premium gift wrap, £12.99 shipping, and £37.98 total, followed by address and card fields and a large orange Pay now button. The earlier preview also displays a regenerate button priced in dollars, creating a currency inconsistency.
- *Reaction:* At least, the full £37.98 total is shown before payment and I cannot see any subscription. I would not enter my card for this unfinished book, and the earlier $4.99 regeneration price in dollars makes me uneasy about currency and pricing clarity.
  - [language, sev 2] The checkout repeats the misspelled title "The Magical Adventrue of Aarav", and the preview page shows "Regenerate entire book – $4.99" alongside a GBP checkout.
  - [emotional_resonance, sev 3] The price is clear, but charging £37.98 for a visibly unfinished personalised keepsake would undermine trust in the product.
- **Change I'd make:** Correct the title, use one currency consistently, and prevent checkout or ordering until the proof has passed a final proofread and personalisation check. Keep the itemised total visible before card entry.
- **Suggested rewrite:** Checkout Hardcover: The Magical Adventures of Aarav — £24.99 Premium gift wrap — £7.99 Shipping & handling — £12.99 Total — £37.98 No subscription or additional charges. Delivery address and payment Pay now

**Top changes to the output:** 1. Rewrite the story around the supplied memory: Aarav's fifth birthday at Abbey Park, teaching his little sister Meera to find shapes in the clouds while holding Rory. | 2. Proofread every page: change "Adventrue" to "Adventure", fix "Aara", correct possessives and pronouns, complete the last sentence, and remove duplicate and placeholder text. | 3. Remove Uncle Bartholomew, the storm, the threatening woods, and the balloon, or replace them with gentle events that support the cloud-game memory. | 4. Regenerate all artwork in the selected crayon style, with consistent Aarav matching short black hair, big brown eyes, and a red dinosaur T-shirt, plus a clearly recognisable red Rory throughout. | 5. Include Meera visibly and consistently from her first appearance through the ending. | 6. Simplify the prose to short, concrete sentences suitable for an independent early reader around age five. | 7. Keep the upfront itemised checkout total, but use pounds consistently and correct the title before payment is enabled.

## Recommendations (participant's priorities)
- **[high] Rewrite the story around the supplied memory, with Aarav teaching Meera to find shapes in the clouds at Abbey Park on his fifth birthday.** (Generated storybook preview) - This is the personal part I wanted to buy. The current story leaves out Meera and turns the memory into something unrelated.
- **[high] Proofread the title and every page: fix “Adventrue”, “Aara”, possessives, pronouns, repeated text and the unfinished final sentence.** (Generated storybook preview) - The obvious mistakes make the present feel cheap and made me question whether the rest could be trusted.
- **[high] Match the generated artwork to the selected crayon style and keep Aarav, Meera and Rory visually consistent.** (Generated storybook preview) - The pictures are part of the gift. Getting pop-art instead of crayon, with generic characters, was disappointing.
- **[high] Use short, concrete sentences suitable for a five-year-old and remove frightening or unrelated events such as the threatening woods and storm.** (Generated storybook preview) - I need something gentle and readable for Aarav, not difficult vocabulary or a scary plot.
- **[high] Never pre-select premium gift wrap, and show the full price including delivery before I start creating the book.** (Home page and Hardcover checkout) - I need to know what it costs before spending ten minutes on a present. A £45.97 total with gift wrap already ticked felt like a trap.
- **[high] Explain what the paid regeneration button changes, how much it costs, and whether it is the only way to fix mistakes.** (Generated storybook preview) - I would not pay £4.99 without knowing what would improve, especially when the basic output was already wrong.
- **[high] Remove the unexplained profile sync error or explain plainly whether any details were affected.** (My books dashboard) - An error after a successful login immediately makes me wonder whether my account or family details are safe.
- **[high] Add clear privacy reassurance before the optional photo upload, including how the photo is used, stored and deleted.** (Optional photo upload) - A child's photo is much more sensitive than basic story details, so I need to know what happens to it.
- **[medium] Make the phone navigation fit properly and keep menu items on predictable lines.** (All mobile pages) - The wrapped navigation looks broken on my small phone and makes the site feel less trustworthy.
- **[medium] Replace jargon with plain language and give a short explanation beside the reading-level choices.** (Home page and Reading level and illustration) - “Multimodal generative narrative engine” means nothing to me, and I had to guess what the reading-level labels meant.
- **[medium] Make the next-page control a clearly labelled button and keep the gift-wrap checkbox attached to its label.** (Generated storybook preview and Hardcover checkout) - I use my phone one-handed, so unclear controls are easy to tap in the wrong place.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** It is for making a personalised birthday storybook with your child as the main character. I can imagine it being useful for parents looking for a quick, meaningful present.
- **What was the most frustrating or confusing moment, and why?** The generated book was the worst moment. I chose crayon style and got pop-art artwork, the title was misspelled, the story was frightening and unrelated in places, and the final sentence stopped halfway through.
- **What was the best moment?** The best moment was entering Aarav's details, Rory, Abbey Park and the cloud-shape memory. That part felt quick and exciting because I could see a real birthday present taking shape.
- **Was there any point where, in real life, you would have given up? Where and why?** I would probably have abandoned it at the preview. Reading nine pages only to find the important memory missing, with errors and a price hidden at the end, is too much effort for a present.
- **What did you expect to find or be able to do that wasn't there?** I expected Meera to be included and the birthday memory to be the heart of the story. I also needed the final price before spending all that time creating the book, and a clear explanation of the photo privacy.
- **Did you trust this website with your information (and your family's)? Why or why not?** I was happy to enter the fictional family details, but I would not have trusted it with a child's photo without clear privacy information. The unexplained profile sync error and misleading gift-wrap selection also made me cautious.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** Not for this version. Even a basic finished book would need to be around £25 including delivery to feel fair, and I would pay more only if the story really captured our memory, looked like the chosen style, and had no obvious errors.
- **If the site produced something for you, how do you feel about it overall?** It was recognisably about Aarav, but it felt like an unproofed draft rather than a keepsake. I would be too disappointed and embarrassed to give it to him for his birthday.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | Okay, that sounds like exactly what I need for Aarav. “Multimodal generative narrative engine” is far too much jargon, but the big “Proceed” button is obvious. I’ll log in first. | click |
| 2 | Log in – StoryHearth | reassured (1) | Okay, this is straightforward. I can see the email and password boxes immediately, and the big orange Log in button is obvious. I’ll fill those in and get on with Aarav’s book. | type; type; click |
| 3 | My books – StoryHearth | confused (0) | I'm logged in, and the big button is exactly what I need. The profile sync error looks a bit worrying, though—it doesn't tell me whether my account or family details are affected. I'll ignore it for now and try creating  | click |
| 4 | Create your book – StoryHearth | neutral (1) | This looks quick enough. I can fill in Aarav and Meera, but “Grandparent” being selected before I’ve even entered Meera feels a bit odd. I’ll change it to Sibling and continue. | type; select; select; type; type; select |
| 5 | Create your book – StoryHearth | reassured (1) | Yes, that’s all correct. I can see the choices stayed selected, and the big “Next” button is obvious. I’ll tap that and get on with the actual memory. | click |
| 6 | Create your book – StoryHearth | reassured (1) | This is straightforward and only three short things to fill in. I know exactly what to put: Abbey Park, Rory, and the cloud-shape memory on Aarav’s birthday. | type; type; type; click |
| 7 | Create your book – StoryHearth | pleased (1) | Good, this is a short choice screen. For Aarav at five I’ll choose the easiest reading level, and crayon sounds more like his kind of book. The navigation at the top wraps awkwardly, but the actual choices are clear. | click; click; click |
| 8 | Create your book – StoryHearth | reassured (1) | Good, it’s nearly ready. I’m not uploading a child’s photo without thinking about privacy, especially since it’s optional and I can work from the description already entered. I’ll tap “Create my book.” | click; wait_for_change |
| 9 | Your storybook – StoryHearth | annoyed (-1) | It worked, but I chose “Crayon” and this says “Pop-art comic,” so the style hasn’t matched what I selected. “Adventrue” is spelled wrong too. I still need to read all nine pages before checking the hardcover price. | flip_through |
| 10 | Your storybook – StoryHearth | annoyed (-1) | I’ve looked through all nine pages. The ending sentence is incomplete—“he would always remember” just stops there—which makes the finished present feel rushed. I won’t pay the $4.99 to regenerate; I’ll check the actual h | click |
| 11 | Checkout – StoryHearth | suspicious (-1) | There it is: £45.97 including delivery. That’s a lot for £24.99, and I didn’t ask for premium gift wrap—it was already ticked. I’m going to untick it so I can see the real basic cost clearly. I’m definitely not entering  | click |
| 12 | Checkout – StoryHearth | reassured (1) | Good, unticking the gift wrap worked and the total dropped by £7.99. So the real cost with delivery is £37.98, and I’m definitely stopping before the address and payment form. | done |
