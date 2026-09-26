# UserQA report: Harold Brooks on http://127.0.0.1:8765/

*Persona:* **Harold Brooks** (78) - Retired carpenter with macular degeneration who browses at 200% zoom.  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 15 steps | *Pages reviewed:* 9 | *Issues:* 36 | *LLM calls:* 18 | *Wall time:* 340.5 s

## What the agent understood the website to be
- **what it is:** A website that makes personalised, illustrated digital storybooks starring family members and can print them as hardcovers.
- **who it is for:** Families wanting to preserve a child’s or relative’s memory as a storybook.
- **value proposition:** Turn family memories and details about loved ones into a personalised storybook preview, with UK-printed hardcovers available.
- **pricing model:** The page says the digital preview is free and hardcovers are printed and shipped across the UK, but it gives no price here.
- **fit for me:** It sounds very suitable for making a book for Lily about Conker, provided the wording, text, controls, and final book are clear enough for me to use independently.
- **main tasks:** Log in, Add a child and another person as characters, Enter a family memory, Generate and read the storybook, Check hardback printing prices

## Scores
- SUS: **32.5** (grade F; 68 = industry average)
- UEQ-S: pragmatic -1.0, hedonic 0.5 (range -3..+3)
- Likelihood to recommend (0-10): 2
- Output keepsake-worthiness (1-5): 1
- Verdict: *"The workshop door was easy to find, but the book came out like the wrong piece of furniture, so I would not use it for Lily."*

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 3 | ACC | Hardcover checkout, My books dashboard, Reading level and illustration style, Optional photo upload (x4) | Legal and contact links are unreadable | Links [12], [13], and [14] are marked “faint/small text you cannot make out”; the footer also includes unreadable text. | Use normal-sized, high-contrast text for these links and display visible labels rather than tiny faint writing. |
| 3 | ACC | StoryHearth home page | Main description is too pale for my eyes | “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.” | Use plain English with at least 16px dark text on a light background, for example: “Turn your family’s happy memories into a personalised illustrated storybook.” |
| 3 | H9 | My books dashboard | Unexplained technical error after login | “Error 0x80070057: profile sync incomplete.” | Replace the code with a plain-English message such as “Some account details have not loaded. Your book has not been lost. Try again,” and provide a clearly labelled “Try again” button if action is nee |
| 3 | H3 | Create your book — story characters | Back does not explain whether the later story answers were kept | After clicking “Back” on the story-details page, the site returned to “Who's the star of the story?” without any message about the entered story details. | Keep all form entries, and when returning from a later step, show a clear message such as “Your story details have been kept. You are back on step 1 of 2.” |
| 3 | H5 | Story details | The memory box silently keeps only 200 characters | Textbox [18] shows 200 characters ending with “carved Conker from wood in his workshop shed, wor…”. | Show a clear character limit and counter, warn while I type, and provide a way to continue into another paragraph or expand the limit. |
| 3 | H5 | Storybook preview | Chosen illustration style was not followed | I selected “Watercolour — soft and dreamy,” but the preview says “Illustration style: Pop-art comic.” | Use the selected Watercolour style, or clearly warn me before generation and offer labelled choices to keep or change it. |
| 3 | ACC | Storybook preview | Page controls are small and symbol-only | [6] button "‹" and [7] button "›"; the controls are described as tiny and hard to hit at 200% zoom. | Use large buttons labelled “Previous page” and “Next page,” including page numbers such as “Go to page 2 of 9.” |
| 3 | ACC | Storybook preview | Page navigation buttons are very small | [6] and [7] are tiny arrow buttons, with [7] labelled only “›” | Make the previous and next controls large, high-contrast buttons with visible text such as “Previous page” and “Next page”. |
| 3 | CONTENT | Storybook preview | The final sentence is incomplete | “And from that day on, whenever Lily looked up at the sky, she would always remember” | Complete the sentence with a clear, child-friendly ending that connects back to Conker, the Christmas gift, or her gallop across the Norfolk fields. |
| 3 | DECEPTIVE | Hardcover checkout | Gift wrap is selected without being requested | Control [6] says “Premium gift wrap” and is checked; it adds “£7.99” to the £45.97 total. | Make optional extras unchecked by default and show the base hardcover, delivery, optional extras, and total separately with plain wording. |
| 2 | ACC | StoryHearth home page, Log in, Create your book — story characters, Storybook preview (x4) | Footer links and copyright text are too faint and small | “Privacy”; “Terms”; “Contact”; “© 2026 StoryHearth Ltd.” | Use dark, adequately sized text and visible focus states for these links. |
| 2 | CONTENT | Storybook preview (x2) | The title contains a spelling mistake | “The Magical Adventrue of Lily” | Correct the title to “Adventure” and provide a clearly labelled “Edit title” control before ordering. |
| 2 | CONTENT | StoryHearth home page | The main introductory language is needlessly technical | “multimodal generative narrative engine” and “lived-experience corpus” | Replace technical wording with familiar language and explain only the essentials. |
| 2 | ACC | StoryHearth home page | The main image has no description | [image (no description) 577x440] | Provide meaningful alternative text, or hide the image from assistive technology if it is purely decorative. |
| 2 | H2 | StoryHearth home page | The primary call to action does not say what happens next | [5] link “Proceed →” | Label it “Create your storybook” or “Start a free storybook preview” and say whether login comes next. |

## Page-by-page
### StoryHearth home page  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Introduce the personalised family-storybook service and offer ways to log in, begin, or inspect pricing.
- **What's happening:** The home page displays the main offer, calls to proceed and see pricing, a three-step explanation, customer quotations, and question links below the fold.
- **First impression (Harold):** "The main promise and big buttons are easy to see, and the subject is right up my alley. However, the pale supporting sentence is hard to read and far too technical."
- **Cognitive walkthrough:** Q1 Yes, I would try logging in to begin my account. / Q2 Yes, the large black “Log in” button is immediately noticeable at the top right. / Q3 Yes. “Log in” plainly says what will happen, unlike the vague “Proceed” wording.
  - [ACC sev 3] **Main description is too pale for my eyes** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Use plain English with at least 16px dark text on a light background, for example: “Turn your family’s happy memories into a personalised illustrated storybook.”
  - [CONTENT sev 2] **The main introductory language is needlessly technical** - evidence: “multimodal generative narrative engine” and “lived-experience corpus”. Fix: Replace technical wording with familiar language and explain only the essentials.
  - [ACC sev 2] **The main image has no description** - evidence: [image (no description) 577x440]. Fix: Provide meaningful alternative text, or hide the image from assistive technology if it is purely decorative.
  - [ACC sev 2] **Footer links and copyright text are too faint and small** - evidence: “Privacy”; “Terms”; “Contact”; “© 2026 StoryHearth Ltd.”. Fix: Use dark, adequately sized text and visible focus states for these links.
  - [H2 sev 2] **The primary call to action does not say what happens next** - evidence: [5] link “Proceed →”. Fix: Label it “Create your storybook” or “Start a free storybook preview” and say whether login comes next.
- **Positives:** The large black “Log in” button has a clear text label and is visually prominent.; The heading “Your family's stories, bound for generations.” is large, dark, and easy to read.; The plain-English heading “How it works” promises three understandable steps.; The page clearly says “Free digital preview,” so I know I can inspect a book before considering a printed copy.; The customer quotations are supportive and relevant to keeping family stories alive.

### Log in  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** Sign in to an existing StoryHearth account.
- **What's happening:** The page presents email and password entry fields, a login button, an account-creation link, and small footer information.
- **First impression (Harold):** "The main form is large, clear, and easy to recognise. I can make out the fields and button without hunting around."
- **Cognitive walkthrough:** Q1 Yes, this is the next step I intended to take. / Q2 Yes, the email and password boxes and the “Log in” button are prominent. / Q3 Yes. “Log in” and the placeholders “Email” and “Password” match what I want to do.
  - [ACC sev 2] **Email and password fields have placeholders but no permanent labels** - evidence: [5] textbox (no label) placeholder “Email”; [6] textbox (no label) placeholder “Password”. Fix: Add permanent, high-contrast labels reading “Email address” and “Password” above the fields, with matching accessible names.
  - [ACC sev 2] **Footer information is too faint and small to read** - evidence: The links to Privacy, Terms, Contact, and “© 2026 StoryHearth Ltd.” are described as faint and small.. Fix: Use dark, high-contrast text at a readable size, and do not rely on very small footer print.
- **Positives:** The “Welcome back” heading clearly identifies the page.; The email and password fields are large and visually distinct.; The “Log in” button has a plain-language label and a large click area.; The login page loaded quickly and clearly follows my last action.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** Show the books in the signed-in account and let the user begin creating a new book.
- **What's happening:** The account dashboard says there are no books and offers a “Create a new book” link. However, an error banner reports that profile synchronisation is incomplete.
- **First impression (Harold):** "The big button and simple message are easy to follow, but the technical error code at the top spoils my confidence and makes me wonder whether my account is faulty."
- **Cognitive walkthrough:** Q1 Yes, because I have come here specifically to make Lily’s book. / Q2 Yes, the large orange “+ Create a new book” button is prominent. / Q3 Yes. “Create a new book” plainly describes starting the book I want.
  - [H9 sev 3] **Unexplained technical error after login** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the code with a plain-English message such as “Some account details have not loaded. Your book has not been lost. Try again,” and provide a clearly labelled “Try again” button if action is needed.
  - [H2 sev 2] **Error code is technical and unexplained** - evidence: “Error 0x80070057”. Fix: Put the code in small support details rather than the main message, and lead with a human explanation of what happened and whether my work is safe.
  - [ACC sev 2] **Faint secondary text** - evidence: “You have no books yet.” is pale grey. Fix: Use a dark, high-contrast text colour rather than pale grey.
  - [ACC sev 2] **Footer text is too faint to read** - evidence: The footer links [7], [8], and [9] are described as faint/small and I cannot make them out.. Fix: Use darker text, a larger font, and clearly worded labels for Privacy, Terms, and Contact.
- **Positives:** The dashboard clearly says that there are no books yet.; The “Create a new book” control is large, plainly labelled, and visually prominent.; There is a visible “Log out” control.

### Create your book — story characters  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Collect details about the child who will be the story’s main character and another person who should appear in it.
- **What's happening:** The form has empty name, age, and pronouns controls at the top, followed by appearance and other-character fields below. The relationship is already set to “Grandparent,” and the form is ready for the family’s details before the “Next” button is used.
- **First impression (Harold):** "The large labels and boxes are encouraging, and I know what to put in them. However, I can only see part of the form at once and the footer words are too faint to read."
- **Cognitive walkthrough:** Q1 Yes. This is plainly where I enter Lily’s details before continuing. / Q2 Yes. “Child’s first name,” “Age,” and “Pronouns” are clearly visible, and the lower controls can be reached by scrolling. / Q3 Yes. The labels use plain language and match the information I need about Lily and Grandpa Harold.
  - [H3 sev 3] **Back does not explain whether the later story answers were kept** - evidence: After clicking “Back” on the story-details page, the site returned to “Who's the star of the story?” without any message about the entered story details.. Fix: Keep all form entries, and when returning from a later step, show a clear message such as “Your story details have been kept. You are back on step 1 of 2.”
  - [ACC sev 2] **Important form fields are hidden below the fold at high zoom** - evidence: “What do they look like? (optional),” “Who else is in the story?,” and the “Next” button are all marked “offscreen.”. Fix: Use a single-column form that reflows well at 200% zoom, keep large spacing between controls, and provide a clear progress indicator showing how many sections remain.
  - [ACC sev 2] **Footer text is too faint to read** - evidence: The Privacy, Terms, Contact, and copyright text is described as faint and unreadable.. Fix: Use dark, high-contrast text for footer links and copyright information, with a minimum readable font size of 14px before browser scaling.
- **Positives:** The form begins with the plain-language question, “Who’s the star of the story?”; Field labels clearly identify the information being requested.; The visible input boxes and dropdowns are large and have strong borders.; Age and pronouns are not hidden behind complicated wording.

### Story details  (step 5)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_05.jpg)
- **Purpose:** Collect the setting, important object, and family memory needed to write the personalised story.
- **What's happening:** The page presents three empty fields for the story setting, a special object, and the memory behind the story. Back and Next controls are below the visible area.
- **First impression (Harold):** "The bold questions are straightforward, like three instruction cards on a workshop wall. I can see where to put each part of the story, although the example writing is too pale for comfortable reading."
- **Cognitive walkthrough:** Q1 Yes, I would fill in these fields now because this is the part where I can describe the real family memory. / Q2 Yes, the three large text boxes are noticeable, and the heading “Your story” tells me this is the next stage. / Q3 Yes. “Where does the story happen?”, “A special object”, and “Tell us the memory or idea behind your story” closely match what I want to say, although “A special object” could be more conversational.
  - [H5 sev 3] **The memory box silently keeps only 200 characters** - evidence: Textbox [18] shows 200 characters ending with “carved Conker from wood in his workshop shed, wor…”.. Fix: Show a clear character limit and counter, warn while I type, and provide a way to continue into another paragraph or expand the limit.
  - [ACC sev 2] **Placeholder text is too faint** - evidence: The examples “e.g. the beach at Grandma's”, “e.g. a yellow bucket”, and “What happened? Why does it matter to your family?” are pale grey inside the boxes.. Fix: Use dark, high-contrast placeholder text that still passes WCAG contrast requirements, while keeping the entered-text contrast high.
  - [H1 sev 1] **No visible confirmation that character details were saved** - evidence: After the previous Next action, the page changed directly to “Your story” without a message saying Lily’s details were saved.. Fix: After moving forward, show a short confirmation such as “Lily and Grandpa Harold added — you can go back to change these details.”
- **Positives:** The field labels are written in plain English.; The boxes are large and clearly separated.; A Back control is available, although I must scroll to reach it.

### Reading level and illustration style  (step 8)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_08.jpg)
- **Purpose:** Choose the intended reading difficulty and visual appearance of the children's storybook.
- **What's happening:** Four reading-level radio buttons are shown, with “Lexile 200L–500L” selected. Below the fold are three illustration styles, with “Watercolour — soft and dreamy” selected, followed by Back and Next.
- **First impression (Harold):** "The choices look neat and the controls are large, but “Lexile” and the L ranges are not plain English. I have to work out which one suits a child aged four."
- **Cognitive walkthrough:** Q1 Yes, I need to choose suitable settings before continuing. / Q2 Yes, the reading-level radio buttons are prominent at the top. / Q3 Only partly. I want the wording to be suitable for a four-year-old, but the choices use “Lexile” and “200L–500L” rather than explaining that the BR–200L choice is for early readers.
  - [H2 sev 2] **Reading levels are labelled in specialist terms** - evidence: The choices are “Lexile BR–200L”, “Lexile 200L–500L”, “Lexile 500L–800L” and “Lexile 800L+”.. Fix: Give each option a plain description, such as “Early reading (ages 4–7)” and “Independent readers (ages 8–12)”, while keeping the Lexile range as secondary information.
  - [ACC sev 2] **Footer text is too faint to read** - evidence: “Privacy”, “Terms” and “Contact” are described as faint small text that I cannot make out.. Fix: Use dark, high-contrast text at a readable size and make the footer links large enough to select.
- **Positives:** The page has a clear heading.; The selected radio button is visibly marked.; The reading-level options are large and labelled in full.; Back and Next controls are available.

### Optional photo upload  (step 10)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_10.jpg)
- **Purpose:** Offer an optional child photo before generating the personalised storybook.
- **What's happening:** The page offers a file upload for a clear photo of the child's face, with no file chosen. It also provides buttons to go back or create the book.
- **First impression (Harold):** "Straightforward and reassuring. The wording tells me the photo is optional, so I know I can safely continue without one."
- **Cognitive walkthrough:** Q1 Yes, I would try to create the book now because the photo is optional and I do not have a suitable file available. / Q2 Yes, the large green “Create my book” button is very noticeable. / Q3 Yes. “Create my book” plainly says that pressing it will make the book I have been setting up.
  - [ACC sev 2] **Photo upload lacks a proper visible field label** - evidence: [30] file-upload (no label); the screen only shows the native control “Choose file” and “No file chosen”.. Fix: Associate the upload control with a large visible label such as “Photo of Lily (optional)” and keep the full-size “Choose photo” target labelled with words.
  - [ACC sev 2] **Footer text is faint and too small to read** - evidence: [13] link [faint/small text you cannot make out]; [14] link [faint/small text you cannot make out]; [15] link [faint/small text you cannot make out]. Fix: Use dark, high-contrast text at a readable size and enlarge the footer link targets.
- **Positives:** The heading and explanation are large and straightforward.; The word “(optional)” makes it clear that skipping the photo is allowed.; The “Create my book” button is large, high-contrast, and clearly labelled.; A clearly labelled “Back” button is available.

### Storybook preview  (step 11)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_11.jpg)
- **Purpose:** Display the newly generated personal storybook so I can read and check every page before considering a printed copy.
- **What's happening:** A generated 9-page preview is open at page 1 of 9. The cover is titled “The Magical Adventrue of Lily,” and the page lists “Illustration style: Pop-art comic.” There are previous and next controls, a $4.99 whole-book regeneration control, and an option to order a hardcover.
- **First impression (Harold):** "The book has appeared, which is good, but the misspelling and sudden change from Watercolour to Pop-art comic make me mistrust the result. The cover drawing is also rather bare and plain for a special present."
- **Cognitive walkthrough:** Q1 Yes, I need to read all nine pages carefully to see whether Lily, Grandpa Harold, and Conker are properly included. / Q2 The tiny right-arrow next control is present but currently below the visible area, and the page shows 1 / 9 so I know there is more to inspect. / Q3 The overall purpose is clear from “Preview · 9 pages,” but the icon-only arrows do not clearly say “Next page” and “Previous page.”
  - [H5 sev 3] **Chosen illustration style was not followed** - evidence: I selected “Watercolour — soft and dreamy,” but the preview says “Illustration style: Pop-art comic.”. Fix: Use the selected Watercolour style, or clearly warn me before generation and offer labelled choices to keep or change it.
  - [ACC sev 3] **Page controls are small and symbol-only** - evidence: [6] button "‹" and [7] button "›"; the controls are described as tiny and hard to hit at 200% zoom.. Fix: Use large buttons labelled “Previous page” and “Next page,” including page numbers such as “Go to page 2 of 9.”
  - [ACC sev 3] **Page navigation buttons are very small** - evidence: [6] and [7] are tiny arrow buttons, with [7] labelled only “›”. Fix: Make the previous and next controls large, high-contrast buttons with visible text such as “Previous page” and “Next page”.
  - [CONTENT sev 3] **The final sentence is incomplete** - evidence: “And from that day on, whenever Lily looked up at the sky, she would always remember”. Fix: Complete the sentence with a clear, child-friendly ending that connects back to Conker, the Christmas gift, or her gallop across the Norfolk fields.
  - [CONTENT sev 2] **The title contains a spelling mistake** - evidence: “The Magical Adventrue of Lily”. Fix: Correct the title to “Adventure” and provide a clearly labelled “Edit title” control before ordering.
  - [VALUE sev 2] **Paid regeneration is prominent without explaining the effect** - evidence: [8] “Regenerate entire book – $4.99”. Fix: Explain what regeneration changes, show the price plainly, require confirmation, and offer a free way to edit or retry the style.
  - [CONTENT sev 2] **Generated book title contains a spelling error** - evidence: “The Magical Adventrue of Lily”. Fix: Check the title before presenting it, or allow the title to be edited before ordering.
  - [H2 sev 1] **Page content appears below the cover image rather than as a clear page-reading area** - evidence: The page lists “The Magical Adventrue of Lily,” “A StoryHearth original,” and the style after the cover image.. Fix: Separate the page image from clearly labelled preview details, and place the page counter and navigation directly beside the book.
  - [ACC sev 1] **Footer text has insufficient visibility** - evidence: The “Privacy,” “Terms,” and “Contact” links are described as faint and too small to read.. Fix: Use dark, high-contrast text at a readable size and enlarge the footer link targets.
- **Positives:** The page clearly states that a preview with 9 pages has been created.; The book title is large and readable.; The current page position is shown as 1 / 9.; There is an obvious “Order hardcover” link for the next stage without forcing an immediate purchase.

### Hardcover checkout  (step 14)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_14.jpg)
- **Purpose:** Show the price of ordering the generated story as a printed hardcover and collect delivery and payment details.
- **What's happening:** The page prices one hardcover at £24.99, lists shipping and handling at £12.99, and displays a total of £45.97 because £7.99 premium gift wrap is pre-selected. A countdown says the price is reserved for 09:57, and blank address and card fields appear below.
- **First impression (Harold):** "The main price is plainly visible, which is helpful, but my eye went straight to the already-ticked gift-wrap box. I would stop there to remove an extra I never chose."
- **Cognitive walkthrough:** Q1 Yes, because my purpose is to find out what the hardcover really costs. / Q2 Yes, the checked “Premium gift wrap” control and its £7.99 charge are visible. / Q3 The hardcover and shipping lines match what I wanted to inspect, but the pre-selected gift wrap does not.
  - [DECEPTIVE sev 3] **Gift wrap is selected without being requested** - evidence: Control [6] says “Premium gift wrap” and is checked; it adds “£7.99” to the £45.97 total.. Fix: Make optional extras unchecked by default and show the base hardcover, delivery, optional extras, and total separately with plain wording.
  - [ACC sev 3] **Legal and contact links are unreadable** - evidence: Links [12], [13], and [14] are marked “faint/small text you cannot make out”; the footer also includes unreadable text.. Fix: Use normal-sized, high-contrast text for these links and display visible labels rather than tiny faint writing.
  - [VALUE sev 2] **The core delivery cost is not summarised clearly** - evidence: The page shows “Hardcover” £24.99 and “Shipping & handling” £12.99, but the prominently displayed “Total” is £45.97 because of the selected extra.. Fix: Display “Hardcover with UK delivery: £37.98” and separately identify any optional extras.
  - [H1 sev 2] **Checkout timer creates needless pressure** - evidence: “Your price is reserved for 09:57” is shown in prominent red text.. Fix: Give a reasonable extended reservation without a countdown, or explain plainly when the price might change.
  - [DECEPTIVE sev 2] **The price-reservation timer may create unnecessary urgency** - evidence: “Your price is reserved for 09:35”. Fix: Explain plainly what the timer does and give ample time, or remove it unless the reservation genuinely requires one.
  - [H3 sev 2] **There is no clear way to leave checkout without losing my place** - evidence: The visible checkout controls are “Premium gift wrap,” the address and payment fields, and the links at the bottom; no “Cancel,” “Back,” or “Save and finish later” control is visible.. Fix: Add clearly labelled “Back to book,” “Cancel,” and “Save and finish later” controls.
- **Positives:** The hardcover name and £24.99 price are shown near the top.; Shipping and handling are listed as a separate £12.99 charge rather than being hidden.; The page uses readable headings and reasonably large prices.; No payment details have been entered and the “Pay now” button is separate from the price summary.

## Generated output assessment
*Artifact:* Nine-page personalized hardcover children's story preview and checkout page

> I have looked through every page, and I am disappointed. The site has remembered a few names, but it has lost the heart of the story: my shed, my careful work, Christmas, Lily, and Conker riding across Norfolk. The spelling mistakes, placeholders, frightening scenes, wrong pictures, unfinished ending, and Watercolour style not followed would stop me from buying this.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | The output uses Lily, Harold's shed, Norfolk, and Conker, but it never shows Harold carving or giving Conker at Christmas, never shows Lily's strawberry-blonde bob or pink wellies, and omits the central imaginary gallop. |
| coherence | 1 | The opening sentence is repeated on Page 6; Page 4 says Lily follows Uncle Bartholomew and then “he followed him”; the journey into the woods is unexplained; and Page 7 stops after “remember.” |
| age fit | 1 | The measured grade level is 8.1 despite a requested age of four. Page 2 contains “ephemeral luminescence,” “crepuscular firmament,” and “existential trepidation,” while Page 5 describes shadows that “grew teeth” and thre |
| language | 1 | There are multiple serious errors: “Adventrue,” “Lil,” unresolved “{{recipient_name}}” and “{{sender_name}},” duplicated story opening and “The End,” an unfinished final sentence, and the faulty phrase “he followed him.” |
| text image fit | 1 | Conker is absent from every story illustration despite being the central object. I5 shows bright sunshine instead of pouring rain, and the woods on I7 do not have toothed shadows. Most pages reuse nearly the same shed, c |
| character consistency | 1 | The same simplified child is reused, but she does not match Lily's strawberry-blonde bob or pink wellies. Harold never appears with his white hair, flat cap, or carpenter's apron, and an invented bald Uncle Bartholomew r |
| visual quality | 2 | The images are clean enough to avoid obvious anatomical artefacts, but they are extremely simple, repetitive, and not in the requested Watercolour style. The cover title and checkout both contain the major misspelling “A |
| emotional resonance | 1 | The book does not communicate Harold's love, pride, craftsmanship, Christmas gift, or family memory. Its generic repeated pictures, threatening wood scene, placeholders, and unfinished ending make it unsuitable as a pers |

- **used correctly:** Lily's name and age were used correctly on the opening page.; Lily is treated as the central child.; Harold's workshop shed and the Norfolk fields are named.; Conker is correctly named and called a hand-carved wooden rocking horse.; Premium gift wrap was selected at checkout.
- **missing:** Grandpa Harold as an active character in the story; Harold's white hair, flat cap, and carpenter's apron; Harold carving Conker; The Christmas gift presentation; Lily's strawberry-blonde bob; Lily's pink wellies; Lily's imaginary gallop across the Norfolk fields; The requested Watercolour illustration style; A simple warm reading level suitable for a four-year-old; Properly completed dedication
- **changed:** The warm family memory became a dark fantasy involving an unknown uncle, threatening woods, and a red balloon.; Lily's supplied appearance was changed to a bald, generic figure.; The requested Watercolour look became a stated Pop-art comic style.; The title was changed to “The Magical Adventrue of Lily,” including a misspelling.
- **invented:** Uncle Bartholomew; A lantern and winding path; A deep dark wood; Shadows that grew teeth; A shiny red balloon; Repeated use of nearly identical outdoor scenes

### Part by part
#### Cover
![I1](artifacts/capture_01/img_00.jpg)
> The Magical Adventrue of Lily A StoryHearth original Illustration style: Pop-art comic
- *Picture:* A very simple flat illustration of a small shed, a smiling child labelled Lily, three trees, a grey oval, and a bright sun. There is no rocking horse, Harold, workshop activity, Christmas scene, or Norfolk landscape. The title is printed across the sky.
- *Reaction:* I can read the cover, but “Adventrue” is plainly wrong. I asked for a watercolour look and a story about my rocking horse, yet this looks like a basic pop-art template.
  - [language, sev 3] The title says “The Magical Adventrue of Lily”; “Adventure” is misspelled.
  - [fidelity, sev 4] The promised subject, Conker, and Grandpa Harold are absent from the cover, as are the Christmas gift and Lily riding across the Norfolk fields.
  - [visual_quality, sev 3] The page declares “Illustration style: Pop-art comic” and uses very basic geometric shapes rather than the promised Watercolour style.
  - [character_consistency, sev 3] Lily is shown as a bald, generic child in a green top, not as a four-year-old with a strawberry-blonde bob and pink wellies.
- **Change I'd make:** Correct the title, use the selected Watercolour style, and show Lily with her strawberry-blonde bob and pink wellies receiving or riding Conker, with Harold in his white hair, flat cap, and carpenter's apron.
- **Suggested rewrite:** Lily and Conker A Christmas Story from Grandpa Harold

#### Dedication
![I2](artifacts/capture_04/view_00.jpg)
> For {{recipient_name}}, with love from {{sender_name}}
- *Picture:* The capture shows the lower part of the book viewer rather than a dedicated illustration. A page counter reads 2 / 9, small arrow buttons sit beside it, and large “Regenerate entire book — $4.99” and “Order hardcover” buttons appear below.
- *Reaction:* Those braces mean the names were never filled in. I was asked to be Harold, so I would expect Lily's name and mine to be written clearly rather than left as a workshop fault.
  - [language, sev 4] The page visibly contains unresolved placeholders: “{{recipient_name}}” and “{{sender_name}}”.
  - [fidelity, sev 3] The supplied recipient Lily and sender Harold do not appear in the dedication.
  - [visual_quality, sev 2] The page arrow controls are small, and the captured dedication area is blank rather than a finished illustrated page.
- **Change I'd make:** Replace both template variables with the verified names and make the page controls large and clearly labelled.
- **Suggested rewrite:** For Lily, with love from Grandpa Harold

#### Page 1
![I3](artifacts/capture_05/img_00.jpg)
> Once upon a time, in Harold's workshop shed and the Norfolk fields, there lived a curious child named Lily. Lily was 4 years old and loved nothing more than Conker, the hand-carved wooden rocking horse.
- *Picture:* A generic child stands outdoors between a small shed and three trees under a large sun. The picture is almost the same as the cover and does not show Harold carving Conker, the workshop interior, or a rocking horse.
- *Reaction:* The words mention my shed, Norfolk, Lily, and Conker, so the site has not forgotten everything. The picture, however, gives me no sign of the rocking horse I spent so long carving.
  - [fidelity, sev 4] The story does not show or describe Harold making Conker, the Christmas presentation, or Lily riding him across the fields.
  - [text_image_fit, sev 4] The text says Lily loves “Conker, the hand-carved wooden rocking horse,” but no horse or carving activity appears in I3.
  - [visual_quality, sev 3] The image repeats a generic outdoor template instead of illustrating Harold's workshop and craftsmanship.
  - [character_consistency, sev 3] Lily has no visible strawberry-blonde bob or pink wellies, and Harold is not shown.
- **Change I'd make:** Open the story properly with Harold carving Conker in his shed and give him a Christmas scene in which he presents the finished horse to Lily.
- **Suggested rewrite:** In Grandpa Harold's workshop, the smell of fresh wood filled the shed. Harold, in his flat cap and carpenter's apron, shaped and smoothed Conker, his beautiful wooden rocking horse.  At Christmas, Lily's strawberry-blonde hair bounced as she opened her present. She gave a delighted giggle.  “Thank you, Grandpa Harold. Let's take Conker to the fields!”

#### Page 2
![I4](artifacts/capture_06/img_00.jpg)
> One evening Lily gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* The same generic Lily stands near a shed and trees beneath a purple and pink evening sky with several stars.
- *Reaction:* I have never needed a dictionary to read a bedtime story to a four-year-old. This sentence is far beyond Lily and rather beyond me as well.
  - [age_fit, sev 4] The prose uses “ephemeral luminescence,” “crepuscular firmament,” “engendered,” “ineffable,” and “existential trepidation” for a four-year-old.
  - [language, sev 3] The sentence is grammatically elaborate but far beyond the requested simple, warm language; the measured grade level is 8.1 rather than BR–200L.
  - [fidelity, sev 3] The page introduces a melancholy evening that was not part of the supplied rocking-horse memory and does not advance Conker's story.
  - [text_image_fit, sev 2] The picture shows an evening sky, but it does not visually convey the elaborate sadness, wonder, and anxiety stated in the text.
- **Change I'd make:** Replace the sentence with two or three short lines about Lily seeing the first star and asking Harold to ride Conker under the Norfolk sky.
- **Suggested rewrite:** That evening, the sky turned pink and gold. Lily looked up at the first bright star.  “Can we ride Conker, Grandpa Harold?” she asked.

#### Page 3
![I5](artifacts/capture_07/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Lil pulled up her hood and ran for shelter, holding Conker, the hand-carved wooden rocking horse tight.
- *Picture:* Lily stands in bright sunshine beneath a large sun. The same shed, trees, and grey oval appear, but there is no rain, puddles, hood, running, or Conker.
- *Reaction:* I can see at once that the picture is wrong: it is bright and dry while the words say pouring rain. “Lil” is another mistake, and my rocking horse is again missing.
  - [language, sev 3] Lily's name is misspelled as “Lil,” and the sentence needs a comma after “horse.”
  - [text_image_fit, sev 4] I5 shows a bright sun and no rain, directly contradicting “the rain began to pour” and “Big grey drops splashed into the puddles.”
  - [fidelity, sev 3] Although Conker is named, he is absent from the image, and the rain and hood were not details of the requested memory.
  - [character_consistency, sev 3] Lily has neither her described strawberry-blonde bob nor pink wellies, and the story says she pulled up a hood that is not present.
- **Change I'd make:** Do not add an unrelated storm. Show Lily carrying Conker toward the field, or redraw genuine rain and add Conker to her arms.
- **Suggested rewrite:** Lily carried Conker carefully across the wet grass. She sat on the rocking horse and held on tight.  “Off we go!” she cried. Conker bounced along as if he were galloping over the waves.

#### Page 4
![I6](artifacts/capture_08/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Lily, follow me!" he called, and he followed him along the winding path.
- *Picture:* A tall bald man in a blue top holds a yellow rectangular lantern beside the smaller generic Lily. A shed and trees remain in the background. The image labels the man “Uncle Bartholomew.”
- *Reaction:* I never mentioned an Uncle Bartholomew, and Lily cannot follow him and also follow him. This page reads as though a strange extra character has wandered into our family story.
  - [fidelity, sev 4] The supplied cast was Lily and Grandpa Harold, but the page invents “Uncle Bartholomew” and removes Harold from the scene.
  - [coherence, sev 4] “Lily, follow me!” is followed by “he followed him,” so the subject and direction of action are contradictory.
  - [language, sev 3] The sentence “he followed him” is logically and grammatically wrong in this context.
  - [character_consistency, sev 4] The invented man is shown as a bald generic adult rather than Harold, who was described as white-haired and wearing a flat cap and carpenter's apron.
  - [text_image_fit, sev 2] The lantern and two figures broadly match the text, but the picture does not show a winding path or make their movement clear.
- **Change I'd make:** Remove Uncle Bartholomew and replace the scene with Lily and Grandpa Harold taking Conker from the shed to the field.
- **Suggested rewrite:** Grandpa Harold picked up the lantern. "Come along, Lily," he said. "Conker is ready for his first gallop."  Lily held his hand as they followed the path out of the shed.

#### Page 5
![I7](artifacts/capture_09/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Lily again. Lily clutched a shiny red balloon and trembled in the dark.
- *Picture:* Lily stands under a crescent moon with a red balloon beside three trees. There is no dense wood, no visible toothed shadows, and no clear expression of trembling.
- *Reaction:* “The shadows grew teeth” is too frightening for this gentle family keepsake, especially for a four-year-old. The red balloon has also appeared from nowhere.
  - [age_fit, sev 4] The threatening image of shadows with teeth and the prospect that “no one would ever find Lily again” are unnecessarily frightening for a four-year-old.
  - [fidelity, sev 4] The dark woods, threatening shadows, and red balloon were not supplied and replace the warm Christmas and Norfolk-field memories.
  - [text_image_fit, sev 3] The image has a red balloon, but the woods are sparse and the shadows do not have teeth or appear to whisper.
  - [coherence, sev 3] Lily has apparently entered deep woods without Grandpa Harold after the previous page, but no explanation is given for where he went or why they stopped together.
- **Change I'd make:** Replace the threatening episode with a gentle problem and solution, such as Conker's reins catching on a gate or Lily counting the horses across the fields.
- **Suggested rewrite:** Out in the fields, Conker caught his reins on a gate. Lily gently lifted them free.  “Thank you, Conker,” she said. “We can go home now.”

#### Page 6
![I8](artifacts/capture_10/img_00.jpg)
> Once upon a time, in Harold's workshop shed and the Norfolk fields, there lived a curious child named Lily. At last the sun came out, and Lily skipped all the way home, happier than ever.
- *Picture:* The generic child stands under a large sun between a shed and three trees. Conker is absent, and there is no visible skipping, route home, or field journey.
- *Reaction:* This repeats the opening instead of moving the story forward. Lily is happier, but I cannot see how she got home, and Conker has vanished again.
  - [coherence, sev 4] The exact opening sentence is repeated, while the transition from the frightening woods to sunshine and home has no explanation.
  - [fidelity, sev 4] The page does not show Lily riding Conker across the Norfolk fields, the central event from Harold's memory.
  - [text_image_fit, sev 3] The sun supports “the sun came out,” but Conker, Lily's skipping, and her journey home are not shown.
  - [character_consistency, sev 3] Lily remains the same bald generic figure and still lacks her strawberry-blonde bob, pink wellies, and her described appearance.
- **Change I'd make:** Continue directly from the field adventure and make Lily ride Conker home while describing her happy imaginary gallop.
- **Suggested rewrite:** Lily climbed onto Conker once more. With a whoosh, they galloped all the way home across the sunny fields.  “Best Christmas ever,” Lily said. “Thank you, Grandpa Harold.”

#### Page 7
![I9](artifacts/capture_11/img_00.jpg)
> The End And from that day on, whenever Lily looked up at the sky, she would always remember The End
- *Picture:* A flat orange sunset scene with a shed, generic Lily, three trees, and the large words “The End.” It does not show Lily riding Conker or looking at the sky.
- *Reaction:* The last thought stops dead after “remember,” and “The End” is printed twice. I would not want to pay £45.97 for a keepsake left unfinished like this.
  - [language, sev 4] The sentence ends abruptly at “remember” without a final punctuation mark or completed thought, and “The End” appears twice.
  - [coherence, sev 4] The ending does not resolve the dark-woods episode or the invented Uncle Bartholomew, and it does not mention Conker or Grandpa Harold's gift.
  - [fidelity, sev 3] The promised keepsake thought—Harold remembering making the horse for Lily—is absent.
  - [text_image_fit, sev 3] The text says Lily looks up at the sky, but she stands facing forward and Conker is absent.
  - [visual_quality, sev 3] The image repeats the same basic characters and landscape with a different background colour and does not provide a proper closing illustration.
- **Change I'd make:** Complete the final sentence, show it only once, and close with Lily and Harold together with Conker so the gift has emotional closure.
- **Suggested rewrite:** From then on, whenever Lily rode Conker across the Norfolk fields, she thought of Grandpa Harold and his careful carpentry.  The End

#### Checkout
![I10](artifacts/capture_13/view_00.jpg)
![I11](artifacts/capture_13/view_01.jpg)
![I12](artifacts/capture_13/view_02.jpg)
> Checkout Your price is reserved for 09:40 Hardcover: The Magical Adventrue of Lily	£24.99  Premium gift wrap	£7.99 Shipping & handling	£12.99 Total	£45.97 Delivery Address Payment Card number Expiry CVC Pay now
- *Picture:* A checkout page lists the misspelled title, gift wrap, shipping, an address field, payment fields, and a large orange Pay now button. The captures show only portions of the long form, and the price reservation changes from 09:40 in the extracted text to 09:39 in I10.
- *Reaction:* The layout is reasonably plain, but I would hesitate over a £45.97 purchase of a misspelt, unfinished book. A countdown also makes me feel pushed rather than fully in control.
  - [language, sev 3] The bill repeats “The Magical Adventrue of Lily” with the same title misspelling.
  - [coherence, sev 1] The reservation is shown as “09:40” in the captured text but “09:39” in I10, making the offer appear unstable.
  - [visual_quality, sev 2] The long checkout form requires scrolling, and the footer text is very pale grey with low contrast.
- **Change I'd make:** Correct the title everywhere, extend or remove the reservation pressure, increase footer contrast, and keep the complete price and purchase controls visible without relying on repeated scrolling.

**Top changes to the output:** 1. Rebuild the story around Harold carving Conker, giving it to Lily at Christmas, and taking her on an imaginary gallop across the Norfolk fields. | 2. Correct “Adventrue,” “Lil,” the repeated sentences, the unresolved dedication placeholders, the faulty pronoun wording, and the unfinished final sentence. | 3. Use the requested Watercolour style and create distinct illustrations for the workshop carving, Christmas presentation, and gallop across the fields. | 4. Draw Lily consistently with a strawberry-blonde bob and pink wellies, and draw Harold consistently with white hair, a flat cap, and a carpenter's apron. | 5. Remove Uncle Bartholomew, the red balloon, and the toothed-shadow scene; use simple warm sentences suitable for a four-year-old. | 6. Show Conker clearly on every page where the text mentions him, with no image contradicting the weather, setting, or action.

## Recommendations (participant's priorities)
- **[high] Make the book follow the real memory: Harold carving Conker, giving it to Lily at Christmas, and Lily riding it across the Norfolk fields.** (Storybook preview) - Those details are the whole reason I wanted to make the book.
- **[high] Fix all spelling, grammar, repeated sentences, unfinished sentences, and unresolved name placeholders.** (Storybook preview) - A book with obvious mistakes is not fit to give to a child or keep as a family memory.
- **[high] Use the selected Watercolour style and show Conker, Lily, Harold, the workshop, and the fields accurately in the pictures.** (Storybook preview) - The pictures should match the words and the style I chose, especially for a present.
- **[high] Use simple, warm language suitable for a four-year-old instead of words such as “ephemeral luminescence” and frightening toothed shadows.** (Storybook preview) - Lily is only four, and I want the story to be comforting and easy for her to hear.
- **[high] Make the preview a clear page-reading area with large, labelled Previous and Next buttons.** (Storybook preview) - The little arrow buttons were difficult to use at 200% zoom, and I need to inspect every page myself.
- **[high] Explain clearly when information is saved, and say what Back and Next will do without losing later answers.** (Create your book) - I need to know my words are safe before carrying on.
- **[high] Show the 200-character limit before I reach it and tell me when text has been shortened.** (Create your book — story details) - I do not want the important parts of my memory to disappear without warning.
- **[high] Replace pale text with darker, larger text and make footer and legal text readable.** (All pages) - Pale grey writing is almost invisible to me, and I must be able to read every instruction and detail.
- **[medium] Remove the unexplained technical error and replace it with a plain explanation of what happened and what I should do.** (My books) - An error after login made me wonder whether I had done something wrong.
- **[medium] Explain reading levels in ordinary language and suggest the right level for a four-year-old.** (Create your book — reading level) - “Lexile” is a workshop label I do not understand, and the chosen level was far too advanced.
- **[high] Do not tick gift wrap automatically, and show every charge in one clear summary before payment.** (Checkout) - I do not want an extra £7.99 selected without my asking.
- **[medium] Remove the count-down pressure and provide a clear way to leave checkout without losing my place.** (Checkout) - I need time to read the costs and terms without being hurried.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This website is for making personalised storybooks with family members and special memories. It seems intended for parents, grandparents, and other people wanting a keepsake for a child.
- **What was the most frustrating or confusing moment, and why?** The most frustrating moment was seeing the finished book. It had the wrong title spelling, did not use the Watercolour style I chose, left Conker out of the pictures, and ended with an unfinished sentence. It felt like the workshop had made the wrong box entirely.
- **What was the best moment?** The best moment was choosing the watercolour illustrations and pressing the large button to create the book. That part was clear and the orange button was easy to hit.
- **Was there any point where, in real life, you would have given up? Where and why?** I would not have given up while filling in the form, because the questions were mostly understandable. I would have stopped before paying because the book was not suitable, and I would have been worried about the gift wrap being ticked for me.
- **What did you expect to find or be able to do that wasn't there?** I expected to see Conker, Lily, Harold, the shed, Christmas, and the imaginary gallop across the Norfolk fields. I also expected a clear, large way to read every page and fix the story before ordering.
- **Did you trust this website with your information (and your family's)? Why or why not?** I was cautious about trusting it with family information. I entered the details because I was testing it, but the technical error, wrong pictures, unfinished ending, and pre-ticked gift wrap made me doubt whether it was handling my story properly.
- **If the site produced something for you, how do you feel about it overall?** I was disappointed. The site remembered a few names, but it lost the heart of the story and produced something I would not give to Lily.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | The idea is very relevant—I’d like to make Lily a book about Conker, the rocking horse I carved. But that heading underneath is pale and full of words like “multimodal” and “corpus,” which sounds more like a workshop too | click |
| 2 | Log in – StoryHearth | reassured (1) | This is straightforward enough: the two boxes tell me which one is which, and the button is plain English. I can enter the account details I was given, then log in. | type; type; click |
| 3 | My books – StoryHearth | confused (-1) | Well, the login worked, but that error has caught my eye. “Profile sync incomplete” sounds technical and worrying—have I done something wrong? The large orange button is easy enough to see, so I’ll try making the book. | click |
| 4 | Create your book – StoryHearth | reassured (1) | This form looks straightforward, like filling in the details on a drawing. I can enter Lily first, but at 200% zoom the page is very tall and I’ll have to work my way down carefully rather like climbing a ladder. | type; select; select; type; type; click |
| 5 | Create your book – StoryHearth | reassured (1) | This part makes sense: I can name my workshop and the Norfolk fields, then mention Conker and explain the memory. The examples in the boxes are rather pale, but the bold questions above them are clear enough. I’ll fill t | type; type; type; scroll; click |
| 6 | Create your book – StoryHearth | confused (-1) | Ah, so “Back” put me at the beginning of the form, rather than just taking me one small step along it. Lily’s details are still here, which is good, but I’m wondering whether my Conker story is still safely recorded. I’l | scroll; click |
| 7 | Create your book – StoryHearth | reassured (1) | Good, the first two answers are safe, but that long box is still stopping me at exactly 200 characters. I’ll rewrite the memory more concisely so the gift at Christmas and Lily’s gallop across the fields both fit, then I | type; scroll; click |
| 8 | Create your book – StoryHearth | reassured (1) | Aha, this is choosing how the book should read and look. “Lexile” sounds like a tool-box label I don't know, so for a four-year-old I think “Lexile BR–200L” is the proper starting level. I won't leave it at the middle ch | click; scroll |
| 9 | Create your book – StoryHearth | reassured (2) | The illustration choices are easy to understand. Watercolour is already selected, and it sounds pleasant for Lily’s present, so I’ll leave that choice and move on. The big orange “Next” button is very easy to hit at this | click |
| 10 | Create your book – StoryHearth | reassured (2) | This is the last bit before the workshop starts turning my words into a book. I haven't got a clear photo of Lily to hand, and it says the photo is optional, so I’ll leave it empty and press “Create my book.” | click; wait_for_change |
| 11 | Your storybook – StoryHearth | hesitant (-1) | Well, it has made a book, and nine pages sounds sensible. But “Adventrue” is spelled wrongly, and although I chose Watercolour, the cover says “Pop-art comic.” The picture is very simple, too; I need to inspect every pag | scroll |
| 12 | Your storybook – StoryHearth | hesitant (-1) | I can see the cover and the page controls, but the little arrow buttons are rather fiddly at this zoom. I need to read all nine pages carefully, including the picture and the words, before I decide whether this is suitab | flip_through |
| 13 | Your storybook – StoryHearth | frustrated (-1) | That ending sounds like I’ve come to the gate without a word of what Lily remembered. It needs another cut of the workshop, please. I’ve now looked through all nine pages, so I’ll select “Order hardcover” to see the actu | click |
| 14 | Checkout – StoryHearth | suspicious (-1) | Well, I can see the cost, but somebody has ticked “Premium gift wrap” for me before I asked. I don't want to pay £7.99 for that by accident. I'll untick it, check the new total and the rest of the page for any other char | click; scroll |
| 15 | Checkout – StoryHearth | reassured (1) | That is the price I need: £37.98, made up of the £24.99 hardcover and £12.99 delivery. I’m not going to enter any card details or press “Pay now”; the site has given me enough information for the present. The “Your price | done |
