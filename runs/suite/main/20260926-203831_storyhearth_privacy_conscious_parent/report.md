# UserQA report: Elena Petrova on http://127.0.0.1:8765/

*Persona:* **Elena Petrova** (45) - Paralegal and mother who reads the privacy policy before trusting a site with her child's data.  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 16 steps | *Pages reviewed:* 10 | *Issues:* 34 | *LLM calls:* 19 | *Wall time:* 404.0 s

## What the agent understood the website to be
- **what it is:** A website that generates personalised, illustrated family storybooks and apparently offers printed hardcovers.
- **who it is for:** Families wanting stories featuring their children and other relatives or pets.
- **value proposition:** Turn a family memory into a bespoke illustrated storybook that can be previewed digitally and potentially printed as an heirloom.
- **pricing model:** The page says there is a free digital preview, but it gives no actual printed-book price here.
- **fit for me:** Potentially a good fit because it promises a reassuring story about Nikolai at his new school, but I do not yet trust it enough to enter family information or upload anything.
- **main tasks:** Log in, Describe the child and another character, Provide details of a family memory, Generate and read a storybook preview, Check the price of a printed hardcover

## Scores
- SUS: **27.5** (grade F; 68 = industry average)
- UEQ-S: pragmatic -1.5, hedonic 0.0 (range -3..+3)
- Likelihood to recommend (0-10): 1
- Output keepsake-worthiness (1-5): 1
- Verdict: *"A promising idea, but I would not trust it with Nikolai's details or pay for a book that changes his name, ignores my instructions and uses pressure at checkout."*
- Would have abandoned at step 5 (127.0.0.1:8765/privacy.html \| Privacy notice): The privacy notice is too vague about retention, technology partners, AI use and deletion to share sensitive information about my child. [self-report]

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 4 | TRUST | Privacy and terms | Data retention and deletion are unspecified | “Uploaded images may be retained to improve our services” | State specific retention periods for each type of data, explain when deletion occurs, and provide a clear account or contact process to request deletion. |
| 4 | TRUST | Privacy and terms | Technology partners are unidentified | “may be processed by our technology partners” | Name the relevant processors and describe their role, location, data categories, and whether uploaded images or generated content are used to train AI or improve models. |
| 3 | H9 | My books dashboard (x2) | Unexplained technical profile-sync error | “Error 0x80070057: profile sync incomplete.” | Replace the code with a plain-language message explaining what did not sync, whether any information was lost, and give a clear Retry or Contact support action. |
| 3 | H1 | My books dashboard | Technical error shown without status or effect | The warning only says “profile sync incomplete” and does not state whether the rest of the account works. | Add a short impact statement, such as “Your saved account details are safe. Some optional profile fields are temporarily unavailable,” and show a current status. |
| 3 | CONTENT | Privacy and terms | Purpose of image processing is too vague | “to create your book” and “improve our services” | Separate essential processing from optional model training or product improvement, state the purposes plainly, and require an explicit opt-in for any optional use. |
| 3 | CONTENT | Privacy and terms | Terms are not a substitute for full terms | “Digital previews are provided as-is.” | Provide complete terms covering preview limitations, errors, corrections, production approval, cancellation, refunds, delivery and customer support. |
| 3 | VALUE | Privacy and terms | Cancellation and refund limitation is abrupt | “Printed orders are non-refundable once production begins.” | Explain the exact production stage, show cancellation and refund rules before checkout, and state remedies for damaged, delayed or materially incorrect books. |
| 3 | TRUST | Optional photo upload | Photo upload lacks specific privacy disclosure | “Upload a clear photo of your child's face so the illustrations look like them.” The page itself does not explain whether the image is used for AI training, who | Place a concise disclosure beside the upload stating whether photos train AI, named categories of processors or recipients, retention periods, deletion rights, and whether deleting the book also delet |
| 3 | H2 | Generated storybook preview | Selected illustration style was not applied | The page says “Illustration style: Pop-art comic,” while the earlier selection was “Watercolour — soft and dreamy.” | Apply the selected style to the generated book and, if the style cannot be reproduced, explain the substitution before generation. |
| 3 | CONTENT | Generated storybook preview | Generated cover does not reflect the supplied character details | I entered “blond straight hair, gap in his front teeth, yellow raincoat,” but the cover shows Nikolai with blond hair, no visible gap in his front teeth, and no | Use the supplied appearance details consistently across the cover and story, and tell the user which details could not be represented. |
| 3 | CONTENT | Generated storybook preview | The final sentence is incomplete | “And from that day on, whenever Nikolai looked up at the sky, he would always remember” | Generate a complete final sentence that identifies what Nikolai remembered and connect it explicitly to bravery and the stone. |
| 3 | DECEPTIVE | Hardcover checkout | Optional gift wrap is pre-selected | [6] checkbox "Premium gift wrap" (checked), with "£7.99" added and "Total £45.97" | Default every optional add-on to unchecked, make it a separate clearly labelled section, and update the total only after an affirmative choice. |
| 2 | ACC | My books dashboard, Optional photo upload (x2) | Footer links have very low contrast | The visible “Privacy,” “Terms,” and “Contact” links are extremely pale against the footer background. | Use darker, higher-contrast text and meet WCAG contrast requirements for all footer links. |
| 2 | CONTENT | Generated storybook preview, Hardcover checkout (x2) | Typographical error in the book title | The cover and heading read “The Magical Adventrue of Nikolai.” | Use a spelling check and correct “Adventrue” to “Adventure” before displaying or printing the title. |
| 2 | CONTENT | StoryHearth landing page | Overly technical language obscures what is shared with the service | “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.” | Replace this with plain language, for example: “Tell us about a family memory. We use the details you provide to create a story and illustrations for you only.” Link directly to a clear data-use summa |

## Page-by-page
### StoryHearth landing page  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Explain the service, show how creation works, and direct visitors to creation, pricing, privacy, and login.
- **What's happening:** The landing page advertises AI-generated family stories, offers “Proceed” and “See pricing” controls, explains three creation steps, includes testimonials and FAQ links, and provides Privacy, Terms, and Contact links below the fold.
- **First impression (Elena):** "It looks warm and professionally designed, but the jargon in the main description immediately makes me cautious about what data is collected and how it is used."
- **Cognitive walkthrough:** Q1 Not yet. I would inspect Privacy and Terms before creating a story or entering family information. / Q2 Yes, I notice “Proceed,” “See pricing,” and the footer links for “Privacy” and “Terms.” / Q3 “Proceed” is too vague about what happens next, while “See pricing” clearly suggests viewing costs; “Privacy” and “Terms” are the relevant labels for my immediate concern.
  - [CONTENT sev 2] **Overly technical language obscures what is shared with the service** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Replace this with plain language, for example: “Tell us about a family memory. We use the details you provide to create a story and illustrations for you only.” Link directly to a clear data-use summary.
  - [ACC sev 2] **Main illustration has no accessible description** - evidence: [image (no description) 430x440]. Fix: Add concise alternative text describing the relevant book-preview illustration, or mark it as decorative if it adds no information.
  - [VALUE sev 2] **Printed price is not visible on the landing page** - evidence: “Free digital preview · Printed hardcovers shipped across the UK”. Fix: Show a clear “Digital preview: free; hardcover from £X” statement and link to the full price list.
  - [H2 sev 1] **Creation action does not disclose the next step** - evidence: [5] link “Proceed →”. Fix: Rename the link “Start your story” and state beneath it: “You’ll sign in and enter family details; you can review privacy information first.”
- **Positives:** The three-step explanation is easy to scan.; The page explicitly says the digital preview is free.; Privacy, Terms, and Contact links are present without requiring account creation.; The overall design is calm and family-oriented, with no visible countdown or false scarcity.

### Log in  (step 3)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** Allow an existing StoryHearth customer to access their account.
- **What's happening:** The page displays empty email and password fields and a login button. Navigation and policy links are visible above and below the login card.
- **First impression (Elena):** "It looks calm, uncluttered and easy to understand. Privacy and Terms are available without creating another account, which is a good sign."
- **Cognitive walkthrough:** Q1 Yes, I am ready to log in using the account details supplied for this study. / Q2 Yes, the Email and Password fields and the orange “Log in” button are visually prominent. / Q3 Yes, although the fields have placeholders rather than persistent visible labels.
  - [ACC sev 2] **Email and password fields lack persistent visible labels** - evidence: Items [5] and [6] are described as textboxes with no label and rely on the placeholders “Email” and “Password”.. Fix: Add persistent visible labels such as “Email address” and “Password” associated with the controls, while retaining placeholders only as supplementary examples.
- **Positives:** The primary login action is large and clearly labelled.; Privacy and Terms links are visible in the footer.; The page is visually restrained and contains no urgency messaging or distracting sign-ups.; The account-creation link is clearly separated as optional.

### My books dashboard  (step 4)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** This page confirms the signed-in account and provides access to create or manage family storybooks.
- **What's happening:** The site says the account has no books and offers a button to create one. A warning reports an incomplete profile sync, but it provides no plain-language explanation or recovery action.
- **First impression (Elena):** "The basic layout is easy to understand, but the raw hexadecimal error immediately makes me wonder whether my account or any future family data is incomplete."
- **Cognitive walkthrough:** Q1 I would not enter Nikolai's information yet; I would first investigate the profile-sync warning and read the privacy policy. / Q2 Yes, the “+ Create a new book” control is prominent, and the “Privacy” link is visible in the footer. / Q3 Yes, “Create a new book” clearly matches my goal, although I do not yet trust the creation process enough to use it.
  - [H9 sev 3] **Unexplained technical profile-sync error** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the code with a plain-language message explaining what did not sync, whether any information was lost, and give a clear Retry or Contact support action.
  - [H1 sev 3] **Technical error shown without status or effect** - evidence: The warning only says “profile sync incomplete” and does not state whether the rest of the account works.. Fix: Add a short impact statement, such as “Your saved account details are safe. Some optional profile fields are temporarily unavailable,” and show a current status.
  - [ACC sev 2] **Footer links have very low contrast** - evidence: The visible “Privacy,” “Terms,” and “Contact” links are extremely pale against the footer background.. Fix: Use darker, higher-contrast text and meet WCAG contrast requirements for all footer links.
  - [H9 sev 2] **Technical error remains unexplained** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Explain in plain English what the error means, say whether any information was affected, and provide a retry or support option.
- **Positives:** The successful-login state is explicit with “Welcome back, Demo.”; The “+ Create a new book” control is visible and plainly labelled.; Privacy, Terms, and Contact links are available without creating another book.

### Privacy and terms  (step 5)
`http://127.0.0.1:8765/privacy.html`

![screenshot](screenshots/step_05.jpg)
- **Purpose:** To explain how StoryHearth handles family information, photographs, previews and printed orders.
- **What's happening:** I am viewing a short privacy notice and terms summary. No form or account controls are present, and there is no clear route to request deletion or ask questions about data handling.
- **First impression (Elena):** "I expected a proper privacy policy with specific retention periods, named or clearly described recipients, deletion rights, and details about automated processing. Instead I see broad and potentially alarming wording, so I do not trust it enough to upload a child’s data."
- **Cognitive walkthrough:** Q1 No. I would not upload Nikolai’s photo or submit his story after reading this. / Q2 I noticed the Privacy, Terms and Contact links, and the Terms link is present, but there is no delete-data control or privacy settings link. / Q3 The heading “Privacy notice” matches the broad goal, but the content does not clearly answer what happens to my child’s information.
  - [TRUST sev 4] **Data retention and deletion are unspecified** - evidence: “Uploaded images may be retained to improve our services”. Fix: State specific retention periods for each type of data, explain when deletion occurs, and provide a clear account or contact process to request deletion.
  - [TRUST sev 4] **Technology partners are unidentified** - evidence: “may be processed by our technology partners”. Fix: Name the relevant processors and describe their role, location, data categories, and whether uploaded images or generated content are used to train AI or improve models.
  - [CONTENT sev 3] **Purpose of image processing is too vague** - evidence: “to create your book” and “improve our services”. Fix: Separate essential processing from optional model training or product improvement, state the purposes plainly, and require an explicit opt-in for any optional use.
  - [CONTENT sev 3] **Terms are not a substitute for full terms** - evidence: “Digital previews are provided as-is.”. Fix: Provide complete terms covering preview limitations, errors, corrections, production approval, cancellation, refunds, delivery and customer support.
  - [VALUE sev 3] **Cancellation and refund limitation is abrupt** - evidence: “Printed orders are non-refundable once production begins.”. Fix: Explain the exact production stage, show cancellation and refund rules before checkout, and state remedies for damaged, delayed or materially incorrect books.
- **Positives:** The page has a clear Privacy heading.; It explicitly mentions names, stories and uploaded photographs.; A Contact link is available.; The wording does not show obvious countdown pressure or a pre-ticked consent box.
- **Would abandon here:** The privacy notice is too vague about retention, technology partners, AI use and deletion to share sensitive information about my child.

### Create your book – character details  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Collect basic details about the child and another person before moving on to the family-memory story.
- **What's happening:** The form asks for the child's first name, age, pronouns, optional appearance, another character, and that character's relationship. A “Next” button advances the process.
- **First impression (Elena):** "The form is visually clear and manageable, but I noticed immediately that “Grandparent” is preselected in the relationship menu, making me check that it is not carried forward incorrectly."
- **Cognitive walkthrough:** Q1 Yes, I would enter the basic character details because the fields match what the story needs. / Q2 Yes, I noticed the name, age, pronouns, appearance, other-character, and relationship controls, plus the “Next” button. / Q3 Mostly. “Who else is in the story?” fits, but asking only for a relationship without a specific “Mama” option makes the Parent category feel slightly generic.
  - [H5 sev 2] **Relationship is preselected without a choice** - evidence: [11] displays “Grandparent” as the selected option before I make a selection.. Fix: Default the relationship field to “Select…” and make the user choose a value explicitly.
  - [TRUST sev 2] **No reminder of data-use limits before personal details** - evidence: The form immediately requests a child's name, age, pronouns and appearance, while the only policy information is in the footer links “Privacy” and “Terms”.. Fix: Add a short notice above the form stating what happens to the supplied details, whether they are used for AI training, and how to access or delete them, with a direct link to the full privacy notice.
  - [H2 sev 1] **Mother is not named as a relationship option** - evidence: [11] offers “Grandparent \| Parent \| Sibling \| Friend \| Pet \| Other” rather than a specific “Mother” option.. Fix: Include role-specific choices such as “Mother,” “Father,” or “Parent,” while keeping the categories understandable.
- **Positives:** The heading clearly explains the purpose of the form.; The fields are plainly labelled and laid out in a logical order.; The appearance field is explicitly marked optional.; The “Next” button is visually prominent and easy to find.

### Story details  (step 9)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_09.jpg)
- **Purpose:** Collect the setting, meaningful object, and family memory that the website will use to create Nikolai's personalised storybook.
- **What's happening:** The form offers three empty text fields for the location, special object, and memory, followed by Back and Next buttons. No generated story or preview is present yet.
- **First impression (Elena):** "The form is calm, clear, and uncluttered. The questions feel relevant to making the story meaningful, and there are no pressure messages or unnecessary options."
- **Cognitive walkthrough:** Q1 Yes, I would enter these details now because the prompts directly match the story I want to create. / Q2 Yes, I can clearly see one textbox for each of the three questions, plus a prominent “Next” button. / Q3 Yes. “Where does the story happen?”, “A special object”, and “Tell us the memory or idea behind your story” all match what I want to provide.
  - [CONTENT sev 1] **Fields are not marked optional** - evidence: [16] “Where does the story happen?”, [17] “A special object”, and [18] “Tell us the memory or idea behind your story” have no “optional” label.. Fix: Mark every non-essential field “(optional)”; otherwise, explain which fields are required before the form is completed.
- **Positives:** The prompts are plain, warm, and relevant to a family memory.; The layout is uncluttered and the input controls are large and easy to identify.; A visible “Back” button gives me control without losing this step.; There are no pre-ticked choices, false urgency, or other pressure tactics on this screen.

### Choose look and feel  (step 10)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_10.jpg)
- **Purpose:** Choose the intended reading level and visual style for the personalised book.
- **What's happening:** Four reading-level radio options and three illustration-style options are shown. The middle reading level and watercolour style are currently selected, and the user can go back or continue.
- **First impression (Elena):** "The page is orderly and not overwhelming. The storybook-style choices feel suitable, although “Lexile” may not mean much to an ordinary parent."
- **Cognitive walkthrough:** Q1 Yes. I want a book that suits Nikolai’s age and looks comforting rather than frightening. / Q2 Yes. The radio buttons and the “Next” button are clearly visible. / Q3 Partly. The illustration labels are clear, but the Lexile ranges do not plainly say “for children who can read independently” or “best read aloud to a child.”
  - [H2 sev 2] **Reading-level labels require specialist knowledge** - evidence: “Reading level” followed by “Lexile BR–200L” and “Lexile 200L–500L”. Fix: Show plain-language guidance, such as “Read independently” and “Read with an adult,” and recommend a level based on the child’s age while allowing me to override it.
  - [H6 sev 1] **Preselected options are not explained** - evidence: [22] “Lexile 200L–500L” (checked) and [25] “Watercolour — soft and dreamy” (checked). Fix: Label preselected options as “Recommended for age 6” or “Default choice,” and briefly explain the recommendation.
- **Positives:** The choices are presented in two clearly separated groups.; Each illustration style has a helpful plain-language description.; The controls have large, visible targets.; Back and Next provide straightforward navigation.

### Optional photo upload  (step 11)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_11.jpg)
- **Purpose:** Offer a final optional photo for likeness-based illustrations and let the user submit the book for generation.
- **What's happening:** The page asks the user to optionally upload a clear photo of the child's face. No photo is selected, and the available actions are “Back” and “Create my book.”
- **First impression (Elena):** "The choice is simple and genuinely optional, but I do not trust the upload because the nearby screen gives no photo-specific explanation about AI training, sharing, retention, or deletion."
- **Cognitive walkthrough:** Q1 I would create the book without uploading because I can describe Nikolai's appearance and the privacy notice has not earned my trust regarding facial images. / Q2 Yes, the file chooser is visible under the instruction, and “Create my book” is prominent on the right. / Q3 Mostly. “Create my book” clearly expresses the final action, while the native “Choose file” control is weak and the upload has no visible field label.
  - [TRUST sev 3] **Photo upload lacks specific privacy disclosure** - evidence: “Upload a clear photo of your child's face so the illustrations look like them.” The page itself does not explain whether the image is used for AI training, who can access it, how long it is retained, or how it can be deleted.. Fix: Place a concise disclosure beside the upload stating whether photos train AI, named categories of processors or recipients, retention periods, deletion rights, and whether deleting the book also deletes the original. Link to the detailed privacy notice.
  - [ACC sev 2] **File control has no explicit accessible label** - evidence: [30] file-upload (no label), with only the native text “Choose file”. Fix: Add a visible label such as “Child photo (optional)” and give the upload an explicit accessible name, accepted file formats, file-size limit, and alternative-text instructions.
  - [ACC sev 2] **Footer text has weak contrast** - evidence: The “Privacy,” “Terms,” and “Contact” links and “© 2026 StoryHearth Ltd.” appear extremely faint against the background.. Fix: Use WCAG-compliant text and link colours with sufficient contrast, and make the targets large enough to activate comfortably.
- **Positives:** The heading clearly says the photo is optional, so I do not feel forced to provide it.; The “Back” button allows me to return and review the preceding choices.; “Create my book” clearly communicates the final action.; The written description route means I can proceed without uploading sensitive information.

### Generated storybook preview  (step 12)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_12.jpg)
- **Purpose:** To present the generated personal storybook and allow the user to page through the preview, regenerate it, or proceed to a hardcover order.
- **What's happening:** A nine-page preview titled “The Magical Adventrue of Nikolai” is displayed. The cover says “A StoryHearth original” and “Illustration style: Pop-art comic,” despite the previously selected watercolour style. The current page is 1 of 9, the previous-page control is disabled, and the next-page control is active. Lower on the page are a paid regeneration option, an “Order hardcover” link, and privacy, terms, and contact links.
- **First impression (Elena):** "I can see that the book was made, but the mismatch between my selected “Watercolour — soft and dreamy” style and the stated “Pop-art comic” style makes me distrust the generation. “The Magical Adventrue” looks careless rather than comforting."
- **Cognitive walkthrough:** Q1 Yes, I would try reading the next pages because I need to check whether the story actually includes Nikolai, Mama, the rainy school gate, and the brave stone. / Q2 Yes, I notice the right-facing next-page button and the “1 / 9” page indicator. / Q3 The “›” control is understandable as the next-page control, although the button has no descriptive text and the disabled previous control is only an arrow.
  - [H2 sev 3] **Selected illustration style was not applied** - evidence: The page says “Illustration style: Pop-art comic,” while the earlier selection was “Watercolour — soft and dreamy.”. Fix: Apply the selected style to the generated book and, if the style cannot be reproduced, explain the substitution before generation.
  - [CONTENT sev 3] **Generated cover does not reflect the supplied character details** - evidence: I entered “blond straight hair, gap in his front teeth, yellow raincoat,” but the cover shows Nikolai with blond hair, no visible gap in his front teeth, and no yellow raincoat.. Fix: Use the supplied appearance details consistently across the cover and story, and tell the user which details could not be represented.
  - [CONTENT sev 3] **The final sentence is incomplete** - evidence: “And from that day on, whenever Nikolai looked up at the sky, he would always remember”. Fix: Generate a complete final sentence that identifies what Nikolai remembered and connect it explicitly to bravery and the stone.
  - [CONTENT sev 2] **Typographical error in the book title** - evidence: The cover and heading read “The Magical Adventrue of Nikolai.”. Fix: Use a spelling check and correct “Adventrue” to “Adventure” before displaying or printing the title.
  - [CONTENT sev 2] **The cover does not clearly show the requested school-gate memory** - evidence: The cover shows a simple house-like building, Nikolai, a sun, and a grey stone, but not a clear school gate or rainy setting.. Fix: Ensure the cover and story consistently represent the specified place, weather, and key memory, while explaining any creative deviations.
  - [VALUE sev 2] **Paid regeneration option is prominent before I have inspected the book** - evidence: [8] “Regenerate entire book – $4.99” appears below the preview.. Fix: Explain what regeneration changes, whether it replaces the existing book, and the full cost before presenting the paid control. Do not imply that regeneration is necessary unless the output is visibly faulty.
  - [CONTENT sev 2] **The ending introduces an unrelated idea** - evidence: “whenever Nikolai looked up at the sky”. Fix: Ground the final page in the rainy school gate, Mama, the smooth grey brave stone, and Nikolai feeling brave.
- **Positives:** The page clearly shows that a nine-page book was generated.; The page counter makes the length of the preview clear.; There is an obvious next-page control, and a return to “My books” is available.; The privacy, terms, and contact links remain accessible from the preview.

### Hardcover checkout  (step 15)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_15.jpg)
- **Purpose:** Collect delivery and payment details so the selected hardcover can be purchased.
- **What's happening:** The page displays the hardcover price, an active reservation countdown, a pre-checked optional gift-wrap charge, shipping, and a total, followed by empty address and payment fields.
- **First impression (Elena):** "The arithmetic is visible, but I do not trust the total because “Premium gift wrap” was checked without my consent and the countdown is pressuring me to hurry."
- **Cognitive walkthrough:** Q1 I would only try the gift-wrap checkbox to reveal the cost without it; I would not proceed to payment or order this poor preview. / Q2 Yes, the checked “Premium gift wrap” checkbox is immediately visible between the book price and shipping charge. / Q3 The label identifies the add-on, but its checked state does not honestly represent my choice; I want the base hardcover and delivery cost.
  - [DECEPTIVE sev 3] **Optional gift wrap is pre-selected** - evidence: [6] checkbox "Premium gift wrap" (checked), with "£7.99" added and "Total £45.97". Fix: Default every optional add-on to unchecked, make it a separate clearly labelled section, and update the total only after an affirmative choice.
  - [DECEPTIVE sev 2] **Countdown timer creates purchase pressure** - evidence: "Your price is reserved for 09:57". Fix: Remove the countdown. If a genuine reservation is necessary, state exactly what is reserved, until when, and under what conditions it ends.
  - [VALUE sev 2] **Base delivery-inclusive price is not made prominent** - evidence: "Hardcover £24.99", "Shipping & handling £12.99", and "Total £45.97". Fix: Show a clear subtotal, separately identify delivery and optional extras, and state the payable total before checkout starts.
  - [CONTENT sev 2] **Poorly generated book title is carried into the order** - evidence: "Hardcover: The Magical Adventrue of Nikolai". Fix: Allow correction of the title and validate spelling before allowing an order.
- **Positives:** The item and individual charges are shown with pound values.; The gift-wrap checkbox is visible rather than buried.; Address and payment fields are still empty, so I can inspect pricing without committing to anything.
- **Would abandon here:** I would not continue to payment because gift wrap was pre-selected and the generated book itself has the wrong illustration style, misses key character details, and contains a misspelled title and unfinished text.

## Generated output assessment
*Artifact:* A generated nine-page personalised children's storybook preview and hardcover checkout page

> I recognise Nikolai, Varna and the brave stone, but this is not the reassuring story I asked for. Unresolved placeholders, a wrong name, a changed pronoun, a missing Mama, threatening imagery and an unfinished ending would be immediately obvious to any family. With no clear privacy and cancellation information at checkout, I would not trust it with Nikolai's details or pay for it in this state.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 2 | The output uses Nikolai's correct name, age 6, the new school, the rainy-morning premise, the smooth grey brave stone and Varna. However, Mama is entirely absent, the stone is not actually given to him by her, the yellow |
| coherence | 1 | The narrative jumps from a rainy school gate to evening, rain, an invented uncle, threatening woods, night and then home. The opening sentence is repeated on page 6, and the final sentence is unfinished. |
| age fit | 1 | The measured reading level is grade 8.3 for an intended six-year-old. Page 2 contains advanced adult vocabulary such as “ephemeral,” “crepuscular,” “engendered” and “existential trepidation,” while page 5 says toothy sha |
| language | 1 | There are unresolved template placeholders, the title is misspelled “Adventrue,” Nikolai becomes “Nikola,” “she” contradicts the supplied pronouns, an opening is duplicated, the closing sentence is incomplete and formatt |
| text image fit | 2 | Pages described as rainy show a bright sun; a raincoat and hood are absent; the gate is missing; the image on page 6 does not show a journey home; the lantern is a floating square; and Nikolai is not clutching the red ba |
| character consistency | 2 | Nikolai is represented by a nearly identical round-headed figure throughout, which provides some basic continuity. However, he never clearly has the requested straight blond hair, visible tooth gap or yellow raincoat, an |
| visual quality | 1 | The selected watercolour style was not delivered; the site explicitly labels the art “Pop-art comic.” The pictures use crude geometric shapes, repeated stock compositions, floating objects, text labels embedded awkwardly |
| emotional resonance | 1 | The central reassuring relationship is missing: Mama never gives or uses the stone with Nikolai, and the story never clearly shows him overcoming his fear. The invented threatening forest and generic magical adventure ma |

- **used correctly:** Nikolai's first name and age of six; The he/him pronouns in most passages; The new-school and rainy-morning premise; The smooth grey brave stone; The stone's connection to the beach in Varna; The requested Lexile target as a stated intention, although the resulting prose does not meet an age-six reading level; Premium gift wrap, which I had selected
- **missing:** Mama as a character; Mama's parent relationship with Nikolai; Mama giving Nikolai the stone; Nikolai's blond straight hair; The gap in Nikolai's front teeth; The yellow raincoat; A coherent first morning at school; A story in the requested soft watercolour style
- **changed:** Rainy weather was repeatedly rendered as bright sunshine; The location was described as “in the gate” instead of “at the gate”; Nikolai was referred to as “she” on page 4; Mama's support was replaced by an invented uncle; The requested school story became a nighttime magical woodland adventure; The promising ending was changed into an unfinished sentence
- **invented:** Uncle Bartholomew; A lantern; A winding path; Dark woods with toothy shadows; A shiny red balloon; The word “curious” as Nikolai's defining quality

### Part by part
#### Cover / Title page
![I1](artifacts/capture_01/img_00.jpg)
> A StoryHearth original Illustration style: Pop-art comic The Magical Adventrue of Nikolai
- *Picture:* A very basic flat-colour illustration of a bald or blond-headed boy in a green top, a grey stone, a small house-like school building, and a large bright sun. The cover has no rain, no visible school gate and no yellow raincoat.
- *Reaction:* The misspelling in “Adventrue” is immediately visible, and this is plainly not the soft watercolour I selected. It looks like an unfinished pop-art template rather than a keepsake.
  - [language, sev 3] The title reads “The Magical Adventrue of Nikolai”; “Adventrue” should be “Adventure.”
  - [fidelity, sev 3] The requested appearance was “blond straight hair, gap in his front teeth, yellow raincoat,” but none is shown clearly.
  - [fidelity, sev 3] The selected style was “Watercolour,” while the page explicitly says “Illustration style: Pop-art comic.”
  - [text_image_fit, sev 2] The cover promises Nikolai's story but shows a bright sunny scene without the specified rainy school-gate setting.
  - [visual_quality, sev 3] The image uses crude geometric shapes, a floating stone, a generic house rather than a school gate, and labels the child “Nikolai” beneath him.
- **Change I'd make:** Correct the title and regenerate the cover in soft watercolour, showing Nikolai with straight blond hair, a visible gap in his teeth and a yellow raincoat, holding the grey stone beside a school gate on a rainy morning.
- **Suggested rewrite:** The Magic Brave Stone of Nikolai A StoryHearth original Illustration style: soft watercolour

#### Title / Dedication page
![I2](artifacts/capture_04/view_00.jpg)
> The Magical Adventrue of Nikolai Preview · 9 pages For {{recipient_name}}, with love from {{sender_name}} 2 / 9 Regenerate entire book – $4.99 Order hardcover StoryHearth How it works Pricing My books Log out Privacy Terms Contact © 2026 StoryHearth Ltd.
- *Picture:* A screenshot of the book viewer showing a mostly blank white rounded page with an unresolved italic dedication. The interface also shows regeneration and ordering controls, with very faint footer links.
- *Reaction:* Unresolved template markers make this look like a production error, not a finished gift. I was apparently already logged in before seeing the book, and this page gives me no meaningful privacy or cancellation information.
  - [language, sev 4] The page displays “For {{recipient_name}}, with love from {{sender_name}}” with both variables unresolved.
  - [language, sev 3] The misspelled title “Adventrue” is repeated in the viewer.
  - [visual_quality, sev 3] The nearly empty page contains raw template syntax rather than a finished dedication.
  - [emotional_resonance, sev 3] The failed placeholder prevents the book from feeling personally prepared for Nikolai.
- **Change I'd make:** Resolve both variables before publication, correct the title, and provide a real privacy summary explaining data use, AI training, retention, deletion and cancellation before any account or payment step.
- **Suggested rewrite:** The Magic Brave Stone of Nikolai For Nikolai, with love from Mama

#### Page 1
![I3](artifacts/capture_05/img_00.jpg)
> Once upon a time, in the gate of his new school on a rainy morning, there lived a curious child named Nikolai. Nikolai was 6 years old and loved nothing more than the smooth grey "brave stone" from the beach in Varna.
- *Picture:* The same simple boy and grey stone appear beside a small house under a large bright sun. There is no visible rain or gate.
- *Reaction:* The stone, Varna, school and rainy-morning premise are there, but “in the gate” is awkward and the cheerful sunny picture contradicts the words. Mama and the moment when she gives him the stone are still missing.
  - [language, sev 2] “In the gate of his new school” is grammatically awkward; “at the gate of his new school” would be natural.
  - [fidelity, sev 3] The requested memory says Mama gave Nikolai the stone, but neither Mama nor the gift appears here.
  - [text_image_fit, sev 3] The text says “a rainy morning,” but I3 shows a bright sun and no rain; it also shows no school gate.
  - [character_consistency, sev 3] Nikolai has no visible blond hair, tooth gap or yellow raincoat.
- **Change I'd make:** Show rainy weather, a clear school gate, Mama handing Nikolai the stone, and all three requested appearance details. Use simple, warm sentences suitable for a six-year-old.
- **Suggested rewrite:** On a rainy morning, Nikolai stood at the gate of his new school. His hands felt cold and his stomach felt wobbly. “You can do this,” said Mama. She put the smooth grey brave stone from their beach holiday in Varna into his pocket. “I’ll be here after school.” Nikolai took a deep breath.

#### Page 2
![I4](artifacts/capture_06/img_00.jpg)
> One evening Nikolai gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* A flat purple and pink evening sky with stars, the same generic boy, and the school-like building. He is not visibly looking upward or showing a clear emotional response.
- *Reaction:* This sentence is far beyond a six-year-old's reading level and has no connection to the first-morning story. It reads like an unrelated line of adult literary fiction.
  - [age_fit, sev 4] The sentence uses “ephemeral,” “luminescence,” “crepuscular,” “engendered,” “melancholy,” “juxtaposing,” “ineffable” and “existential trepidation”; the measured grade level is 8.3.
  - [coherence, sev 3] The story changes abruptly from a rainy morning at the school gate to “One evening” with no transition or reason.
  - [text_image_fit, sev 2] Nikolai stands facing forward rather than clearly gazing upward, and his melancholy cannot be read from the simple expression.
- **Change I'd make:** Replace this with a short thought from Nikolai about using the stone for courage while he stands at the school gate.
- **Suggested rewrite:** Nikolai looked up at the grey morning sky. He squeezed the brave stone in his pocket. “Just one step,” he whispered.

#### Page 3
![I5](artifacts/capture_07/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Nikola pulled up his hood and ran for shelter, holding the smooth grey "brave stone" from the beach in Varna tight.
- *Picture:* A bright sunny scene with the boy beside the school-like building and a floating grey stone. He has no hood and there is no rain, puddle or shelter.
- *Reaction:* The picture directly contradicts nearly every important detail in the sentence. The misspelling “Nikola” is also a serious mistake in a book meant to reassure a child about his own name.
  - [language, sev 4] Nikolai's name is misspelled as “Nikola.”
  - [text_image_fit, sev 4] The text says rain is pouring and Nikolai pulls up his hood, while I5 has a large sun, no rain, no puddles, no shelter and no hood.
  - [fidelity, sev 3] The requested yellow raincoat is absent, despite this being the page where the hood should be visible.
  - [visual_quality, sev 2] The stone floats separately from Nikolai rather than being held tightly in his hand or pocket.
- **Change I'd make:** Show Nikolai in his yellow raincoat, with the hood up, clutching the stone while rain falls and puddles splash around him. Preserve the spelling “Nikolai.”
- **Suggested rewrite:** Raindrops splashed into the puddles. Nikolai pulled up the hood of his yellow raincoat and held his brave stone tightly.

#### Page 4
![I6](artifacts/capture_08/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Nikolai, follow me!" he called, and she followed him along the winding path.
- *Picture:* Two simplistic figures stand beside the building. The taller figure is labelled “Uncle Bartholomew” and has a small floating yellow square intended to represent a lantern; Nikolai stands apart without the stone.
- *Reaction:* Mama has been replaced by an invented uncle, and the story changes Nikolai's pronoun to “she.” I cannot keep this for a child whose name and identity have been entered so carefully.
  - [fidelity, sev 4] The requested character was “Mama,” but “Uncle Bartholomew” is invented and Mama never appears.
  - [fidelity, sev 4] The entered pronouns were “he / him,” but the text says “she followed him.”
  - [coherence, sev 3] The uncle appears suddenly and leads Nikolai along a path, but the preceding page places Nikolai at school in the rain with no destination or explanation.
  - [text_image_fit, sev 3] The image places both figures beside the building and shows no winding path; the lantern is reduced to an unexplained floating yellow square.
  - [character_consistency, sev 2] Nikolai's grey stone and yellow raincoat disappear on this page.
- **Change I'd make:** Remove the invented uncle and keep Mama as the reassuring companion. Use “he” consistently and show the pair approaching the school entrance together.
- **Suggested rewrite:** Mama knelt beside him and pushed down the hood of his yellow raincoat. “I’ll be waiting here,” she said. “You can be brave, and I can be right here when you come out.” Nikolai nodded and held the brave stone in his palm.

#### Page 5
![I7](artifacts/capture_09/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Nikolai again. Nikolai clutched a shiny red balloon and trembled in the dark.
- *Picture:* A dark outdoor scene with Nikolai, three simple trees, a crescent moon and a floating red balloon. The woodland is minimal, the stone and raincoat are absent, and there are no literal toothed shadows.
- *Reaction:* The threatening language and unexplained red balloon are not comforting for an anxious six-year-old. This feels like a different, darker adventure rather than a gentle first day at school.
  - [age_fit, sev 4] “The shadows grew teeth and whispered that no one would ever find Nikolai again” introduces vivid threat and prolonged disappearance without reassurance.
  - [fidelity, sev 4] A red balloon is invented, while the requested school gate, Mama and brave stone disappear.
  - [coherence, sev 4] The school-morning story suddenly becomes a nighttime woodland adventure with no transition.
  - [text_image_fit, sev 3] Nikolai is trembling and clutching a balloon in the text, but he stands passively with empty hands; the image does not show threatening toothed shadows.
  - [visual_quality, sev 3] The balloon floats above him rather than being clutched, and the threatening scene is rendered with crude circles and rectangles.
- **Change I'd make:** Delete the threatening woodland episode and the balloon. Continue at school with Nikolai taking a manageable first step, seeing an adult or teacher, and using the stone for reassurance.
- **Suggested rewrite:** Nikolai looked at the busy playground and felt his knees wobble. Then he saw his teacher smiling and waving. “Hello,” he said, still holding the brave stone. “I’m Nikolai.”

#### Page 6
![I8](artifacts/capture_10/img_00.jpg)
> Once upon a time, in the gate of his new school on a rainy morning, there lived a curious child named Nikolai. At last the sun came out, and Nikolai skipped all the way home, happier than ever.
- *Picture:* A generic boy skips or stands in front of the same school-like building beneath a bright sun. There is no visible gate, rain, raincoat, stone, Mama or clear journey home.
- *Reaction:* The opening has simply been repeated and then attached to a resolution. Nikolai is declared happier, but the book never shows what helped him become brave.
  - [coherence, sev 4] The sentence “Once upon a time…” repeats the opening almost verbatim rather than continuing the plot.
  - [fidelity, sev 3] The image and text still omit Mama, the school gate and the yellow raincoat; the brave stone is not shown.
  - [text_image_fit, sev 3] The text says he skipped all the way home, while the image merely places him in front of the school-like building; no journey home is depicted.
  - [emotional_resonance, sev 3] The conclusion asserts that he is “happier than ever” without showing the fear, courage or reunion that would make the moment meaningful.
- **Change I'd make:** Replace the repeated opening with a clear school-based resolution showing Nikolai saying hello, joining a class activity, and returning to Mama.
- **Suggested rewrite:** By lunchtime, Nikolai had said hello to his teacher and found a place in the class. When the final bell rang, Mama was waiting at the gate. Nikolai showed her the brave stone. “I did it,” he said, and Mama hugged him.

#### Page 7 / Closing page
![I9](artifacts/capture_11/img_00.jpg)
> The End And from that day on, whenever Nikolai looked up at the sky, he would always remember The End
- *Picture:* An orange-gradient end page with “The End” above the generic boy and school-like building. Nikolai is still labelled beneath the image; the unfinished sentence is not represented visually.
- *Reaction:* The final thought trails off and then repeats “The End.” It is an abrupt, obviously incomplete ending, not a keepsake-quality conclusion.
  - [language, sev 4] The sentence ends after “he would always remember” without saying what he remembered or providing punctuation.
  - [language, sev 3] “The End” appears both before and after the unfinished closing sentence.
  - [emotional_resonance, sev 4] The omitted conclusion removes the intended message about courage and leaves the personal story unresolved.
  - [text_image_fit, sev 2] The page says Nikolai would remember something, but the generic image gives no clue what that memory is and repeats the school scene.
- **Change I'd make:** Complete the thought with a concrete memory of overcoming the first morning, include final punctuation, and show Nikolai safely with Mama in the yellow raincoat.
- **Suggested rewrite:** The End From that day on, whenever Nikolai felt worried, he remembered the brave stone in his pocket—and remembered that he could take one small step at a time.

#### Checkout
![I10](artifacts/capture_13/view_00.jpg)
![I11](artifacts/capture_13/view_01.jpg)
> Checkout Your price is reserved for 09:41 Hardcover: The Magical Adventrue of Nikolai	£24.99 Premium gift wrap	£7.99 Shipping & handling	£12.99 Total	£45.97 Delivery Address Payment Card number Expiry CVC Pay now
- *Picture:* A checkout form with a red countdown notice, a checked Premium gift wrap box, item and shipping costs, address field, card fields and a large Pay now button. The navigation shows the account is logged in.
- *Reaction:* The arithmetic is correct and the gift wrap was something I selected, but the countdown is needless pressure after such an obviously unfinished preview. I still cannot judge data use, AI training, deletion or cancellation from what is shown, so I would not enter payment details.
  - [language, sev 3] “Your price is reserved for 09:41” uses urgency without explaining whether the reservation is real, reversible or tied to a genuine deadline.
  - [language, sev 3] The checkout repeats the misspelled hardcover title “The Magical Adventrue of Nikolai.”
  - [fidelity, sev 4] Although I selected Premium gift wrap and it remains checked, the page does not address the stated priorities of explaining data use, AI training, deletion and cancellation.
  - [visual_quality, sev 3] The payment form offers no visible explanation of cancellation, returns, recurring charges or what happens to the child's submitted information.
- **Change I'd make:** Remove the countdown, make optional extras default to unticked, and provide plain-language information immediately before payment about the total delivery cost, cancellation and returns, retention and deletion of Nikolai's data, third-party access, and whether any submitted text or images are used to train AI. Do not permit payment until the unfinished title, placeholders and story errors are corrected.

**Top changes to the output:** 1. Run a mandatory name, pronoun, placeholder and proof-reading check before allowing preview or purchase; fix “Adventrue,” “Nikola,” “she” and all unresolved variables. | 2. Rewrite the complete story around Nikolai's first rainy morning with Mama, the school gate and the Varna brave stone, using simple language and a clear arc from fear to one brave step and a happy reunion. | 3. Remove the invented uncle, lantern, balloon and threatening woodland, or make every added element clearly gentle, relevant and approved. | 4. Regenerate every illustration in the requested soft watercolour style with consistent Nikolai, straight blond hair, a visible tooth gap, the yellow raincoat and the grey stone shown in the right hands. | 5. Ensure image prompts and final captions agree on weather, location, clothing, characters and actions before rendering. | 6. Before payment, disclose data use, AI-training practices, access and retention, deletion rights, cancellation and returns, gift-wrap preselection and the full delivered price without a fake countdown.

## Recommendations (participant's priorities)
- **[high] Rewrite and check the entire story before showing it, removing unresolved placeholders, spelling errors, invented threatening characters and the unfinished ending; use simple language suitable for a six-year-old.** (Your storybook) - The current story is incoherent and contains obvious errors, so it would be embarrassing and confusing for Nikolai and unsuitable as a personal keepsake.
- **[high] Generate illustrations in the selected soft watercolour style, with consistent Nikolai, straight blond hair, visible tooth gap, yellow raincoat, school gate, rainy weather and the grey brave stone in the correct hands.** (Choose look and feel and Your storybook) - The visual result did not match either my chosen style or the details I supplied, which undermines the personal value of the book.
- **[high] State clearly whether photos are used for AI training, identify every recipient or technology partner, explain retention periods and provide an obvious deletion process.** (Privacy and terms; Optional photo upload) - I will not upload a child's photograph while phrases such as “may be processed” and “improve our services” leave the important consequences unknown.
- **[high] Add a mandatory name, pronoun, placeholder and proof-reading check, and prevent purchase when those checks fail.** (Your storybook and Checkout) - Nikolai became “Nikola,” his pronoun changed, and “Adventrue” was carried into the order. These are basic trust and quality failures.
- **[high] Remove the countdown timer, explain all preselected options, show the base price prominently and make gift wrap opt-in with no hidden additions.** (Hardcover checkout) - The pre-ticked gift wrap increased the total from £37.98 to £45.97 and the timer applied pressure. That is exactly the kind of deceptive pattern that makes me leave.
- **[high] Explain data use again immediately before entering personal family details and provide persistent, accessible labels for all fields and file controls.** (Create your book – character details; Optional photo upload) - The site should not rely on a distant privacy page when it is asking for sensitive information about a child.
- **[medium] Do not preselect a relationship, and include “Mother” as a relationship option; explain which fields are required and which are optional.** (Create your book – character details; Story details) - “Grandparent” was selected by default, and the form did not clearly distinguish required information from optional information.
- **[medium] Replace the unexplained technical sync error with a plain-language status, or remove it if it has no effect on the account.** (My books) - An unexplained error makes me wonder whether my data or account is safe, even when the rest of the page appears to work.
- **[medium] Describe reading levels in ordinary language and explain any preselected appearance or illustration options.** (Choose look and feel) - Lexile ranges require specialist knowledge, and unexplained defaults made me unsure what had been selected for Nikolai.
- **[low] Improve accessible labels, illustration descriptions and footer contrast, and tell users what happens after they choose the main creation action.** (All pages, especially Log in, landing page and footer) - Clear labels and visible links are important for understanding the service, especially when the site is asking for family information.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This is a service for creating personalised children's storybooks featuring a child and meaningful memories, apparently for parents or other family members. The idea could be lovely, especially for a child like Nikolai, but it needs honest data practices and dependable results.
- **What was the most frustrating or confusing moment, and why?** The most frustrating moment was the generated preview: I chose soft watercolour illustrations, but received crude pop-art images, while the title contained “Adventrue,” Nikolai became “Nikola,” his pronoun changed to “she,” and the story ended with an unfinished sentence. The pre-ticked gift wrap and countdown at checkout were also seriously objectionable.
- **What was the best moment?** The best moment was seeing that the story had retained Nikolai, the new school, Varna and the brave stone in its premise. The story details were easy to enter, and the wording about the school morning felt personal and relevant.
- **Was there any point where, in real life, you would have given up? Where and why?** I would have given up before uploading a photograph, because the privacy notice did not say clearly whether images train AI, who receives them, how long they are kept or how to delete them. I might also have abandoned the purchase after seeing the poor preview, but the pre-ticked gift wrap and pressure timer had already made me unwilling to enter payment details.
- **What did you expect to find or be able to do that wasn't there?** I expected a gentle, coherent story about Nikolai's first rainy morning, with Mama giving him the Varna stone and helping him take one brave step. I also expected clear information about data use, retention, deletion, cancellation, returns and the actual delivered price, plus a book that respected my selected style and character details.
- **Did you trust this website with your information (and your family's)? Why or why not?** No, not with Nikolai's information or my family's. The phrases “may be retained,” “may be processed by our technology partners” and “improve our services” are too vague, and I still could not tell whether uploaded photographs are used to train AI. I also did not trust a purchase page that used a pre-ticked add-on and a countdown timer.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would consider paying around £20 to £30 for a genuinely good personalised keepsake, but I would want the exact price, delivery, cancellation and refund terms shown without pressure first. I might pay more for high-quality illustrations and a carefully checked story, but not for the result shown here.
- **If the site produced something for you, how do you feel about it overall?** I recognise Nikolai, Varna and the brave stone, but this is not the reassuring story I asked for. The missing Mama, invented characters, changing pronoun, unresolved placeholders, threatening imagery, incorrect illustrations and unfinished ending would make it unsuitable as a keepsake for my son.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | suspicious (0) | The service sounds relevant to what I want, but “multimodal generative narrative engine” and “household’s lived-experience corpus” sound deliberately technical rather than reassuring. Before sharing anything about Nikola | read_page |
| 2 | StoryHearth – Personalised storybooks st | suspicious (0) | The service is relevant to what I want, but the wording “multimodal generative narrative engine” and “household’s lived-experience corpus” still sounds deliberately technical rather than reassuring. Before I share anythi | click |
| 3 | Log in – StoryHearth | reassured (1) | The page is simple and the “Log in” control is obvious. I can see the Privacy and Terms links in the footer, but I’ll deal with those before entering sensitive family information. The form itself looks straightforward, a | type; type; click |
| 4 | My books – StoryHearth | suspicious (-1) | I can see that I am logged in, but that technical error is not reassuring. Before I enter anything about Nikolai, I want to read the Privacy link and check what happens to photos, the memory, and generated stories. I wil | click |
| 5 | Privacy – StoryHearth | suspicious (-2) | This is not a privacy notice detailed enough for me. “May be retained,” “may be processed by our technology partners” and “improve our services” do not tell me who the partners are, whether photos train AI, how long they | click |
| 6 | My books – StoryHearth | hesitant (-1) | I can see that “My books” worked, because I am back on the account dashboard and it says “You have no books yet.” The sync error is still there and remains unexplained, but the next step is clearly the orange “+ Create a | click |
| 7 | Create your book – StoryHearth | hesitant (0) | This form is easy to understand, and I can see the controls I need. However, “Relationship” is already set to “Grandparent”; I will change that to “Parent” so it accurately describes Mama. I am still cautious about enter | type; select; select; type; type; select |
| 8 | Create your book – StoryHearth | reassured (1) | The form now shows the correct details, and the relationship has been changed to “Parent,” so I am ready to continue. The appearance field looks truncated in the box, but the entered value is still shown elsewhere as com | click |
| 9 | Create your book – StoryHearth | reassured (2) | This step is straightforward and the wording feels personal rather than technical. I can put Nikolai at the gate of his new school, give him the smooth grey “brave stone” from Varna, and explain that Mama gave it to him  | type; type; type; click |
| 10 | Create your book – StoryHearth | reassured (1) | This is a simple design, and the illustration choices are pleasant. For Nikolai at age six, I would prefer the lower “Lexile BR–200L” option rather than a wide 200L–500L range. The labels use Lexile terminology without t | click; click; click |
| 11 | Create your book – StoryHearth | suspicious (-1) | I am not uploading a photograph of Nikolai. The privacy notice still does not clearly say whether images are used to train AI, who receives them, how long they are kept, or how deletion works, and “optional” is not enoug | click; wait_for_change |
| 12 | Your storybook – StoryHearth | confused (-1) | The book has been generated, so the creation step worked, but I am immediately concerned. I selected “Watercolour — soft and dreamy,” yet the preview says “Illustration style: Pop-art comic.” The title also contains the  | read_page |
| 13 | Your storybook – StoryHearth | frustrated (-1) | I can see that the book was generated, but the cover immediately feels wrong: Nikolai is shown without the yellow raincoat or the obvious gap in his front teeth that I supplied, and the picture is very basic rather than  | flip_through |
| 14 | Your storybook – StoryHearth | frustrated (-2) | I have now seen every page, but the ending is very weak: “And from that day on, whenever Nikolai looked up at the sky, he would always remember” is an unfinished thought, and the sky was not established in the story. The | click |
| 15 | Checkout – StoryHearth | annoyed (-2) | There it is: the checkout makes the optional gift wrap look as though I selected it, but the box was already ticked. That means the real checkout total is being presented as £45.97 rather than £37.98, and the countdown a | click |
| 16 | Checkout – StoryHearth | frustrated (-1) | The change was clear: unchecking the premium gift wrap reduced the total from £45.97 to £37.98. I will not enter payment details or press “Pay now”; the real cost and the unwanted add-on have now been checked, and I have | done |
