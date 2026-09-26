# UserQA report: Daniel Okafor on http://127.0.0.1:8765/

*Persona:* **Daniel Okafor** (41) - Software engineer and early adopter who stress-tests every AI product he touches.  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 16 steps | *Pages reviewed:* 11 | *Issues:* 46 | *LLM calls:* 19 | *Wall time:* 344.4 s

## What the agent understood the website to be
- **what it is:** A web service that creates personalised, illustrated family storybooks from supplied characters, memories, places, and treasured objects.
- **who it is for:** Families wanting personalised stories featuring their children and other relatives or pets.
- **value proposition:** Turn a family memory into a custom illustrated digital storybook, with printed hardcover options.
- **pricing model:** A free digital preview is advertised; a separate Pricing link and printed hardcovers are mentioned, but no actual price is visible here.
- **fit for me:** Potentially a good fit for a space-themed story for Zara, but I need to assess character consistency, story quality, editing controls, and privacy before trusting it with family photos.
- **main tasks:** Log in, Add family characters, Describe a memory, Generate and read an illustrated preview, Find the price of a printed hardcover

## Scores
- SUS: **30.0** (grade F; 68 = industry average)
- UEQ-S: pragmatic 1.5, hedonic 0.0 (range -3..+3)
- Likelihood to recommend (0-10): 0
- Output keepsake-worthiness (1-5): 1
- Verdict: *"Promising concept, broken execution: the product ignored my inputs, misrepresented the family memory and failed the basic quality and privacy checks needed for a personalised children's keepsake."*

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 4 | TRUST | Privacy notice | Child-photo retention period is undefined | “Uploaded images may be retained to improve our services” | State a specific retention period for originals, generated derivatives, backups, and deleted-account data, and explain what happens when the account or book is deleted. |
| 4 | TRUST | Privacy notice | Use for service improvement is not distinguished from model training | “retained to improve our services” | State plainly whether customer photos and generated images are used for AI training, human review, or product analytics. If they are, require an explicit opt-in and never bundle consent with book crea |
| 3 | CONTENT | Generated storybook preview (x2) | Final-page sentence is incomplete | “And from that day on, whenever Zara looked up at the sky, they would always remember” | Validate generated sentences for syntactic completion and regenerate or flag incomplete output before presenting the preview. |
| 3 | H9 | My books dashboard | Raw error code and vague sync warning | “Error 0x80070057: profile sync incomplete.” | Replace the hexadecimal code with a plain-language message such as “We couldn’t refresh your saved profile. Your book has not been changed. Retry.” Add a working Retry control and explain which accoun |
| 3 | TRUST | My books dashboard | Potential profile reliability and privacy uncertainty | “profile sync incomplete” immediately after logging in | Clearly state whether profile sync is required, whether data was saved, and whether the user can continue safely; provide retry and support options. |
| 3 | H5 | Create your book — characters | Wrong default relationship creates a contradictory character setup | [11] Relationship is selected as “Grandparent” by default while the adjacent field says [10] “Who else is in the story?” | Use “Select…” as the initial relationship value and require an explicit choice before continuing. |
| 3 | H3 | Story details | Back preserves a corrupted truncated memory | Textbox [18] still ends with “It matters because it was o” and has no character counter or truncation warning. | Store the full field value separately, restore it after Back, and display a live character counter plus a warning when content is truncated. |
| 3 | H5 | Reading level and illustration style | Story field silently truncates valid input | The memory box now only shows 200 characters and the entered text ends with: “…favourite purple sock. It matters because it was o” | Show a live character counter before the limit, enforce the documented limit when input or submission begins, and block progression until the text fits or provide a non-destructive way to save longer  |
| 3 | H1 | Reading level and illustration style | Truncation occurred after submission without feedback | The typed 304-character value was accepted, but the box “only shows 200 characters” and the final sentence was cut off. | After validation, show “Story shortened to 200 characters” beside an error and focus the truncated field; never silently alter submitted content. |
| 3 | TRUST | Optional photo upload | Child-photo privacy handling is not disclosed before upload | The page says “Upload a clear photo of your child's face” but provides no nearby statement about training use, retention, third-party processing, or deletion. | Place a concise privacy summary beside the uploader stating whether photos are used for model training, who can process them, where they are stored, how long they are retained, and how a user requests |
| 3 | CONTENT | Generated storybook preview | Generated protagonist does not match the supplied appearance | The supplied description was “Black hair in two puffs, purple glasses, astronaut hoodie,” but the cover depicts a generic short-haired figure with no glasses or | Use appearance constraints during every page generation and run a consistency check against each character profile before publishing the preview. |
| 3 | H2 | Generated storybook preview | Output style contradicts the selected style | The preview states “Illustration style: Pop-art comic,” while I selected watercolour on the look-and-feel step. | Pass the selected style into generation, label the result with the actual style used, and prevent previewing if output style validation fails. |
| 3 | CONTENT | Generated storybook preview | The central memory objects are visually misunderstood | The cover shows what looks like a house with a rocket attached, while a standalone purple “J” is presented instead of clearly depicting a purple sock used as a  | Preserve the specified object relationships and use targeted prompts plus image checks for “cardboard rocket,” “purple sock,” and “sock used as a flag.” |
| 3 | CONTENT | Generated storybook preview | Final image remains inconsistent with the requested style | The cover and final image are flat, outlined vector-style illustrations despite watercolour being selected. | Pass the selected style into every image-generation call and validate the resulting style before loading the book. |
| 3 | DECEPTIVE | Hardcover checkout | Paid gift wrap is pre-selected by default | [6] checkbox “Premium gift wrap” (checked), with “£7.99” added and “Total £45.97”. | Default this optional add-on to unchecked and make any change update the total immediately with a short confirmation. |

## Page-by-page
### StoryHearth landing page  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Introduce the personalised family-story service and direct visitors to creation, pricing, or account login.
- **What's happening:** A static marketing page presents the proposition, primary calls to action, workflow, testimonials, FAQs, and legal/contact links. The supplied account has not yet been used.
- **First impression (Daniel):** "Clean enough and the task is immediately apparent, but the AI-heavy copy sounds engineered rather than warm or trustworthy. The promise is clear: family memories become illustrated books, but the actual quality and privacy handling remain unknown."
- **Cognitive walkthrough:** Q1 Yes, I would try creating a story because the three-step process sounds straightforward and directly matches what I want for Zara. / Q2 Yes. The prominent “Proceed →” control and separate “Log in” button are both obvious. / Q3 “Proceed →” is broadly understandable, though “Create my story” would be more specific. “Log in” exactly matches my immediate goal.
  - [CONTENT sev 2] **Marketing copy uses opaque technical jargon** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Replace this with plain language, for example: “Turn a family memory into a personalised illustrated story featuring your child.”
  - [H6 sev 2] **Editing control is deferred behind an FAQ** - evidence: [9] button "Can I edit the story?". Fix: State near “We write & illustrate” that generated stories can be edited or regenerated, with a direct link to an example or editing explanation.
  - [ACC sev 1] **Hero image has no accessible description** - evidence: [image (no description) 430x440]. Fix: Add meaningful alt text if it conveys content, or mark it explicitly decorative with alt="" if it is purely ornamental.
- **Positives:** The primary login and creation paths are visible without hunting.; The three-step workflow sets a clear expectation.; The page explicitly says the digital preview is free.; Privacy, Terms, and Contact links are available in the footer.

### Log in  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** Authenticate an existing StoryHearth customer so they can create and manage a personalised family storybook.
- **What's happening:** The page presents an empty email/password login form, a registration alternative, and supporting policy/contact links.
- **First impression (Daniel):** "Clean, conventional, and efficient. The main action is obvious, although the fields are not programmatically or visibly labelled and the footer is unusually washed out."
- **Cognitive walkthrough:** Q1 Yes, I immediately want to log in and test the actual story-generation workflow. / Q2 Yes, the two central fields and large "Log in" button are the first obvious controls. / Q3 Yes, the placeholders "Email" and "Password" describe the expected values, though persistent visible labels would be better.
  - [ACC sev 2] **Login fields have no persistent labels** - evidence: [5] and [6] are textboxes with no label, using only placeholders "Email" and "Password".. Fix: Add persistent visible <label> elements for "Email" and "Password", and associate each label with its input using for/id. Keep placeholders only as examples where useful.
  - [ACC sev 2] **Footer links have very low contrast** - evidence: The bottom links "Privacy", "Terms", and "Contact" appear extremely faint against the pale background.. Fix: Use a substantially darker text colour that meets WCAG contrast requirements and verify the disabled-looking treatment is intentional.
- **Positives:** The primary login button is large, clearly labelled, and easy to locate.; The layout is uncluttered and the form hierarchy is immediately understandable.; The page offers a direct route to create an account for new users.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** Shows the signed-in user’s existing storybooks and provides the main action for creating a new one.
- **What's happening:** The site has opened the signed-in dashboard, says there are no books, and offers a button to create one. A visible error says that profile sync is incomplete.
- **First impression (Daniel):** "The layout is clean and the next action is obvious, but the raw hexadecimal error and vague “profile sync incomplete” message feel like an internal failure leaked into the UI."
- **Cognitive walkthrough:** Q1 Yes. I want to create Zara’s book, and the dashboard appears to be the right place to start. / Q2 Yes. The prominent orange “+ Create a new book” button is immediately visible. / Q3 Yes. “Create a new book” exactly describes the action I need to take.
  - [H9 sev 3] **Raw error code and vague sync warning** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the hexadecimal code with a plain-language message such as “We couldn’t refresh your saved profile. Your book has not been changed. Retry.” Add a working Retry control and explain which account details are affected.
  - [TRUST sev 3] **Potential profile reliability and privacy uncertainty** - evidence: “profile sync incomplete” immediately after logging in. Fix: Clearly state whether profile sync is required, whether data was saved, and whether the user can continue safely; provide retry and support options.
  - [ACC sev 2] **Footer text has very low contrast** - evidence: “Privacy”, “Terms”, “Contact” and “© 2026 StoryHearth Ltd.” appear extremely faint.. Fix: Use WCAG-compliant text contrast and a darker footer treatment while preserving the current restrained design.
- **Positives:** The successful-login state is obvious.; The primary “+ Create a new book” action is prominent and clearly labelled.; The empty library is represented plainly rather than adding unnecessary onboarding.

### Create your book — characters  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Collect the main child and another character’s details before generating the personalised storybook.
- **What's happening:** The form presents fields for the child’s name, age, pronouns and appearance, followed by a second character’s name and relationship. The relationship currently defaults to “Grandparent,” and the other character’s description is not requested on this step.
- **First impression (Daniel):** "Visually simple and easy to scan, but the preselected “Grandparent” relationship is a bad default, and the form does not explain how these details will affect character consistency."
- **Cognitive walkthrough:** Q1 Yes, because this is the obvious setup step and the controls are all visible. / Q2 Yes, I immediately noticed the textboxes, dropdowns and orange “Next” button. / Q3 Mostly. The child fields match my goal, but “Who else is in the story?” is vague about whether I can add a full name and appearance, and it provides no field for Dad’s appearance.
  - [H5 sev 3] **Wrong default relationship creates a contradictory character setup** - evidence: [11] Relationship is selected as “Grandparent” by default while the adjacent field says [10] “Who else is in the story?”. Fix: Use “Select…” as the initial relationship value and require an explicit choice before continuing.
  - [CONTENT sev 2] **No description field for the second character** - evidence: [10] “Who else is in the story?” and [11] “Relationship” are the only controls for the second person; there is no appearance field.. Fix: Add an optional “What do they look like?” field for the second character.
  - [ACC sev 1] **Footer text and links have very low contrast** - evidence: The footer links “Privacy”, “Terms” and “Contact” appear extremely faint against the background.. Fix: Use WCAG-compliant text contrast and visibly increase the footer link contrast.
- **Positives:** The primary fields and Next action are visible without scrolling.; Labels are mostly explicit and the form has a simple visual hierarchy.; The child’s appearance is optional, which suits quick setup.

### Story details  (step 5)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_05.jpg)
- **Purpose:** Collect the setting, meaningful object, and source memory needed to generate a personalised story.
- **What's happening:** The form has three empty inputs: story location, special object, and a larger memory textarea. Back and Next controls sit below the fields.
- **First impression (Daniel):** "Clean and focused. The three questions are immediately understandable, unlike the vague AI language on the landing page; the footer links are again extremely faint."
- **Cognitive walkthrough:** Q1 Yes, I want to supply the specific memory and see whether the generated book remains faithful to it. / Q2 Yes, the fields are prominent and the orange Next button is the obvious primary control. / Q3 Yes. “Tell us the memory or idea behind your story” maps directly to what I need, while the first two fields are concise prompts rather than opaque AI terminology.
  - [H3 sev 3] **Back preserves a corrupted truncated memory** - evidence: Textbox [18] still ends with “It matters because it was o” and has no character counter or truncation warning.. Fix: Store the full field value separately, restore it after Back, and display a live character counter plus a warning when content is truncated.
  - [ACC sev 2] **Footer navigation has very low contrast** - evidence: The footer labels “Privacy”, “Terms”, “Contact” and “© 2026 StoryHearth Ltd.” are rendered in extremely faint grey.. Fix: Use WCAG-compliant text contrast for footer links and copyright text, ideally with a clearly visible focus and hover state.
- **Positives:** The form is compact and avoids unnecessary explanation.; Visible labels clearly identify every input.; The large textarea supports a detailed memory prompt.; Back gives me control without abandoning the draft.

### Reading level and illustration style  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** Choose the intended reading difficulty and visual treatment before generating the storybook.
- **What's happening:** Four Lexile reading-level options and three illustration styles are presented as radio groups. Lexile 200L–500L and Watercolour are currently selected, with Back and Next buttons below.
- **First impression (Daniel):** "Compact, uncluttered, and easy to scan. The explicit labels are good, though “Choose the look & feel” is broader than the actual controls on this step."
- **Cognitive walkthrough:** Q1 Yes, after I have verified the truncated memory text. / Q2 Yes, both radio groups and the Back/Next buttons are prominent. / Q3 Mostly. The style labels match, but “Choose the look & feel” is vague; I would rather it say “Reading level & illustration style.”
  - [H5 sev 3] **Story field silently truncates valid input** - evidence: The memory box now only shows 200 characters and the entered text ends with: “…favourite purple sock. It matters because it was o”. Fix: Show a live character counter before the limit, enforce the documented limit when input or submission begins, and block progression until the text fits or provide a non-destructive way to save longer text.
  - [H1 sev 3] **Truncation occurred after submission without feedback** - evidence: The typed 304-character value was accepted, but the box “only shows 200 characters” and the final sentence was cut off.. Fix: After validation, show “Story shortened to 200 characters” beside an error and focus the truncated field; never silently alter submitted content.
  - [H2 sev 1] **Heading does not precisely describe the controls** - evidence: “Choose the look & feel”. Fix: Rename the heading to “Choose the reading level and illustration style.”
  - [CONTENT sev 1] **No explanation of Lexile bands for lay users** - evidence: “Lexile BR–200L”, “Lexile 200L–500L”, “Lexile 500L–800L”, and “Lexile 800L+”. Fix: Add plain-English age or reading-ability descriptions beside each Lexile range, such as “Early reader” and “Independent chapter-book reader.”
- **Positives:** The selected states are immediately visible.; Radio groups make it clear that only one reading level and one illustration style can be chosen.; Back and Next are clearly available.; The layout is restrained and free of promotional clutter.

### Optional photo upload  (step 9)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_09.jpg)
- **Purpose:** Allows the user to optionally upload a child photo before generating the personalised book.
- **What's happening:** The user is on the final creation step, with no photo chosen, and can go Back or create the book without one.
- **First impression (Daniel):** "The layout is clean and the main button is obvious, but a child-photo uploader without a nearby privacy explanation is a red flag. I’m not comfortable uploading Zara’s image until I know how it is used and retained."
- **Cognitive walkthrough:** Q1 I would click “Create my book” now, but not upload a photo without clearer data-handling information. / Q2 Yes, the prominent “Create my book” button is immediately visible, and the optional file picker is also visible. / Q3 Yes, “Create my book” clearly matches my goal. The upload instruction also says the photo may help the illustrations resemble the child, though the claim is vague.
  - [TRUST sev 3] **Child-photo privacy handling is not disclosed before upload** - evidence: The page says “Upload a clear photo of your child's face” but provides no nearby statement about training use, retention, third-party processing, or deletion.. Fix: Place a concise privacy summary beside the uploader stating whether photos are used for model training, who can process them, where they are stored, how long they are retained, and how a user requests deletion.
  - [ACC sev 2] **File upload has no accessible label** - evidence: [30] is shown as “file-upload (no label)” while the visible control only says “Choose file” and “No file chosen.”. Fix: Add a visible or programmatically associated label such as “Child photo” and include accepted file types, maximum size, and basic photo guidance.
  - [ACC sev 2] **Footer links have very low contrast** - evidence: “Privacy”, “Terms”, and “Contact” appear extremely faint in the footer, while [13] and [14] show that relevant policies are linked there.. Fix: Use the same dark body-text colour for footer links, verify WCAG contrast, and make keyboard focus states clearly visible.
  - [CONTENT sev 1] **Likeness claim is vague and unsupported** - evidence: “Upload a clear photo of your child's face so the illustrations look like them.”. Fix: State that the photo is used as visual reference for the generated child character and avoid implying guaranteed facial accuracy.
- **Positives:** The upload is clearly marked optional, so the journey is not forced to include a child’s photo.; “Create my book” is prominent and its label precisely describes the next action.; A visible Back button preserves user control before generation.

### Book generation loading  (step 10)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_10.jpg)
- **Purpose:** Process the submitted family-memory details and generate the personalised book.
- **What's happening:** The create form has been replaced by a generic animated spinner. No generated book or preview is available yet, and the page contains no visible generation message, progress indicator, estimated time, retry control, or cancel/back action.
- **First impression (Daniel):** "The spinner is clean enough, but this is opaque and under-communicated. I know the product is probably generating because I clicked “Create my book”, but the interface has been stripped down to an ambiguous loop."
- **Cognitive walkthrough:** Q1 Yes, but I would only wait for a short period without more context because the screen gives no confidence about progress. / Q2 No relevant progress or cancel control is visible; only the animated spinner can be noticed. / Q3 No. There is no label or status message, so the visual does not tell me that my family story is being turned into pages, nor whether the optional-photo decision was accepted.
  - [H1 sev 2] **Loading state has no text or stage information** - evidence: The central bordered panel contains only an animated circular spinner.. Fix: Show a live status such as “Creating Zara’s story” followed by discrete stages like “Building the story”, “Illustrating 8 pages”, and “Almost ready”, plus an estimated time.
  - [H3 sev 2] **No cancel or back control while waiting** - evidence: No Cancel, Back, or “work in background” control appears beside the spinner.. Fix: Provide Cancel and Back controls, and explain whether cancelling preserves the entered story details.
  - [ACC sev 2] **Footer and inactive elements have extremely low contrast** - evidence: “Privacy”, “Terms”, “Contact”, and “© 2026 StoryHearth Ltd.” are rendered in barely visible pale grey.. Fix: Use WCAG AA contrast for footer text and links, including default and visited states.
- **Positives:** The animation makes some feedback visible immediately.; The loading panel is visually restrained and does not add distracting marketing content.; Global navigation remains available, including “My books” and “Pricing”.

### Generated storybook preview  (step 11)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_11.jpg)
- **Purpose:** Present the generated nine-page storybook so the user can inspect every page before ordering a hardcover.
- **What's happening:** The completed preview is open on page 1 of 9. The cover contains a generated illustration and title; controls allow forward navigation, paid whole-book regeneration, and ordering a hardcover.
- **First impression (Daniel):** "The player is easy to understand, but the first page fails the basic fidelity test: Zara’s defining appearance is absent, the style appears wrong, the title is misspelled, and the illustration is crude and semantically confused."
- **Cognitive walkthrough:** Q1 Yes, I would read through all nine pages now because I need to judge consistency, faithfulness, and suitability for a seven-year-old. / Q2 Yes, the right-arrow button and “1 / 9” counter are immediately visible. / Q3 The arrow clearly advances through the preview, but the labels “Regenerate entire book – $4.99” and “Order hardcover” do not reveal what can be edited locally before paying.
  - [CONTENT sev 3] **Generated protagonist does not match the supplied appearance** - evidence: The supplied description was “Black hair in two puffs, purple glasses, astronaut hoodie,” but the cover depicts a generic short-haired figure with no glasses or hoodie.. Fix: Use appearance constraints during every page generation and run a consistency check against each character profile before publishing the preview.
  - [H2 sev 3] **Output style contradicts the selected style** - evidence: The preview states “Illustration style: Pop-art comic,” while I selected watercolour on the look-and-feel step.. Fix: Pass the selected style into generation, label the result with the actual style used, and prevent previewing if output style validation fails.
  - [CONTENT sev 3] **The central memory objects are visually misunderstood** - evidence: The cover shows what looks like a house with a rocket attached, while a standalone purple “J” is presented instead of clearly depicting a purple sock used as a flag.. Fix: Preserve the specified object relationships and use targeted prompts plus image checks for “cardboard rocket,” “purple sock,” and “sock used as a flag.”
  - [CONTENT sev 3] **Final-page sentence is incomplete** - evidence: “And from that day on, whenever Zara looked up at the sky, they would always remember”. Fix: Validate generated sentences for syntactic completion and regenerate or flag incomplete output before presenting the preview.
  - [CONTENT sev 3] **Final image remains inconsistent with the requested style** - evidence: The cover and final image are flat, outlined vector-style illustrations despite watercolour being selected.. Fix: Pass the selected style into every image-generation call and validate the resulting style before loading the book.
  - [CONTENT sev 2] **Generated title contains an obvious misspelling** - evidence: The title reads “The Magical Adventrue of Zara” twice.. Fix: Run spelling and title validation before showing the cover, with a direct edit/regenerate-title option before purchase.
  - [H3 sev 2] **Only whole-book regeneration is exposed and it is paid** - evidence: [8] “Regenerate entire book – $4.99”. Fix: Provide per-page regenerate and edit controls, show their cost before activation, and retain successful pages when another page is changed.
  - [VALUE sev 2] **Hardcover price is not shown beside the order action** - evidence: [9] “Order hardcover” is visible only below the fold, while [8] shows a $4.99 regeneration price without context.. Fix: Keep the preview focused, then show a clear product summary and full hardcover price breakdown before checkout.
  - [CONTENT sev 2] **Zara is referred to as “they” despite supplied she/her pronouns** - evidence: “whenever Zara looked up at the sky, they would always remember”. Fix: Use the supplied child pronouns consistently in the generation prompt and post-generation checks.
  - [ACC sev 1] **Footer legal and contact links have very low contrast** - evidence: The footer labels “Privacy”, “Terms”, and “Contact” are rendered in extremely faint text against the white background.. Fix: Use WCAG-compliant text and link contrast, with a clearly visible hover or focus state.
- **Positives:** The 1-of-9 counter gives a clear indication of preview length.; Forward and backward navigation controls are easy to find.; The book can be inspected before navigating to checkout.

### Hardcover checkout  (step 14)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_14.jpg)
- **Purpose:** Configure delivery and payment for a printed hardcover copy.
- **What's happening:** The page itemises the £24.99 hardcover and £12.99 shipping, with a £7.99 premium gift wrap option already checked, for a £45.97 total. It also collects an address and card details, while a 09:57 price-reservation timer runs.
- **First impression (Daniel):** "The arithmetic is clear, but the default £7.99 add-on makes the total feel padded. At least there’s no hidden fee beyond the explicitly listed shipping and gift wrap."
- **Cognitive walkthrough:** Q1 Yes, but only to inspect the cost; I would not pay for this book after the poor preview. / Q2 Yes, the checked “Premium gift wrap” checkbox is immediately visible in the price summary. / Q3 The label and separate £7.99 price clearly describe the charge, although it should not have been selected by default.
  - [DECEPTIVE sev 3] **Paid gift wrap is pre-selected by default** - evidence: [6] checkbox “Premium gift wrap” (checked), with “£7.99” added and “Total £45.97”.. Fix: Default this optional add-on to unchecked and make any change update the total immediately with a short confirmation.
  - [VALUE sev 2] **Shipping cost is not qualified by destination or service** - evidence: “Shipping & handling £12.99” is shown before an address has been entered.. Fix: State what the charge covers, such as “UK standard tracked shipping,” and explain whether the amount changes after the address is entered.
  - [DECEPTIVE sev 2] **Artificial reservation countdown lacks context** - evidence: “Your price is reserved for 09:37”. Fix: Explain exactly how long the price is guaranteed and what the price becomes afterwards; avoid urgency unless there is a real deadline.
  - [ACC sev 2] **Footer links have very low contrast** - evidence: The bottom links “Privacy”, “Terms”, and “Contact” appear very faint against the white footer.. Fix: Use WCAG-compliant link contrast and visible keyboard focus states.
  - [DECEPTIVE sev 1] **Reservation countdown may create unnecessary urgency** - evidence: “Your price is reserved for 09:57” is presented prominently in red at the top.. Fix: Use neutral wording or omit the countdown until the user expresses clear intent to purchase, and explain exactly what expires.
- **Positives:** The hardcover, gift wrap, shipping, and total are itemised visibly.; Prices are in pounds and the total arithmetic is correct.; The page does not request card details before showing the price.

### Privacy notice  (step 16)
`http://127.0.0.1:8765/privacy.html`

![screenshot](screenshots/step_16.jpg)
- **Purpose:** Explain how StoryHearth handles account details, family stories, and uploaded child photographs, and present the associated terms.
- **What's happening:** I reached a standalone legal-information page. It acknowledges processing of names, stories, and photographs, states that uploaded images may be retained and handled by technology partners, and states that printed orders are non-refundable after production begins.
- **First impression (Daniel):** "The page is clean and easy to scan, but it reads more like a disclaimer than a usable privacy notice. The retention wording, unspecified partners, and “as-is” preview term are exactly the wrong things to say about a child’s photos and a visibly faulty generated book."
- **Cognitive walkthrough:** Q1 Yes, I would immediately look for retention, training use, deletion, processor, and rights details after being invited to upload Zara’s photo. / Q2 Yes, the navigation and checkout both provided a visible “Privacy” link, and it led here. / Q3 The label “Privacy” matches what I wanted to inspect, but the page title “Privacy notice” overpromises the amount of actual notice supplied.
  - [TRUST sev 4] **Child-photo retention period is undefined** - evidence: “Uploaded images may be retained to improve our services”. Fix: State a specific retention period for originals, generated derivatives, backups, and deleted-account data, and explain what happens when the account or book is deleted.
  - [TRUST sev 4] **Use for service improvement is not distinguished from model training** - evidence: “retained to improve our services”. Fix: State plainly whether customer photos and generated images are used for AI training, human review, or product analytics. If they are, require an explicit opt-in and never bundle consent with book creation.
  - [TRUST sev 3] **Secondary processing is vague** - evidence: “may be processed by our technology partners”. Fix: Name the processing categories and vendors where practical, list their countries or transfer mechanism, and specify that partner access is limited to providing the service.
  - [TRUST sev 3] **No practical privacy rights or controls** - evidence: The notice contains no stated access, correction, deletion, portability, objection, or automated decision-making process.. Fix: Add direct account and book deletion controls, explain how to request a copy or correction of data, identify any legal exceptions, and provide a functioning privacy-request channel.
  - [CONTENT sev 2] **The legal page conflates privacy and commercial terms** - evidence: The same page shows “# Privacy notice” and “## Terms,” with [7] “Terms” linking to /privacy.html#terms.. Fix: Separate privacy information from full terms of sale, with distinct pages and clear headings.
  - [CONTENT sev 2] **Faulty-output liability is disclaimed too broadly** - evidence: “Digital previews are provided as-is.”. Fix: Explain that customers can review, regenerate, edit, or report errors before ordering, and that printing is based on the version the customer approves.
  - [ACC sev 2] **Low-contrast footer text** - evidence: The footer links “Privacy,” “Terms,” “Contact,” and “© 2026 StoryHearth Ltd.” appear very faint against the white background.. Fix: Use WCAG AA contrast, a visible hover/focus state, and adequately sized footer links.
- **Positives:** The page is plainly labelled and the navigation action worked.; It explicitly acknowledges that names, stories, and uploaded photographs are processed rather than claiming there is no collection.; The content is concise enough to scan quickly.

## Generated output assessment
*Artifact:* AI-generated personalised nine-page children's storybook with illustrations and a checkout page

> I can see that the system used some of my keywords, but this is not the story I asked for and it is not print-worthy. The unresolved placeholders, misspelled title, wrong-looking Zara, invented uncle, disconnected plot, terrible age fit and misleading illustrations are obvious without even stress-testing the site. I would not print this or pay £45.97 for it.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | The output uses Zara, age 7, the living room, cardboard rocket, thunderstorm and purple sock in places, but it omits Dad/Daniel, invents Uncle Bartholomew, misnames Zara as Zar, repeats input-like phrases and replaces th |
| coherence | 1 | The story jumps from a living-room rocket to a sky, a rain scene, a winding path, threatening woods and a homecoming, while repeating the opening sentence and ending with an incomplete thought. |
| age fit | 1 | The text uses adult vocabulary such as "ephemeral", "crepuscular", "ineffable", "juxtaposing" and "existential trepidation", and the toothed-shadow wording is more ominous than necessary for a seven-year-old. |
| language | 1 | The output contains the misspelled title "Adventrue", raw placeholders "{{recipient_name}}" and "{{sender_name}}", the name error "Zar", awkward template phrasing, repeated sentences and an unfinished final sentence. |
| text image fit | 1 | Several images do not match their pages: rain is replaced by sunshine, the living room is replaced by an exterior, the sock is represented as a purple J, and the rocket is an ambiguous house-like shape. |
| character consistency | 1 | Zara is drawn as the same bald, green-clothed generic child throughout, but none of the supplied identifying features appear: black hair in two puffs, purple glasses or astronaut hoodie. The visual system therefore fails |
| visual quality | 1 | The illustrations are crude and repetitive, with flat generic shapes, ambiguous architecture, inconsistent detail between text and image, and a purple J that does not resemble the requested sock. The output labels the st |
| emotional resonance | 1 | The supplied memory was a loving shared adventure in which Zara felt brave imagining space with Dad, but the generated story omits Dad and substitutes a generic uncle, threatening woods, a balloon and repeated template l |

- **used correctly:** Zara's first name is generally used correctly on most pages.; The age 7 is included.; The living room, cardboard rocket, thunderstorm and purple sock appear in the text.; The name Zara appears repeatedly in the illustrations.
- **missing:** Dad's name, Daniel.; The parent relationship.; Zara's black hair in two puffs.; Purple glasses.; Astronaut hoodie.; The shared emotional point that Zara felt brave imagining space with Dad.; A coherent Moon journey.; A clear, recognisable purple sock used as a flag in the illustrations.
- **changed:** Dad was changed into an invented Uncle Bartholomew.; The living-room memory was changed into a generic outdoor adventure.; The purple sock was changed into a purple J-shaped symbol in the images.; Zara was incorrectly called Zar on page 5.; The title was changed to the misspelled "The Magical Adventrue of Zara".
- **invented:** Uncle Bartholomew.; A winding path.; Threatening toothed shadows in the woods.; A shiny red balloon.; A generic outdoor house or rocket setting not present in the supplied memory.

### Part by part
#### Cover
![I1](artifacts/capture_01/img_00.jpg)
> A StoryHearth original Illustration style: Pop-art comic The Magical Adventrue of Zara
- *Picture:* A simple pop-art style outdoor scene showing a small house or rocket-like building, a bald child in a green top labelled Zara, a bright sun, and a purple object shaped like a capital J rather than a sock.
- *Reaction:* This is not a credible representation of Zara or the memory I supplied. The title is misspelled, the character has none of the requested black puffs, purple glasses or astronaut hoodie, and the purple J does not communicate a sock.
  - [fidelity, sev 4] The requested character description was "Black hair in two puffs, purple glasses, astronaut hoodie", but the cover shows a bald child in a green top.
  - [language, sev 3] The title reads "The Magical Adventrue of Zara"; "Adventrue" is misspelled.
  - [text_image_fit, sev 4] The requested object is "A purple sock used as a flag", but the image shows a purple J-shaped symbol.
  - [visual_quality, sev 3] The cover is extremely generic, the rocket/house shape is ambiguous, and the purple symbol resembles a letter rather than a sock.
  - [character_consistency, sev 4] The illustrated Zara does not match the supplied appearance, so it is not an acceptable character reference for later pages.
- **Change I'd make:** Redesign the cover around Zara and Dad building a recognisable cardboard rocket in the living room during a thunderstorm, with Zara wearing her astronaut hoodie and the purple sock clearly tied to a flag. Correct the title to "The Magical Adventure of Zara".
- **Suggested rewrite:** The Magical Adventure of Zara

#### Title page
![I2](artifacts/capture_03/view_00.jpg)
> For {{recipient_name}}, with love from {{sender_name}}
- *Picture:* A website screenshot of page 2 showing the StoryHearth interface and a mostly empty white story panel; no actual story illustration is visible.
- *Reaction:* The page is not finished product copy. Both personalisation fields are exposed as raw template placeholders, and the screenshot makes clear that the page contains no usable illustration.
  - [language, sev 4] The page literally shows "{{recipient_name}}" and "{{sender_name}}".
  - [fidelity, sev 3] The page does not use the supplied recipient or sender information.
  - [text_image_fit, sev 3] No story picture is shown in the captured title page.
- **Change I'd make:** Replace the unresolved placeholders with the intended names and render a finished title-page illustration rather than exposing the website frame.
- **Suggested rewrite:** For Zara, with love from Dad

#### Page 3
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in The living room, where we built a cardboard rocket from boxes during a thunderstorm, there lived a curious child named Zara. Zara was 7 years old and loved nothing more than A purple sock used as a flag.
- *Picture:* The same generic outdoor scene as the cover: a bald child labelled Zara stands near a house or rocket-like structure under a bright sun. There is no visible living room, cardboard rocket, Dad, sock or thunderstorm.
- *Reaction:* The text contains several of my input phrases, but it reads like fields have been pasted into a template rather than turned into a story. The illustration contradicts almost every important visual detail.
  - [fidelity, sev 4] The text mentions "The living room" and a rocket, but the image shows an outdoor house-like object, with no Dad, cardboard construction or thunderstorm.
  - [language, sev 3] The sentence contains the awkward capitalisation "in The living room" and the field-like phrase "A purple sock used as a flag".
  - [character_consistency, sev 4] Zara is bald and wears a green top, not the specified black hair, purple glasses and astronaut hoodie.
  - [text_image_fit, sev 4] The text describes a living-room memory while the picture shows a generic exterior.
- **Change I'd make:** Rewrite this as a natural scene showing Zara and Dad in the living room with a clearly recognisable cardboard rocket, thunder at the window, and the purple sock tied to a small flag.
- **Suggested rewrite:** On a stormy evening, Zara and Dad built a rocket in the living room. They stacked cardboard boxes, taped on a window, and tied Zara's favourite purple sock to the top like a flag. "Ready for the Moon?" Dad asked. Zara grinned. "Ready!"

#### Page 4
![I4](artifacts/capture_05/img_00.jpg)
> One evening Zara gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* Zara stands outdoors beneath a purple and pink night sky with stars, next to the same generic house or rocket structure. The image does not show her looking upward through a living-room window or holding the sock.
- *Reaction:* The picture broadly supports a sky scene, but the prose is obviously aimed at an adult literary reader. A seven-year-old would need much simpler words, and the image still fails to carry the rocket-and-sock memory forward.
  - [age_fit, sev 4] The sentence uses "ephemeral", "crepuscular", "engendered", "juxtaposing", "ineffable" and "existential trepidation".
  - [language, sev 3] "The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy..." is excessively difficult and unnatural for the format.
  - [text_image_fit, sev 3] The image shows an outdoor night sky, but the established rocket, Dad and sock flag are absent.
  - [fidelity, sev 3] The requested relationship "Dad (Daniel)" does not appear anywhere in this page.
- **Change I'd make:** Use short, concrete sentences and keep the emotional focus on Zara feeling brave and excited rather than melancholy.
- **Suggested rewrite:** Outside, the thunder rumbled. Zara looked up at the dark sky and imagined the Moon glowing above the rooftops. She held Dad's hand and smiled. One day, she thought, our cardboard rocket might really fly.

#### Page 5
![I5](artifacts/capture_06/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Zar pulled up their hood and ran for shelter, holding A purple sock used as a flag tight.
- *Picture:* Zara stands outside beside the same house or rocket-like structure under a bright sun, next to a purple J-shaped object. There is no rain, puddle, hood detail, Dad, cardboard rocket or sock.
- *Reaction:* This is a major mismatch. The story says rain and shelter, while the picture shows sunshine and a static outdoor scene; the name is also misspelled as "Zar".
  - [fidelity, sev 3] The supplied name is "Zara", but the page says "Zar".
  - [text_image_fit, sev 4] The text describes pouring rain and puddles, while the image shows a clear sun and no rain.
  - [language, sev 3] "holding A purple sock used as a flag tight" is grammatically awkward and repeats the input label.
  - [character_consistency, sev 4] The illustrated Zara still has no black puffs, purple glasses or astronaut hoodie.
- **Change I'd make:** Keep the spelling Zara and show the actual thunderstorm: rain outside the living-room window, Dad helping Zara, and the sock tied securely to the cardboard rocket.
- **Suggested rewrite:** Thunder shook the window, and rain spilled from the clouds. Dad helped Zara carry the purple sock flag inside. "The rocket needs a crew," he said. Zara climbed aboard. "Let's go to the Moon!"

#### Page 6
![I6](artifacts/capture_07/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Zara, follow me!" he called, and she followed him along the winding path.
- *Picture:* A bald adult labelled Uncle Bartholomew stands beside Zara in an outdoor scene. The adult holds a small yellow rectangle, while the generic house or rocket structure remains in the background.
- *Reaction:* This is where the story invents a major character and removes the person I explicitly asked for. Uncle Bartholomew is not Dad, and the image still looks like a generic outdoor scene rather than our living-room adventure.
  - [fidelity, sev 4] I requested "Dad (Daniel)" with relationship "Parent", but the story introduces "Uncle Bartholomew" and never includes Dad.
  - [coherence, sev 3] The story moves from the living-room rocket and storm to a winding path with a newly invented uncle without explaining the transition.
  - [text_image_fit, sev 2] The image does include Bartholomew, but it does not show the lantern clearly or the winding path described in the text.
  - [character_consistency, sev 4] Bartholomew is a crude generic figure, while Zara does not match the supplied description.
- **Change I'd make:** Replace Uncle Bartholomew with Dad, Daniel, and make the sequence continue the cardboard-rocket launch from the living room.
- **Suggested rewrite:** Dad checked the cardboard boxes one last time. "All aboard, Zara!" he said. Zara sat behind the purple sock flag and gripped the sides of the rocket. With a loud countdown, they blasted off across the stormy living room.

#### Page 7
![I7](artifacts/capture_08/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would find Zara again. Zara clutched a shiny red balloon and trembled in the dark.
- *Picture:* Zara stands in a dark outdoor scene under a crescent moon with a red balloon, several trees, and a few stars. The requested living room, Dad and cardboard rocket are absent; the image does not visibly show toothed shadows.
- *Reaction:* The woods and balloon loosely match the text, but the story has abandoned the personal rocket adventure and becomes a generic threat scene. The wording is also more frightening than the rest of the book without serving the requested memory.
  - [fidelity, sev 4] The page replaces the shared Dad-and-Zara rocket memory with an unexplained trip into the woods and a red balloon.
  - [coherence, sev 4] There is no explanation for why Zara left the cardboard rocket or why she is now alone in the woods.
  - [age_fit, sev 3] "the shadows grew teeth" and "no one would find Zara again" introduce unnecessarily threatening imagery for a seven-year-old's keepsake.
  - [text_image_fit, sev 2] The red balloon and dark woods are present, but the toothed shadows and whispering threat are not clearly depicted.
  - [character_consistency, sev 4] Zara remains the same bald, green-clothed figure but still does not match the requested black-haired child in purple glasses and an astronaut hoodie.
- **Change I'd make:** Make this a benign imaginative Moon landscape, with Dad and Zara still together in the cardboard rocket and the sock flag clearly visible.
- **Suggested rewrite:** The cardboard rocket floated through the make-believe darkness. Zara saw a pretend forest of silver trees below. Dad pointed to a bright round Moon. "That is our destination," he said. Zara hugged the purple sock flag and felt brave.

#### Page 8
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in The living room, where we built a cardboard rocket from boxes during a thunderstorm, there lived a curious child named Zara. At last the sun came out, and Zara skipped all the way home, happier than ever.
- *Picture:* The same generic daytime outdoor scene appears again: Zara stands near the house or rocket-like building under a bright sun. There is no Dad, rocket, cardboard boxes, living room, sock flag or visible homecoming action.
- *Reaction:* The story repeats the opening sentence almost verbatim and then jumps to Zara going home. It feels assembled from disconnected prompts rather than written as a continuous keepsake story.
  - [coherence, sev 4] The opening sentence is repeated: "Once upon a time, in The living room..." and the transition to Zara skipping home is not connected to the preceding adventure.
  - [fidelity, sev 4] The image does not show the supplied living-room memory, Dad, cardboard rocket or purple sock flag, and the text barely mentions the important relationship.
  - [text_image_fit, sev 3] The text says Zara went home, while the image shows her standing outside the same ambiguous structure; no homecoming is depicted.
  - [language, sev 3] The capitalised sentence fragment "in The living room" and the repeated template-like opening are not polished story copy.
- **Change I'd make:** Do not repeat the opening. Resolve the actual memory: Dad and Zara return from their pretend Moon adventure, place the sock flag by the window, and remember feeling brave.
- **Suggested rewrite:** When the thunder passed, Dad and Zara landed their cardboard rocket safely in the living room. Zara carefully took down the purple sock flag. "We really flew to the Moon," she said. Dad smiled. "We sure did."

#### Page 9
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Zara looked up at the sky, they would always remember The End
- *Picture:* A generic orange sunset scene with the same bald child in green clothing, the ambiguous house or rocket structure, and no visible purple sock flag, Dad, rocket interior, or personal detail.
- *Reaction:* The page contains an unfinished sentence and repeats "The End" awkwardly. The pronoun "they" also does not match the established girl character, and the picture gives no meaningful closing image for this family memory.
  - [language, sev 4] The sentence ends with "they would always remember" without a finishing phrase, and "The End" is repeated.
  - [coherence, sev 4] The incomplete final sentence prevents the story from reaching a complete emotional conclusion.
  - [fidelity, sev 3] The closing image omits Dad, the cardboard rocket and the purple sock flag, which are the most distinctive parts of the supplied memory.
  - [character_consistency, sev 4] Zara remains bald and green-clothed, with none of the supplied identifying features.
  - [text_image_fit, sev 3] The text refers to remembering the sky, while the image is a generic sunset and does not show the rocket or Dad.
- **Change I'd make:** Finish the sentence, remove the duplicate ending, and close on Dad and Zara together with the cardboard rocket and sock flag.
- **Suggested rewrite:** The End From that day on, whenever Zara looked up at the sky, she remembered the thunder, the cardboard rocket, and Dad beside her in the living room. She smiled. That was the day she felt brave enough to dream of space.

#### Checkout
![I10](artifacts/capture_13/view_00.jpg)
![I11](artifacts/capture_13/view_01.jpg)
> Checkout Your price is reserved for 09:42 Hardcover: The Magical Adventrue of Zara	£24.99  Premium gift wrap	£7.99 Shipping & handling	£12.99 Total	£45.97 Delivery Address Payment Card number Expiry CVC Pay now
- *Picture:* A StoryHearth checkout page showing the hardcover, a selected premium gift-wrap checkbox, shipping and handling, total, address and payment fields, and a Pay now button. The title is visibly misspelled.
- *Reaction:* The checkout is functional-looking, but it offers a £45.97 book with a broken title, unresolved story quality and no visible explanation of what happens to the submitted family information or photos. I would not proceed with payment.
  - [language, sev 3] The checkout repeats the misspelled title "The Magical Adventrue of Zara".
  - [fidelity, sev 2] The purchase summary does not identify the supplied personalisation details or indicate that the book contains the requested Dad-and-Zara memory.
  - [language, sev 2] The captured page shows a small empty-looking gift-wrap checkbox beside the price, while the text summary does not clearly explain the selection state.
  - [visual_quality, sev 2] The checkout itself is usable, but the purchase is attached to a visibly defective product rather than a finished book.
- **Change I'd make:** Do not offer checkout until the generated book has passed title, placeholder, character, illustration, continuity and final-sentence checks. Also provide a clear privacy notice explaining whether a child's photos are used for training, how long they are retained, and how to request deletion.

**Top changes to the output:** 1. Replace Uncle Bartholomew with Dad/Daniel and make the cardboard-rocket memory the central story from beginning to end. | 2. Use a consistent Zara model with black hair in two puffs, purple glasses and an astronaut hoodie, and show the purple sock as a clearly recognisable flag. | 3. Replace the adult vocabulary and threatening woods passage with simple, warm, age-seven language and a positive space-adventure arc. | 4. Fix all output defects before checkout: correct "Adventure", resolve all placeholders, remove repeated text, complete the final sentence, and run an automated preflight check. | 5. Show clear, specific privacy and retention information for any uploaded child photos or personal data, including whether they are used for training and how to request deletion.

## Recommendations (participant's priorities)
- **[high] Generate a faithful, coherent story that preserves the supplied family relationships, pronouns, memory, central objects and beginning-to-ending plot.** (Generated storybook preview) - The current book omits Dad, invents an uncle, changes Zara's name and loses the cardboard-rocket adventure.
- **[high] Keep Zara visually consistent with her specified black puffs, purple glasses and astronaut hoodie, and make the purple sock a recognisable flag.** (Generated storybook preview) - The defining character and object details are the reason a personalised keepsake is valuable; ignoring them makes the images generic and inaccurate.
- **[high] Run an output preflight check that removes unresolved placeholders, spelling errors, repeated sentences, wrong names, wrong pronouns and incomplete sentences before presenting the book.** (Generated storybook preview) - The current output contains obvious template and language defects that should never reach a checkout page.
- **[high] Stop silently truncating the memory and story fields; show character counts, preserve the full value after Back, and provide a clear way to replace the entire affected text safely.** (Create your book — Story details) - Silent data loss is a basic trust failure and directly damages fidelity to the user's memory.
- **[high] Provide specific privacy disclosures before child-photo upload, including training use, retention period, processors, deletion rights and whether images are used to improve the service.** (Optional photo upload and Privacy) - Zara is a child, and the current policy does not provide enough information to make an informed decision.
- **[high] Honour the selected illustration style and clearly show the actual selected style throughout generation and the finished book.** (Reading level and illustration style / Generated storybook preview) - Selecting watercolour and receiving flat pop-art or vector-style images is a direct contradiction that damages trust.
- **[medium] Set relationship defaults safely, require confirmation for contradictory character setups, and provide description fields for all characters where needed.** (Create your book — Characters) - The default Grandparent relationship created the wrong family structure before I corrected it, and there was no field for the second character's description.
- **[high] Add targeted editing and regeneration controls for a single image, character, object or scene rather than exposing only whole-book regeneration.** (Generated storybook preview) - A good overall story should not be lost because one page has a visual or text error, and paid whole-book regeneration is a poor workaround.
- **[high] Replace the raw sync error with an actionable message that explains whether the profile is affected, whether creation is safe, and how to recover.** (My books) - A raw Windows-style error is alarming and leaves me guessing whether my family data is reliable.
- **[medium] Add text-based loading status, generation stages, an estimated wait and a cancel or back control.** (Book generation loading) - A spinner without status or recovery options makes the system feel fragile and gives me no control while waiting.
- **[medium] Make hardcover price visible next to the order action, uncheck paid gift wrap by default, and explain shipping basis and delivery scope.** (Generated storybook preview and Hardcover checkout) - The checkout introduced a hidden £12.99 gift-wrap charge and did not make the £24.99 book plus £12.99 shipping cost clear beforehand.
- **[medium] Use persistent visible labels for form controls, including the photo upload field, and improve footer contrast and accessible descriptions.** (Login, Create your book, Optional photo upload and StoryHearth landing page) - Placeholder-only labels, an unlabelled upload and low-contrast links create unnecessary accessibility problems.
- **[low] Replace opaque marketing terms with plain descriptions of the generation process and what the product actually does.** (StoryHearth landing page) - “Multimodal generative narrative engine” and “lived-experience corpus” sound like jargon rather than useful product information.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** StoryHearth is meant to create personalised, illustrated storybooks featuring the user and their family, with a printable or hard-cover edition. In principle, that is useful for parents who want a keepsake built around a real family memory, especially for younger children.
- **What was the most frustrating or confusing moment, and why?** The generated book was the worst moment: Zara had the wrong appearance, the selected watercolour style was ignored, Dad was replaced by an invented uncle, central objects were misunderstood, and the final sentence was unfinished. The undefined child-photo retention policy was nearly as serious.
- **What was the best moment?** The best moment was reaching the storybook preview because I was genuinely curious to see whether the system could turn the cardboard-rocket memory into a coherent space story. The concept was promising, but the result immediately exposed major generation defects.
- **Was there any point where, in real life, you would have given up? Where and why?** In real life, I would probably have abandoned the process after seeing the book preview, or at least after the incomplete ending and mismatched illustrations. Paying for a hardcover after that would feel irrational, and the £45.97 checkout reinforced that decision.
- **What did you expect to find or be able to do that wasn't there?** I expected the system to preserve my full memory, follow the relationship and character details, keep Zara visually consistent, honour the selected art style, and make a specific object or scene editable or regenerable. I also expected clear answers before upload about whether Zara's photos are used for training, who processes them, how long they are retained, and how deletion works.
- **Did you trust this website with your information (and your family's)? Why or why not?** I would not trust StoryHearth with Zara's information or photos. The upload screen gave no privacy assurance, and the privacy notice only said images may be retained and used to improve the service, without a defined retention period or named processors.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would pay for a genuinely polished keepsake, but I would not pay for this output. I would need a real preview of the final quality and a fair price; a hard cover around £25–30 before shipping would be more acceptable, with the option to repair and approve individual pages before ordering.
- **If the site produced something for you, how do you feel about it overall?** The output is not print-worthy and does not represent the story I supplied. It mostly used keywords while producing incorrect characters, disconnected scenes, adult language, unresolved placeholders, a typo, an unfinished sentence and misleading illustrations. I would not pay £45.97 for it.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | The product sounds relevant, but the phrase “multimodal generative narrative engine” and “lived-experience corpus” is needless AI jargon. I want to see the actual workflow and quality, so I’ll log in first with the suppl | click |
| 2 | Log in – StoryHearth | neutral (0) | Straightforward and visually clean. I can immediately see the login action, but the inputs have placeholders rather than proper visible labels, and the footer text looks very faint. I’m entering the supplied account deta | type; type; click |
| 3 | My books – StoryHearth | annoyed (-1) | I’m logged in, but that raw Windows-style error is a poor sign. “Profile sync incomplete” is ambiguous: it doesn’t say whether my saved family details are affected or whether I can still create the book. The create butto | click |
| 4 | Create your book – StoryHearth | annoyed (-1) | This is a clean, compact form, but the default relationship of “Grandparent” is actively dangerous because I’m entering Dad. I’m also slightly annoyed that my saved profile hasn’t prefilled Zara, especially after the syn | type; select; type; type; select; click |
| 5 | Create your book – StoryHearth | curious (1) | This is a sensible progression and the labels are clear. I’ll give the model the concrete setting, object, and memory rather than vague prompts, then generate the book and judge whether it actually follows them. | type; type; type; click |
| 6 | Create your book – StoryHearth | annoyed (-1) | The controls are clear, but I caught a more important defect on the previous step: the memory field silently truncated my 304-character input to 200 and cut off the end. I’m going Back to fix that before generating, beca | click |
| 7 | Create your book – StoryHearth | frustrated (-1) | Good, Back preserved most of the form, but the textarea is still corrupt at the 200-character boundary and there’s no clear way to replace just the text. The useful core survived—the living-room rocket, thunderstorm, Moo | click |
| 8 | Create your book – StoryHearth | curious (1) | The reading range is appropriate for Zara, and the controls are clear enough. I’ll keep the watercolour style and click Next to generate the preview, then inspect the whole book rather than judging the marketing copy. | click |
| 9 | Create your book – StoryHearth | suspicious (0) | I’m skipping the upload because it’s optional and this page gives me no privacy assurance for Zara’s image; I’d want that clarified before uploading. The final action is obvious, so I’ll create the book without a photo a | click |
| 10 | Create your book – StoryHearth | impatient (-1) | The click did trigger something, but this is weak system feedback. I can infer generation from the spinner and the context, yet the page gives me no status, progress, timeout expectation, or cancel control, so I’m going  | wait_for_change |
| 11 | Your storybook – StoryHearth | frustrated (-2) | This is already off. Zara looks nothing like the girl I described—no black puffs, purple glasses, or astronaut hoodie—and the output says “Pop-art comic” even though I selected watercolour. The title has the typo “Advent | flip_through |
| 12 | Your storybook – StoryHearth | frustrated (-2) | The ending is grammatically broken: “whenever Zara looked up at the sky, they would always remember” has no remembered thing. The image is also still flat vector art rather than the selected watercolour style, and Zara s | scroll |
| 13 | Your storybook – StoryHearth | frustrated (-2) | The ending is still plainly broken, and the illustration has lost the purple glasses, astronaut hoodie, and the purple-sock flag from the supplied memory. I’ve finished checking every page; now I’m following Order hardco | click |
| 14 | Checkout – StoryHearth | annoyed (-1) | There it is: £45.97, with gift wrap silently pre-selected. I’m unchecking that so I can see the genuine unavoidable cost, then I’ll inspect the rest of checkout without entering any personal or payment details. | click; scroll |
| 15 | Checkout – StoryHearth | suspicious (-1) | The unavoidable cost is £24.99 for the book plus £12.99 shipping. That countdown is suspiciously pushy without explaining what happens to the price afterward, and I’m not entering payment details. I’ll open Privacy now t | click |
| 16 | Privacy – StoryHearth | suspicious (-2) | This is technically worse than the sparse upload screen, because it confirms that Zara’s images may be retained and used to improve the service without defining how long they remain or who processes them. “May be process | done |
