# UserQA report: Margaret Ellison on http://127.0.0.1:8765/

*Persona:* **Margaret Ellison** (71) - Retired primary-school teacher who wants to pass family stories on to her grandchildren.  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 11 steps | *Pages reviewed:* 10 | *Issues:* 30 | *LLM calls:* 14 | *Wall time:* 266.2 s

## What the agent understood the website to be
- **what it is:** A website that turns family memories into personalised, illustrated digital storybooks and printed hardcovers.
- **who it is for:** Families wanting a child and loved one to become characters in a story based on a real memory.
- **value proposition:** A free illustrated preview, with optional printed hardcovers delivered across the UK.
- **pricing model:** A free digital preview is advertised, while a separate Pricing page and printed hardcovers are available; no exact price is shown here.
- **fit for me:** It sounds well suited to preserving my father's blue-shirt kite story for Oliver, but I want the writing to be simple and personal, and I need clear costs before ordering.
- **main tasks:** Log in, Add a child and another character, Describe a family memory, Generate and read a storybook preview, Check pricing for a printed hardcover

## Scores
- SUS: **30.0** (grade F; 68 = industry average)
- UEQ-S: pragmatic 0.25, hedonic -0.5 (range -3..+3)
- Likelihood to recommend (0-10): 2
- Output keepsake-worthiness (1-5): 1
- Verdict: *"The idea is appealing, but the book was not personal, polished, or trustworthy enough to pay for, and the site needs clearer explanations and a much more faithful story."*

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 3 | H9 | My books dashboard | Unexplained technical error creates doubt after login | “Error 0x80070057: profile sync incomplete.” | Replace the code with a plain-English message, such as “Some account details have not loaded. Your login is safe. Try again,” and provide a “Try again” button. Keep the technical code available only i |
| 3 | H1 | Reading level and illustration style | No confirmation that the complete long memory was saved | The previous result says the story box “now only shows 200 characters; the end of what you typed was cut off” and ended at “with G”. | Tell me how many characters the field accepts, preserve the full entry internally, and state, “Your complete story has been saved,” with the option to review it before continuing. |
| 3 | H1 | Book generation loading screen | Loading state has no explanatory status text | The page shows only a circular spinner in an otherwise empty panel. | Add clear text such as 'Creating Oliver's storybook…' and, if the process has stages, show a calm progress indicator with an estimated time. |
| 3 | CONTENT | Generated storybook preview | Spelling error in the book title | “The Magical Adventrue of Oliver” | Correct the title to “The Magical Adventure of Oliver” before generation and add a spelling check or editing step for generated titles. |
| 3 | CONTENT | Generated storybook preview | The final story sentence is incomplete | “And from that day on, whenever Oliver looked up at the sky, he would always remember” | Complete the sentence with what Oliver remembered, and run a final grammar check before presenting the book. |
| 3 | DECEPTIVE | Hardcover checkout | Gift wrap is selected without my consent | [6] checkbox “Premium gift wrap” (checked) with “£7.99” | Leave the gift-wrap checkbox unchecked by default and state clearly that it is an optional extra. |
| 3 | TRUST | Hardcover checkout | Checkout requests payment and personal details before showing any further useful order information | The page immediately shows empty “Address” and payment fields, including “Card number”, “Expiry”, and “CVC”. | Show the complete order summary, delivery estimate, cancellation or privacy information, and what happens after payment before asking for details. |
| 2 | ACC | Log in form, My books dashboard, Story details, Story details form (x4) | Footer links have very low contrast | The visible footer links “Privacy”, “Terms”, and “Contact” are shown in very faint grey. | Use darker text with sufficient contrast against the background and make the links at least comfortably readable. |
| 2 | CONTENT | StoryHearth home page | The introduction uses unexplained technical language | “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.” | Replace this with: “Turn a treasured family memory into a beautifully illustrated storybook featuring your own family.” |
| 2 | ACC | StoryHearth home page | The main illustration has no accessible description | [image (no description) 430x440] | Provide a useful alternative description such as: “An illustrated open book with a child and adult standing on either side.” |
| 2 | ACC | Log in form | Login fields have no visible labels | [5] textbox (no label) placeholder "Email"; [6] textbox (no label) placeholder "Password" | Add persistent visible labels, such as “Email address” and “Password”, above or beside the fields, and ensure they are programmatically associated with the inputs. |
| 2 | H2 | My books dashboard | The account greeting uses “Demo” rather than the account holder’s name | “Welcome back, Demo” | Use the account holder’s chosen name, such as “Welcome back, Margaret,” and allow it to be changed in account settings. |
| 2 | H2 | Reading level and illustration style | Reading-level choices use unexplained terminology | The choices are labelled “Lexile BR–200L,” “Lexile 200L–500L,” “Lexile 500L–800L,” and “Lexile 800L+,” with no explanation. | Add plain-English help beneath each option, such as “Best for children beginning to read (ages 4–6),” “Early readers (ages 6–8),” and so on, while retaining Lexile information. |
| 2 | H6 | Reading level and illustration style | No selected-age guidance | Oliver's age was entered previously as 5, but this screen only presents Lexile ranges. | Use Oliver's entered age to recommend a level, with a message such as “Recommended for Oliver: beginning reader,” and allow me to change it. |
| 2 | ACC | Optional photo upload | The photo upload has no visible label | [30] file-upload (no label); the control displays only “Choose file” and “No file chosen.” | Add a visible label such as “Photo of Oliver (optional)” and associate it programmatically with the file input. |

## Page-by-page
### StoryHearth home page  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Introduce the personalised family-story service and direct visitors to pricing, account access, or story creation.
- **What's happening:** The landing page presents the service proposition, two main calls to action, a three-step explanation, customer quotations, and footer links. No story has yet been created.
- **First impression (Margaret):** "The warm cream-and-rust appearance is attractive, and the three steps are reassuringly straightforward. The main introductory paragraph sounds like computer jargon rather than a message to an ordinary family, which makes me pause."
- **Cognitive walkthrough:** Q1 Yes, I would try logging in and beginning my story. / Q2 Yes, the dark “Log in” button at the top right is very noticeable. / Q3 Yes, “Log in” clearly describes what I want to do, although “Proceed” is less explicit.
  - [CONTENT sev 2] **The introduction uses unexplained technical language** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Replace this with: “Turn a treasured family memory into a beautifully illustrated storybook featuring your own family.”
  - [ACC sev 2] **The main illustration has no accessible description** - evidence: [image (no description) 430x440]. Fix: Provide a useful alternative description such as: “An illustrated open book with a child and adult standing on either side.”
  - [H2 sev 1] **The primary action does not say what happens next** - evidence: [5] link “Proceed →”. Fix: Rename the link “Create our story” or “Start your storybook” and state that signing in may be required.
- **Positives:** The heading clearly communicates the family-memory purpose.; The three numbered steps make the process easy to understand.; “Free digital preview” gives a useful, reassuring starting point.; The contrast is generally good and the main controls are comfortably sized.; Privacy, Terms, and Contact links are present.

### Log in form  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** To let an existing StoryHearth customer sign in to their account.
- **What's happening:** The page presents an email field, password field, and Log in button, with a link to create an account and links to Privacy, Terms, and Contact.
- **First impression (Margaret):** "The page is calm and uncluttered, and the form is easy to recognise. The main fields are large enough, but the missing visible labels make me rely on the grey placeholder words."
- **Cognitive walkthrough:** Q1 Yes, I would try logging in because I want to create a storybook. / Q2 Yes, the email and password fields and the Log in button are all visible. / Q3 Yes, “Log in” clearly matches what I want to do, and the placeholders indicate what belongs in each field.
  - [ACC sev 2] **Login fields have no visible labels** - evidence: [5] textbox (no label) placeholder "Email"; [6] textbox (no label) placeholder "Password". Fix: Add persistent visible labels, such as “Email address” and “Password”, above or beside the fields, and ensure they are programmatically associated with the inputs.
  - [ACC sev 2] **Footer links have very low contrast** - evidence: The visible footer links “Privacy”, “Terms”, and “Contact” are shown in very faint grey.. Fix: Use darker text with sufficient contrast against the background and make the links at least comfortably readable.
- **Positives:** The form is simple and has a clear “Welcome back” heading.; The Log in button is prominent and easy to find.; The page provides clear links to account creation and related information.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** This is my account area, where I should see books I have created and begin a new book.
- **What's happening:** The page says “Welcome back, Demo,” reports that I have no books, and offers a “+ Create a new book” link. An unexplained profile-sync error appears above this information.
- **First impression (Margaret):** "The main task is obvious and the page looks calm and uncluttered, but that technical error is alarming and gives me no way to understand what is incomplete."
- **Cognitive walkthrough:** Q1 Yes, I would try creating the book because that is clearly what I came here to do. / Q2 Yes, the large orange “+ Create a new book” button is very noticeable. / Q3 Yes, “Create a new book” plainly matches my intention to begin Oliver’s storybook.
  - [H9 sev 3] **Unexplained technical error creates doubt after login** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the code with a plain-English message, such as “Some account details have not loaded. Your login is safe. Try again,” and provide a “Try again” button. Keep the technical code available only in a small support-details section.
  - [H2 sev 2] **The account greeting uses “Demo” rather than the account holder’s name** - evidence: “Welcome back, Demo”. Fix: Use the account holder’s chosen name, such as “Welcome back, Margaret,” and allow it to be changed in account settings.
  - [ACC sev 2] **Footer text has very low contrast** - evidence: The footer links “Privacy,” “Terms,” and “Contact,” and the copyright line, appear extremely pale against the background.. Fix: Use dark, high-contrast text for all footer links and the copyright line, meeting WCAG contrast requirements.
- **Positives:** The page clearly states that I have no books yet.; The “+ Create a new book” control is prominent, clearly labelled, and easy to find.; The dashboard has a simple layout without distracting choices.

### Story details form  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** To collect the main child and the other character for the personalised story.
- **What's happening:** A short form is open for entering the child's name, age, pronouns and appearance, followed by the other character's name and relationship. The relationship is already set to “Grandparent,” and the orange “Next” button should continue to the memory details.
- **First impression (Margaret):** "The form is calm, uncluttered and easy to understand. The labels are clear, and the fields look large enough for me."
- **Cognitive walkthrough:** Q1 Yes, I would complete this form now. / Q2 Yes, the relevant fields and the “Next” button are easy to notice. / Q3 Yes. “Child’s first name,” “Age,” “Pronouns,” and “Who else is in the story?” match what I need; “Relationship” also fits, although the relationship might affect the wording.
  - [ACC sev 1] **Footer text has very low contrast** - evidence: “Privacy  Terms  Contact” and “© 2026 StoryHearth Ltd.” are shown in extremely faint grey.. Fix: Use darker footer text with sufficient contrast and make the links at least 16 pixels.
- **Positives:** The form is divided into two clear groups: the star of the story and the other character.; The field labels are visible rather than relying only on placeholder text.; The large text, generous spacing and uncluttered layout are comfortable.; The appearance field is clearly marked optional.

### Story details  (step 5)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_05.jpg)
- **Purpose:** Collect the setting, important object, and family memory that will inform the personalised storybook.
- **What's happening:** The character-details step has been completed successfully, and the site is now asking for three blank story fields. A Back button allows me to return, while Next should save these details and continue.
- **First impression (Margaret):** "The page looks calm and readable, with generous spacing and three plainly worded questions. The examples help me understand what belongs in each box."
- **Cognitive walkthrough:** Q1 Yes, I would complete these fields now because they ask for exactly the information I want the story to include. / Q2 Yes, the three labelled text boxes are prominent, and I can clearly see the orange “Next” button. / Q3 Yes. “Where does the story happen?”, “A special object”, and “Tell us the memory or idea behind your story” correspond neatly to the windmill hill, the blue kite, and the family memory.
  - [ACC sev 2] **Footer text has very faint contrast** - evidence: “Privacy”, “Terms”, “Contact” and “© 2026 StoryHearth Ltd.” appear in extremely pale grey against the white footer.. Fix: Use darker text and links that meet WCAG contrast requirements.
  - [H5 sev 1] **The essential story fields are not marked required or optional** - evidence: The page presents “Where does the story happen?”, “A special object”, and “Tell us the memory or idea behind your story” without saying whether any can be left blank.. Fix: Mark truly required fields with “(required)” and optional fields with “(optional)”, or place brief guidance beside them.
  - [ACC sev 1] **Footer text is very small** - evidence: The Privacy, Terms and Contact links look smaller than the main form text.. Fix: Use at least 16-pixel text for footer links and company information.
- **Positives:** The three questions use warm, plain language rather than technical wording.; The example prompts help me understand what to write without overcomplicating the task.; The large Next button has strong contrast and a clear label.; The Back button gives me a visible way to correct the previous step.; The uncluttered layout gives the family memory proper attention.

### Reading level and illustration style  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** Choose the intended difficulty of the story and its visual style before generating the book.
- **What's happening:** Four Lexile reading ranges and three illustration styles are offered as radio buttons. The current selections are “Lexile 200L–500L” and “Watercolour — soft and dreamy,” with Back and Next controls below.
- **First impression (Margaret):** "The page is calm, uncluttered, and easy to scan. I am less comfortable choosing the reading level because “Lexile” and the L ranges are unexplained and I do not want to make the wrong choice for Oliver."
- **Cognitive walkthrough:** Q1 Yes, but I would hesitate over the reading level because the ranges are not explained. / Q2 Yes. The reading-level radio buttons and the orange “Next” button are prominent. / Q3 Partly. “Watercolour — soft and dreamy” clearly matches my wish for warm pictures, but “Lexile BR–200L” does not clearly say that it is intended for a child who is beginning to read.
  - [H1 sev 3] **No confirmation that the complete long memory was saved** - evidence: The previous result says the story box “now only shows 200 characters; the end of what you typed was cut off” and ended at “with G”.. Fix: Tell me how many characters the field accepts, preserve the full entry internally, and state, “Your complete story has been saved,” with the option to review it before continuing.
  - [H2 sev 2] **Reading-level choices use unexplained terminology** - evidence: The choices are labelled “Lexile BR–200L,” “Lexile 200L–500L,” “Lexile 500L–800L,” and “Lexile 800L+,” with no explanation.. Fix: Add plain-English help beneath each option, such as “Best for children beginning to read (ages 4–6),” “Early readers (ages 6–8),” and so on, while retaining Lexile information.
  - [H6 sev 2] **No selected-age guidance** - evidence: Oliver's age was entered previously as 5, but this screen only presents Lexile ranges.. Fix: Use Oliver's entered age to recommend a level, with a message such as “Recommended for Oliver: beginning reader,” and allow me to change it.
- **Positives:** The reading-level and illustration choices are clearly separated.; The selected radio buttons are easy to identify.; The illustration descriptions are warm and easy to understand.; “Back” gives me reassurance that I can return to the story details.

### Optional photo upload  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Offer an optional photo that could help the illustrations resemble Oliver, then let the user create the book.
- **What's happening:** The page presents an image upload control, explains that a clear photo may help the illustrations look like the child, and offers “Back” and “Create my book” buttons. No file is selected.
- **First impression (Margaret):** "I like that the photograph is clearly marked optional and that the page itself is simple. I am comfortable proceeding without one, although the privacy consequences of uploading a child's photograph are not explained and the upload control lacks a proper label."
- **Cognitive walkthrough:** Q1 Yes. I would proceed without uploading because the photograph is optional and I do not want to share a picture of Oliver until I understand what happens to it. / Q2 Yes. The “Choose file” control and “No file chosen” indication are visible, as are the two decision buttons. / Q3 Partly. “Create my book” clearly matches what I want, and “Back” gives me a way to revisit my answers, but the file control itself has no descriptive visible label.
  - [ACC sev 2] **The photo upload has no visible label** - evidence: [30] file-upload (no label); the control displays only “Choose file” and “No file chosen.”. Fix: Add a visible label such as “Photo of Oliver (optional)” and associate it programmatically with the file input.
  - [TRUST sev 2] **The privacy handling of a child's photo is not explained before upload** - evidence: “Upload a clear photo of your child's face so the illustrations look like them.” There is no nearby explanation of storage, retention, deletion, sharing, or whether the uploaded photo itself is kept.. Fix: Add a short privacy note beneath the upload control explaining why the photo is used, how long it is retained, whether it is shared, and how to request deletion, with a link to the full privacy policy.
- **Positives:** The heading clearly states “Add a photo (optional),” so I understand that the site will let me continue without one.; The page gives a straightforward reason for using a photo: to help the illustrations resemble the child.; Both “Back” and “Create my book” are large, clearly labelled controls.; The uncluttered layout and good contrast make the step easy to read.

### Book generation loading screen  (step 8)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_08.jpg)
- **Purpose:** To process my completed book details and generate the personalised story.
- **What's happening:** The form has changed to a mostly blank panel containing a circular loading indicator. The page provides no status text, progress information, cancellation control, or explanation of what stage is occurring.
- **First impression (Margaret):** "The spinner tells me that the site is working, but it feels very bare and a little worrying. I cannot tell whether my story is being made properly or whether something has gone wrong."
- **Cognitive walkthrough:** Q1 I would wait, because the spinner suggests the book is being generated, but I would be uncomfortable waiting for an unlimited time without an explanation. / Q2 I notice the loading spinner, but there is no control to cancel, go back, or ask for help. / Q3 There is no label or status message describing the action, so it does not clearly explain what is happening after creating the book.
  - [H1 sev 3] **Loading state has no explanatory status text** - evidence: The page shows only a circular spinner in an otherwise empty panel.. Fix: Add clear text such as 'Creating Oliver's storybook…' and, if the process has stages, show a calm progress indicator with an estimated time.
  - [H3 sev 2] **No way to leave or cancel while waiting** - evidence: Only the StoryHearth, How it works, Pricing, My books, and Log out links are visible; the waiting panel has no Cancel or Back control.. Fix: Provide a clearly labelled 'Cancel' or 'Back to my books' control, and explain that cancelling will not lose the entered story.
  - [CONTENT sev 2] **Generation progress is not explained** - evidence: No text explains whether the site is writing the story, preparing illustrations, or saving the book.. Fix: Use a short, reassuring message such as 'We are writing Oliver's story and preparing the pictures. This may take a minute.'
- **Positives:** The page is visually uncluttered.; The visible loading spinner provides some indication that the system is working.; The main navigation remains available, including 'My books' and 'Log out'.

### Generated storybook preview  (step 9)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_09.jpg)
- **Purpose:** To display the generated nine-page storybook and provide controls for reading it, regenerating it, or ordering a printed copy.
- **What's happening:** The first of nine preview pages is shown. The cover is titled “The Magical Adventrue of Oliver,” and the lower part of the screen contains an offscreen $4.99 regeneration button and an “Order hardcover” link.
- **First impression (Margaret):** "I can see that the book was created, and the large picture is easy to look at, but the title contains an obvious spelling mistake. The cover feels rather plain and does not make the family connection to Grandma Maggie immediately apparent."
- **Cognitive walkthrough:** Q1 Yes, I would begin by pressing the right-facing arrow to read the next page. / Q2 Yes, the right-facing arrow marked “›” is clearly visible beside “1 / 9.” / Q3 The arrow is understandable for moving to the next page, although the controls are labelled only with symbols and have no explanatory text.
  - [CONTENT sev 3] **Spelling error in the book title** - evidence: “The Magical Adventrue of Oliver”. Fix: Correct the title to “The Magical Adventure of Oliver” before generation and add a spelling check or editing step for generated titles.
  - [CONTENT sev 3] **The final story sentence is incomplete** - evidence: “And from that day on, whenever Oliver looked up at the sky, he would always remember”. Fix: Complete the sentence with what Oliver remembered, and run a final grammar check before presenting the book.
  - [CONTENT sev 2] **The cover does not clearly represent the requested family story** - evidence: The cover shows Oliver, a house, a sun, and a kite, but no visible Grandma Maggie or identifiable Welsh hill/farmhouse setting.. Fix: Include both Oliver and Grandma Maggie on the cover and show the old farmhouse and windy hill more recognisably.
  - [VALUE sev 2] **Regeneration price is visible without an explanation** - evidence: “Regenerate entire book – $4.99”. Fix: Explain the consequences and number of credits involved, show the price before the action, and ask for confirmation.
  - [CONTENT sev 2] **The final illustration omits the story's central keepsake and relationship** - evidence: The final picture shows Oliver and a farmhouse, but no blue kite and no Grandma Maggie.. Fix: Ensure the ending reflects the selected story details, particularly the blue kite and the relationship between Oliver and Grandma Maggie.
  - [H2 sev 1] **Preview controls are not described** - evidence: The only visible controls are “‹”, “1 / 9”, and “›”.. Fix: Add visible labels such as “Previous page” and “Next page,” with accessible names for screen readers.
- **Positives:** The page clearly says “Preview · 9 pages,” so I know there is a complete book to read.; The large cover image and generous text size are easy to see.; The next-page control is visible immediately, and the previous-page control is correctly disabled on page one.

### Hardcover checkout  (step 11)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_11.jpg)
- **Purpose:** To show the total cost of ordering the generated story as a hardcover and collect delivery and payment information.
- **What's happening:** The checkout displays the book price and a countdown saying the price is reserved, with gift wrap preselected. Empty address, card number, expiry, and CVC fields are ready for personal and payment information, and the “Pay now” button is below the visible area.
- **First impression (Margaret):** "The prices are clear, but the automatically selected gift wrap makes the total feel inflated and less trustworthy. I also do not want to enter my address or card details merely to find out more about the order."
- **Cognitive walkthrough:** Q1 I would be willing to inspect the price breakdown, but I would not want to complete checkout. / Q2 Yes, the gift-wrap checkbox and the price breakdown are easy to notice, although the gift-wrap checkbox appears above its description. / Q3 The labels “Hardcover”, “Shipping & handling”, and “Total” match what I want to know. “Premium gift wrap” is clear about what the extra is, but not about why it has been selected for me.
  - [DECEPTIVE sev 3] **Gift wrap is selected without my consent** - evidence: [6] checkbox “Premium gift wrap” (checked) with “£7.99”. Fix: Leave the gift-wrap checkbox unchecked by default and state clearly that it is an optional extra.
  - [TRUST sev 3] **Checkout requests payment and personal details before showing any further useful order information** - evidence: The page immediately shows empty “Address” and payment fields, including “Card number”, “Expiry”, and “CVC”.. Fix: Show the complete order summary, delivery estimate, cancellation or privacy information, and what happens after payment before asking for details.
  - [VALUE sev 2] **Optional add-on is not clearly separated from the required cost** - evidence: The page shows “Premium gift wrap” and “£7.99” between the hardcover and shipping rows, while the total is “£45.97”.. Fix: Show “Book £24.99”, “Shipping £12.99”, and “Gift wrap £7.99” as separate optional and required items, with the total before and after the add-on.
  - [DECEPTIVE sev 2] **The reserved-price countdown may be unnecessary pressure** - evidence: [5] “Your price is reserved for 09:57”. Fix: Explain what the reservation means, when it began, and whether the price really changes; avoid urgency language unless there is a genuine expiry.
- **Positives:** The itemised prices and total are visible without entering any details.; The checkout is clearly separated into Delivery and Payment sections.; The book title and hardcover format are shown before payment.

## Generated output assessment
*Artifact:* Generated nine-page children's storybook with checkout page for ordering a hardcover

> I would be pleased that a book was produced, but I would not recognize this as the family story I asked for. The title typo, unfinished ending, incorrect pronoun, frightening invented adventure, and missing Grandma Maggie are too serious to overlook. I would want a corrected preview before considering payment.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 2 | The book uses Oliver, age five, Wales, the old farmhouse, the windy hill, Grandpa, and the blue kite, but omits Grandma Maggie and Oliver's described appearance. It invents Uncle Bartholomew, woods, a red balloon, rain,  |
| coherence | 1 | The story begins on the hill, shifts abruptly into rain, a stranger, a dark wood, and then a repeated opening. The pronoun changes to “she,” and the final sentence ends at “remember.” |
| age fit | 1 | The supplied measurement reports Flesch-Kincaid grade 8.5 for a requested reading age of five. Page 2 contains words such as “ephemeral,” “crepuscular,” “juxtaposing,” “ineffable,” and “existential,” while page 5 is frig |
| language | 1 | There are visible placeholders, the repeated title misspelling “Adventrue,” “Olive” instead of Oliver, incorrect pronouns, capitalization errors, awkward grammar, an unfinished sentence, and duplicate “The End”. |
| text image fit | 2 | The illustrations often repeat a generic hill scene. The rain page shows sunshine, the final page lacks the kite and Grandma Maggie, and several pictures do not show the actions or threatening details described in the te |
| character consistency | 2 | Oliver is generally shown as the same simple round-faced figure, but the image does not match his requested brown curly hair, freckles, or green wellies. Page 4 also shows a different, bald-looking Oliver without the des |
| visual quality | 2 | The clean shapes and bright colors are easy to see, but the illustrations are very sparse and generic, the child does not match the requested appearance, and the title has a visible typo. |
| emotional resonance | 1 | The central family memory of Margaret's father, the old shirt kite, Wales, and Oliver sharing it with Grandma Maggie is mostly lost. The replacement story is generic and includes frightening material. |

- **used correctly:** Oliver's first name and age five; The pronoun information was supplied correctly as he/him, although the generated story does not preserve it; Wales; The hill behind the old farmhouse; The blue kite made by Grandpa from an old blue shirt; The broad idea of Oliver flying a kite on the hill
- **missing:** Grandma Maggie as a character and speaking partner; Oliver's brown curly hair, freckles, and green wellies; The intended happy ending with Oliver and Grandma Maggie watching the kite soar; The sense that the memory belongs to Margaret, Oliver, and Grandma Maggie together
- **changed:** The calm family memory became a dark adventure; The intended hilltop kite-flying story became a sequence involving rain, woods, a lantern, a balloon, and a threat; Oliver's appearance and clothing were omitted
- **invented:** Uncle Bartholomew; The lantern; The dark woods; The red balloon; The threatening shadows; The rain sequence; The unexplained need to find shelter

### Part by part
#### Cover
![I1](artifacts/capture_01/img_00.jpg)
> The Magical Adventrue of Oliver
- *Picture:* Simple pop-art style cover showing a small child on a green hill beside a farmhouse and a blue kite, with a bright sun in the background.
- *Reaction:* The cover is cheerful and easy to look at, but the title misspells “Adventure,” and Oliver is not shown with the brown curly hair, freckles, or green wellies I gave.
  - [language, sev 3] The title reads “The Magical Adventrue of Oliver.”
  - [fidelity, sev 3] The requested description was “Brown curly hair, freckles, and green wellies,” but the cover shows a bald, generic child in dark clothing.
  - [character_consistency, sev 3] The pictured child has no visible brown curly hair, freckles, or green wellies.
- **Change I'd make:** Correct the title and illustrate Oliver with brown curly hair, freckles, and green wellies.
- **Suggested rewrite:** The Blue Kite on the Welsh Hill

#### Title page
![I2](artifacts/capture_03/view_00.jpg)
> For {{recipient_name}}, with love from {{sender_name}}
- *Picture:* The website preview page shows the book title, a mostly empty white book panel with the placeholder dedication, page navigation, and an “Order hardcover” button.
- *Reaction:* This is not acceptable as a finished keepsake because the website has left its internal placeholders visible.
  - [language, sev 4] The dedication still contains “{{recipient_name}}” and “{{sender_name}}”.
  - [fidelity, sev 3] The book does not identify the recipient as Oliver or the sender as Grandma Maggie.
- **Change I'd make:** Replace both placeholders with the intended names and check that no template code can appear in the printed book.
- **Suggested rewrite:** For Oliver, with love from Grandma Maggie

#### Page 1
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in The windy hill behind the old farmhouse in Wales, there lived a curious child named Oliver. Oliver was 5 years old and loved nothing more than The blue kite Grandpa made from an old blue shirt.
- *Picture:* Oliver stands on a green hill near a simple farmhouse and a blue kite under a bright sun.
- *Reaction:* This begins warmly and uses the hill, Wales, Oliver, and the kite, but the capitalization is wrong and the wording is clumsy rather than story-like.
  - [language, sev 2] The text says “in The windy hill” and “than The blue kite”; “The” should not be capitalized in those positions.
  - [coherence, sev 2] The opening is understandable, but “there lived” and “loved nothing more than The blue kite” are stiff constructions.
  - [fidelity, sev 2] The page names Oliver, Wales, the hill, the farmhouse, and Grandpa's blue kite, but omits Grandma Maggie and Oliver's appearance.
- **Change I'd make:** Turn the prompt into natural child-friendly narration and introduce Grandma Maggie and Oliver's appearance.
- **Suggested rewrite:** On a windy hill behind the old farmhouse in Wales, Oliver stood with his green wellies on. His brown curly hair blew about his freckled face. He held the blue kite Grandpa had made from an old blue shirt. “It is ready for the sky!” said Grandma Maggie.

#### Page 2
![I4](artifacts/capture_05/img_00.jpg)
> One evening Oliver gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* Oliver stands on the hill at sunset or twilight, looking toward a purple and pink sky with a few stars.
- *Reaction:* The picture is gentle, but the words are far too difficult for a five-year-old and make the story sound like a formal, gloomy science passage.
  - [age_fit, sev 4] The sentence uses “ephemeral,” “luminescence,” “crepuscular,” “engendered,” “melancholy,” “juxtaposing,” “ineffable,” “existential,” and “trepidation.”
  - [language, sev 3] The prose is grammatically overcomplicated and includes “crepuscular,” which the analysis flags as a possible non-dictionary or typo word.
  - [text_image_fit, sev 2] The twilight image fits looking upward, but it does not communicate the abstract sadness and existential ideas in the text.
- **Change I'd make:** Replace the sentence with short, concrete words about the evening sky and the kite's movement.
- **Suggested rewrite:** The sun began to go down. Oliver looked up at the pink and gold sky. The wind tugged at the blue kite, and it pulled gently against his hands.

#### Page 3
![I5](artifacts/capture_06/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Olive pulled up his hood and ran for shelter, holding The blue kite Grandpa made from an old blue shirt tight.
- *Picture:* The image shows a clear, sunny hill with Oliver and the kite; no rain, puddles, or hood is visible.
- *Reaction:* The rain itself sounds vivid, but Oliver's name is misspelled and the illustration shows sunshine instead of rain.
  - [language, sev 3] Oliver is called “Olive.”
  - [language, sev 2] “Holding The blue kite Grandpa made from an old blue shirt tight” is awkward word order, and “The” is incorrectly capitalized.
  - [text_image_fit, sev 3] The text says rain poured, grey drops splashed, and Oliver pulled up his hood, while the picture has a bright sun and no rain or hood.
  - [fidelity, sev 2] The page changes Oliver's appearance by giving him a hood, and the image does not show the requested green wellies.
- **Change I'd make:** Correct Oliver's name, improve the sentence, and show rain, puddles, his hood, and the kite.
- **Suggested rewrite:** Rain began to patter on the hill. Big drops splashed in the puddles. Oliver pulled up his hood and held the blue kite close while he ran toward the old farmhouse.

#### Page 4
![I6](artifacts/capture_07/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Oliver, follow me!" he called, and she followed him along the winding path.
- *Picture:* A tall dark-haired figure labeled “Uncle Bartholomew” stands beside Oliver on the hill near the farmhouse, holding a small yellow lantern.
- *Reaction:* This page introduces an unexpected stranger and then changes Oliver's pronoun from he to she, which is a serious error.
  - [fidelity, sev 3] Uncle Bartholomew is not in the supplied family story and is not connected to the memory.
  - [language, sev 4] The text says “she followed him” after establishing Oliver with he/him pronouns.
  - [coherence, sev 4] Uncle Bartholomew appears suddenly with no setup or explanation, and the path leads into a dark-woods adventure unrelated to the requested kite memory.
  - [text_image_fit, sev 2] The picture shows Oliver and Bartholomew on the hill, but not the winding path mentioned in the text.
- **Change I'd make:** Remove Bartholomew and the invented adventure, keep Oliver's pronouns consistent, and bring Grandma Maggie into the actual memory.
- **Suggested rewrite:** Grandma Maggie came up the path carrying a basket. “Hold the kite high,” she said. “Let the wind lift it!” Oliver smiled and ran with her to the top of the hill.

#### Page 5
![I7](artifacts/capture_08/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Oliver again. Oliver clutched a shiny red balloon and trembled in the dark.
- *Picture:* Oliver stands at night beside a red balloon, with dark trees, a crescent moon, and a very dark background.
- *Reaction:* The threatening shadows and claim that no one would find Oliver are frightening for a five-year-old, and the red balloon has not been prepared.
  - [age_fit, sev 4] The story says the shadows “grew teeth” and threatened that “no one would ever find Oliver again.”
  - [fidelity, sev 4] A red balloon, dark woods, and a threat are invented and displace the hill, farmhouse, kite, and family memory.
  - [coherence, sev 4] The story abruptly moves from the hill and lantern to a threatening dark wood, without explaining why.
  - [text_image_fit, sev 2] The image shows a red balloon and dark setting, but it does not visibly show teeth, whispering shadows, or Oliver trembling.
- **Change I'd make:** Replace the frightening scene with a safe, playful moment on the Welsh hill involving the kite and Grandma Maggie.
- **Suggested rewrite:** The kite dipped toward the grass. Oliver gave it a gentle pull, and it climbed high again. “I can feel the wind!” he laughed. Grandma Maggie stood beside him and cheered.

#### Page 6
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in The windy hill behind the old farmhouse in Wales, there lived a curious child named Oliver. At last the sun came out, and Oliver skipped all the way home, happier than ever.
- *Picture:* Oliver stands on the sunny hill beside the farmhouse, with no kite or Grandma Maggie visible.
- *Reaction:* The sun returns, but the page repeats the opening almost word for word and gives no proper conclusion to the kite story.
  - [coherence, sev 4] The page repeats “Once upon a time...” and then jumps to the sun coming out without resolving the dark-woods plot.
  - [fidelity, sev 4] The requested ending—Oliver and Grandma Maggie watching the kite soar above the Welsh hill—is absent.
  - [text_image_fit, sev 2] The text says Oliver skipped home, but the image simply shows him standing still on the hill, without visible movement or a homeward journey.
  - [language, sev 1] “in The windy hill” repeats the capitalization error.
- **Change I'd make:** Replace the repeated opening with a complete, satisfying ending that shows the kite flying and includes Grandma Maggie.
- **Suggested rewrite:** The sun came out, and the wind lifted the blue kite high above the Welsh hill. Oliver looked up with Grandma Maggie beside him. “It flew all the way from Grandad's old shirt,” Oliver said. “Now it is our special kite too.”

#### Page 7
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Oliver looked up at the sky, he would always remember The End
- *Picture:* An orange sunset background with Oliver standing on the hill beside the farmhouse, and the words “The End” at the top.
- *Reaction:* The final page is especially disappointing: the sentence is unfinished, “The End” is repeated, and the important family moment is missing.
  - [language, sev 4] The final sentence ends abruptly at “remember” with no object or punctuation.
  - [language, sev 3] “The End” appears twice on the same page.
  - [fidelity, sev 4] The requested final image of Oliver and Grandma Maggie watching the kite soar above the hill is not present in either the text or the picture.
  - [emotional_resonance, sev 4] The ending gives no sense that the memory has been handed from Margaret to Oliver.
  - [text_image_fit, sev 3] The picture shows Oliver and the farmhouse, but not the kite, Grandma Maggie, or the skyward ending described by the text.
- **Change I'd make:** Complete the sentence, remove the duplicate ending, and show Oliver and Grandma Maggie together beneath the flying blue kite.
- **Suggested rewrite:** The End From that day on, whenever Oliver looked up at the sky, he remembered the windy Welsh hill and the blue kite Grandad had made. He knew that this special story belonged to him and Grandma Maggie too.

#### Checkout
![I10](artifacts/capture_12/view_00.jpg)
![I11](artifacts/capture_12/view_01.jpg)
> Checkout Your price is reserved for 09:44 Hardcover: The Magical Adventrue of Oliver	£24.99  Premium gift wrap	£7.99 Shipping & handling	£12.99 Total	£45.97 Delivery Address Payment Card number Expiry CVC Pay now
- *Picture:* A checkout form showing a countdown, the hardcover price, a selected premium gift-wrap charge, shipping charge, total, address field, card fields, and a large Pay now button.
- *Reaction:* The total is clear, but the selected £7.99 gift wrap and £12.99 shipping raise the price to £45.97, and the title still contains the spelling mistake.
  - [language, sev 3] The checkout repeats the misspelled title “The Magical Adventrue of Oliver.”
  - [fidelity, sev 3] No correction is offered before purchase, despite the visible error on the cover and checkout.
  - [emotional_resonance, sev 3] The order summary presents a premium hardcover purchase before the unfinished story has been repaired.
- **Change I'd make:** Correct the title, require an explicit choice before adding gift wrap, explain shipping, and show the delivery date and returns information before payment.
- **Suggested rewrite:** Hardcover: The Blue Kite on the Welsh Hill — £24.99 Shipping: shown before checkout Gift wrap: optional, not selected by default Total: clearly recalculated after every choice

**Top changes to the output:** 1. Repair the entire story before checkout: complete the ending, remove the duplicate “The End,” fix “Adventrue,” replace “Olive,” and correct every pronoun and placeholder. | 2. Rewrite the plot around the actual memory: Oliver, Grandma Maggie, the Welsh hill, the old farmhouse, and the blue kite made from Grandpa's old blue shirt. | 3. Use short, warm sentences and ordinary five-year-old vocabulary; remove the frightening dark-woods material and the advanced words on page 2. | 4. Create matching illustrations of Oliver with brown curly hair, freckles, and green wellies, and include Grandma Maggie in the final scene beneath the flying kite. | 5. At checkout, make gift wrap optional rather than preselected, explain shipping and delivery clearly, and do not accept payment until the corrected preview has been reviewed.

## Recommendations (participant's priorities)
- **[high] Rewrite the story around the actual memory, with Oliver and Grandma Maggie flying the blue kite made from Grandpa's old blue shirt on the windy Welsh hill.** (Your storybook – preview) - This is the central purpose of the book, and the current plot has lost the family connection that made me want to make it.
- **[high] Repair the text before checkout: correct “Adventrue,” replace “Olive” with “Oliver,” fix the pronoun errors, remove placeholders, complete the final sentence, and remove the duplicate “The End.”** (Your storybook – preview) - These errors make the book look careless and prevent me from trusting that it is suitable for my grandson or worth paying for.
- **[high] Use short, warm sentences and ordinary vocabulary for a five-year-old, removing words such as “ephemeral,” “crepuscular,” and “juxtaposing,” as well as frightening dark-woods material.** (Your storybook – preview) - The reading level was far too advanced for Oliver, and the frightening material was not what I intended to pass on to him.
- **[high] Redesign the illustrations to show Oliver with brown curly hair, freckles, and green wellies, with Grandma Maggie, the blue kite, the hill, and the farmhouse appearing naturally in the story.** (Your storybook – preview) - The pictures should make the book personal and reassure me that the website has understood the people and memory I entered.
- **[high] Make gift wrap unselected by default, show the total price and delivery cost separately, and explain postage, delivery time, returns, and optional extras before requesting payment or a full address.** (Checkout) - I need to understand precisely what I am paying for and must not be pressured into buying something I did not choose.
- **[high] Show a clear confirmation that the complete memory was saved, explain what happens after pressing the main button, and provide an option to cancel or leave while the book is being prepared.** (Story details and book generation) - I was unsure whether my details had been accepted, and the silent spinner made me anxious about a keepsake involving my family.
- **[high] Replace technical terms such as “Lexile” with a simple explanation and give a recommended choice for a five-year-old.** (Reading level and illustration style) - I do not know what the ranges mean, and guessing made me worry that I had chosen the wrong setting.
- **[medium] Add proper visible labels to the login and photo-upload fields, mark story fields as required or optional, and improve the contrast and size of small footer text.** (Log in and story details) - Clear labels and larger, higher-contrast text would help me understand the forms without having to guess or strain to read them.
- **[medium] Explain how Oliver's photograph would be used, retained, protected, and deleted, and make clear that it is genuinely optional.** (Optional photo upload) - A child's photograph is personal information, and I would only share it if I understood the reason and safeguards.
- **[medium] Replace unexplained error codes such as “0x80070057” with a plain-English explanation and a clear next step, and address the user by the correct account name.** (My books) - A technical code gives me no idea whether my account or information is safe, and “Demo” makes the service feel impersonal.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This is a website for making personalised storybooks in which a child and a loved one can be the stars. It could be especially useful for grandparents who want to turn a real family memory into something a child can keep.
- **What was the most frustrating or confusing moment, and why?** The checkout was the most frustrating moment because gift wrap was selected without my permission, the extra cost was not clearly separated, and the site asked for payment and personal details before giving me enough useful information. I do not like being asked for those details when the consequences are unclear.
- **What was the best moment?** The best moment was entering the family memory and seeing that I could make Oliver the hero with Grandma Maggie beside him. The story-entry pages were calm and reasonably easy to follow, and I felt reassured that uploading a photograph was optional.
- **Was there any point where, in real life, you would have given up? Where and why?** I would probably have stopped at the checkout until the price, delivery information, and optional extras were explained properly. If I had reached checkout and found a surprise charge, I would have left without paying; if the website had damaged the story or asked for payment before I approved it, I would have given up altogether.
- **What did you expect to find or be able to do that wasn't there?** I expected to be able to review a faithful, polished story with Oliver, Grandma Maggie, the blue kite, Grandpa, and the Welsh hill before paying. I also expected to know exactly what would happen after pressing the main button, what the reading-level choices meant, and how any photograph of a child would be stored and used.
- **Did you trust this website with your information (and your family's)? Why or why not?** I was willing to share information when the purpose was clear, but I did not upload Oliver's photograph because the website did not explain the privacy arrangements. The unexplained error message after login also made me wonder whether my details were safe, and the technical wording made me distrustful without giving me any reassurance.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would pay for a genuinely personalised, well-written hardcover book, but not for the version I saw. A fair price would be around £15 to £20, provided that printing, postage, delivery time, and any optional extras were shown clearly beforehand; I would pay more for excellent illustrations, accurate proofreading, and a meaningful keepsake presentation.
- **If the site produced something for you, how do you feel about it overall?** I was pleased that a book appeared, but I would not recognise it as the family story I asked for. The spelling mistake, unfinished sentence, invented frightening adventure, advanced vocabulary, and missing Grandma Maggie meant that I would want a corrected preview before considering payment.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | The purpose is clear, and the promise sounds exactly like what I want for Oliver. However, the sentence beginning “Leverage our multimodal generative narrative engine…” is unnecessarily technical; “story artefacts” and “ | click |
| 2 | Log in – StoryHearth | reassured (1) | This is straightforward, and the wording is easy to understand. I can see the email and password fields, although they are marked only by placeholders rather than proper visible labels. I will enter the account details p | type; type; click |
| 3 | My books – StoryHearth | anxious (-1) | I can see that my login worked because the page welcomes me and offers to create a book, but that error message makes me uneasy. “0x80070057” and “profile sync incomplete” tell me nothing about what has happened or wheth | click |
| 4 | Create your book – StoryHearth | reassured (1) | This is clear enough and reasonably easy to follow. I can put Oliver in as the star and myself in as the other person; the default “Grandparent” is correct, although “Grandparent” is a little impersonal for the story. | type; select; select; type; type; click |
| 5 | Create your book – StoryHearth | reassured (2) | This is a calm, uncluttered page, and the questions are pleasantly straightforward. I can describe the real memory without using technical language. I shall put Oliver in the story as the kite-flying hero, with Grandma M | type; type; type; click |
| 6 | Create your book – StoryHearth | hesitant (0) | This is a tidy screen, and I can clearly see the choices. However, I do not know what “Lexile” means, and the ranges do not tell me which one is right for a five-year-old. I shall choose “Lexile BR–200L” because I associ | click; click |
| 7 | Create your book – StoryHearth | reassured (1) | This is calm and uncluttered, and I can see that uploading a photograph is optional. I do not wish to upload a picture of Oliver without first being told how the photo will be used, retained, and protected, so I shall le | click |
| 8 | Create your book – StoryHearth | anxious (-1) | I can see that something is happening because the spinner is turning, but the page does not tell me whether my book is being written, whether my details were accepted, or how long I should wait. Since this is a keepsake  | wait_for_change |
| 9 | Your storybook – StoryHearth | curious (0) | The book has appeared, which is reassuring, but the misspelling “Adventrue” immediately makes me less confident about the care taken. The cover picture is cheerful, although it does not show Grandma Maggie or the hill an | flip_through |
| 10 | Your storybook – StoryHearth | frustrated (-1) | I have reached a proper ending, which is good, but this page does not feel worthy of a keepsake. The sentence is unfinished, and the picture does not show the blue kite or Grandma Maggie, even though those are central pa | click |
| 11 | Checkout – StoryHearth | annoyed (-1) | I can now see the full cost before entering any details, which is good. However, I did not choose the £7.99 premium gift wrap, so I am annoyed that it is ticked by default. The screen also asks for a full address and pay | read_page; done |
