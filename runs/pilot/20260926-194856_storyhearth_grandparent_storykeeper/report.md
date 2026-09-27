# UserQA report: Margaret Ellison on http://127.0.0.1:8765/

*Persona:* **Margaret Ellison** (71) - Retired primary-school teacher who wants to pass family stories on to her grandchildren.  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 12 steps | *Pages reviewed:* 10 | *Issues:* 27 | *LLM calls:* 15 | *Wall time:* 310.9 s

## What the agent understood the website to be
- **what it is:** A website that turns family memories into personalised, illustrated storybooks.
- **who it is for:** Families who want to preserve a personal memory as a story starring their relatives.
- **value proposition:** Create a bespoke digital story preview, with the option of ordering a printed hardcover shipped across the UK.
- **pricing model:** A free digital preview is advertised, and physical hardcovers are sold; exact prices are not shown here.
- **fit for me:** It appears well suited to preserving a family story for Oliver, although I would need plain language and clear costs before trusting it with personal details.
- **main tasks:** Create or log into an account, Add a child and another family member, Describe a family memory, Read the generated storybook preview, Check the price of a printed hardcover

## Scores
- SUS: **37.5** (grade F; 68 = industry average) - inconsistent responding flagged
- UEQ-S: pragmatic -1.5, hedonic -0.75 (range -3..+3)
- Likelihood to recommend (0-10): 2
- Output keepsake-worthiness (1-5): 1
- Verdict: *"A promising idea spoiled by a book that was not personal, not suitable for Oliver, and not clear or trustworthy enough to buy."*
- Would have abandoned at step 12 (127.0.0.1:8765/checkout.html \| Checkout): I would not continue because the paid gift-wrap option was selected without my consent, the total is considerably higher than the base book price, and I do not need to provide payment details merely to establish the cost. [self-report]

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 3 | H9 | My books dashboard | Unexplained technical profile-sync error | “Error 0x80070057: profile sync incomplete.” | Replace the error code with a plain-language message such as “We could not finish loading your profile. Your account is secure; please try again,” and provide a visible “Try again” control. |
| 3 | CONTENT | Generated storybook preview | The title contains a spelling error | The heading says “The Magical Adventrue of Oliver” and the cover repeats “The Magical Adventrue of Oliver.” | Correct the title to “The Magical Adventure of Oliver” and review all generated titles for spelling before showing the preview. |
| 3 | H2 | Generated storybook preview | The selected illustration style was not followed | The earlier choice was “soft watercolour,” but the generated page says “Illustration style: Pop-art comic” and the cover has a flat, simple cartoon style. | Apply the selected “soft watercolour” style consistently, or clearly explain that the chosen style is unavailable and ask me to choose again. |
| 3 | DECEPTIVE | Hardcover checkout | Premium gift wrap is selected by default | [6] “Premium gift wrap” is checked, with “£7.99” added to the total. | Make every paid add-on unchecked by default, place its full price beside the option, and recalculate the total immediately when it is changed. |
| 2 | ACC | Log in, My books dashboard, Create your book – characters, Story details form, Generating book (x5) | Footer text has very weak contrast | The links “Privacy,” “Terms,” “Contact,” and “© 2026 StoryHearth Ltd.” are shown in extremely pale grey. | Use a darker, higher-contrast text colour with a contrast ratio of at least 4.5:1. |
| 2 | H2 | StoryHearth home page | The opening description uses unnecessary technical language | “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.” | Replace this with plain language such as: “Turn a treasured family memory into a personal storybook starring your loved ones.” |
| 2 | ACC | Log in | Email and password fields have no visible labels | Items [5] and [6] are described as textboxes with no label; only the placeholders say “Email” and “Password.” | Add permanent visible labels, “Email address” and “Password,” and associate each label properly with its textbox. |
| 2 | H2 | My books dashboard | The dashboard greets the account name rather than the person's name | “Welcome back, Demo” | Use the account holder's first name, or omit the name entirely if the service does not know a real first name. |
| 2 | H2 | Choose the look & feel | Lexile ranges are unexplained | The page labels the choices “Lexile BR–200L,” “Lexile 200L–500L,” “Lexile 500L–800L,” and “Lexile 800L+.” | Add a plain-English explanation, such as “Easiest—suitable for children beginning to read,” and show the recommended reading range by age. |
| 2 | H5 | Choose the look & feel | The default reading level may be too advanced for Oliver | “Lexile 200L–500L” is already checked, even though Oliver is five and the requested reading age is five. | Default to the easiest range when the child's age is five, and ask for confirmation with a sentence such as “This is the recommended level for a child aged five.” |
| 2 | TRUST | Optional photo upload | No plain-language explanation of how an uploaded photo is handled | “Upload a clear photo of your child's face so the illustrations look like them.” No nearby text explains whether the original photo is kept, whether faces are c | Add a short link or note stating whether photos are used only to create the illustrations, whether the original upload is deleted, and where the privacy explanation can be read. |
| 2 | H1 | Generating book | The loading state has no explanatory text | The page shows only a circular loading indicator and no message such as “Creating Oliver’s book.” | Add a clear status message: “Creating Oliver’s book. This may take a moment.” Include the book title and, if available, a progress indicator. |
| 2 | H3 | Generating book | No way to cancel or leave the loading process | There is no “Cancel,” “Back,” or “Continue later” control on the loading page. | Provide a clearly labelled “Cancel” or “Continue later” action, with an explanation of whether the entered story details will be saved. |
| 2 | CONTENT | Generated storybook preview | The generated cover omits important personal details | The cover shows “Oliver,” a farmhouse, and a blue kite, but not his brown curly hair, freckles, green wellies, Grandma Maggie, or the kite’s connection to Grand | Use the supplied character descriptions on the cover and throughout the illustrations, or explain which details are intentionally left out. |
| 2 | VALUE | Hardcover checkout | The cost rises sharply through shipping and the added option | “Hardcover: The Magical Adventure of Oliver £24.99,” followed by “Premium gift wrap £7.99,” “Shipping & handling £12.99,” and “Total £45.97.” | State “£37.98 delivered without gift wrap” prominently and provide a plain-language explanation of the delivery charge. |

## Page-by-page
### StoryHearth home page  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Introduce the personalised storybook service and lead the visitor into creating a book, checking prices, or logging in.
- **What's happening:** The home page displays the service proposition, prominent calls to action, a three-step explanation, customer quotations, and links to help, privacy, terms, and contact details.
- **First impression (Margaret):** "The warm cream colour and simple layout feel suitable for a family keepsake, but the opening description sounds technical and off-putting. The more straightforward “How it works” section reassures me."
- **Cognitive walkthrough:** Q1 Yes. I understand that “Proceed” should lead to creating a story, and the free preview means I can explore without paying. / Q2 Yes. The orange “Proceed →” button and “See pricing” button are both prominent. / Q3 Mostly. “Proceed” is clear enough, although “Create my storybook” would tell me more precisely where I am going. “See pricing” also matches what I want to know.
  - [H2 sev 2] **The opening description uses unnecessary technical language** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Replace this with plain language such as: “Turn a treasured family memory into a personal storybook starring your loved ones.”
  - [VALUE sev 1] **Exact hardcover prices are not shown on the landing page** - evidence: The page says “See pricing” and “Printed hardcovers shipped across the UK” but gives no price.. Fix: Show a clear starting price, such as “Hardcovers from £24.99,” while retaining the Pricing link.
  - [ACC sev 1] **The decorative image has no description** - evidence: The image beside the opening text is shown as “image (no description)”.. Fix: Add concise alternative text describing the personalised children's book and family characters.
- **Positives:** The page clearly states “Free digital preview,” which reduces concern about having to pay immediately.; The three-step explanation uses straightforward headings and promises an illustrated preview in about a minute.; The main text is large with strong contrast.; Pricing, privacy, login, and contact options are visible without hunting.

### Log in  (step 3)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** Sign in to an existing StoryHearth account.
- **What's happening:** The page shows two empty fields for an email address and password, a “Log in” button, an option to create an account, and footer links for Privacy, Terms, and Contact.
- **First impression (Margaret):** "It looks calm, uncluttered, and easy to understand. I can see the form immediately, although the fields should have proper labels rather than relying only on placeholders."
- **Cognitive walkthrough:** Q1 Yes. The page clearly asks for the account details I already have. / Q2 Yes. The two large fields and the “Log in” button are immediately visible. / Q3 Mostly. The “Log in” button and the “Email” and “Password” placeholders match what I want, but the fields themselves have no accessible labels.
  - [ACC sev 2] **Email and password fields have no visible labels** - evidence: Items [5] and [6] are described as textboxes with no label; only the placeholders say “Email” and “Password.”. Fix: Add permanent visible labels, “Email address” and “Password,” and associate each label properly with its textbox.
  - [ACC sev 2] **Footer text has very weak contrast** - evidence: The links “Privacy,” “Terms,” “Contact,” and “© 2026 StoryHearth Ltd.” are shown in extremely pale grey.. Fix: Use a darker, higher-contrast text colour with a contrast ratio of at least 4.5:1.
- **Positives:** The page has a clear “Welcome back” heading.; The form is uncluttered and the Log in button is large and prominent.; The page offers a clear route to create an account if needed.; Privacy, Terms, and Contact links are present.

### My books dashboard  (step 4)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Shows the books in the signed-in account and provides the main control for starting a new personalised book.
- **What's happening:** After login, the dashboard says “You have no books yet” and offers “+ Create a new book.” A warning at the top says that profile synchronisation is incomplete.
- **First impression (Margaret):** "The large orange button is easy to find and the empty-book message is reassuring, but the technical error code makes the page look unreliable and leaves me wondering whether it has affected my account."
- **Cognitive walkthrough:** Q1 Yes, I would try creating the book because the prominent button appears to be the clear next step. / Q2 Yes, “+ Create a new book” is prominent beneath the empty-book message. / Q3 Yes. It plainly says that I can create a new book, although “book” could be explained more specifically as a personalised storybook.
  - [H9 sev 3] **Unexplained technical profile-sync error** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the error code with a plain-language message such as “We could not finish loading your profile. Your account is secure; please try again,” and provide a visible “Try again” control.
  - [H2 sev 2] **The dashboard greets the account name rather than the person's name** - evidence: “Welcome back, Demo”. Fix: Use the account holder's first name, or omit the name entirely if the service does not know a real first name.
  - [ACC sev 2] **Footer text has weak contrast and is very small** - evidence: The “Privacy,” “Terms,” “Contact,” and “© 2026 StoryHearth Ltd.” footer text appears faint and undersized.. Fix: Use at least 16-pixel text with strong colour contrast and make the clickable areas comfortably large.
- **Positives:** The change to the book dashboard and the “Log out” link clearly confirm that login has largely worked.; “You have no books yet” is short and easy to understand.; The “+ Create a new book” button is prominent and clearly named.; The page has an uncluttered layout with plenty of space.

### Create your book – characters  (step 5)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_05.jpg)
- **Purpose:** Collect the names and basic descriptions of the child who will be the story's hero and another person who should appear.
- **What's happening:** The form is empty except for 'Grandparent' as the selected relationship. I am being asked to identify Oliver as the child, choose his age and pronouns, describe his appearance, and name another character.
- **First impression (Margaret):** "The heading and labels are clear, and the form is not asking for anything unnecessary. I can see exactly what I need to enter, although the footer links and copyright line are very pale."
- **Cognitive walkthrough:** Q1 Yes, I would complete these details now because this is exactly the information needed to put Oliver and Grandma Maggie in the story. / Q2 Yes, the matching text boxes and drop-down lists are directly beneath clear labels, and the 'Next' button is prominent. / Q3 Yes. 'Child's first name', 'Age', 'Pronouns' and 'Who else is in the story?' plainly describe what I want to provide.
  - [ACC sev 2] **Footer text has very low contrast** - evidence: The footer links 'Privacy', 'Terms' and 'Contact', together with '© 2026 StoryHearth Ltd.', are extremely pale grey on an off-white background.. Fix: Use a much darker footer text colour with strong contrast and keep the font size at least 16 pixels.
  - [H2 sev 1] **Relationship is preselected without an explanation** - evidence: [11] shows 'Grandparent' already selected, although no relationship has yet been entered.. Fix: Start with a neutral 'Choose relationship' option, or add a brief note that the preselected value should be checked.
- **Positives:** The heading 'Who's the star of the story?' immediately explains the purpose of the form in friendly language.; All fields have clear visible labels, and optional information is plainly marked as optional.; The descriptions can be entered without uploading a photograph, which is reassuring.; The orange 'Next' button is large and easy to see.

### Story details form  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** Collect the setting, important object, and family memory needed to create the personalised book.
- **What's happening:** The form is waiting for three pieces of information: where the story happens, what special object is involved, and the memory or idea behind the story.
- **First impression (Margaret):** "This is a calm, uncluttered form, and the questions are phrased in ordinary language. I can see where to type everything, although the footer links are very pale."
- **Cognitive walkthrough:** Q1 Yes, I would enter the information now because the three questions clearly lead me to describe the memory. / Q2 Yes, I noticed the three text boxes and the “Next” button immediately. / Q3 Yes. “Where does the story happen?”, “A special object”, and “Tell us the memory or idea behind your story” match what I want to explain.
  - [ACC sev 2] **Footer links are very low contrast** - evidence: “Privacy”, “Terms”, and “Contact” in the footer are very pale grey. Fix: Use darker, high-contrast footer text while keeping the page background unchanged.
- **Positives:** The form has a clear progression from character details to story details.; The field labels are plain and specific rather than technical.; Back and Next controls are both clearly visible.

### Choose the look & feel  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Choose the reading difficulty and illustration style for the personalised book.
- **What's happening:** The form offers four Lexile reading ranges and three illustration styles. “Lexile 200L–500L” and “Watercolour — soft and dreamy” are currently selected, with Back and Next buttons below.
- **First impression (Margaret):** "The page looks calm and uncluttered, and the illustration descriptions are helpful. However, I cannot tell from “Lexile BR–200L” what it means in ordinary terms or why this is the best choice for a five-year-old."
- **Cognitive walkthrough:** Q1 Yes. I want the book to suit Oliver's reading age, so I am willing to choose a reading level. / Q2 Yes. The reading-level radio buttons are clearly visible beneath “Reading level.” / Q3 Not quite. The control is called “Reading level,” but its choices use unexplained Lexile ranges rather than saying which range is intended for a child aged five.
  - [H2 sev 2] **Lexile ranges are unexplained** - evidence: The page labels the choices “Lexile BR–200L,” “Lexile 200L–500L,” “Lexile 500L–800L,” and “Lexile 800L+.”. Fix: Add a plain-English explanation, such as “Easiest—suitable for children beginning to read,” and show the recommended reading range by age.
  - [H5 sev 2] **The default reading level may be too advanced for Oliver** - evidence: “Lexile 200L–500L” is already checked, even though Oliver is five and the requested reading age is five.. Fix: Default to the easiest range when the child's age is five, and ask for confirmation with a sentence such as “This is the recommended level for a child aged five.”
- **Positives:** The illustration-style descriptions are warm, clear, and easy to compare.; The page is uncluttered and the radio buttons have large, easy-to-click areas.; There is a clear Back button, so I know I have not lost my earlier answers.

### Optional photo upload  (step 8)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_08.jpg)
- **Purpose:** Offer an optional child photograph that may make the generated illustrations resemble Oliver, then allow the user to create the book.
- **What's happening:** The page explains the possible purpose of a photo upload, states that the upload is optional, and provides controls to go back or create the book. No file has been selected.
- **First impression (Margaret):** "The page looks straightforward and reassuring. I notice that the photo is optional, and I am comfortable continuing without one because I have not been given permission from Oliver's parent to upload his picture."
- **Cognitive walkthrough:** Q1 Yes, I would try creating the book without a photograph. / Q2 Yes, the green “Create my book” button is prominent, and the file chooser is also visible. / Q3 Yes. “Create my book” plainly indicates that the book will be generated, while the heading clearly marks the photo as optional.
  - [TRUST sev 2] **No plain-language explanation of how an uploaded photo is handled** - evidence: “Upload a clear photo of your child's face so the illustrations look like them.” No nearby text explains whether the original photo is kept, whether faces are copied, or who can see it.. Fix: Add a short link or note stating whether photos are used only to create the illustrations, whether the original upload is deleted, and where the privacy explanation can be read.
  - [ACC sev 1] **File control has no explicit visible label** - evidence: [30] file-upload (no label), although the browser button reads “Choose File” and the heading says “Add a photo (optional).”. Fix: Give the file field an explicit accessible label such as “Choose an optional photo of Oliver.”
- **Positives:** The heading clearly says “(optional),” so I know I can continue without a photo.; The page plainly explains that the photo may help the illustrations resemble the child.; The Back and Create my book buttons are large, clear, and comfortably separated.; Creating the digital book does not ask for payment details on this screen.

### Generating book  (step 9)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_09.jpg)
- **Purpose:** To process the story details and generate the personalised digital book.
- **What's happening:** The page has changed from the optional-photo screen to a loading state with a circular spinner. The navigation and footer remain visible, but no book title, progress, waiting time, or generation message is shown.
- **First impression (Margaret):** "I can see that the site is doing something, but I am not sure whether it is creating the book, saving my answers, or having a problem. The lack of words beside the spinner makes me unnecessarily worried."
- **Cognitive walkthrough:** Q1 Yes, I would wait for a short while, but I would become anxious if there were no explanation or progress for long. / Q2 There is no control to inspect or cancel the process; only the spinner is visible. / Q3 There is no label at all explaining that Oliver’s book is being generated.
  - [H1 sev 2] **The loading state has no explanatory text** - evidence: The page shows only a circular loading indicator and no message such as “Creating Oliver’s book.”. Fix: Add a clear status message: “Creating Oliver’s book. This may take a moment.” Include the book title and, if available, a progress indicator.
  - [H3 sev 2] **No way to cancel or leave the loading process** - evidence: There is no “Cancel,” “Back,” or “Continue later” control on the loading page.. Fix: Provide a clearly labelled “Cancel” or “Continue later” action, with an explanation of whether the entered story details will be saved.
  - [ACC sev 2] **Very pale footer text** - evidence: The footer items “Privacy,” “Terms,” “Contact,” and “© 2026 StoryHearth Ltd.” are extremely faint against the background.. Fix: Use darker, higher-contrast footer text and provide more spacing or a minimum readable text size.
- **Positives:** The navigation still shows that I am logged in and can return to “My books.”; The loading animation gives some indication that the site has not simply stopped responding.

### Generated storybook preview  (step 10)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_10.jpg)
- **Purpose:** To show the generated digital book so I can read it before considering a printed copy.
- **What's happening:** The first page of a nine-page preview is displayed. It contains the cover image and a next-page control, with an option below to regenerate the entire book for $4.99 and a link to order a hardcover.
- **First impression (Margaret):** "I can see the book at last, and the cover is readable, but the misspelling “Adventrue” makes it feel careless. The Pop-art comic style also does not match the soft watercolour style I chose, and the illustration looks too simple and generic for a family keepsake."
- **Cognitive walkthrough:** Q1 Yes, I would try reading it because I want to judge the complete book, but I am already wary about the spelling and the mismatch with my chosen style. / Q2 Yes, the right-pointing “›” control is visible and appears to be the way to turn the page. I also notice the “1 / 9” page count. / Q3 The arrow control is understandable, but “›” is only a symbol and has no visible wording explaining that it goes to the next page. I understand the preview’s purpose, although the style mismatch makes me distrust the result.
  - [CONTENT sev 3] **The title contains a spelling error** - evidence: The heading says “The Magical Adventrue of Oliver” and the cover repeats “The Magical Adventrue of Oliver.”. Fix: Correct the title to “The Magical Adventure of Oliver” and review all generated titles for spelling before showing the preview.
  - [H2 sev 3] **The selected illustration style was not followed** - evidence: The earlier choice was “soft watercolour,” but the generated page says “Illustration style: Pop-art comic” and the cover has a flat, simple cartoon style.. Fix: Apply the selected “soft watercolour” style consistently, or clearly explain that the chosen style is unavailable and ask me to choose again.
  - [CONTENT sev 2] **The generated cover omits important personal details** - evidence: The cover shows “Oliver,” a farmhouse, and a blue kite, but not his brown curly hair, freckles, green wellies, Grandma Maggie, or the kite’s connection to Grandpa’s shirt.. Fix: Use the supplied character descriptions on the cover and throughout the illustrations, or explain which details are intentionally left out.
  - [ACC sev 1] **The next-page control is not described** - evidence: The only visible page navigation is a small button labelled “›,” with “1 / 9” shown below the book.. Fix: Give the button an accessible label such as “Next page” and make the control large enough to click comfortably.
- **Positives:** The preview clearly identifies the book as nine pages.; The cover image is large enough to inspect.; The page count and forward navigation make it easy to continue through the whole book.; The free digital preview does not require me to enter payment details.

### Hardcover checkout  (step 12)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_12.jpg)
- **Purpose:** To show the price of printing the generated story as a hardcover and collect delivery and payment details for an order.
- **What's happening:** The page shows a timed reservation message, the named hardcover and its price, a pre-selected premium gift-wrap option, shipping and handling, and the full total. It then requests an address and card details before payment.
- **First impression (Margaret):** "The costs are visible, which is helpful, but the pre-checked £7.99 gift wrap feels like an attempt to add something I did not ask for. The £12.99 delivery charge also makes the £24.99 book considerably more expensive than its advertised base price."
- **Cognitive walkthrough:** Q1 I would try to verify the cost and conditions, but I would not proceed with an order here. / Q2 Yes, the premium gift-wrap checkbox is easy to notice because it is visibly checked immediately above its £7.99 charge. / Q3 The labels clearly describe the charge, but I did not choose gift wrap, so the default does not match my intention.
  - [DECEPTIVE sev 3] **Premium gift wrap is selected by default** - evidence: [6] “Premium gift wrap” is checked, with “£7.99” added to the total.. Fix: Make every paid add-on unchecked by default, place its full price beside the option, and recalculate the total immediately when it is changed.
  - [VALUE sev 2] **The cost rises sharply through shipping and the added option** - evidence: “Hardcover: The Magical Adventure of Oliver £24.99,” followed by “Premium gift wrap £7.99,” “Shipping & handling £12.99,” and “Total £45.97.”. Fix: State “£37.98 delivered without gift wrap” prominently and provide a plain-language explanation of the delivery charge.
  - [DECEPTIVE sev 2] **Timed reservation may create unnecessary pressure** - evidence: “Your price is reserved for 09:57.”. Fix: Remove the countdown, or explain plainly whether leaving the page changes the price and how long the price is genuinely held.
  - [TRUST sev 2] **Payment security and delivery terms are not visible before entering details** - evidence: The visible checkout shows card fields, while “Privacy” and “Terms” are below the fold; no payment-security statement is shown near the fields.. Fix: Place a brief reassurance and links to the full terms, returns policy, and privacy notice beside the payment section, with a plain summary of charges and cancellation rights.
  - [H2 sev 2] **Sparse address field may be unsuitable for UK delivery** - evidence: [7] is a single textbox labelled only “Address,” even though the service is described as UK-delivered.. Fix: Use clearly labelled UK address fields for address line 1, optional line 2, town or city, county, and postcode.
- **Positives:** The base hardcover price, delivery charge, optional charge, and total are all visible before payment.; The book title and format are clearly named.; The checkout does not obscure that payment is a separate final action.
- **Would abandon here:** I would not continue because the paid gift-wrap option was selected without my consent, the total is considerably higher than the base book price, and I do not need to provide payment details merely to establish the cost.

## Generated output assessment
*Artifact:* Nine-page generated children's story preview with cover, dedication, illustrations, and hardcover-order controls

> I can see that the website noticed the blue kite, Wales, and the old farmhouse, but it has not preserved the family story I wanted to give Oliver. The wrong name, broken dedication, adult-level vocabulary, invented uncle, frightening forest, pronoun error, and unfinished ending would be spotted immediately by a child. This is not a book I would be willing to hand to Oliver or keep as a family record.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 2 | The book correctly retains Oliver, age 5, Wales, the windy hill, the old farmhouse, and the blue kite made from Grandpa's old shirt. However, “Grandma Maggie” appears zero times; Oliver's appearance and green wellies are |
| coherence | 1 | There are abrupt invented events, a repeated opening, a pronoun change from Oliver to “she,” an unexplained journey into the woods, and the unfinished final sentence “he would always remember”. |
| age fit | 1 | The analysis reports grade level 8.0 for a requested reading age of 5, and the sentence “The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with ex |
| language | 1 | There are numerous failures: “Adventrue,” “Olive,” unresolved “{{recipient_name}}” and “{{sender_name}}” placeholders, incorrect capitalisation of “The,” “she followed him,” repeated opening material, and an incomplete f |
| text image fit | 2 | Some broad settings match, such as the evening sky and moonlit trees, but page 5 shows bright sunshine instead of pouring rain, page 6 shows Oliver standing rather than skipping home, page 7 shows him smiling rather than |
| character consistency | 2 | Oliver is broadly recognisable across the simple illustrations, but he never has the specified brown curly hair, freckles, or green wellies. The generic bald design does not match the supplied child description or any pr |
| visual quality | 2 | The graphics are clean enough to avoid obvious anatomical artefacts, but they are very simple, reuse the same daytime hill image several times, label characters inside the artwork, and do not follow the expected soft wat |
| emotional resonance | 1 | The central relationship with Grandma Maggie never appears, the kite is reduced to a repeated prop, and the invented danger takes the story away from the real family memory. The unfinished ending cannot serve as a meanin |

- **used correctly:** Oliver's first name; Oliver's age of 5; The general hill setting; The old farmhouse; Wales; The blue kite; The detail that the kite was made from Grandpa's old blue shirt
- **missing:** Grandma Maggie as a character; The relationship between Oliver and Grandma Maggie; Oliver's brown curly hair; Oliver's freckles; Oliver's green wellies; The intended shared kite-flying memory with Oliver as the hero; The family story being passed between Oliver and his grandmother
- **changed:** The original memory of Maggie's father making the kite was not presented as Maggie's memory.; The requested uplifting kite story became a dark adventure involving rain, a lantern, woods, threatening shadows, and a red balloon.; Oliver's stated pronouns were changed from he/him to “she” on one page.; The kite is described as being tightly held and later disappears rather than being successfully flown.
- **invented:** Uncle Bartholomew; A winding path leading to danger; A deep, threatening wood; Shadows that grew teeth and whispered; A shiny red balloon; The claim that Oliver might never be found

### Part by part
#### Cover
![I1](artifacts/capture_01/img_00.jpg)
> A StoryHearth original Illustration style: Pop-art comic 1 / 9
- *Picture:* A simple, flat-colour illustration shows a small house on a green hill, a smiling child labelled Oliver, a blue kite, a bright sun, and a pale blue sky. The title printed above the picture reads “The Magical Adventrue of Oliver.”
- *Reaction:* I notice the misspelling “Adventrue” immediately. The picture is pleasant enough, but it looks like a generic template, and Oliver has neither the brown curly hair and freckles nor the green wellies I supplied.
  - [language, sev 3] The title says “The Magical Adventrue of Oliver”; “Adventrue” is not a word.
  - [character_consistency, sev 3] The illustrated Oliver is bald, has no freckles, and wears dark trousers rather than green wellies.
  - [visual_quality, sev 2] The metadata explicitly says “Illustration style: Pop-art comic,” whereas the soft watercolour look I expected was not used.
  - [emotional_resonance, sev 2] The generic house, child, sun, and kite do not suggest my particular Welsh family memory.
- **Change I'd make:** Retitle the book “Oliver and the Blue Kite,” use the requested soft watercolour style, and redraw Oliver with brown curls, freckles, and green wellies on the windy Welsh hill.
- **Suggested rewrite:** Oliver and the Blue Kite A StoryHearth story for Oliver

#### Dedication
![I2](artifacts/capture_03/view_00.jpg)
> For {{recipient_name}}, with love from {{sender_name}} 2 / 9
- *Picture:* This is a screenshot of the StoryHearth preview rather than a finished story illustration. Inside a large white preview box, the unresolved dedication is shown above page controls. Below it are “Regenerate entire book – $4.99” and “Order hardcover”; no total hardcover price is visible in this capture.
- *Reaction:* Those bracket-like names are not personal at all; the website has failed to fill in Oliver and Grandma Maggie. Before ordering, I would also want the actual hardcover price and delivery information stated clearly.
  - [language, sev 4] The page visibly contains “For {{recipient_name}}, with love from {{sender_name}}” rather than completed names.
  - [fidelity, sev 3] The supplied names Oliver and Grandma Maggie do not appear in the dedication.
  - [visual_quality, sev 2] The preview page shows an empty white story panel and website controls rather than the finished dedication artwork.
- **Change I'd make:** Replace the unresolved variables, render the dedication as a proper illustrated page, and show the complete hardcover price and any delivery charge before an order button.
- **Suggested rewrite:** For Oliver, with love from Grandma Maggie

#### Page 1
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in The windy hill behind the old farmhouse in Wales, there lived a curious child named Oliver. Oliver was 5 years old and loved nothing more than The blue kite made from Grandpa's old blue shirt. 3 / 9
- *Picture:* The same basic daytime hill scene used on the cover appears again: house, Oliver, and blue kite beneath a bright sun. Oliver does not have the supplied curls, freckles, or green wellies.
- *Reaction:* This includes several correct details, but the grammar is stiff and the capital “The” treats the kite and location like names. More importantly, Maggie is missing from the scene that should connect us.
  - [fidelity, sev 3] The page includes Oliver, his age, Wales, the hill, farmhouse, and blue kite, but “Grandma Maggie” never appears anywhere in the book.
  - [language, sev 2] “in The windy hill” and “nothing more than The blue kite” contain unnatural capital letters.
  - [character_consistency, sev 3] The picture does not show Oliver's brown curly hair, freckles, or green wellies.
  - [text_image_fit, sev 2] The image shows Oliver standing still, rather than showing the special kite and the old farmhouse as memorable parts of a family outing.
- **Change I'd make:** Use simple story language, name the hill naturally, and put Oliver and Grandma Maggie together flying the kite.
- **Suggested rewrite:** On a windy hill behind the old farmhouse in Wales, Oliver stood with Grandma Maggie. They held a blue kite. It was made from Grandpa's old blue shirt. “Are you ready?” asked Grandma Maggie.

#### Page 2
![I4](artifacts/capture_05/img_00.jpg)
> One evening Oliver gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation. 4 / 9
- *Picture:* Oliver stands on the hill at twilight under a purple-pink sky with a few simple stars. The house remains behind him.
- *Reaction:* This is not language for a five-year-old. I would stop here and ask an adult to explain several of these long words, which defeats the purpose of reading to Oliver himself.
  - [age_fit, sev 4] The sentence uses “ephemeral luminescence,” “crepuscular firmament,” “juxtaposing,” and “existential trepidation”; the readability analysis also gives an average grade level of 8.0 for a requested reading age of 5.
  - [emotional_resonance, sev 3] The abstract melancholy has no connection to flying a handmade kite with his grandmother.
  - [text_image_fit, sev 1] The image supports Oliver looking at an evening sky, but it cannot depict the abstract meanings of the sentence.
- **Change I'd make:** Replace the sentence with one or two short, concrete sentences about the wind lifting the blue kite.
- **Suggested rewrite:** The wind caught the kite and lifted it high. Oliver looked up and laughed.

#### Page 3
![I5](artifacts/capture_06/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Olive pulled up his hood and ran for shelter, holding The blue kite made from Grandpa's old blue shirt tight. 5 / 9
- *Picture:* The illustration shows the same bright sun, dry-looking green hill, house, Oliver, and blue kite. There is no rain, puddle, hood, or running movement.
- *Reaction:* “Olive” is another version of my grandson's name, and a child would notice that at once. The picture makes it look sunny while the story says pouring rain.
  - [language, sev 4] Oliver is suddenly called “Olive,” and “The blue kite” is again capitalised incorrectly.
  - [text_image_fit, sev 3] The text describes pouring rain, puddles, a hood, and running, but the picture shows a bright sun and Oliver standing still without a hood.
  - [fidelity, sev 2] The supplied green wellies are not shown, even though Oliver is supposedly running in the rain.
- **Change I'd make:** Keep Oliver's name consistent and either illustrate the rain properly or remove this invented incident. A gusty wind would better support the kite story.
- **Suggested rewrite:** A strong gust pulled the kite down. Oliver held on tightly. His green wellies dug into the wet grass.

#### Page 4
![I6](artifacts/capture_07/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Oliver, follow me!" he called, and she followed him along the winding path. 6 / 9
- *Picture:* At dusk, a tall figure in a blue top stands beside Oliver near the house and holds up a small yellow rectangle resembling a lantern. The figure is labelled “Uncle Bartholomew,” while Oliver stands to the right.
- *Reaction:* Where did Uncle Bartholomew come from? I never supplied him, and the story changes Oliver from “he” to “she” in the next sentence. This is a serious error in a book meant to keep family names straight.
  - [fidelity, sev 4] “Uncle Bartholomew” is invented and has no connection to the supplied family memory.
  - [coherence, sev 4] The supplied pronouns are “he / him,” but the text says “she followed him” after Oliver is directly addressed.
  - [language, sev 3] The standalone heading “Uncle Bartholomew” is followed by a pronoun error and an unexplained change of direction into danger.
  - [emotional_resonance, sev 3] A mysterious lantern-bearing uncle displaces Grandma Maggie from the central family story.
  - [text_image_fit, sev 2] The picture broadly depicts Oliver and the invented uncle, but Oliver is not shown following him or holding the kite as stated in the surrounding story.
- **Change I'd make:** Remove Uncle Bartholomew and continue the memory with Grandma Maggie helping Oliver keep the kite in the wind.
- **Suggested rewrite:** The string began to slip. “Keep holding it tight!” called Grandma Maggie. Oliver wrapped the string around his hand.

#### Page 5
![I7](artifacts/capture_08/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Oliver again. Oliver clutched a shiny red balloon and trembled in the dark. 7 / 9
- *Picture:* Oliver stands smiling beside a red balloon at night, with three simple trees under a crescent moon. The picture does not show teeth, whispering shadows, trembling, or Oliver looking afraid.
- *Reaction:* This is an unpleasant surprise in a bedtime story, especially “the shadows grew teeth” and “no one would ever find Oliver again.” The cheerful smile in the picture makes the threat feel even more careless.
  - [age_fit, sev 3] The threatening images “the shadows grew teeth” and “no one would ever find Oliver again” are unnecessarily frightening for a five-year-old.
  - [fidelity, sev 4] The woods, threatening shadows, and shiny red balloon were all invented without basis in the family memory.
  - [coherence, sev 3] The story moves from the hill and winding path to “Deep in the woods” without explaining how Oliver got there or why the red balloon appeared.
  - [text_image_fit, sev 2] The picture shows Oliver smiling, not trembling, and the shadows and trees have no visible teeth.
- **Change I'd make:** Remove the threatening forest sequence. Return to the kite, show Oliver safely with Grandma Maggie, and illustrate his determined expression rather than fear.
- **Suggested rewrite:** Oliver took two little steps back. Then he ran forward. The kite rose higher than the old apple tree. “I did it!” he shouted.

#### Page 6
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in The windy hill behind the old farmhouse in Wales, there lived a curious child named Oliver. At last the sun came out, and Oliver skipped all the way home, happier than ever. 8 / 9
- *Picture:* Oliver is standing still on the familiar green hill beside the house under a bright sun. No blue kite, movement, path home, or Grandma Maggie is shown.
- *Reaction:* The opening has simply been repeated in the middle, which tells me the story has lost its thread. The picture does not show Oliver skipping, and the blue kite has disappeared.
  - [coherence, sev 4] The sentence beginning “Once upon a time” repeats the opening almost exactly in the penultimate story page, then jumps abruptly to Oliver going home.
  - [text_image_fit, sev 3] The text says Oliver “skipped all the way home,” but the picture shows him standing still on the hill; the kite is also absent.
  - [fidelity, sev 3] The central requested relationship between Oliver and Grandma Maggie is still missing at the apparent resolution.
- **Change I'd make:** Delete the repeated opening and build toward a real ending in which Oliver and Grandma Maggie fly the kite together and connect it to Maggie's own childhood.
- **Suggested rewrite:** Oliver flew the blue kite above the hill while Grandma Maggie cheered. The wind carried it high against the blue sky. “You did it!” she said.

#### Page 7
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Oliver looked up at the sky, he would always remember The End 9 / 9
- *Picture:* An orange sunset or solid orange sky hangs over the familiar hill, house, and standing Oliver. “The End” is printed at the top, while Oliver's name remains below him.
- *Reaction:* The final thought stops in the middle and never says what Oliver would remember. It is not a proper ending for a keepsake, particularly when the whole purpose was to pass on my memory.
  - [language, sev 4] The sentence ends with “he would always remember” without an object or final punctuation, and “The End” is then repeated.
  - [coherence, sev 4] The unfinished final sentence prevents the story from completing its emotional and narrative arc.
  - [fidelity, sev 4] The ending does not mention Grandpa's shirt, Grandma Maggie, or the family memory being passed on.
  - [text_image_fit, sev 3] The orange scene does not show the blue kite, Grandma Maggie, or the requested shared flying moment.
  - [emotional_resonance, sev 4] An incomplete, generic ending is not meaningful enough to become a family keepsake.
- **Change I'd make:** Complete the sentence, connect the present-day kite flight to Maggie's own memory, and show Oliver and Grandma Maggie together with the kite in the final picture.
- **Suggested rewrite:** From then on, whenever Oliver saw a kite, he remembered that day with Grandma Maggie. Grandma remembered the blue kite her own father had made for her. Now the family story had flown on.  The End

**Top changes to the output:** 1. Put Grandma Maggie at the centre of the story and show Oliver flying the kite with her on the Welsh hill. | 2. Correct “Adventrue” to “Adventure,” replace every placeholder, restore Oliver throughout, and complete the final sentence. | 3. Rewrite the story for a reading age of 5 using short sentences and familiar words, with a verified level near BR–200L. | 4. Remove Uncle Bartholomew, the red balloon, and the threatening forest; replace them with a gentle problem-and-solution involving the wind. | 5. Redraw Oliver with brown curly hair, freckles, and green wellies, and use soft watercolour illustrations throughout. | 6. Show the complete hardcover price and delivery cost clearly before any order button.

## Recommendations (participant's priorities)
- **[high] Rewrite the story so Oliver and Grandma Maggie fly the blue kite together on the windy hill behind the farmhouse in Wales.** (Generated storybook preview) - This is the actual family memory and must remain the emotional centre of the keepsake.
- **[high] Use short, familiar sentences suitable for a five-year-old, remove the invented uncle, balloon and threatening forest, and complete the final sentence properly.** (Generated storybook preview) - The current language is too advanced and the story is frightening, incoherent and unfinished for Oliver's age.
- **[high] Correct “Adventrue”, replace unresolved name placeholders, and check spelling, grammar, names and pronouns throughout the book.** (Generated storybook preview) - These errors immediately make the book look careless and would be obvious to a child and parent.
- **[high] Follow the selected soft watercolour style and show Oliver with brown curly hair, freckles and green wellies.** (Choose the look & feel and Generated storybook preview) - The pictures should match my choices and make the book feel personal rather than generic.
- **[high] Show the complete hardcover price, delivery charge, gift-wrap charge and total before the order button, with premium gift wrap unselected by default.** (Hardcover checkout) - I need to know exactly what I am paying for and must not discover surprise charges at the final step.
- **[medium] Replace technical wording such as “multimodal”, “generative narrative engine”, “artefacts” and “corpus” with ordinary explanations.** (StoryHearth home page) - I want to understand the service before deciding whether to trust it with family details.
- **[medium] Explain “Lexile” in plain English and show a reading age or level that is clearly appropriate for a five-year-old.** (Choose the look & feel) - The unexplained abbreviation and apparently advanced default made me uncertain about the suitability of the book.
- **[medium] Give the loading screen a clear message such as “We are creating Oliver's book” and explain how long it may take, with a way to leave safely.** (Generating book) - The unexplained spinner made me anxious and left me unsure whether anything was happening properly.
- **[medium] Provide a plain-language explanation of how an uploaded photograph would be stored and used, and add a clear visible label to the file control.** (Optional photo upload) - I am cautious about sharing pictures of my grandson and need to know why the information is wanted.
- **[medium] Replace the technical profile-sync error with a human explanation and a clear next step.** (My books dashboard) - The error was alarming and made me wonder whether my details had been saved properly.
- **[low] Increase the contrast and size of footer text and use proper visible labels for the email and password fields.** (Log in and footer areas) - The pale, tiny text and absent labels were difficult to read and made the service less accessible.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This website is for making personalised storybooks in which a child or family member becomes the hero. It seems intended for parents and grandparents who want to turn a family memory into a keepsake.
- **What was the most frustrating or confusing moment, and why?** The most frustrating moment was seeing the finished story: it had “Adventrue” misspelt, adult and difficult language, an invented uncle and threatening forest, missing details about Grandma Maggie, and an unfinished final sentence. The checkout was also unsettling because premium gift wrap had been selected and the total rose to £45.97.
- **What was the best moment?** The best moment was entering the real family memory. The form allowed me to describe Oliver, the blue kite, the windy Welsh hill, and Grandma Maggie, and it felt calm and reassuring at that point.
- **Was there any point where, in real life, you would have given up? Where and why?** I would probably have stopped at the checkout rather than pay, because the shipping and gift-wrap charges were unexpected and the full cost was not clear enough beforehand. I would also have been seriously discouraged if the incorrect story could not be corrected before purchase.
- **What did you expect to find or be able to do that wasn't there?** I expected the book to show Oliver flying the kite with Grandma Maggie on the Welsh hill, in the soft watercolour style I selected. I also expected a clearly explained reading level, a meaningful loading message, a complete ending, an explanation of how photographs are used, and the full delivery price before any order button.
- **Did you trust this website with your information (and your family's)? Why or why not?** I was willing to share basic details because the form appeared to be for creating Oliver's story, but I would not have uploaded a photograph of him without a plain explanation of how it would be stored and used. The unexplained technical error and unexpected checkout charges made me cautious about trusting the site with my information or money.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would only pay for a finished book that faithfully retold the memory and looked genuinely suitable for a five-year-old. The £24.99 hardcover price would feel reasonable if delivery were clear and reasonable, but I would not accept an unexpected total of £45.97. I might pay more for carefully checked language, attractive watercolour illustrations, and a proper hardcover, provided the additional cost was explained before I committed.
- **If the site produced something for you, how do you feel about it overall?** The output was disappointing and not keepsake-worthy. Although it kept some broad details such as Wales, the farmhouse, and the blue kite, it lost the relationship with Grandma Maggie, ignored Oliver's appearance, added unpleasant invented events, and contained obvious spelling and language errors. I would not hand this book to Oliver.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | This sounds very relevant to me, and I can see that I would not need to pay for a digital preview. However, that first description is full of words I do not understand—“multimodal,” “generative narrative engine,” “artefa | read_page |
| 2 | StoryHearth – Personalised storybooks st | curious (1) | I understand the broad idea now, but the opening wording is still much more technical than it needs to be. I am going to log in first, using the account details I have been given, and then I can see what information the  | click |
| 3 | Log in – StoryHearth | reassured (1) | This is simple and I can see exactly where to type my email and password. I am a little concerned that the boxes themselves have no proper labels, although the placeholders do make sense. I will enter the account details | type; type; click |
| 4 | My books – StoryHearth | confused (-1) | I can see that I am logged in because the page has changed to “My books” and includes a “Log out” link. However, “Error 0x80070057: profile sync incomplete” is alarming and quite technical, and I wonder whether my detail | click |
| 5 | Create your book – StoryHearth | reassured (1) | This form is straightforward and uses ordinary words, which I appreciate. I can enter Oliver's details and include Grandma Maggie as the other character. The pale footer text is rather difficult to read, but it does not  | type; select; select; type; type; click |
| 6 | Create your book – StoryHearth | reassured (2) | The form is easy to understand. I can give the setting, the blue kite, and explain the family memory while making Oliver the hero and including Grandma Maggie. | type; type; type; click |
| 7 | Create your book – StoryHearth | confused (0) | The choices are clear enough, but “Lexile” is an abbreviation I do not know, and the ranges are not particularly meaningful to me. Since this is for Oliver, who is five and is just learning to read, I will choose “Lexile | click; click |
| 8 | Create your book – StoryHearth | reassured (2) | This is very simple and calm, and I appreciate that it says “optional.” I would rather not upload a photograph of Oliver without first understanding how it will be stored and used, and I do not need one to make the story | click |
| 9 | Create your book – StoryHearth | anxious (-1) | The spinner tells me that something is happening, but it does not tell me that my book is actually being created or how long this may take. I am willing to wait for a little while, but a plain message such as “We’re crea | wait_for_change |
| 10 | Your storybook – StoryHearth | annoyed (-1) | The book has appeared, which is good, but I immediately notice two disappointments. “Adventrue” is misspelled, and the style is called “Pop-art comic” rather than the soft watercolour style I chose. The picture is simple | flip_through |
| 11 | Your storybook – StoryHearth | frustrated (-1) | I have now looked at every page, and the final page is visible. The website has shown that the preview has reached its end, although the closing sentence feels unfinished: “he would always remember” does not say what he  | click |
| 12 | Checkout – StoryHearth | suspicious (-1) | At last, I can see the full cost, but I am not pleased that premium gift wrap has been selected for me. The base hardcover is £24.99, but shipping is unexpectedly high and gift wrap takes it to £45.97. I will not enter p | done |
