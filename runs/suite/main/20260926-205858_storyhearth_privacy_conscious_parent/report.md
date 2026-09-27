# UserQA report: Elena Petrova on http://127.0.0.1:8765/

*Persona:* **Elena Petrova** (45) - Paralegal and mother who reads the privacy policy before trusting a site with her child's data.  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 14 steps | *Pages reviewed:* 11 | *Issues:* 43 | *LLM calls:* 18 | *Wall time:* 322.7 s

## What the agent understood the website to be
- **what it is:** A website that creates personalised, illustrated family storybooks from supplied characters and a family memory.
- **who it is for:** Parents and other families who want a story featuring their child and another favourite person.
- **value proposition:** Turn a meaningful family memory into a customised illustrated storybook, available as a free digital preview and potentially as a printed UK hardcover.
- **pricing model:** The digital preview is described as free, while a 'See pricing' link indicates that printing is a separate paid product. No actual price is visible yet.
- **fit for me:** It sounds relevant because Nikolai is six and anxious about a new school, and a brave story featuring him and his mother could help. I need clear data-use, deletion, pricing, and cancellation terms before I am comfortable supplying childhood details or photographs.
- **main tasks:** Log in, Describe two family characters, Submit a memory, place, and treasured object, Generate and read an illustrated storybook, Review the price and options for a printed hardcover

## Scores
- SUS: **52.5** (grade D; 68 = industry average) - inconsistent responding flagged
- UEQ-S: pragmatic -0.5, hedonic 0.0 (range -3..+3)
- Likelihood to recommend (0-10): 1
- Output keepsake-worthiness (1-5): 1
- Verdict: *"The idea could be lovely, but I would not trust this version with Nikolai's data or pay for such an inaccurate and pressure-driven checkout."*
- Would have abandoned at step 12 (127.0.0.1:8765/checkout.html \| Checkout): I would not enter my address or payment details until the pre-selected £7.99 add-on is removed and the basic delivered price is made clear. The countdown would make me more cautious, not more willing to buy. [self-report]

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 4 | DECEPTIVE | Hardcover checkout | Premium gift wrap is selected by default | [6] checkbox “Premium gift wrap” (checked), adding “£7.99” | Make every optional extra unticked by default and clearly state “Optional — £7.99” beside the checkbox. Show the basic hardcover total and full total separately. |
| 3 | CONTENT | Generated storybook preview, Hardcover checkout (x2) | Spelling error in the book title | The title reads “The Magical Adventrue of Nikolai” on both the page heading and the cover. | Correct “Adventrue” to “Adventure” before presenting the preview, and run a spelling check over all generated titles and page text. |
| 3 | H9 | My books dashboard | Unexplained account sync error | "Error 0x80070057: profile sync incomplete." | Explain what failed in plain language, identify whether user data is affected, and provide a retry or support action. |
| 3 | TRUST | Optional photo upload | No privacy explanation beside a child-photo upload | “Upload a clear photo of your child's face so the illustrations look like them.” | Add a short data-use summary directly above the upload control linking to a clear privacy notice, including processor access, retention, AI-training use, deletion rights, and children’s-data handling. |
| 3 | H1 | Book creation progress | Silent loading screen does not explain the process | The page shows only a circular spinner and no status text. | Display a clear status such as “Creating Nikolai’s book…” alongside a text progress indicator and estimated time. |
| 3 | H3 | Book creation progress | No way to stop or recover from generation | No “Cancel”, “Back”, or “Start over” control is visible. | Add a clearly labelled “Cancel creation” control that returns me to the editable story details without losing them, plus a note about whether an incomplete book is saved. |
| 3 | H9 | Book creation progress | Processing time and failure behaviour are not explained | There is no time estimate, timeout guidance, retry option, or explanation of what to do if generation fails. | Show an approximate wait time and, on failure, a specific error message with “Try again” and “Return to my draft” options. |
| 3 | H4 | Generated storybook preview | The requested illustration style was not applied | I selected “Watercolour — soft and dreamy,” but the preview says “Illustration style: Pop-art comic.” | Apply the selected style to generation, confirm that the returned book metadata matches the selection, and prevent preview generation when those values conflict. |
| 3 | H4 | Generated storybook preview | Important supplied details are missing from the cover | The cover shows bright sunshine and a simple child, while I asked for “the gate of his new school on a rainy morning” and supplied “blond straight hair, gap in  | Ensure the specified setting, weather, appearance details, and keepsake are reflected consistently in the story and illustrations, and let me report a missed detail for correction. |
| 3 | CONTENT | Generated storybook preview | The final sentence is incomplete | “And from that day on, whenever Nikolai looked up at the sky, he would always remember” | Complete the sentence with a clear reference to courage, his mother, and the smooth grey stone. |
| 3 | CONTENT | Generated storybook preview | The final illustration does not match the supplied memory | The image shows Nikolai beside a simple house under an orange sky, while the requested setting was “the gate of his new school on a rainy morning.” | Ensure the final scene depicts the rainy school gate and includes meaningful details from the memory, with a preview or warning if details cannot be rendered. |
| 3 | DECEPTIVE | Hardcover checkout | Countdown timer creates false urgency | “Your price is reserved for 09:57” | Remove the countdown, or replace it with a neutral statement such as “This price is available while the book remains available,” with any genuine reservation terms clearly stated. |
| 3 | VALUE | Hardcover checkout | The basic delivered cost is not shown before the optional add-on | “Hardcover: The Magical Adventrue of Nikolai £24.99”; “Premium gift wrap £7.99”; “Shipping & handling £12.99”; “Total £45.97” | Show “Hardcover £24.99”, “Delivery £12.99” and “Total before optional extras £36.98”, then update the final total only when an extra is actively selected. |
| 3 | DECEPTIVE | Hardcover checkout | The checkout claims the price is reserved without explaining the conditions | “Your price is reserved for 09:37” | Remove the countdown unless there is a genuine, verifiable reservation. If a reservation is necessary, state exactly what is reserved, how long it lasts, and what price or availability applies afterwa |
| 3 | TRUST | Privacy notice | No explanation of children's data | “StoryHearth Ltd processes the information you provide (including names, stories and any photographs you upload) to create your book.” | State the age position, the legal basis for processing children's data, whether parental consent is required, and the specific safeguards used. |

## Page-by-page
### Home page  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Introduce the personalised storybook service, explain the three-step process, and direct visitors to pricing, login, or story creation.
- **What's happening:** The public landing page presents the service proposition, a three-step overview, customer quotations, FAQ controls, and footer links. No story has been generated or entered yet.
- **First impression (Elena):** "Visually calm and reasonably clear, but the opening paragraph sounds corporate and opaque rather than warm and trustworthy. I can see that a free digital preview and UK delivery are offered, but I cannot yet judge privacy or the real cost of a hardcover."
- **Cognitive walkthrough:** Q1 Yes, I would inspect the privacy information and pricing before entering Nikolai's details, and I would log in to use the account provided. / Q2 Yes, the clearly visible 'Log in' button is at the upper right. The 'Privacy', 'Terms', and 'Pricing' links are also available, although privacy is only visible after scrolling. / Q3 Yes, 'Log in' clearly matches the immediate task. 'Proceed' is less clear because it does not say whether it starts creation, accepts the privacy terms, or requires an account.
  - [CONTENT sev 2] **Opening copy uses opaque technical jargon** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Replace this with plain wording such as: 'Tell us about a family member and a treasured memory. We use those details to write and illustrate a personalised storybook preview.'
  - [H2 sev 2] **Main creation button does not describe its consequence** - evidence: [5] link "Proceed →". Fix: Label it explicitly as 'Create a storybook' and state any account or consent requirements before activation.
  - [TRUST sev 2] **Privacy is not prominent at the point of beginning** - evidence: The visible controls are [2] “How it works”, [3] “Pricing”, and [4] “Log in”; [10] “Privacy” only appears in the offscreen footer.. Fix: Add a visible 'How we use your data' link near 'Proceed', with a short summary stating data recipients, AI-training policy, retention, and deletion rights.
  - [ACC sev 1] **Illustration lacks a useful text alternative** - evidence: [image (no description) 430x440]. Fix: Add a meaningful alt description, or mark the image as decorative with empty alt text if it conveys no information.
- **Positives:** The service is described in a clear three-step process.; The page says the digital preview is free, without an account wall.; Pricing, privacy, terms, and contact links are present.; The interface avoids countdown timers, scarcity claims, and pre-ticked options.; The wording says printed hardcovers are shipped across the UK.

### Log in  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** Allows an existing StoryHearth customer to access their account.
- **What's happening:** The page displays a login form with empty email and password fields, plus links to create an account or access privacy, terms, and contact information.
- **First impression (Elena):** "Clean and straightforward, but the form relies entirely on placeholders instead of persistent field labels, and the footer legal links are very hard to see."
- **Cognitive walkthrough:** Q1 Yes. Signing in is the next necessary step, and the form is short and understandable. / Q2 Yes. The two fields and the large "Log in" button are immediately noticeable. / Q3 The placeholders "Email" and "Password" and the button "Log in" match what I want, but they are not proper visible labels.
  - [ACC sev 2] **Login fields have no persistent labels** - evidence: [5] and [6] are textboxes with "no label"; only the placeholders "Email" and "Password" are shown. Fix: Add persistent visible labels, "Email address" and "Password", and associate each label programmatically with its textbox.
  - [ACC sev 2] **Privacy, terms and contact links have very low contrast** - evidence: The footer items "Privacy", "Terms" and "Contact" are displayed in extremely faint text. Fix: Use text and link colours that meet WCAG contrast requirements and make the links visibly interactive on hover and focus.
- **Positives:** The page has a clear "Welcome back" heading and a prominent login button.; Privacy, terms and contact links are present directly on the screen.; There are no preselected options, urgency messages or distracting promotional elements.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** To show the signed-in user's book collection and provide a way to create a new book.
- **What's happening:** The account dashboard is displayed with a welcome message, an account sync warning, an empty-book state, and a button to create a new book.
- **First impression (Elena):** "The layout is calm and straightforward, but the prominent technical error message immediately undermines my confidence in whether the account is working properly."
- **Cognitive walkthrough:** Q1 Yes, I would try creating a book because that is the next step in my task and the purpose of this page is clear. / Q2 Yes, the orange "+ Create a new book" button is prominent and easy to notice. / Q3 Yes, "Create a new book" clearly matches what I want to do.
  - [H9 sev 3] **Unexplained account sync error** - evidence: "Error 0x80070057: profile sync incomplete.". Fix: Explain what failed in plain language, identify whether user data is affected, and provide a retry or support action.
  - [CONTENT sev 2] **Technical error code is not user-friendly** - evidence: "Error 0x80070057". Fix: Replace or supplement the code with a plain-language message and a visible recovery option.
  - [TRUST sev 2] **Unclear account identity** - evidence: "Welcome back, Demo". Fix: Display the account email or a recognisable account name and allow the user to verify which profile is active.
- **Positives:** The main action is visually prominent and clearly labelled.; Privacy, Terms, and Contact links are visible in the footer.; The empty state explains that there are no books yet rather than leaving the page blank.

### Create your book – character details  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Collect basic details about the child who will be the story’s hero and another person who will appear in it.
- **What's happening:** The character setup form is empty. Age and pronouns are unselected, while the additional person’s relationship is preselected as “Grandparent”.
- **First impression (Elena):** "The form is clean, concise and reasonably easy to understand. The question “Who’s the star of the story?” feels warmer and more personal than technical language, although I am wary of entering family details before checking the privacy link."
- **Cognitive walkthrough:** Q1 Yes, but I would first want to check the Privacy link because the form is collecting details about my child. / Q2 Yes, the relevant text boxes, drop-downs and the orange “Next” button are visible without scrolling. / Q3 Mostly. “Child’s first name,” “Age,” and “Pronouns” match my goal. “Who else is in the story?” and “Relationship” also work, although I would expect separate appearance fields for both characters rather than one appearance field that appears to refer only to the child.
  - [H3 sev 2] **Additional person relationship is preselected** - evidence: [11] “Relationship” is preselected as “Grandparent” even though no character has been entered.. Fix: Default Relationship to “Select relationship” and make it disabled or require a selection once a second person is added.
  - [CONTENT sev 2] **Only one appearance field is provided** - evidence: [9] “What do they look like? (optional)” appears between the child’s Pronouns field and “Who else is in the story?”. Fix: Label this field explicitly as “What does the child look like?” and add a separate optional appearance field for the additional character.
  - [TRUST sev 2] **Privacy information is not available without leaving the form** - evidence: The footer only provides links labelled “Privacy,” “Terms” and “Contact.”. Fix: Place a brief data-use reassurance beside the form and link directly to a clear privacy notice explaining retention, model training, third-party access and deletion.
- **Positives:** The form asks only for necessary basic information at this stage.; Appearance details are explicitly marked optional.; Pronouns are offered and include “he / him.”; The orange “Next” button is visually prominent.; Privacy, Terms and Contact links are visible in the footer.

### Story details form  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** Collect the setting, a meaningful object, and the family memory or idea that should guide the personalised story.
- **What's happening:** The page presents three empty input fields under 'Your story' and offers Back and Next buttons. Navigation links and legal/contact links remain available around the form.
- **First impression (Elena):** "This is uncluttered, easy to scan, and reassuringly ordinary. I do not feel manipulated or asked for more personal information than the story needs."
- **Cognitive walkthrough:** Q1 Yes, I would enter the three details now because they map directly to the story I want. / Q2 Yes, I notice a separate textbox for the setting, another for the special object, and a larger text area for the memory. / Q3 Yes. 'A special object' fits the brave stone, and 'Tell us the memory or idea behind your story' clearly asks for the school-morning memory.
  - [ACC sev 2] **Footer links have very low contrast** - evidence: The visible footer text 'Privacy', 'Terms', 'Contact' and '© 2026 StoryHearth Ltd.' is extremely faint against the pale background.. Fix: Use a darker, WCAG-compliant text colour while retaining a visibly separate footer area.
- **Positives:** All fields have visible labels, not placeholders alone.; The placeholders provide helpful examples without pretending to be completed values.; The form contains only the information needed to shape the story.; Back and Next controls are clearly visible.; Privacy, Terms and Contact links remain available.

### Reading level and illustration style  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Choose the intended reading difficulty and visual style for the personalised children's book.
- **What's happening:** The page presents four Lexile reading-level options and three illustration styles. Lexile 200L–500L and Watercolour are currently selected, with Back and Next controls available.
- **First impression (Elena):** "The page is uncluttered and easy to scan, but Lexile ranges are not an intuitive way for a parent to choose a reading level for a six-year-old. I would still continue because the range labels and radio buttons are visible and the options are limited."
- **Cognitive walkthrough:** Q1 Yes. I want an age-appropriate and comforting book, so I am willing to choose these settings. / Q2 Yes. The reading-level radio buttons and their current checked state are prominent. / Q3 Partly. “Lexile BR–200L” is recognisable as a beginner range, but the site should translate it into plain language and relate it to a child's age.
  - [H2 sev 2] **Reading-level choices are not explained in plain language** - evidence: The choices are labelled “Lexile BR–200L”, “Lexile 200L–500L”, “Lexile 500L–800L” and “Lexile 800L+”, with no explanation of what Lexile means or which range suits Nikolai.. Fix: Add a short plain-English explanation, such as “Best for ages 4–7”, and preserve the Lexile range as secondary information.
  - [H5 sev 2] **The default reading level may be too advanced for a six-year-old** - evidence: “Lexile 200L–500L” is checked even though the child previously entered was age 6.. Fix: Default to a range appropriate for the entered age and visibly explain why that range was selected, while allowing the parent to change it.
- **Positives:** The current selection is clearly visible in each group.; The three illustration-style descriptions give useful, non-technical choices.; The page preserves obvious Back and Next controls.; Privacy, Terms and Contact links remain available in the footer.

### Optional photo upload  (step 8)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_08.jpg)
- **Purpose:** Offer an optional reference photo before generating the personalised book.
- **What's happening:** The page asks for a clear photo of the child, explains that it will help the illustrations resemble them, and allows the user to go back or create the book. The upload is currently empty.
- **First impression (Elena):** "The screen is simple and the word “optional” reassures me, but the explanation says nothing here about who can see an uploaded child’s photo, whether it is used to train AI, or how deletion works."
- **Cognitive walkthrough:** Q1 I would not upload Nikolai’s photo yet because this page does not explain the photo’s privacy, retention, AI-training, or deletion terms. / Q2 Yes, I can see the “Choose file” control under the explanatory text. / Q3 The instruction “Upload a clear photo of your child’s face so the illustrations look like them” matches the purpose, but the browser control itself has no accessible label beyond “Choose file.”
  - [TRUST sev 3] **No privacy explanation beside a child-photo upload** - evidence: “Upload a clear photo of your child's face so the illustrations look like them.”. Fix: Add a short data-use summary directly above the upload control linking to a clear privacy notice, including processor access, retention, AI-training use, deletion rights, and children’s-data handling.
  - [ACC sev 2] **File upload has no descriptive label** - evidence: [30] file-upload (no label) accepts image/* (no file chosen). Fix: Give the upload control a visible label such as “Child reference photo (optional)” and associate it programmatically with file-format and size guidance.
  - [ACC sev 2] **Footer links have very low contrast** - evidence: “Privacy”, “Terms”, “Contact” and “© 2026 StoryHearth Ltd.” appear in extremely faint text.. Fix: Use darker footer text with a contrast ratio of at least 4.5:1 and retain a clear visible focus state.
- **Positives:** The heading explicitly says “optional,” so I do not feel forced to upload a child’s photo.; Back is available, giving me a clear way to revisit earlier choices.; The primary button, “Create my book,” clearly describes the result of continuing.; The screen is uncluttered and the remaining choice is easy to understand.

### Book creation progress  (step 9)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_09.jpg)
- **Purpose:** To process the submitted story details and generate the personalised digital book.
- **What's happening:** The page has changed to a large animated spinner, indicating that processing is underway, but there is no progress message, stage name, time estimate, cancel control, or error-handling information visible.
- **First impression (Elena):** "I can see that the site is busy, but “busy” is not a useful explanation. The silent spinner feels vague, particularly because the book concerns Nikolai’s personal details."
- **Cognitive walkthrough:** Q1 I would wait briefly because the spinner indicates activity, but I would not wait indefinitely without knowing what is happening. / Q2 I notice the spinner, but there is no labelled progress control or way to cancel and return. / Q3 No—there is no label explaining that the personalised book is being created.
  - [H1 sev 3] **Silent loading screen does not explain the process** - evidence: The page shows only a circular spinner and no status text.. Fix: Display a clear status such as “Creating Nikolai’s book…” alongside a text progress indicator and estimated time.
  - [H3 sev 3] **No way to stop or recover from generation** - evidence: No “Cancel”, “Back”, or “Start over” control is visible.. Fix: Add a clearly labelled “Cancel creation” control that returns me to the editable story details without losing them, plus a note about whether an incomplete book is saved.
  - [H9 sev 3] **Processing time and failure behaviour are not explained** - evidence: There is no time estimate, timeout guidance, retry option, or explanation of what to do if generation fails.. Fix: Show an approximate wait time and, on failure, a specific error message with “Try again” and “Return to my draft” options.
  - [TRUST sev 2] **No privacy reassurance during personalised generation** - evidence: The page contains no visible reference to privacy, data use, AI processing, retention, or deletion.. Fix: Add a brief, prominent note such as “Your story is used to generate this book. See our privacy notice for retention, AI-training and deletion details,” with a direct Privacy link.
- **Positives:** The animated spinner gives some indication that the site is processing my request.; The Privacy, Terms and Contact links remain available in the footer.; The page is uncluttered and keeps the processing indicator visually prominent.

### Generated storybook preview  (step 10)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_10.jpg)
- **Purpose:** Preview the generated personalised storybook, read all nine pages, regenerate the book, and proceed to hardcover ordering.
- **What's happening:** The first page of a generated nine-page book is displayed. The cover title contains a spelling error, the stated illustration style conflicts with the selected watercolour style, and pricing-related regeneration and hardcover-order controls appear below the preview.
- **First impression (Elena):** "I can see that a book was produced, but it feels generic rather than faithfully tailored to Nikolai and the memory I supplied. The title typo, wrong art style, sunny weather, and missing yellow raincoat undermine my confidence before I read further."
- **Cognitive walkthrough:** Q1 Yes, I would page through the book because I need to read every page carefully and check whether the school memory was used correctly. / Q2 Yes, I notice the right-arrow button labelled “›” immediately below the preview and can see that it is enabled while the left arrow is disabled on page 1. / Q3 Partly. The arrow is recognisable, but “1 / 9” is more prominent than an explicit next-page label; I understand it because it is positioned beside the arrow.
  - [CONTENT sev 3] **Spelling error in the book title** - evidence: The title reads “The Magical Adventrue of Nikolai” on both the page heading and the cover.. Fix: Correct “Adventrue” to “Adventure” before presenting the preview, and run a spelling check over all generated titles and page text.
  - [H4 sev 3] **The requested illustration style was not applied** - evidence: I selected “Watercolour — soft and dreamy,” but the preview says “Illustration style: Pop-art comic.”. Fix: Apply the selected style to generation, confirm that the returned book metadata matches the selection, and prevent preview generation when those values conflict.
  - [H4 sev 3] **Important supplied details are missing from the cover** - evidence: The cover shows bright sunshine and a simple child, while I asked for “the gate of his new school on a rainy morning” and supplied “blond straight hair, gap in his front teeth, yellow raincoat.” No rain, gate, or yellow raincoat is visible.. Fix: Ensure the specified setting, weather, appearance details, and keepsake are reflected consistently in the story and illustrations, and let me report a missed detail for correction.
  - [CONTENT sev 3] **The final sentence is incomplete** - evidence: “And from that day on, whenever Nikolai looked up at the sky, he would always remember”. Fix: Complete the sentence with a clear reference to courage, his mother, and the smooth grey stone.
  - [CONTENT sev 3] **The final illustration does not match the supplied memory** - evidence: The image shows Nikolai beside a simple house under an orange sky, while the requested setting was “the gate of his new school on a rainy morning.”. Fix: Ensure the final scene depicts the rainy school gate and includes meaningful details from the memory, with a preview or warning if details cannot be rendered.
  - [VALUE sev 2] **Paid regeneration price appears without context** - evidence: [8] “Regenerate entire book – $4.99”. Fix: State the full regeneration charge and consequences before the control, including currency, whether it is non-refundable, and whether it counts toward the hardcover price.
- **Positives:** The page clearly shows that generation finished and presents the book as a nine-page preview.; The previous control is correctly disabled on the first page, preventing an unnecessary move backwards.; The generated cover is readable and Nikolai is named in the title.; A separate “Order hardcover” link is available without making payment the only immediate action.

### Hardcover checkout  (step 12)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_12.jpg)
- **Purpose:** Collect delivery and payment details to purchase a printed hardcover copy.
- **What's happening:** The page itemises the £24.99 hardcover, £7.99 premium gift wrap and £12.99 shipping and handling for a £45.97 total. Gift wrap is checked by default, the price is said to be reserved for 09:57, and empty address and payment fields are shown.
- **First impression (Elena):** "The itemised total is easy to find, which is helpful, but the pre-ticked gift wrap and countdown make me suspicious of the £45.97 headline. I also notice the typo “Adventrue” repeated in the product title."
- **Cognitive walkthrough:** Q1 I would try removing the unwanted gift-wrap option, but I would not proceed to payment until the delivery cost and basic total were clear. / Q2 Yes, I notice the checked “Premium gift wrap” checkbox, although it is visually detached from the pricing line and not clearly presented as an optional add-on. / Q3 The label tells me what the charge is, but not that it is optional; “Your price is reserved for 09:57” also suggests urgency without explaining whether the book or only the discounted price is being held.
  - [DECEPTIVE sev 4] **Premium gift wrap is selected by default** - evidence: [6] checkbox “Premium gift wrap” (checked), adding “£7.99”. Fix: Make every optional extra unticked by default and clearly state “Optional — £7.99” beside the checkbox. Show the basic hardcover total and full total separately.
  - [DECEPTIVE sev 3] **Countdown timer creates false urgency** - evidence: “Your price is reserved for 09:57”. Fix: Remove the countdown, or replace it with a neutral statement such as “This price is available while the book remains available,” with any genuine reservation terms clearly stated.
  - [VALUE sev 3] **The basic delivered cost is not shown before the optional add-on** - evidence: “Hardcover: The Magical Adventrue of Nikolai £24.99”; “Premium gift wrap £7.99”; “Shipping & handling £12.99”; “Total £45.97”. Fix: Show “Hardcover £24.99”, “Delivery £12.99” and “Total before optional extras £36.98”, then update the final total only when an extra is actively selected.
  - [DECEPTIVE sev 3] **The checkout claims the price is reserved without explaining the conditions** - evidence: “Your price is reserved for 09:37”. Fix: Remove the countdown unless there is a genuine, verifiable reservation. If a reservation is necessary, state exactly what is reserved, how long it lasts, and what price or availability applies afterwards.
  - [CONTENT sev 2] **Product title contains a spelling error** - evidence: “The Magical Adventrue of Nikolai”. Fix: Correct “Adventrue” to “Adventure” everywhere the title appears.
  - [TRUST sev 2] **Privacy and terms are below the fold** - evidence: [12] link “Privacy” (offscreen); [13] link “Terms” (offscreen). Fix: Place Privacy, Terms and delivery/refund information visibly near the price and before the payment fields, with a short plain-English summary of how the purchase data is used.
- **Positives:** The price components and total are itemised rather than hidden behind an unlabelled total.; The delivery and payment sections are clearly separated.; A Privacy link, Terms link and Contact link are present, even though they require scrolling to see.
- **Would abandon here:** I would not enter my address or payment details until the pre-selected £7.99 add-on is removed and the basic delivered price is made clear. The countdown would make me more cautious, not more willing to buy.

### Privacy notice  (step 14)
`http://127.0.0.1:8765/privacy.html`

![screenshot](screenshots/step_14.jpg)
- **Purpose:** To explain how StoryHearth handles personal information, uploaded photographs and printed orders.
- **What's happening:** The page displays two short paragraphs covering information supplied for book creation, possible retention and processing of photographs by technology partners, and the non-refundable status of printed orders after production starts.
- **First impression (Elena):** "The page looks clean and easy to read, but the disclosure is far too vague for a service handling a child's photographs and personal family memories."
- **Cognitive walkthrough:** Q1 No, I would not upload a child's photograph because the notice does not provide enough information for me to make an informed decision. / Q2 Yes, the “Privacy” link was prominent in the checkout footer, although I only noticed it after creating the book. / Q3 Partly. “Privacy” correctly signposts this page, but “Privacy notice” promises more meaningful information than the page actually gives.
  - [TRUST sev 3] **No explanation of children's data** - evidence: “StoryHearth Ltd processes the information you provide (including names, stories and any photographs you upload) to create your book.”. Fix: State the age position, the legal basis for processing children's data, whether parental consent is required, and the specific safeguards used.
  - [TRUST sev 3] **Retention period is undefined** - evidence: “Uploaded images may be retained to improve our services”. Fix: Give separate retention periods for account data, source photographs, generated books and production files, including what happens after account deletion.
  - [TRUST sev 3] **Technology partners are not identified** - evidence: “may be processed by our technology partners”. Fix: Name every relevant provider and processor and link to a current subprocessor list explaining each provider's role, location and data access.
  - [TRUST sev 3] **AI training and model use are not disclosed** - evidence: The page does not mention artificial intelligence, model training or the use of uploaded images and stories to train generative models.. Fix: State explicitly whether customer photographs, stories or generated content are used for model training, including every model provider involved, and make any non-training use an informed, unbundled choice.
  - [H3 sev 3] **Deletion and account-control rights are missing** - evidence: The notice provides no information about viewing, exporting, correcting or deleting personal data or generated books.. Fix: Explain users' rights and provide direct controls to delete a book, uploaded source image and account, plus a confirmation that deletion has been completed.
  - [CONTENT sev 2] **No data-category or purpose detail** - evidence: The notice only says information is processed “to create your book” and images may be retained “to improve our services.”. Fix: List each category of data, each purpose, the legal basis, recipients and retention rule in a clear table.
  - [TRUST sev 2] **No security, location or rights information** - evidence: The page does not state where data is stored, what safeguards are used, or how to complain to a regulator.. Fix: Add processing locations and transfer safeguards, a summary of security controls, an automated-decision statement and the relevant supervisory authority or complaint route.
  - [H10 sev 2] **Refund term buried beside privacy** - evidence: “Printed orders are non-refundable once production begins.”. Fix: Move cancellation and refund terms into a properly labelled Terms or Delivery and Returns section, define the production cut-off and state when statutory consumer rights remain available.
  - [H10 sev 2] **Privacy link was only available at checkout** - evidence: I reached this information by clicking the checkout footer link after the upload and generation journey.. Fix: Place a concise privacy summary and upload link on the photo-selection screen, with a prominent “Privacy and photo use” link beside the upload control.
- **Positives:** The page title clearly identifies the subject as a privacy notice.; The prose is plain and not obscured by a sales message.; It acknowledges that names, stories and photographs are processed.; It gives a contact email for questions.
- **Would abandon here:** I would not upload a child's photograph or trust the service with further personal data while retention, partner use, AI training and deletion are unexplained.

## Generated output assessment
*Artifact:* Personalised children's storybook preview and checkout page

> I can see the seed of a comforting story about Nikolai and his brave stone, but this version is not trustworthy enough. The spelling errors, placeholder text, wrong pronouns, invented uncle, frightening forest scene, inaccurate illustrations and unfinished ending are all major failures. I would not pay £45.97 for this as a keepsake for Nikolai.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 2 | The output uses Nikolai, age six, the school gate, rainy morning, Varna, the smooth grey stone and the first-morning theme. It omits Mama, changes the yellow raincoat and blond appearance, invents Uncle Bartholomew, a la |
| coherence | 1 | The story jumps from a rainy school morning to an evening sky, a winding path, dark woods and home. It repeats the opening sentence, introduces unexplained objects and contradicts Nikolai's pronoun with “she followed him |
| age fit | 1 | The measured grade level is 8.3 for a requested reading age of six, and the prose uses words such as “ephemeral,” “crepuscular,” “ineffable” and “existential trepidation.” The threatening shadows may also frighten a youn |
| language | 1 | There are unresolved placeholders, the title says “Adventrue,” the name is misspelled “Nikola,” the pronoun is wrong, the ending is incomplete, “The End” is duplicated and several sentences are awkward. |
| text image fit | 2 | The cover and several story pages show bright sunshine even when the text describes rain, puddles and a school gate. The dark-woods image does not show the described teeth or whispering, and the final image does not repr |
| character consistency | 2 | The child is broadly repeated as the same simple figure, but he is consistently bald and green-clad rather than blond with a visible gap in his front teeth and a yellow raincoat. Mama is never depicted. |
| visual quality | 2 | The images are clean, simple and free of obvious anatomical artefacts, but they are rudimentary rather than attractive keepsake illustrations, use the wrong stated style, contain repeated compositions and do not match im |
| emotional resonance | 1 | The stone and school-anxiety theme have potential, but the story never develops the promised bond with Mama and replaces it with a threatening fantasy sequence. The unfinished ending makes the book feel unreliable rather |

- **used correctly:** Nikolai's first name; His age of six; The he/him pronoun in most of the story; The school-gate setting; The rainy-morning premise in the opening; The smooth grey brave stone; The beach in Varna; The requested first morning at a new school
- **missing:** Mama as a character; The parent relationship; The yellow raincoat; The blond straight hair; The gap in Nikolai's front teeth; A coherent story about entering the new school; A proper dedication using the recipient and sender information
- **changed:** The intended school-morning story becomes an evening and dark-woods fantasy; Mama is replaced by an invented Uncle Bartholomew; The requested yellow raincoat becomes a green top; The intended gentle reassurance becomes a sequence involving threatening shadows; The requested BR-200L level is replaced by adult-level vocabulary
- **invented:** Uncle Bartholomew; A lantern; A winding path; Dark woods with shadows that grow teeth; A shiny red balloon; A final sentence about looking up at the sky

### Part by part
#### Cover / Title page
![I1](artifacts/capture_01/img_00.jpg)
> A StoryHearth original Illustration style: Pop-art comic
- *Picture:* A simple pale-blue outdoor scene with a small house, a smiling bald child in a green top, a grey stone and a bright sun. The cover title reads “The Magical Adventrue of Nikolai.”
- *Reaction:* The cover is immediately less reassuring than the idea promised. “Adventrue” is an obvious spelling error, the style is labelled “Pop-art comic” rather than the expected watercolour style, and the sunny scene does not reflect the rainy school-morning memory.
  - [language, sev 3] The title visibly says “The Magical Adventrue of Nikolai”.
  - [fidelity, sev 2] The cover shows a sunny scene with a house, stone and child, but does not show the rainy school gate, Mama, the yellow raincoat, blond hair or gap in Nikolai's teeth.
  - [visual_quality, sev 2] The illustration is extremely basic and is not watercolour-style as apparently promised; the title and image also do not establish the intended rainy setting.
- **Change I'd make:** Correct the title to “The Magical Adventure of Nikolai” and redraw the cover as a watercolour-style rainy school gate, with Nikolai's blond hair, visible gap-toothed smile, yellow raincoat and the stone in his pocket.

#### Page 2 / Dedication
![I2](artifacts/capture_03/view_00.jpg)
> For {{recipient_name}}, with love from {{sender_name}}
- *Picture:* A mostly blank preview panel showing the unresolved dedication text, with website navigation and ordering controls around it.
- *Reaction:* This looks unfinished rather than personal. Leaving template placeholders in a finished book is a serious quality-control failure, particularly when this is meant to be a keepsake.
  - [language, sev 4] The page displays “{{recipient_name}}” and “{{sender_name}}”.
  - [fidelity, sev 3] The requested recipient and sender details were not inserted into the dedication.
  - [visual_quality, sev 3] The preview contains a large blank area and unresolved template text.
- **Change I'd make:** Replace the placeholders with a real dedication, for example: “For Nikolai, with love from Mama.” Do not expose the order or regeneration interface in the printed book.
- **Suggested rewrite:** For Nikolai, with love from Mama

#### Page 3 / Opening
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in the gate of his new school on a rainy morning, there lived a curious child named Nikolai. Nikolai was 6 years old and loved nothing more than a smooth grey brave stone from the beach in Varna.
- *Picture:* A simple outdoor scene with a house, a smiling bald child in a green top, a grey stone and a bright sun. Despite the alt text saying “rainy morning,” the image is sunny and has no rain or school gate.
- *Reaction:* The story begins with several of the important details, including the school gate, rainy morning, age and Varna stone. However, the illustration contradicts the text, and “there lived” makes the setting sound like a permanent residence rather than a first morning at school.
  - [text_image_fit, sev 3] The text says “on a rainy morning” and the image shows a bright sun, no rain and no visible school gate.
  - [character_consistency, sev 3] The child is bald and wears a green top, while the requested description says blond straight hair and a yellow raincoat.
  - [fidelity, sev 2] The requested appearance of “blond straight hair, gap in his front teeth, yellow raincoat” is not shown.
  - [language, sev 2] “In the gate of his new school” is awkward wording, and “there lived” does not fit the requested event.
- **Change I'd make:** Rewrite this as a clear first-morning scene and make the image show rain, the school gate, Nikolai's blond hair, gap-toothed smile and yellow raincoat, with Mama giving him the stone.
- **Suggested rewrite:** On the first rainy morning at his new school, Nikolai stood at the gate with Mama. He was six and felt a little scared. Mama put a smooth grey brave stone from their beach holiday in Varna into his pocket. “You can keep it with you,” she said. “Whenever you feel worried, remember how calm the sea was.”

#### Page 4 / The sky
![I4](artifacts/capture_05/img_00.jpg)
> One evening Nikolai gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* A simple child standing beside the house under a purple evening sky with stars. The child is bald and wears a green top.
- *Reaction:* This is clearly aimed at an adult reader rather than a six-year-old. The dense, abstract vocabulary is both difficult and emotionally cold, and it changes the story from a first school morning to an unexplained evening scene.
  - [age_fit, sev 4] The sentence uses “ephemeral,” “luminescence,” “crepuscular,” “engendered,” “melancholy,” “juxtaposing,” “ineffable” and “existential trepidation.”
  - [coherence, sev 3] The story moves from “a rainy morning” to “One evening” without explaining the time change or connection to the school gate.
  - [character_consistency, sev 2] The child remains bald and wears a green top instead of the requested blond hair and yellow raincoat.
  - [fidelity, sev 3] The requested event was Nikolai's first morning at school, not an evening meditation beneath the sky.
- **Change I'd make:** Replace the passage with short, concrete sentences about the rainy sky, the school gate and Nikolai asking Mama whether he can go in.
- **Suggested rewrite:** Nikolai looked up at the grey sky. Rain dripped from his yellow hood. He held Mama's stone tightly. “I can do this,” he said, even though his voice shook a little.

#### Page 5 / Rain and shelter
![I5](artifacts/capture_06/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Nikola pulled up his hood and ran for shelter, holding a smooth grey brave stone from the beach in Varna tight.
- *Picture:* A simple outdoor scene with a house, a bald child in a green top, a grey stone and a bright sun. There is no rain, puddle, hood or sense of running for shelter.
- *Reaction:* The story has another useful bravery detail, but it misspells Nikolai and the image repeats the sunny scene instead of showing the rain. I would notice that immediately and would not trust the rest of the book.
  - [language, sev 3] The child's name is incorrectly written as “Nikola,” and “holding ... tight” should be “holding ... tightly.”
  - [text_image_fit, sev 3] The text describes heavy rain, puddles, a hood and running, while the image shows sunshine, no puddles and no hood.
  - [character_consistency, sev 2] The child is bald and wears green rather than having blond hair and wearing a yellow raincoat.
  - [fidelity, sev 2] The yellow raincoat requested for Nikolai is absent.
- **Change I'd make:** Correct the name and grammar, and replace the repeated sunny image with Nikolai in his yellow raincoat, holding the stone while he waits near the school gate with Mama.
- **Suggested rewrite:** Then the rain began to pour. Big grey drops splashed into the puddles. Nikolai pulled up the hood of his yellow raincoat and hurried back toward the school gate, holding the smooth grey stone tightly. “Stay with me,” Mama said. “You are not alone.”

#### Page 6 / Uncle Bartholomew
![I6](artifacts/capture_07/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Nikolai, follow me!" he called, and she followed him along the winding path.
- *Picture:* A simple scene showing a taller adult in a blue top holding a yellow lantern-like shape beside Nikolai. The background is brown and green, with the same house.
- *Reaction:* This is a major narrative and identity error. Uncle Bartholomew was never requested, the setting inexplicably becomes a winding path, and “she” contradicts the established he/him pronouns.
  - [fidelity, sev 4] “Uncle Bartholomew” and the lantern are invented, while the requested companion was Mama.
  - [coherence, sev 4] The story jumps from the school gate to a winding path without explanation, and “she followed him” contradicts Nikolai's specified pronouns.
  - [character_consistency, sev 3] The child is still bald and wears green, not blond hair and a yellow raincoat; the new adult is not Mama.
  - [text_image_fit, sev 2] The image does show an adult and Nikolai, but it does not establish the school morning or the requested relationship with Mama.
- **Change I'd make:** Remove Uncle Bartholomew and keep the focus on Nikolai and Mama at the school gate. Correct the pronoun to “he” and show Mama helping him take his first steps inside.
- **Suggested rewrite:** “Come on, Nikolai,” Mama said. “I will wait just inside the gate.” She held out her hand. Nikolai looked at the busy corridor, then felt the stone in his pocket. He took a deep breath and followed her.

#### Page 7 / The dark woods
![I7](artifacts/capture_08/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Nikolai again. Nikolai clutched a shiny red balloon and trembled in the dark.
- *Picture:* A simple night scene with Nikolai, a red balloon, trees, a crescent moon and stars. The illustration does not show teeth in the shadows or any whispering figures.
- *Reaction:* This is frightening and disconnected from the requested school-day story. “The shadows grew teeth” and “no one would ever find Nikolai again” are alarming for a six-year-old, especially when the requested comfort was gentle courage.
  - [age_fit, sev 4] “The shadows grew teeth and whispered that no one would ever find Nikolai again” introduces a threatening, horror-like image.
  - [fidelity, sev 4] The woods, threatening shadows and red balloon are not connected to the supplied school-gate memory.
  - [coherence, sev 4] The story suddenly changes from a school morning to a dark forest and introduces a balloon without setup.
  - [text_image_fit, sev 2] The image contains a balloon and dark setting, but the threatening teeth and whispering are not depicted.
  - [character_consistency, sev 2] Nikolai again appears bald and in green rather than blond with a yellow raincoat.
- **Change I'd make:** Delete the frightening forest sequence. Replace it with a manageable school-corridor moment in which Nikolai hears a loud noise, touches the stone and decides to ask a teacher for help.
- **Suggested rewrite:** Inside, the corridor was louder than Nikolai expected. A group of children hurried past him. His stomach fluttered, so he reached for the stone. Then he remembered Mama's words and asked a teacher, “Where should I go?”

#### Page 8 / The ending
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in the gate of his new school on a rainy morning, there lived a curious child named Nikolai. At last the sun came out, and Nikolai skipped all the way home, happier than ever.
- *Picture:* A simple sunny outdoor scene with the house, bald Nikolai in a green top and no visible stone, rain or school gate. The image closely repeats the cover.
- *Reaction:* The optimistic ending is pleasant, but it repeats the opening almost word for word and does not show Nikolai overcoming the actual school fear. The image is another generic sunny scene rather than a school-morning conclusion.
  - [coherence, sev 3] The opening sentence is repeated in the ending, and the sun suddenly appears after the darker forest sequence without a clear transition.
  - [fidelity, sev 2] The ending returns to the requested school setting only in the repeated sentence; it does not show Mama, the gate, the stone or a first successful school interaction.
  - [text_image_fit, sev 2] The text says Nikolai went home after the sun came out, while the image shows him standing beside the house with no school context or movement.
  - [character_consistency, sev 2] The child is still bald and green-clad rather than blond and wearing the yellow raincoat.
- **Change I'd make:** Replace the repeated opening with a concrete resolution: Nikolai enters the classroom, speaks to his teacher and keeps the stone safe after the school day.
- **Suggested rewrite:** By the end of the morning, Nikolai had found his classroom and spoken to his teacher. When the final bell rang, he waved to Mama. The stone was still in his pocket, and Nikolai smiled. He knew he could be brave and still feel a little scared.

#### Page 9 / Final page
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Nikolai looked up at the sky, he would always remember The End
- *Picture:* An orange end page with a simple house, smiling bald Nikolai in a green top and no story-specific school or rain details.
- *Reaction:* The sentence stops before saying what Nikolai would remember, and “The End” appears twice. This is not a finished keepsake page.
  - [language, sev 4] The final sentence ends abruptly at “remember” and “The End” is printed twice.
  - [coherence, sev 4] The promised reflection is incomplete, so the emotional resolution is missing.
  - [fidelity, sev 2] The final page does not mention Mama, the school gate, the stone or the first morning.
  - [character_consistency, sev 2] The recurring child remains bald and green-clad, not blond in a yellow raincoat.
- **Change I'd make:** Complete the sentence, remove the duplicate ending and use an image that ties back to the school morning and the stone.
- **Suggested rewrite:** The End From that day on, whenever Nikolai felt worried, he touched the stone in his pocket and remembered Mama waiting for him at the gate. Brave did not mean never being afraid. It meant taking one little step anyway.

#### Checkout
![I10](artifacts/capture_12/view_00.jpg)
![I11](artifacts/capture_12/view_01.jpg)
> Checkout Your price is reserved for 09:40 Hardcover: The Magical Adventrue of Nikolai	£24.99  Premium gift wrap	£7.99 Shipping & handling	£12.99 Total	£45.97 Delivery Address Payment Card number Expiry CVC Pay now
- *Picture:* A checkout form showing the book price, a countdown, a pre-ticked premium gift-wrap checkbox, shipping charge, total, blank address and card fields, and a prominent “Pay now” button.
- *Reaction:* I would be wary of paying here. The title is misspelled, the premium gift wrap is pre-ticked, a countdown is creating pressure, and the £45.97 total is much higher than the headline £24.99 book price because of the add-on and shipping.
  - [language, sev 3] The checkout repeats the misspelled title, “The Magical Adventrue of Nikolai.”
  - [fidelity, sev 3] The premium gift wrap was selected in the supplied inputs, but it is visibly pre-ticked at checkout and the page does not clearly show the user actively choosing it.
  - [visual_quality, sev 2] The page uses a countdown message, “Your price is reserved for 09:40,” alongside the payment form.
- **Change I'd make:** Do not preselect gift wrap, explain every charge before checkout, remove artificial urgency, correct the title, and state clearly whether the price includes shipping and whether the order can be cancelled or refunded.

**Top changes to the output:** 1. Replace the invented, frightening plot with a short, reassuring story about Mama helping Nikolai enter his new school. | 2. Fix all title, name, pronoun, grammar, placeholder and ending errors before showing a final proof. | 3. Show Nikolai consistently as blond, gap-toothed and wearing his yellow raincoat, with Mama included. | 4. Generate watercolour-style illustrations that accurately show the rainy school gate, the stone, Mama and the emotional resolution. | 5. Remove the checkout countdown and do not pre-tick gift wrap; make the £45.97 total and cancellation/refund information explicit.

## Recommendations (participant's priorities)
- **[high] Replace the invented and frightening plot with a short, reassuring story about Mama helping Nikolai enter his new school, using the brave stone as the emotional focus.** (Generated storybook preview) - Nikolai is six and anxious about starting school; the book should support his confidence rather than introduce threatening shadows and an unnecessary fantasy adventure.
- **[high] Proof the entire output before presenting it: correct “Adventrue,” “Nikola,” pronouns, placeholders, duplicated text, grammar and the incomplete final sentence.** (Generated storybook preview) - A keepsake with obvious editing failures feels careless and makes the rest of the personalisation untrustworthy.
- **[high] Ensure the selected illustration style is actually applied, and generate watercolour illustrations that consistently show Nikolai as blond and gap-toothed in his yellow raincoat, with Mama included.** (Reading level and illustration style / Generated storybook preview) - The images should reflect the personal details and chosen style, otherwise the book does not feel made for Nikolai.
- **[high] Do not pre-tick “Premium gift wrap,” remove the countdown, show the base hardcover price and total before optional purchases, and state the conditions for any reservation.** (Hardcover checkout) - Pre-ticked add-ons and “reserved for 09:57” pressure are exactly the sort of deceptive patterns that make me leave a site.
- **[high] Provide complete, prominent information about children's data: categories, purposes, technology partners, storage location, retention periods, AI or model use, deletion rights and account controls.** (Privacy notice and optional photo upload) - I need to know exactly who can see my child's details and whether they are used to train AI before uploading anything or entering sensitive information.
- **[high] Add a privacy summary and link directly beside the child-photo upload, with an explicit choice to continue using written details only.** (Optional photo upload) - The decision about a child's photograph should not require leaving the form or guessing what happens to the image.
- **[high] Explain the generation process with plain wording, estimated time, privacy reassurance, failure handling, and a way to stop or retry without submitting duplicate personal data.** (Book creation progress) - The silent spinner made me unsure whether the story was being generated, saved or merely loading.
- **[medium] Add persistent visible labels to the email and password fields and improve the contrast of privacy, terms and contact links.** (Log in) - The placeholders disappeared when I typed, and the faint legal links were too easy to miss.
- **[medium] Explain reading levels in plain language, for example with an age range or a simple “for a six-year-old” label, rather than relying on Lexile codes.** (Reading level and illustration style) - “BR–200L” was not a useful description for choosing a story for a six-year-old, and the default may have been too advanced.
- **[medium] Remove opaque phrases such as “multimodal generative narrative engine” and “lived-experience corpus” from the family-facing homepage.** (Home page) - Plain language is more trustworthy and makes the benefit easier to understand without making the product sound needlessly technical.
- **[low] Describe the main button's consequence clearly, such as “Start creating Nikolai's book,” and provide a useful text alternative for the decorative illustration.** (Home page) - The button should tell me what will happen, and the image should not be inaccessible or presented as essential without explanation.
- **[medium] Explain the “profile sync incomplete” error in plain language and clarify whether any account or personal data is affected.** (My books dashboard) - An unexplained error code made me question the reliability of the account and the data involved.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This is a website for creating personalised storybooks featuring children and other people. It could be especially appealing to parents who want a reassuring story about their child, but it is not currently suitable for handling children's data responsibly.
- **What was the most frustrating or confusing moment, and why?** The checkout page was the most disturbing moment: “Premium gift wrap” was already selected and the countdown said, “Your price is reserved for 09:57.” That made the £45.97 total feel deliberately pressured, especially when the basic delivered cost was not shown before the add-on.
- **What was the best moment?** The story details form was the best part because the prompts helped me describe Nikolai's first morning at school and his smooth grey brave stone without forcing me to upload a photograph. It felt possible that the story could have been genuinely comforting.
- **Was there any point where, in real life, you would have given up? Where and why?** Yes, I would probably have stopped at checkout until the optional gift wrap was unticked and the real price was explained. More seriously, I would have abandoned the purchase after reading the privacy notice, because it did not explain children's data, AI training, retention, technology partners, deletion or account control.
- **What did you expect to find or be able to do that wasn't there?** I expected a clear explanation of what happens to Nikolai's details, whether they are used to train AI, who can access them, how long they are kept and how to delete them. I also expected a complete proof before payment, accurate watercolour illustrations, a finished story, the basic price, and plain-language cancellation and refund terms.
- **Did you trust this website with your information (and your family's)? Why or why not?** No, I would not trust this website with my family's information. Phrases such as “may be retained” and “may be processed by our technology partners” are too vague, and there was no privacy explanation beside the child-photo upload. The unexplained sync error, wrong illustration style and dishonest-feeling checkout patterns reduced my trust further.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would not pay £45.97 for this version. After removing the unnecessary gift wrap, £37.98 still felt too much for a book with spelling errors, an incomplete ending, inaccurate illustrations and a reading level of 8.3 for a six-year-old. I might consider paying around £20 to £25 if the story were genuinely reassuring, properly edited, accurately illustrated and backed by clear privacy, refund and cancellation information.
- **If the site produced something for you, how do you feel about it overall?** I can see the seed of a comforting story about Nikolai and his brave stone, but this version feels unreliable and disappointing. The title misspelling, unfinished sentence, wrong pronouns, invented uncle, frightening forest scene, inaccurate illustrations and missing emotional resolution would make it unsuitable as a keepsake.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | The promise is relevant to what I want, and the three-step explanation is easy to follow. However, 'multimodal generative narrative engine', 'story artefacts' and 'lived-experience corpus' sound needlessly technical for  | click |
| 2 | Log in – StoryHearth | neutral (1) | The login form is simple and uncluttered, but I notice that the email and password fields have no visible labels—only placeholders. I also see the privacy and terms links straight away, which is reassuring, although they | type; type; click |
| 3 | My books – StoryHearth | suspicious (-1) | I have logged in successfully, which is clear from reaching "Welcome back, Demo." However, "Error 0x80070057: profile sync incomplete" is alarming and gives me no explanation of whether my account or any data is affected | click |
| 4 | Create your book – StoryHearth | reassured (1) | This is straightforward and I would be willing to complete it. I notice the Next button, and the labels mostly match what I need. The appearance field example mentions wellies, so I will keep Nikolai’s description concis | type; select; select; type; type; select |
| 5 | Create your book – StoryHearth | reassured (1) | All the selections now show the intended values, including Parent, so I can continue. The appearance text is clipped in the box, but I know what I entered and it is optional anyway. | click |
| 6 | Create your book – StoryHearth | reassured (2) | This is clear and I would fill it in. The labels tell me exactly what is needed, and the prompts help without forcing me into unnecessary detail. I will use the school gate on a rainy morning, Nikolai's smooth grey brave | type; type; type; click |
| 7 | Create your book – StoryHearth | reassured (1) | The controls are visually clear, but “Lexile” is not a familiar way for me to choose a story for a six-year-old. Since “BR–200L” appears to be the beginner range and Nikolai reads at age six, I will select that rather th | click; click |
| 8 | Create your book – StoryHearth | hesitant (0) | This is clear, and “optional” makes it straightforward to decline. I would not upload a child’s photo without first reading the privacy and data-use terms, so I will skip it and create the book from the written details. | click |
| 9 | Create your book – StoryHearth | anxious (-1) | The spinner shows that clicking “Create my book” started something, but it is not clear whether the story is being generated, saved, or merely loading. For a process that uses my child’s details, I would like plain wordi | wait_for_change |
| 10 | Your storybook – StoryHearth | annoyed (-1) | The book has appeared, so the generation worked, but the first thing I notice is the typo in “The Magical Adventrue of Nikolai.” More importantly, I selected “Watercolour — soft and dreamy,” yet the cover says “Illustrat | flip_through |
| 11 | Your storybook – StoryHearth | annoyed (-1) | I have now seen the whole book, and the ending is especially disappointing: the sentence “And from that day on, whenever Nikolai looked up at the sky, he would always remember” does not finish the thought, while the illu | scroll; click |
| 12 | Checkout – StoryHearth | suspicious (-2) | This is the first clear price, but £45.97 is not the price of the hardcover alone. “Premium gift wrap” is already checked without me asking for it, and “Your price is reserved for 09:57” adds pressure; I do not trust tha | click |
| 13 | Checkout – StoryHearth | suspicious (-1) | That worked, at least: the gift-wrap box is empty and the total has dropped by £7.99. The real price without the optional add-on is now £37.98, but I still distrust the countdown because nothing here explains whether the | click |
| 14 | Privacy – StoryHearth | anxious (-2) | This is a privacy notice only in the loosest sense. “May be retained” and “may be processed by our technology partners” do not tell me who those partners are, whether my child's data is used to train AI, how long anythin | done |
