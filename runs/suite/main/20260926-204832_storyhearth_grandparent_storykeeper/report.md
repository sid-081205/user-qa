# UserQA report: Margaret Ellison on http://127.0.0.1:8765/

*Persona:* **Margaret Ellison** (71) - Retired primary-school teacher who wants to pass family stories on to her grandchildren.  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 11 steps | *Pages reviewed:* 9 | *Issues:* 30 | *LLM calls:* 16 | *Wall time:* 367.3 s

## What the agent understood the website to be
- **what it is:** A website for creating illustrated personalised family storybooks, available as a digital preview or printed hardcover.
- **who it is for:** Families wanting to turn memories into storybooks featuring their children and other loved ones.
- **value proposition:** Creates and illustrates a bespoke family story, with a free digital preview and optional printed hardcovers.
- **pricing model:** The homepage says the digital preview is free, but it gives no price. A separate Pricing page is available.
- **fit for me:** This could be a lovely way to turn my father's blue-shirt kite story into a keepsake for Oliver, although I will need clear editing options, child-appropriate content, and a transparent hardcover price.
- **main tasks:** Log in, Add family members as characters, Describe a family memory, Read the generated storybook, Review the price of a printed hardcover

## Scores
- SUS: **45.0** (grade F; 68 = industry average)
- UEQ-S: pragmatic 0.0, hedonic -0.5 (range -3..+3)
- Likelihood to recommend (0-10): 1
- Output keepsake-worthiness (1-5): 1
- Verdict: *"A promising idea, but the result felt generic and unreliable, and I would not trust it with a cherished family story or my money until the story, pictures, explanations, and checkout were properly corrected."*

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 3 | H9 | My books dashboard | Unexplained technical error undermines confidence | “Error 0x80070057: profile sync incomplete.” | Replace the code with a plain-language message such as “Your profile information has not finished updating. You can still create a book; click here to retry your profile.” Include a Help option if the |
| 3 | H1 | My books dashboard | The error gives no clear consequence or recovery route | The banner contains only “profile sync incomplete” and provides no button or instructions. | State whether the error affects book creation, add a “Try again” or “Get help” control, and retain ordinary account actions when they remain safe. |
| 3 | H5 | Reading level and illustration style | My long story description was silently truncated | The previous field accepted 493 characters but displayed only 200 characters, with the end cut off: “...'d blue shirt. We took the blue kite up to the windy hil | Show a visible character limit before typing, warn while approaching it, and confirm that the full submitted text was saved. For a long memory, provide a larger text box or optional upload instead of  |
| 3 | CONTENT | Generated book cover | The title is misspelled on the cover | The page heading and cover both read “The Magical Adventrue of Oliver.” | Correct “Adventrue” to “Adventure” everywhere, and provide a clear edit or regeneration option before ordering. |
| 3 | H2 | Generated book cover | The selected illustration style appears not to have been used | I selected “Storybook classic — timeless ink and colour,” but the preview states “Illustration style: Pop-art comic.” | Honour the selected style, or clearly explain that it is unavailable and ask me to choose again before generation. |
| 3 | CONTENT | Generated book cover | The final sentence is incomplete | “And from that day on, whenever Oliver looked up at the sky, he would always remember” | Complete the sentence with what Oliver remembered, for example, “the windy hill and the blue kite flying above it.” |
| 3 | DECEPTIVE | Hardcover checkout | Optional gift wrap is pre-selected | [6] checkbox "Premium gift wrap" (checked), with "£7.99" shown beneath it | Leave optional extras unchecked by default and clearly state that they are optional, or ask the customer to select them before adding them to the total. |
| 2 | ACC | Log in, My books dashboard, Create your book – characters, Story memory form, Optional photo upload (x5) | Footer links and copyright have very faint contrast | The footer displays 'Privacy', 'Terms', 'Contact', and '© 2026 StoryHearth Ltd.' in very pale grey against the cream background. | Use darker text with sufficient contrast, increase the text size slightly, and make sure the links remain clearly distinguishable. |
| 2 | H2 | StoryHearth home page | The opening description uses confusing technical language | “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.” | Replace it with: “Turn a treasured family memory into a beautifully written and illustrated storybook featuring your loved ones.” |
| 2 | ACC | StoryHearth home page | Decorative image has no description | [image (no description) 430x440] | Add a useful alternative description, such as “An open illustrated storybook showing two children reading together.” |
| 2 | ACC | Log in | Email and password fields have no permanent labels | [5] is described as a 'textbox (no label)' with placeholder 'Email', and [6] is a 'textbox (no label)' with placeholder 'Password'. | Give both fields permanent visible labels, 'Email address' and 'Password', and keep the password field masked. |
| 2 | H2 | Reading level and illustration style | Reading-age scale is unexplained jargon | The labels “Lexile BR–200L,” “Lexile 200L–500L,” “Lexile 500L–800L,” and “Lexile 800L+” appear without a plain-English explanation. | Show plain labels such as “Beginning reader (ages 4–6)” and “Older children and adults,” with a short explanation of Lexile underneath. |
| 2 | H6 | Reading level and illustration style | The selected reading level is not clearly matched to a five-year-old | “Lexile 200L–500L” is checked, although the intended reader is five years old. | Use the entered age to preselect and visibly explain the recommended reading level, while allowing me to change it. |
| 2 | ACC | Optional photo upload | The photo upload control lacks a meaningful page label | [30] file-upload (no label); the only visible wording is the browser control “Choose file” | Give the upload control an explicit visible label such as “Optional photo of Oliver”, an accessible name, and a concise note explaining that it will be used to guide the illustrations. |
| 2 | TRUST | Optional photo upload | The reason and handling of a child's photo are not explained here | “Upload a clear photo of your child's face so the illustrations look like them.” | Add a short explanation of how the photo is used, stored, protected, and deleted, with a link to a plainly written privacy section. |

## Page-by-page
### StoryHearth home page  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Introduces the personalised family-story service, explains the three-step process, and offers paths to log in, begin creation, or view pricing.
- **What's happening:** The homepage is displayed with two main calls to action, a three-step explanation, customer quotations, question links, and policy/contact links below the fold. No story has been generated yet.
- **First impression (Margaret):** "The overall purpose is clear and the design is warm, but the opening paragraph is full of business jargon and does not make me feel especially safe or confident."
- **Cognitive walkthrough:** Q1 Yes. I would log in first because the study instructions tell me to use my account, and because beginning without logging in could make me wonder whether my work would be saved. / Q2 Yes. The clearly visible “Log in” control is at the top right. / Q3 Yes. “Log in” plainly matches what I want to do.
  - [H2 sev 2] **The opening description uses confusing technical language** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Replace it with: “Turn a treasured family memory into a beautifully written and illustrated storybook featuring your loved ones.”
  - [ACC sev 2] **Decorative image has no description** - evidence: [image (no description) 430x440]. Fix: Add a useful alternative description, such as “An open illustrated storybook showing two children reading together.”
  - [H1 sev 1] **The most prominent start action does not say whether login is required** - evidence: [5] “Proceed →” goes to /create.html, while a separate “Log in” control is in the header.. Fix: Add “Create your story” as the button label and a short note such as “You’ll be asked to log in or create an account before your story is saved.”
- **Positives:** The main heading is warm and easy to understand.; The three-step explanation makes the basic process feel manageable.; The free digital preview and UK delivery are stated before creation begins.; The text is generally readable with good visual contrast.; Privacy, terms and contact information are available.

### Log in  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** To let an existing customer sign in and access their storybook account.
- **What's happening:** The page presents two empty sign-in fields with the placeholders 'Email' and 'Password', plus a 'Log in' button. A link is also provided for people who do not yet have an account.
- **First impression (Margaret):** "It looks calm, straightforward, and reasonably trustworthy. The central form is easy to find, although I notice that the fields are labelled only by faint placeholders rather than permanent labels."
- **Cognitive walkthrough:** Q1 Yes, because I already have the account email and password and want to return to my account. / Q2 Yes, the two fields and the orange 'Log in' button are immediately visible in the centre of the page. / Q3 Yes. 'Email', 'Password', and 'Log in' plainly match what I want to do, although the input labels are not persistent.
  - [ACC sev 2] **Email and password fields have no permanent labels** - evidence: [5] is described as a 'textbox (no label)' with placeholder 'Email', and [6] is a 'textbox (no label)' with placeholder 'Password'.. Fix: Give both fields permanent visible labels, 'Email address' and 'Password', and keep the password field masked.
  - [ACC sev 2] **Footer links and copyright have very faint contrast** - evidence: The footer displays 'Privacy', 'Terms', 'Contact', and '© 2026 StoryHearth Ltd.' in very pale grey against the cream background.. Fix: Use darker text with sufficient contrast, increase the text size slightly, and make sure the links remain clearly distinguishable.
- **Positives:** The form is short and has a clear single purpose.; The 'Log in' button is prominent and plainly labelled.; The layout is uncluttered and the text is generally readable.; Privacy, terms, and contact links are available.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** To confirm that the user has signed in and manage the books associated with their account.
- **What's happening:** The page greets “Demo,” says that there are no books yet, offers a control to create a new book, and displays an unexplained profile-sync error.
- **First impression (Margaret):** "The main task is easy to find, but the alarming error code “0x80070057” makes me wonder whether the site is safe or whether my account is damaged."
- **Cognitive walkthrough:** Q1 Yes, I would try creating a new book despite the error, although I would want an explanation first. / Q2 Yes, the large orange “+ Create a new book” button is prominent and visible. / Q3 Yes. It plainly describes beginning a new book and matches what I want to do.
  - [H9 sev 3] **Unexplained technical error undermines confidence** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the code with a plain-language message such as “Your profile information has not finished updating. You can still create a book; click here to retry your profile.” Include a Help option if the problem continues.
  - [H1 sev 3] **The error gives no clear consequence or recovery route** - evidence: The banner contains only “profile sync incomplete” and provides no button or instructions.. Fix: State whether the error affects book creation, add a “Try again” or “Get help” control, and retain ordinary account actions when they remain safe.
  - [ACC sev 2] **Footer links have very low contrast** - evidence: “Privacy”, “Terms”, “Contact”, and “© 2026 StoryHearth Ltd.” appear in very pale grey.. Fix: Use darker text with stronger contrast and make the clickable areas at least 44 by 44 pixels.
  - [H2 sev 1] **Personal greeting uses the account placeholder rather than my name** - evidence: “Welcome back, Demo”. Fix: Use the customer’s first name once it is known, or say “Welcome back” when no personal name is available.
- **Positives:** Signing in has clearly led to an account dashboard.; The “+ Create a new book” control is prominent and clearly labelled.; The page is uncluttered and has plenty of open space.

### Create your book – characters  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Collect basic information about the child who will be the story's hero and the other person who will appear.
- **What's happening:** The form is empty and ready for the child's first name, age, pronouns, optional appearance, the other character's name, and their relationship. “Grandparent” is already selected for the relationship.
- **First impression (Margaret):** "The form looks calm and readable, and the headings “Who's the star of the story?” and “Who else is in the story?” make the purpose clear. I would be happy to complete this page."
- **Cognitive walkthrough:** Q1 Yes, I would fill in these familiar details now. / Q2 Yes, each question has a clearly visible text box or drop-down directly beside or below its label. / Q3 Yes. The labels tell me exactly whose name, age, pronouns, appearance, and relationship to enter.
  - [ACC sev 2] **Footer text has very low contrast** - evidence: The footer text “Privacy”, “Terms”, “Contact” and “© 2026 StoryHearth Ltd.” is very pale grey against the near-white background.. Fix: Use a darker, high-contrast footer colour while retaining the same font size and wording.
  - [CONTENT sev 1] **The form does not state that the other person can be the book creator** - evidence: “Who else is in the story?” and the examples “e.g. Grandma Rose” appear, but there is no explanation that I may enter my own name.. Fix: Add a small note such as “This can be you or another family member.”
- **Positives:** The page has a clear progression and a prominent “Next” button.; The appearance field is explicitly optional, which is reassuring.; The relationship menu already offers the correct “Grandparent” option.; The form asks only for information directly relevant to making the characters personal.

### Story memory form  (step 5)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_05.jpg)
- **Purpose:** Collect the setting, a treasured object, and the family memory that will form the basis of the personalised story.
- **What's happening:** The form presents three empty fields under “Your story,” followed by “Back” and “Next” controls. The setting, object, and memory have not yet been entered.
- **First impression (Margaret):** "This looks calm, clear, and comfortably readable. The questions feel personal rather than technical, although “A special object” is a little vague without an example immediately beside it."
- **Cognitive walkthrough:** Q1 Yes, I would be happy to complete these three fields now. / Q2 Yes, the matching textboxes are directly beneath their questions, and the orange “Next” button is easy to find. / Q3 Mostly. “Tell us the memory or idea behind your story” clearly matches what I want, and the other two labels are understandable; “A special object” could be “The special object from your memory” for greater precision.
  - [ACC sev 2] **Footer links have very faint contrast** - evidence: “Privacy”, “Terms”, and “Contact” appear in very pale grey text in the footer. Fix: Use darker footer text and remove the disabled-looking grey treatment so all links meet accessible contrast requirements.
  - [H2 sev 1] **Vague label for the object field** - evidence: “A special object”. Fix: Change the label to “The special object from this memory” and retain the yellow-bucket example.
- **Positives:** The page is uncluttered, with only the three questions I need to answer.; The field labels and examples are in plain English.; The text is large and generally has good contrast.; A clearly labelled “Back” control means I can return to the character details.

### Reading level and illustration style  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** To let the customer set the difficulty and visual appearance of the generated storybook.
- **What's happening:** Four reading-level choices and three illustration styles are presented. The middle reading level and the watercolour style are currently selected.
- **First impression (Margaret):** "The layout is calm, spacious, and easy to scan, but “Lexile” is jargon that should have been explained in ordinary language."
- **Cognitive walkthrough:** Q1 Yes. I want to choose a style and reading difficulty suitable for Oliver before generating the book. / Q2 Yes, the reading-level and illustration choices are prominent in the centre of the page. / Q3 Partly. The illustration labels describe the looks clearly, but the Lexile labels do not plainly tell me which is best for a five-year-old being read to.
  - [H5 sev 3] **My long story description was silently truncated** - evidence: The previous field accepted 493 characters but displayed only 200 characters, with the end cut off: “...'d blue shirt. We took the blue kite up to the windy hill beh”.. Fix: Show a visible character limit before typing, warn while approaching it, and confirm that the full submitted text was saved. For a long memory, provide a larger text box or optional upload instead of silently discarding text.
  - [H2 sev 2] **Reading-age scale is unexplained jargon** - evidence: The labels “Lexile BR–200L,” “Lexile 200L–500L,” “Lexile 500L–800L,” and “Lexile 800L+” appear without a plain-English explanation.. Fix: Show plain labels such as “Beginning reader (ages 4–6)” and “Older children and adults,” with a short explanation of Lexile underneath.
  - [H6 sev 2] **The selected reading level is not clearly matched to a five-year-old** - evidence: “Lexile 200L–500L” is checked, although the intended reader is five years old.. Fix: Use the entered age to preselect and visibly explain the recommended reading level, while allowing me to change it.
- **Positives:** The page is visually uncluttered, with large controls and strong contrast.; The selected options are easy to see.; There are clear Back and Next controls.; The illustration-style descriptions are warm and understandable.

### Optional photo upload  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Offer an optional way to include a child's photograph so the illustrations may resemble them, and allow the user to proceed to book creation.
- **What's happening:** The page offers a file-upload control, explains what kind of photograph would help, and provides “Back” and “Create my book” buttons. No file has been selected.
- **First impression (Margaret):** "The page is calm and easy to understand. I am comfortable leaving the photograph out, although the small browser control labelled only “Choose file” is not especially clear."
- **Cognitive walkthrough:** Q1 Yes, I would proceed without a photograph because it is explicitly optional. / Q2 Yes, I noticed the file control and the much clearer “Create my book” button. / Q3 Yes, “Create my book” clearly says that it will continue the creation process. The generic “Choose file” label matches its function but does not explain whose photo should be chosen.
  - [ACC sev 2] **The photo upload control lacks a meaningful page label** - evidence: [30] file-upload (no label); the only visible wording is the browser control “Choose file”. Fix: Give the upload control an explicit visible label such as “Optional photo of Oliver”, an accessible name, and a concise note explaining that it will be used to guide the illustrations.
  - [TRUST sev 2] **The reason and handling of a child's photo are not explained here** - evidence: “Upload a clear photo of your child's face so the illustrations look like them.”. Fix: Add a short explanation of how the photo is used, stored, protected, and deleted, with a link to a plainly written privacy section.
  - [ACC sev 1] **Footer text has very low contrast** - evidence: The footer items “Privacy”, “Terms”, “Contact” and “© 2026 StoryHearth Ltd.” are pale grey on a cream background. Fix: Use a substantially darker footer text colour that meets accessible contrast requirements.
- **Positives:** The photo is clearly described as optional.; The “Back” button lets me review my previous answers.; The “Create my book” button has a plain, prominent label.; The page is uncluttered and contains no preselected paid extra.

### Generated book cover  (step 8)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_08.jpg)
- **Purpose:** Show the generated storybook and let the reader begin paging through the preview.
- **What's happening:** A nine-page preview is displayed at page 1 of 9. The cover illustration shows Oliver standing on a green hill beside a blue kite, with a house and sun behind him; the previous-page control is disabled and the next-page control is available.
- **First impression (Margaret):** "The memory ingredients are recognisable, but the misspelled title immediately spoils the keepsake quality. The simple illustration feels generic, and the stated pop-art style conflicts with the classic style I selected."
- **Cognitive walkthrough:** Q1 Yes, I want to read every page carefully before deciding whether the book is suitable. / Q2 Yes, the right-arrow button marked “›” beneath the cover is the obvious control for moving to the next page. / Q3 The arrow is clear enough, although naming it “Next page” would be friendlier and clearer.
  - [CONTENT sev 3] **The title is misspelled on the cover** - evidence: The page heading and cover both read “The Magical Adventrue of Oliver.”. Fix: Correct “Adventrue” to “Adventure” everywhere, and provide a clear edit or regeneration option before ordering.
  - [H2 sev 3] **The selected illustration style appears not to have been used** - evidence: I selected “Storybook classic — timeless ink and colour,” but the preview states “Illustration style: Pop-art comic.”. Fix: Honour the selected style, or clearly explain that it is unavailable and ask me to choose again before generation.
  - [CONTENT sev 3] **The final sentence is incomplete** - evidence: “And from that day on, whenever Oliver looked up at the sky, he would always remember”. Fix: Complete the sentence with what Oliver remembered, for example, “the windy hill and the blue kite flying above it.”
  - [CONTENT sev 2] **Oliver's requested appearance is missing from the cover** - evidence: I described Oliver as having “brown curly hair, freckles, and green wellies,” but the cover shows a generic figure without visible freckles, curls, or green wellies.. Fix: Use the supplied character description in the image prompt and show a short summary of the character details used.
  - [H2 sev 1] **The next-page control has an ambiguous symbol** - evidence: Control [7] is labelled only “›”.. Fix: Label the control “Next page” and give it a sufficiently large clickable area with an accessible name.
- **Positives:** The title, Oliver, the hill, and the blue kite make the intended memory immediately recognisable.; The page counter clearly shows that this is page 1 of 9.; The previous-page button is properly disabled on the first page.; The navigation layout is uncluttered and the text has strong contrast.

### Hardcover checkout  (step 10)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_10.jpg)
- **Purpose:** To show the hardcover price, optional extras, delivery cost, total, and the address and payment fields required to place an order.
- **What's happening:** The page displays the hardcover titled "The Magical Adventrue of Oliver" for £24.99, a preselected "Premium gift wrap" charge of £7.99, shipping and handling of £12.99, and a total of £45.97. A countdown says the price is reserved for 09:57, and empty address and card fields lead to an offscreen "Pay now" button.
- **First impression (Margaret):** "The layout is clear and the prices are easy to see, but I am immediately wary of the gift wrap being pre-selected and the countdown making me feel hurried. I also notice that the title here says "Adventrue" correctly, whereas the preview had the spelling mistake."
- **Cognitive walkthrough:** Q1 Yes, I would untick the gift wrap because I want to establish the cost of the hardcover itself, but I would not enter any payment details. / Q2 Yes, I can see the checkbox beside "Premium gift wrap" and the associated £7.99 charge. / Q3 Yes, "Premium gift wrap" and its price make the extra charge identifiable, although it should not be selected by default.
  - [DECEPTIVE sev 3] **Optional gift wrap is pre-selected** - evidence: [6] checkbox "Premium gift wrap" (checked), with "£7.99" shown beneath it. Fix: Leave optional extras unchecked by default and clearly state that they are optional, or ask the customer to select them before adding them to the total.
  - [DECEPTIVE sev 2] **Checkout uses a reservation countdown** - evidence: "Your price is reserved for 09:57". Fix: Explain what is actually reserved, for how long, and whether the offer is genuine; avoid urgency unless it is materially necessary and clearly stated.
  - [VALUE sev 2] **Hardcover price is not broken down clearly enough** - evidence: "Hardcover ... £24.99", "Shipping & handling £12.99", and "Total £45.97". Fix: Show a simple summary of the basic delivered hardcover price separately, then list gift wrap, shipping, taxes, and any other charges, with the final total.
  - [VALUE sev 2] **The purpose of the gift-wrap charge is not explained** - evidence: The only wording beside the charge is “Premium gift wrap” and “£7.99”.. Fix: Describe the materials and presentation included, and state clearly that it is optional and not required for delivery.
  - [ACC sev 2] **The gift-wrap checkbox is small and visually detached from its label** - evidence: [6] is a very small, empty square positioned above and slightly apart from “Premium gift wrap”.. Fix: Place the checkbox directly beside a larger clickable label and give both a comfortably sized click target.
  - [H2 sev 1] **The meaning of the price-reservation timer is unclear** - evidence: The page says “Your price is reserved for 09:39” but does not explain whether this is a price guarantee, a stock hold, or merely a countdown.. Fix: Explain what is reserved and what will happen when the timer expires, or remove the timer if no action is required.
- **Positives:** The individual price lines and final total are visible without entering any details.; The gift wrap can be removed with a clearly labelled checkbox.; The delivery and payment sections are separated into understandable headings.

## Generated output assessment
*Artifact:* A generated nine-page personalized children's storybook preview with a hardcover checkout page

> I am very disappointed. Although Oliver, the blue kite, and the Welsh hill are present, this does not yet feel like our family story: Grandma Maggie is missing, the kite is not flown together, and the spelling, reading level, pictures, and unfinished ending need correction. I would not give this version to Oliver or print it as a treasured keepsake.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | Oliver, the blue kite, the Welsh hill, and the old farmhouse appear, but Grandma Maggie is missing from the story, the kite's maker is changed from Margaret's father to Grandpa, Oliver and Maggie never fly the kite toget |
| coherence | 1 | The story has repeated opening text, inconsistent Oliver/Olive naming, incorrect pronouns, an invented frightening adventure, a second beginning near the end, and an unfinished final sentence. |
| age fit | 1 | The requested reading age is five, but the prose is grade 8.5 and includes words such as 'ephemeral,' 'crepuscular,' 'juxtaposing,' 'ineffable,' and 'existential trepidation.' The threatening dark-woods passage is also u |
| language | 1 | There are visible template placeholders, the title is misspelled as 'Adventrue,' Oliver becomes 'Olive,' the final sentence ends without punctuation, and 'The End' is duplicated. |
| text image fit | 1 | The rain page shows sunshine without rain or puddles, the dark-woods page does not show teeth or a trembling child, and several pages omit the kite, Grandma Maggie, or the action described in the text. |
| character consistency | 2 | The available descriptions show a generic child rather than Oliver's specified brown curly hair, freckles, and green wellies. Some later images are unavailable for proper visual verification, so full consistency cannot b |
| visual quality | 1 | The artwork is described as flat, basic, and generic, does not closely match Oliver, and uses pop-art comic styling despite the requested classic, timeless ink-and-colour style. |
| emotional resonance | 1 | The central loving memory is not delivered: Oliver and Grandma Maggie do not fly the kite together, and the ending stops before explaining what he will remember. The result feels generic and not keepsake-worthy. |

- **used correctly:** Oliver's first name and age; Oliver's he/him pronouns in most of the story; The windy hill behind the old farmhouse in Wales; The blue kite made from an old blue shirt; The intended five-year-old storybook context
- **missing:** Grandma Maggie as an active character in the story; The shared kite-flying memory; The family message about making something loving and special together; Oliver's brown curly hair, freckles, and green wellies in the available illustrations; A proper completed dedication using Oliver and Grandma Maggie
- **changed:** Margaret's father is changed into 'Grandpa' as the kite's maker; The requested Classic illustration style is changed to Pop-art comic; The intended gentle family memory is changed into a rain, lantern, dark-woods, and balloon adventure
- **invented:** Uncle Bartholomew; A shiny red balloon; A threatening dark-woods adventure with shadows that grow teeth; Oliver being referred to as 'Olive'

### Part by part
#### Cover
![I1](artifacts/capture_01/img_00.jpg)
> A StoryHearth original Illustration style: Pop-art comic
- *Picture:* A simple pop-art-style scene with a small farmhouse, a smiling child identified as Oliver, a blue kite, a green hill, and a bright sun.
- *Reaction:* The blue kite and Welsh farmhouse idea are present, but the title's spelling mistake is immediately disappointing. The picture is very flat and generic, and Oliver does not look like the brown-haired, freckled child in green wellies that I described.
  - [language, sev 3] The title visibly says “The Magical Adventrue of Oliver”.
  - [fidelity, sev 2] The cover shows Oliver without the supplied brown curly hair, freckles, or green wellies.
  - [visual_quality, sev 2] The image uses very basic geometric shapes and a generic smiling figure rather than warm, detailed family-book artwork.
- **Change I'd make:** Correct the title to “The Magical Adventure of Oliver” and redraw Oliver with brown curly hair, freckles, and green wellies. Use warmer, more detailed artwork while retaining the classic storybook feeling.
- **Suggested rewrite:** The Magical Adventure of Oliver

#### Title page
![I2](artifacts/capture_03/view_00.jpg)
> For {{recipient_name}}, with love from {{sender_name}}
- *Picture:* A screenshot of the StoryHearth book viewer showing the title, a blank-looking central page, page navigation marked 2 / 9, and buttons for regenerating the book or ordering the hardcover.
- *Reaction:* This is not ready for a keepsake because the names have not been filled in. The brackets and braces are visible placeholders, and the page is labelled page 2 rather than a proper dedication page.
  - [language, sev 4] “For {{recipient_name}}, with love from {{sender_name}}” contains unfilled template placeholders.
  - [fidelity, sev 3] The recipient and sender should be Oliver and Grandma Maggie, but neither name appears.
  - [coherence, sev 1] The viewer identifies this as page 2 / 9, although it functions as a dedication page rather than the opening story page.
- **Change I'd make:** Replace the placeholders with “For Oliver, with love from Grandma Maggie” and present it as a proper dedication page before page 1.
- **Suggested rewrite:** For Oliver, with love from Grandma Maggie

#### Page 1
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in the windy hill behind the old farmhouse in Wales, there lived a curious child named Oliver. Oliver was 5 years old and loved nothing more than the blue kite made from Grandpa's old blue shirt.
- *Picture:* A child stands on a green hill beside a small farmhouse and a blue kite, with a large sun in the sky. The child is labelled Oliver.
- *Reaction:* This does place Oliver, the hill, the old farmhouse, Wales, and the blue kite together. However, the story says the kite was made by Grandpa, although my memory was that my father made it for me, and the image does not show Grandma Maggie or the details of Oliver's appearance.
  - [fidelity, sev 3] “the blue kite made from Grandpa's old blue shirt” changes the relationship in the supplied memory, where the speaker's father made the kite for Margaret.
  - [fidelity, sev 3] “Grandma Maggie” does not appear, and Oliver is not described or shown with brown curly hair, freckles, or green wellies.
  - [language, sev 2] “in the windy hill” is awkward wording; the natural phrase is “on the windy hill.”
- **Change I'd make:** Rewrite this in short, warm sentences and identify the kite as something my father made for me. Introduce Grandma Maggie and describe Oliver's curly hair, freckles, and wellies.
- **Suggested rewrite:** On a windy hill behind an old farmhouse in Wales, a boy named Oliver played. He had brown curly hair, freckles, and green wellies. His grandmother, Grandma Maggie, held the blue kite that my father had made from an old blue shirt.

#### Page 2
![I4](artifacts/capture_05/img_00.jpg)
![I2](artifacts/capture_03/view_00.jpg)
> One evening Oliver gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* Oliver stands on the hill at twilight beneath a purple and orange sky with a few stars. The farmhouse remains visible, but the kite and any wind are absent.
- *Reaction:* I would not read this page aloud to a five-year-old. The words are far beyond the requested reading level, and the picture does not show Oliver looking upward or interacting with the kite.
  - [age_fit, sev 4] “ephemeral luminescence,” “crepuscular firmament,” “engendered,” “juxtaposing,” “ineffable,” and “existential trepidation” are unsuitable for a five-year-old.
  - [text_image_fit, sev 2] The text says Oliver gazed upward, but the image shows him standing still and looking forward; it also omits the kite and any meaningful sky-related action.
  - [coherence, sev 2] The page introduces melancholy and existential trepidation without giving a clear action or connecting it to flying the kite.
- **Change I'd make:** Use one or two short sentences about Oliver feeling the wind and looking up at the sky. Show him holding the kite and looking toward it.
- **Suggested rewrite:** The sun began to go down. Oliver looked up at the pink and purple sky and felt the wind on his cheeks. “The kite will float high,” Grandma Maggie said.

#### Page 3
![I5](artifacts/capture_06/img_00.jpg)
![I3](artifacts/capture_04/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Olive pulled up his hood and ran for shelter, holding the blue kite made from Grandpa's old blue shirt tight.
- *Picture:* The scene returns to bright daylight with a smiling child, the farmhouse, the blue kite, and a large sun. There is no rain, no puddles, and no visible hood.
- *Reaction:* The name changes from Oliver to Olive, which is a serious error in a personal book. The picture also contradicts the rain scene completely.
  - [language, sev 4] “Olive pulled up his hood” changes Oliver's name to Olive.
  - [text_image_fit, sev 4] The text describes pouring rain, grey drops, puddles, and a hood, while I5 shows sunshine, a clear blue sky, and no rain or puddles.
  - [fidelity, sev 3] The story again calls the kite “made from Grandpa's old blue shirt,” rather than saying that my father made it for me.
- **Change I'd make:** Correct Olive to Oliver, restore the true family history, and show rain, puddles, Oliver's hood, and the kite being carried to shelter.
- **Suggested rewrite:** Then the rain came down. Oliver pulled up his hood and held the blue kite close. He ran with Grandma Maggie towards the old farmhouse while the raindrops splashed in the puddles.

#### Page 4
![I6](artifacts/capture_07/img_00.jpg)
![I4](artifacts/capture_05/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Oliver, follow me!" he called, and she followed him along the winding path.
- *Picture:* A taller figure labelled Uncle Bartholomew holds a yellow lantern beside Oliver. The farmhouse and hill are visible, but there is no clearly shown winding path or shelter.
- *Reaction:* Uncle Bartholomew was never mentioned in my family story, and the change from “he” to “she” makes the page confusing. This invented adventure takes the story away from the loving memory I wanted to pass on.
  - [fidelity, sev 4] “Uncle Bartholomew” appears without being supplied in the family details and replaces the central relationship with Grandma Maggie.
  - [coherence, sev 4] “he called, and she followed him” uses inconsistent pronouns for Oliver, whose pronouns are he / him.
  - [text_image_fit, sev 2] The text mentions a winding path, but the picture shows mainly the two figures and the farmhouse, with no clear path or destination.
- **Change I'd make:** Remove Uncle Bartholomew and keep the story with Oliver and Grandma Maggie. Correct Oliver's pronouns and show them walking together towards the farmhouse or waiting out the rain.
- **Suggested rewrite:** Grandma Maggie held up the lantern. “Come on, Oliver,” she said. “We will wait for the rain to stop under the old farmhouse.” Oliver followed her along the path.

#### Page 5
![I7](artifacts/capture_08/img_00.jpg)
![I5](artifacts/capture_06/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Oliver again. Oliver clutched a shiny red balloon and trembled in the dark.
- *Picture:* Oliver stands at night near a row of simple trees, a red balloon, stars, and a crescent moon. The trees have no visible teeth, and Oliver is not visibly trembling.
- *Reaction:* This page introduces a dark, threatening adventure that is not part of our memory and may worry a young child. The red balloon is also a new object that has no connection to the kite story.
  - [fidelity, sev 4] The dark-woods adventure and shiny red balloon were not supplied and displace the hill, farmhouse, and family kite-flying memory.
  - [age_fit, sev 3] “the shadows grew teeth and whispered that no one would ever find Oliver again” creates unnecessary fear for the requested gentle family story.
  - [text_image_fit, sev 3] The text describes shadows with teeth and Oliver trembling, but the picture shows ordinary round trees and a calm, smiling Oliver.
- **Change I'd make:** Replace this page with a gentle return to the hill. Remove the frightening shadows and balloon, and show Oliver and Grandma Maggie watching the rain pass.
- **Suggested rewrite:** The rain stopped. The clouds moved away, and the sun came out over the hill. Oliver and Grandma Maggie held the blue kite together. “Shall we try again?” Oliver asked.

#### Page 6
![I8](artifacts/capture_09/img_00.jpg)
![I6](artifacts/capture_07/img_00.jpg)
> Once upon a time, in the windy hill behind the old farmhouse in Wales, there lived a curious child named Oliver. At last the sun came out, and Oliver skipped all the way home, happier than ever.
- *Picture:* A smiling Oliver stands beside the farmhouse on the green hill in daylight. The blue kite is not visible, and he is not shown skipping or walking home.
- *Reaction:* The sun returning is a pleasant idea, but the opening sentence repeats page 1 word for word and the final action is not shown. The promised family memory still never happens: Oliver and Grandma Maggie never fly the kite together.
  - [coherence, sev 3] The repeated opening “Once upon a time...” makes the page feel like a second beginning rather than a continuation.
  - [fidelity, sev 4] The supplied memory required Oliver and Grandma Maggie to fly the kite together, but the page only says Oliver went home and never shows the kite.
  - [text_image_fit, sev 3] The text says Oliver skipped all the way home, while the image shows him standing still beside the farmhouse with no kite.
- **Change I'd make:** Remove the repeated opening and make this the central payoff: Oliver and Grandma Maggie hold the kite together, the wind lifts it, and they watch it fly over the Welsh hill.
- **Suggested rewrite:** The sun came out over the Welsh hill. Oliver and Grandma Maggie ran with the blue kite. The wind caught the kite, and it floated high above the old farmhouse. Oliver laughed. “We did it!” he said.

#### Page 7
![I9](artifacts/capture_10/img_00.jpg)
![I7](artifacts/capture_08/img_00.jpg)
> The End And from that day on, whenever Oliver looked up at the sky, he would always remember The End
- *Picture:* An orange end page with Oliver standing beside the old farmhouse. It displays “The End” twice in the surrounding page text, with no completed closing thought.
- *Reaction:* A proper ending is important to me, and this one is visibly unfinished. The final sentence stops at “remember,” so I would not want to give this version to Oliver or print it as a keepsake.
  - [language, sev 4] The sentence ends abruptly at “he would always remember” with no object and no final punctuation.
  - [coherence, sev 2] “The End” is repeated twice on the page.
  - [emotional_resonance, sev 3] The ending never identifies what Oliver remembers, so the family message about making something loving together is not completed.
- **Change I'd make:** Complete the final thought, remove the duplicate “The End,” and end with the family lesson about making something special together.
- **Suggested rewrite:** From that day on, whenever Oliver looked up at the sky, he remembered flying the blue kite with Grandma Maggie. The End

#### Checkout — order summary and delivery
![I10](artifacts/capture_12/view_00.jpg)
![I11](artifacts/capture_12/view_01.jpg)
> Checkout Your price is reserved for 09:42 Hardcover: The Magical Adventrue of Oliver	£24.99  Premium gift wrap	£7.99 Shipping & handling	£12.99 Total	£45.97 Delivery Address
- *Picture:* A StoryHearth checkout page showing the hardcover, premium gift wrap, shipping, total, a countdown banner, and an address field.
- *Reaction:* The itemised prices are easy to see, including the £7.99 gift wrap and £12.99 shipping, but the title remains misspelled. I would want a plain explanation of what the reservation timer means before entering my address or card details.
  - [language, sev 3] The checkout repeats “The Magical Adventrue of Oliver”.
  - [fidelity, sev 2] The checkout confirms the misspelled title rather than offering a corrected title or warning that the preview contains errors.
- **Change I'd make:** Correct the title everywhere, explain the price reservation in plain English, and state whether the delivery charge and gift wrap are compulsory before asking for the address.
- **Suggested rewrite:** Your price is held for 09 minutes and 42 seconds. Hardcover £24.99. Premium gift wrap £7.99 (selected). Shipping & handling £12.99. Total £45.97. Please enter the delivery address for this order.

#### Checkout — payment form
![I11](artifacts/capture_12/view_01.jpg)
![I12](artifacts/capture_13/view_00.jpg)
![I13](artifacts/capture_13/view_01.jpg)
> Checkout Your price is reserved for 09:27 Hardcover: The Magical Adventrue of Oliver	£24.99  Premium gift wrap	£7.99 Shipping & handling	£12.99 Total	£45.97 Payment Card number Expiry CVC
- *Picture:* The lower checkout screenshot shows the gift-wrap checkbox unchecked, the total changed to £37.98, blank card-number, expiry, and CVC fields, and a large “Pay now” button.
- *Reaction:* The payment fields are plain, but the page does not explain why it needs CVC or show any security and privacy reassurance. I also noticed that the screenshots show different countdown times from the extracted text, which makes me uneasy about relying on the reservation.
  - [language, sev 2] The extracted checkout text reports “Your price is reserved for 09:27,” while the visible later screenshot shows “09:26” and the earlier screenshot shows “09:41.”
  - [language, sev 3] The title continues to be shown as “The Magical Adventrue of Oliver”.
  - [fidelity, sev 2] The checkout provides no clear explanation of what information is required for payment or why CVC is being requested.
- **Change I'd make:** Keep the total consistent with the checkbox state, explain what CVC means, and add a short privacy and secure-payment explanation before the card fields. Correct the title in the checkout as well.
- **Suggested rewrite:** CVC means the 3-digit security code printed on the back of your card. Your card details are used only to pay for this order. Premium gift wrap is not selected. Total: £37.98.

#### Cover / Title page
![I1](artifacts/capture_01/img_00.jpg)
> The Magical Adventrue of Oliver A StoryHearth original Illustration style: Pop-art comic
- *Picture:* The supplied evidence does not show I1 clearly enough for an honest visual inspection. The metadata identifies the requested illustration style as pop-art comic.
- *Reaction:* The obvious misspelling in “Adventrue” would embarrass me if this were a real keepsake. I had asked for a classic timeless style, so I would also want the style corrected rather than quietly changed.
  - [language, sev 3] The Magical Adventrue of Oliver
  - [fidelity, sev 3] The requested style was “Classic,” but the page says “Illustration style: Pop-art comic.”
  - [visual_quality, sev 0] I1 is not visible clearly enough in the supplied evidence to judge the artwork or artefacts.
- **Change I'd make:** Correct “Adventrue” to “Adventure” and use the requested classic, timeless ink-and-colour style. A more personal title would be “Oliver and the Blue Kite.”
- **Suggested rewrite:** Oliver and the Blue Kite A StoryHearth family story Classic ink-and-colour storybook

#### Page 8
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in the windy hill behind the old farmhouse in Wales, there lived a curious child named Oliver. At last the sun came out, and Oliver skipped all the way home, happier than ever.
- *Picture:* I8 is not visible in the supplied evidence, so I cannot tell whether Oliver looks like the requested brown-haired, freckled child in green wellies or whether the kite is shown.
- *Reaction:* This repeats the opening instead of completing the memory. Oliver goes home without Grandma Maggie, and the kite is never actually flown together, which is the heart of what I wanted to pass on.
  - [coherence, sev 3] The first sentence repeats the opening almost word for word.
  - [fidelity, sev 4] Oliver skipped all the way home; Grandma Maggie and the shared kite flight are missing from the ending.
  - [emotional_resonance, sev 4] Oliver is "happier than ever," but the ending gives no reason and does not connect the old shirt to the family's love.
  - [character_consistency, sev 0] I8 is unavailable, so the requested appearance and the child's visual continuity cannot be checked.
- **Change I'd make:** End with Oliver and Grandma Maggie successfully flying the blue kite and connect it to the loving family memory.
- **Suggested rewrite:** When the sun came out, Oliver and Grandma Maggie returned to the hill. They gave the kite more string, and it danced above the old farmhouse. Oliver laughed as the blue kite flew high.

#### Page 9
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Oliver looked up at the sky, he would always remember The End
- *Picture:* I9 is not visible in the supplied evidence, so its artwork and any distorted lettering cannot be evaluated.
- *Reaction:* The last sentence stops in the middle, and “The End” appears twice. I have taught children to read for thirty years, and this does not feel like a proper ending to a treasured book.
  - [language, sev 4] whenever Oliver looked up at the sky, he would always remember
  - [coherence, sev 4] The final sentence is incomplete, and “The End” is printed twice.
  - [emotional_resonance, sev 4] The page promises that Oliver will remember something but never says what it was.
- **Change I'd make:** Complete the sentence, name the shared kite-flying memory, and print “The End” only once.
- **Suggested rewrite:** From that day on, whenever Oliver looked up at the sky, he remembered flying Grandpa's blue kite with Grandma Maggie on the windy Welsh hill. The End

**Top changes to the output:** 1. Rewrite the entire story so Oliver and Grandma Maggie fly the blue kite together on the windy Welsh hill, making clear that Margaret's father made it from the old blue shirt. | 2. Remove Uncle Bartholomew, the frightening dark-woods scene, the red balloon, and all unrelated adventure material; use short, warm sentences suitable for a five-year-old. | 3. Fix 'Adventrue' to 'Adventure' everywhere, replace the placeholders with Oliver and Grandma Maggie, correct 'Olive' to Oliver, and complete the final sentence with proper punctuation and only one 'The End.' | 4. Redraw Oliver with brown curly hair, freckles, and green wellies, using the requested classic, timeless ink-and-colour style rather than generic pop-art artwork. | 5. Ensure every illustration matches its page, especially the rain, kite, characters, and final shared kite-flying scene.

## Recommendations (participant's priorities)
- **[high] Rewrite the story so Oliver and Grandma Maggie fly the blue kite together on the windy Welsh hill, making clear that Margaret's father made it from the old blue shirt.** (Generated book preview) - This is the central family memory, and the current version does not capture or personalise it properly.
- **[high] Remove the invented Uncle Bartholomew, frightening dark-woods scene, red balloon, and other unrelated adventure material, and use short, warm sentences suitable for a five-year-old.** (Generated book preview) - The story should be comforting and age-appropriate, not threatening or filled with material I did not request.
- **[high] Correct 'Adventrue' to 'Adventure', replace template placeholders, correct 'Olive' to Oliver, complete the final sentence, remove duplicated text, and check the reading level.** (Generated book preview) - These errors make the book look careless and undermine its value as a keepsake.
- **[high] Redraw Oliver with brown curly hair, freckles, and green wellies, and use the requested classic, timeless ink-and-colour style.** (Generated book cover and illustrations) - The pictures should reflect the child and the special style I selected, not show a generic character in an unrelated style.
- **[high] Ensure every illustration matches its page, particularly the rain, the kite, Oliver, Grandma Maggie, and the final shared kite-flying scene.** (Generated book illustrations) - A picture that contradicts the text, or leaves out an important character, makes the story feel poorly made.
- **[high] Do not preselect optional gift wrap, and show the base book price, delivery, and each extra as separate, clearly labelled charges before payment.** (Hardcover checkout) - I need to know exactly what I am paying for and must not discover an unexpected cost at the final step.
- **[medium] Explain the meaning and purpose of the price-reservation timer, or remove it if it is not essential.** (Hardcover checkout) - An unexplained countdown can feel like pressure and may prevent me from taking time to read the small print.
- **[high] Replace 'Profile sync incomplete' with a plain-language explanation of what happened, whether any information was affected, and how to recover.** (My books dashboard) - Technical errors without consequences or a way forward make me worry that I have lost information or done something wrong.
- **[low] Use the account holder's name in the personal greeting instead of an account placeholder.** (My books dashboard) - It would make the site feel more carefully made and reassure me that I am in the correct account.
- **[medium] Replace technical marketing language such as 'multimodal generative narrative engine' with a simple explanation of what the service does.** (Home page) - Plain English would tell me more quickly whether this is the right service for me.
- **[medium] Explain Lexile in ordinary language and clearly label the level recommended for a five-year-old.** (Reading level and illustration style) - I should not have to guess which range is suitable for my grandson.
- **[high] Show the full story description after submission and warn me if text has been shortened or removed.** (Story memory form) - A silent truncation may lose important details from the memory I want preserved.
- **[high] Explain how a child's photograph would be stored, used, shared, and deleted before I upload it.** (Optional photo upload) - I am cautious about sharing information about a child and need a clear reason before giving consent.
- **[medium] Give the email and password fields permanent, visible labels, improve the contrast of footer text, and describe decorative images.** (Log in, home page, and footer areas) - These changes would make the site easier to read and more accessible, especially as I get older.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** StoryHearth appears to be a website for creating personalised storybooks in which a child or family member is the hero. It seems intended for parents and grandparents who want to turn a family memory into a keepsake.
- **What was the most frustrating or confusing moment, and why?** The most frustrating moment was seeing the generated book: it misspelled 'Adventure', included unfinished and repeated text, changed the names, and did not actually show Oliver and Grandma Maggie flying the kite together. The unexplained 'Profile sync incomplete' message also made me doubt whether my information was safe.
- **What was the best moment?** The best moment was entering the family memory, because the form was calm and easy to read, and I could describe Oliver, the blue kite, and the windy hill in Wales without feeling that I was giving away unnecessary information.
- **Was there any point where, in real life, you would have given up? Where and why?** I would probably have given up after reading the finished preview, especially if I had reached the checkout and been asked to pay for such a poor result. I would not want to spend money on a book that was misspelled, unfinished, and not faithful to our family memory.
- **What did you expect to find or be able to do that wasn't there?** I expected a clear explanation of what each technical term meant, especially Lexile, and a way to see and correct the story before paying. I also expected a proper illustration of Oliver with Grandma Maggie and the blue kite, rather than generic or unrelated artwork.
- **Did you trust this website with your information (and your family's)? Why or why not?** I was willing to share ordinary story details, but I was cautious about uploading a photograph of Oliver because the site did not explain how a child's picture would be stored or used. The unexplained profile error and the preselected gift-wrap charge made me less willing to trust the site with payment or personal information.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would pay about £25 for a well-made hardcover if the story, illustrations, and ending were genuinely good and the delivery charge were clearly explained. I would pay more for excellent artwork, a faithful story, and a finished keepsake, but not for spelling errors, unfinished text, or unexpected extras.
- **If the site produced something for you, how do you feel about it overall?** I am very disappointed. Oliver, the blue kite, and the Welsh hill are present, but Grandma Maggie is missing, the important shared kite-flying scene is absent, and the spelling, reading level, pictures, and ending need substantial correction. I would not give this version to Oliver or print it as a treasured keepsake.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | This sounds like what I wanted, and the three steps are reassuringly straightforward. However, “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your househol | click |
| 2 | Log in – StoryHearth | reassured (1) | This is a simple, uncluttered sign-in page, and the two fields look easy to identify from their placeholders. I can enter the account details supplied for this visit and press the clearly labelled 'Log in' button. | type; type; click |
| 3 | My books – StoryHearth | confused (-1) | I can see that my sign-in worked, but that error code is very unsettling. “Profile sync incomplete” does not explain whether anything is wrong with my account, whether I have lost information, or whether it will affect m | click |
| 4 | Create your book – StoryHearth | reassured (1) | This form is pleasantly straightforward, and the questions are ones I can answer without giving away anything private. I shall put Oliver in first, describe him in the warm, particular way a book should, and include myse | type; select; select; type; type; click |
| 5 | Create your book – StoryHearth | reassured (2) | This is pleasantly straightforward, and the larger text and strong contrast are comfortable to read. I shall describe the windy hill behind the old farmhouse in Wales, the blue kite made from Grandpa’s shirt, and the fam | type; type; type; click |
| 6 | Create your book – StoryHearth | hesitant (1) | I am not sure what “Lexile” means, so I had to work out that the first range is probably the most suitable for a five-year-old. The choices themselves are clear enough, and the page looks calm and uncluttered. I shall ch | click; click; click |
| 7 | Create your book – StoryHearth | reassured (1) | I shall not upload a photograph of Oliver unless I can first understand how the picture will be stored and used, particularly because he is a child. The word “optional” reassures me that I can proceed without one, so I s | click; wait_for_change |
| 8 | Your storybook – StoryHearth | frustrated (-1) | Oliver is unmistakably the hero and the blue kite is there, so the basic memory has been understood. However, “The Magical Adventrue of Oliver” is a serious spelling mistake on the very first page, and the image is much  | flip_through |
| 9 | Your storybook – StoryHearth | frustrated (-1) | The ending is there, which is good, and Oliver remains the hero. However, the final sentence is unfinished: “he would always remember” does not say what he remembered. That makes the book feel less like a proper keepsake | scroll; click |
| 10 | Checkout – StoryHearth | suspicious (-1) | I can now see the cost, but I am uneasy that the £7.99 gift wrap was selected for me. I would want to know what the book costs without that optional extra, so I shall untick it and then read the rest of the page carefull | click; read_page |
| 11 | Checkout – StoryHearth | reassured (1) | That is clearer: removing the gift wrap reduced the total from £45.97 to £37.98. I have now established that the hardcover itself costs £24.99 and that delivery adds £12.99, but I do not need to proceed any further or pr | done |
