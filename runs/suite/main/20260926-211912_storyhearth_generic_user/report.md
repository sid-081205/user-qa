# UserQA report: Test User on http://127.0.0.1:8765/

*Persona:* **Test User** (35) - Baseline condition - a generic adult web user with no persona conditioning (ablation).  
*Model:* `stealth/space-bunny-alpha` | *Status:* **done** after 11 steps | *Pages reviewed:* 9 | *Issues:* 22 | *LLM calls:* 13 | *Wall time:* 251.9 s

## What the agent understood the website to be
- **what it is:** A service that creates personalised, illustrated digital storybooks featuring family members and can also produce printed hardcover books.
- **who it is for:** Families wanting to preserve a child and a favourite grown-up, sibling, or pet in a story based on a real memory.
- **value proposition:** Turn a family memory and treasured details into an illustrated storybook, with a free digital preview and printed hardcovers shipped across the UK.
- **pricing model:** The digital preview is advertised as free, while printed hardcovers are available for a fee. No actual price is shown here.
- **fit for me:** Very relevant because I can create a story starring my five-year-old daughter, Sam, and her Grandpa Joe, based on a beach memory and her yellow bucket.
- **main tasks:** Log in to an existing account, Choose family characters, Provide a place, treasured object, and memory, Generate and read an illustrated storybook, Check pricing for a printed hardcover

## Scores
- SUS: **55.0** (grade D; 68 = industry average) - inconsistent responding flagged
- UEQ-S: pragmatic -0.5, hedonic 0.75 (range -3..+3)
- Likelihood to recommend (0-10): 1
- Output keepsake-worthiness (1-5): 1
- Verdict: *"The idea excited me, but the finished book ignored the most important family details and had too many obvious errors for me to trust or pay for."*
- Would have abandoned at step 10 (127.0.0.1:8765/checkout.html \| Checkout): I would not continue to payment because the pre-selected £7.99 gift wrap makes the checkout feel misleading, and the task only requires finding the price. [self-report]

## Top issues
| Sev | Code | Page | Issue | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 3 | H9 | My books dashboard | Technical sync error creates doubt about account data | “Error 0x80070057: profile sync incomplete.” | Replace the code with a plain-language message such as “Some account details could not be loaded.” Explain what is affected and provide a Retry or Continue button if safe. |
| 3 | H2 | Generated storybook preview | Selected illustration style was not applied | The page says “Illustration style: Pop-art comic,” even though Watercolour was the selected look on the previous screen. | Apply the chosen Watercolour style and show the selected style in the generation summary so a mismatch is obvious and can be corrected. |
| 3 | CONTENT | Generated storybook preview | The generated title is misspelled | “The Magical Adventrue of Sam” | Add a title spell-check and let me edit the title before ordering. |
| 3 | DECEPTIVE | Hardcover checkout | Premium gift wrap is pre-selected | [6] checkbox "Premium gift wrap" (checked), with £7.99 shown beside it | Leave optional extras unchecked by default and show the additional cost immediately beside the checkbox. |
| 2 | CONTENT | StoryHearth homepage | The main description uses unnecessarily technical language | “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.” | Replace it with plain language, for example: “Turn a special family memory into a personalised storybook featuring your child and someone you love.” |
| 2 | ACC | StoryHearth homepage | The prominent hero image lacks a useful description | The image is shown with “no description” despite conveying the core family-book idea visually. | Add concise alternative text that conveys the purpose, such as “An open personalised storybook featuring two family members.” |
| 2 | ACC | Log in | Login fields lack programmatic visible labels | [5] textbox (no label) placeholder "Email" and [6] textbox (no label) placeholder "Password" | Add persistent visible labels such as “Email address” and “Password”, associated with each textbox, while keeping placeholders only as supplementary hints. |
| 2 | H10 | My books dashboard | Sync problem has no recovery guidance | “Error 0x80070057: profile sync incomplete.” There is no Retry, Help, or explanation beside the message. | Add a short explanation and clear actions such as “Try again” and “Continue without syncing,” or a Contact support link. |
| 2 | H4 | My books dashboard | Log out link appears to point to the dashboard | [5] link “Log out” -> /dashboard.html | Make the Log out link navigate to a genuine logged-out page or sign-in screen. |
| 2 | ACC | My books dashboard | Footer links have very low contrast | The footer text “Privacy,” “Terms,” “Contact,” and “© 2026 StoryHearth Ltd.” is extremely faint. | Use a darker text colour with sufficient WCAG contrast and provide visible keyboard focus states. |
| 2 | H2 | Reading level and illustration style | Reading-level choices use unexplained jargon | "Lexile BR–200L", "Lexile 200L–500L", "Lexile 500L–800L", and "Lexile 800L+" | Show an age-friendly label beside each range, such as “Lexile 200L–500L — approximately ages 5–8”, and include a short explanation of Lexile. |
| 2 | ACC | Optional photo upload | File upload lacks a proper label | [30] file-upload (no label); the control only displays “Choose file” | Give the file input a persistent visible label such as “Child’s photo” and associate the explanatory text with it through accessible markup. |
| 2 | TRUST | Optional photo upload | Privacy reassurance is missing beside a child-photo upload | “Upload a clear photo of your child's face so the illustrations look like them.” | Add a short note linking to the Privacy Policy and explaining whether the uploaded photo is used only for generation, stored, or deleted. |
| 2 | CONTENT | Generated storybook preview | The final page does not fit the family memory well | “And from that day on, whenever Sam looked up at the sky, she would always remember” | Generate an ending that refers clearly to the beach, sandcastles, Grandpa Joe, and the yellow bucket. |
| 2 | VALUE | Hardcover checkout | Checkout is not showing what the basic delivered hardcover costs before extras | The page shows “Hardcover: The Magical Adventrue of Sam £24.99,” “Shipping & handling £12.99,” and a separate checked “Premium gift wrap £7.99.” | Show a clear subtotal for the book and delivery, and update the total immediately when the gift-wrap checkbox changes. |

## Page-by-page
### StoryHearth homepage  (step 1)
`http://127.0.0.1:8765/`

![screenshot](screenshots/step_01.jpg)
- **Purpose:** Introduce the personalised storybook service, explain how it works, and offer paths to pricing, login, and story creation.
- **What's happening:** The homepage displays a hero message, two calls to action, a family-themed illustration, a three-step process, testimonials, FAQ controls, and footer links. No generated content is present.
- **First impression (Test):** "The warm cream design and simple three-step explanation make the service look friendly and relevant, but the opening paragraph is needlessly technical and the main illustration has no useful description."
- **Cognitive walkthrough:** Q1 Yes, I want to log in to my account and make our story. / Q2 Yes, the dark “Log in” button at the top right is prominent, and I can also see the “Proceed →” button. / Q3 Yes, “Log in” exactly matches my immediate goal, while “Proceed” is less clear about whether it logs in or starts a new story.
  - [CONTENT sev 2] **The main description uses unnecessarily technical language** - evidence: “Leverage our multimodal generative narrative engine to synthesise bespoke, heirloom-grade story artefacts from your household's lived-experience corpus.”. Fix: Replace it with plain language, for example: “Turn a special family memory into a personalised storybook featuring your child and someone you love.”
  - [ACC sev 2] **The prominent hero image lacks a useful description** - evidence: The image is shown with “no description” despite conveying the core family-book idea visually.. Fix: Add concise alternative text that conveys the purpose, such as “An open personalised storybook featuring two family members.”
  - [H8 sev 1] **The image is marked as decorative-looking but carries meaning** - evidence: [image (no description) 430x440]. Fix: Use a more relevant image showing a child and grandparent with a storybook, or pair the existing graphic with a clear caption.
- **Positives:** The three simple headings “Tell us who,” “Share a memory,” and “We write & illustrate” make the process easy to understand.; “Log in” is visible without scrolling.; The page says the digital preview is free and mentions UK hardcover shipping.; The warm colours and typography create a family-friendly tone.

### Log in  (step 2)
`http://127.0.0.1:8765/login.html`

![screenshot](screenshots/step_02.jpg)
- **Purpose:** To sign into an existing StoryHearth account.
- **What's happening:** The login form is empty and ready for an email address and password. A prominent Log in button is provided, along with a Create an account link and footer links.
- **First impression (Test):** "Simple and familiar. I know exactly what to do, although the input boxes are identified only by placeholder text rather than proper visible labels."
- **Cognitive walkthrough:** Q1 Yes, I would enter my account details and try to sign in now. / Q2 Yes, the Email and Password fields and the Log in button are prominent. / Q3 Mostly. The placeholders “Email” and “Password” match what I want, but proper labels would be clearer and more reliable.
  - [ACC sev 2] **Login fields lack programmatic visible labels** - evidence: [5] textbox (no label) placeholder "Email" and [6] textbox (no label) placeholder "Password". Fix: Add persistent visible labels such as “Email address” and “Password”, associated with each textbox, while keeping placeholders only as supplementary hints.
- **Positives:** The main login form is centered and easy to find.; The Log in button is prominent and clearly matches the next action.; The page provides a clear route to Create an account for new users.

### My books dashboard  (step 3)
`http://127.0.0.1:8765/dashboard.html`

![screenshot](screenshots/step_03.jpg)
- **Purpose:** Shows the books in my account and provides a way to create another one.
- **What's happening:** The dashboard welcomes me, reports that I have no books, and displays a create button. However, it also shows a profile-sync error and a Log out link that appears to point back to the dashboard.
- **First impression (Test):** "The main task is obvious, but the ugly error code makes the page feel unreliable."
- **Cognitive walkthrough:** Q1 Yes, I would try creating a book because that is the next required step. / Q2 Yes, the orange “+ Create a new book” button is prominent and easy to notice. / Q3 Yes, “Create a new book” clearly matches what I want to do.
  - [H9 sev 3] **Technical sync error creates doubt about account data** - evidence: “Error 0x80070057: profile sync incomplete.”. Fix: Replace the code with a plain-language message such as “Some account details could not be loaded.” Explain what is affected and provide a Retry or Continue button if safe.
  - [H10 sev 2] **Sync problem has no recovery guidance** - evidence: “Error 0x80070057: profile sync incomplete.” There is no Retry, Help, or explanation beside the message.. Fix: Add a short explanation and clear actions such as “Try again” and “Continue without syncing,” or a Contact support link.
  - [H4 sev 2] **Log out link appears to point to the dashboard** - evidence: [5] link “Log out” -> /dashboard.html. Fix: Make the Log out link navigate to a genuine logged-out page or sign-in screen.
  - [ACC sev 2] **Footer links have very low contrast** - evidence: The footer text “Privacy,” “Terms,” “Contact,” and “© 2026 StoryHearth Ltd.” is extremely faint.. Fix: Use a darker text colour with sufficient WCAG contrast and provide visible keyboard focus states.
- **Positives:** The “Welcome back, Demo” heading confirms that the site recognised the account.; The dashboard clearly says there are no books yet.; The “+ Create a new book” button is prominent and clearly labelled.

### Create your book - characters  (step 4)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_04.jpg)
- **Purpose:** Collect the main child and another person for the personalised story.
- **What's happening:** The form is ready for the child’s first name, age, pronouns, optional appearance, another character, and relationship. The relationship menu is already set to Grandparent.
- **First impression (Test):** "The form looks clear and neatly arranged. I can understand the fields quickly, although the earlier family-sync error makes me slightly wary that my details may not be fully working."
- **Cognitive walkthrough:** Q1 Yes, this is exactly the setup I need before creating the story. / Q2 Yes, the labelled textboxes and dropdowns are easy to notice, and the orange Next button stands out. / Q3 Yes. “Child’s first name”, “Age”, “Pronouns”, and “Who else is in the story?” match what I want to enter.
  - [H1 sev 1] **No explanation of what happens next** - evidence: The screen ends with the button [12] “Next” and no visible hint that the next screen will ask for the memory itself.. Fix: Add a short line such as “Next, tell us the family memory you want to remember.”
- **Positives:** The form has a clear question: “Who’s the star of the story?”; The fields are grouped logically and the labels are visible.; The orange Next button is visually prominent.

### Story details form  (step 5)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_05.jpg)
- **Purpose:** Collect the setting, an important object, and the family memory to use when generating the personalised storybook.
- **What's happening:** The user is on the second stage of creating a book. Three empty fields are presented for the story location, a special object, and the memory or idea behind the story.
- **First impression (Test):** "The page is calm, neatly laid out, and straightforward. The examples in the boxes make it obvious what to enter."
- **Cognitive walkthrough:** Q1 Yes, I would fill in all three boxes because they match the memory I want in the book. / Q2 Yes, the three labelled text areas and the orange “Next” button are easy to notice. / Q3 Yes. “Where does the story happen?”, “A special object”, and “Tell us the memory or idea behind your story” clearly match what I want to provide.
  - [H2 sev 1] **Special object field is not marked optional** - evidence: “A special object” is presented as a field, while the preceding form used “(optional)” to identify optional information.. Fix: Label this field “A special object (optional)” if it is not required, and similarly clarify whether the location and memory fields are required.
- **Positives:** The field labels plainly describe the information needed.; Helpful placeholders use familiar family-memory examples.; The form is uncluttered and the primary “Next” action stands out.; A clearly visible “Back” control preserves my ability to change earlier details.

### Reading level and illustration style  (step 6)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_06.jpg)
- **Purpose:** Choose how difficult the story should be and what the illustrations should look like.
- **What's happening:** The form presents four Lexile reading-level ranges and three illustration styles. A middle reading range and the watercolour style are selected, and the user can continue with Next.
- **First impression (Test):** "It looks neat and easy, though “Lexile” is jargon I would not normally understand without more explanation."
- **Cognitive walkthrough:** Q1 Yes, I would accept the sensible middle reading range already selected for a five-year-old and continue. / Q2 Yes, the selected radio button and the Next button are both clearly visible. / Q3 Partly. The illustration labels clearly describe the style, but the Lexile labels do not plainly tell me which range is intended for a five-year-old.
  - [H2 sev 2] **Reading-level choices use unexplained jargon** - evidence: "Lexile BR–200L", "Lexile 200L–500L", "Lexile 500L–800L", and "Lexile 800L+". Fix: Show an age-friendly label beside each range, such as “Lexile 200L–500L — approximately ages 5–8”, and include a short explanation of Lexile.
- **Positives:** The page clearly shows which reading level and illustration style are selected.; The watercolour option is described in plain, appealing language.; Back and Next controls are visible and easy to identify.

### Optional photo upload  (step 7)
`http://127.0.0.1:8765/create.html`

![screenshot](screenshots/step_07.jpg)
- **Purpose:** Collect an optional child photo that may be used to personalise the illustrations, then let the user create the book.
- **What's happening:** The screen asks me to optionally upload a clear photo of the child's face. An empty file-upload control, a Back button, and a Create my book button are visible.
- **First impression (Test):** "This is straightforward and I understand that I can skip the photo. The page is clean, although I notice the upload control itself has no proper visible label."
- **Cognitive walkthrough:** Q1 Yes, I would continue by creating the book without adding a photo. / Q2 Yes, I notice the prominent “Create my book” button and understand that “Add a photo (optional)” can be skipped. / Q3 Yes. “Create my book” clearly matches my goal, and the photo heading clearly says it is optional.
  - [ACC sev 2] **File upload lacks a proper label** - evidence: [30] file-upload (no label); the control only displays “Choose file”. Fix: Give the file input a persistent visible label such as “Child’s photo” and associate the explanatory text with it through accessible markup.
  - [TRUST sev 2] **Privacy reassurance is missing beside a child-photo upload** - evidence: “Upload a clear photo of your child's face so the illustrations look like them.”. Fix: Add a short note linking to the Privacy Policy and explaining whether the uploaded photo is used only for generation, stored, or deleted.
- **Positives:** The heading clearly says “(optional),” so skipping the upload feels acceptable.; The primary action has a specific, understandable label: “Create my book.”; A Back control is available before committing to creation.; The page is uncluttered and the main action is visually prominent.

### Generated storybook preview  (step 8)
`http://127.0.0.1:8765/book.html`

![screenshot](screenshots/step_08.jpg)
- **Purpose:** Preview the newly generated family storybook page by page, then regenerate it or proceed to hardcover ordering.
- **What's happening:** The first of nine generated pages is displayed with previous and next controls. A cover titled “The Magical Adventrue of Sam” is labelled as Pop-art comic, while controls farther down offer a $4.99 regeneration and an “Order hardcover” link.
- **First impression (Test):** "It is easy to see that a book was created, but the misspelling “Adventrue” makes it feel careless. I also immediately noticed that the cover says “Pop-art comic” even though I selected “Watercolour,” which makes me question whether my choices were applied."
- **Cognitive walkthrough:** Q1 Yes, I would try reading through the whole book because I need to check whether the beach memory, yellow bucket, Sam, and Grandpa Joe were included and whether the reading level is suitable for a five-year-old. / Q2 Yes, the next-page control labelled “›” is obvious, and “1 / 9” makes it clear that there are eight more pages to inspect. / Q3 Partly. The arrow control works for turning pages, but the book metadata is unclear: “A StoryHearth original” does not explain that this is my generated story, and the style shown conflicts with my Watercolour choice.
  - [H2 sev 3] **Selected illustration style was not applied** - evidence: The page says “Illustration style: Pop-art comic,” even though Watercolour was the selected look on the previous screen.. Fix: Apply the chosen Watercolour style and show the selected style in the generation summary so a mismatch is obvious and can be corrected.
  - [CONTENT sev 3] **The generated title is misspelled** - evidence: “The Magical Adventrue of Sam”. Fix: Add a title spell-check and let me edit the title before ordering.
  - [CONTENT sev 2] **The final page does not fit the family memory well** - evidence: “And from that day on, whenever Sam looked up at the sky, she would always remember”. Fix: Generate an ending that refers clearly to the beach, sandcastles, Grandpa Joe, and the yellow bucket.
  - [H1 sev 1] **The preview does not visibly confirm personalisation** - evidence: The visible cover only shows the title and “Sam”; Grandpa Joe, the beach, the sandcastles, and the yellow bucket are not mentioned on this page.. Fix: After generation, show a short confirmation such as “Created using Sam, Grandpa Joe, the beach, the yellow bucket, and your memory,” or include this in an accessible summary.
  - [VALUE sev 1] **Generated preview regeneration has an immediate charge** - evidence: [8] “Regenerate entire book – $4.99”. Fix: Explain the regeneration price in a confirmation dialog and state that it replaces the whole book, without pre-selecting or enabling payment automatically.
  - [H8 sev 1] **“The End” is repeated twice on the last page** - evidence: The image says “The End,” and the sentence below also ends with “The End”. Fix: Show the final wording only once, or use separate roles for the image text and printed page text.
- **Positives:** The successful generation is shown clearly through a nine-page preview.; Page position is shown as “1 / 9,” so I know there are more pages.; The next-page arrow is prominent and easy to find.; There is a clear path to “Order hardcover” for checking the final price later.

### Hardcover checkout  (step 10)
`http://127.0.0.1:8765/checkout.html`

![screenshot](screenshots/step_10.jpg)
- **Purpose:** Shows the cost of ordering the generated hardcover and collects delivery and payment information.
- **What's happening:** The checkout displays the hardcover for “The Magical Adventrue of Sam,” with a countdown, item prices, shipping, total, and empty address and payment fields. Premium gift wrap is pre-selected.
- **First impression (Test):** "The prices are visible, but I am annoyed that premium gift wrap is already selected. The checkout makes the order feel much more expensive than the £24.99 book price alone."
- **Cognitive walkthrough:** Q1 Yes, I would try to inspect the full cost, but I would not proceed with payment. / Q2 Yes, I noticed the “Premium gift wrap” checkbox and the itemised prices. / Q3 The labels clearly identify the hardcover, gift wrap, shipping, total, address, and payment fields, so they mostly match what I want to check.
  - [DECEPTIVE sev 3] **Premium gift wrap is pre-selected** - evidence: [6] checkbox "Premium gift wrap" (checked), with £7.99 shown beside it. Fix: Leave optional extras unchecked by default and show the additional cost immediately beside the checkbox.
  - [VALUE sev 2] **Checkout is not showing what the basic delivered hardcover costs before extras** - evidence: The page shows “Hardcover: The Magical Adventrue of Sam £24.99,” “Shipping & handling £12.99,” and a separate checked “Premium gift wrap £7.99.”. Fix: Show a clear subtotal for the book and delivery, and update the total immediately when the gift-wrap checkbox changes.
  - [H8 sev 1] **Important pay action is below the fold** - evidence: [11] button "Pay now" (offscreen). Fix: Keep the total and the pay button visible together, or use a sticky checkout summary.
- **Positives:** The checkout clearly itemises the book, gift wrap, shipping, and total.; The order name and price are visible immediately.; The empty payment fields give me a clear place to stop without entering any financial information.
- **Would abandon here:** I would not continue to payment because the pre-selected £7.99 gift wrap makes the checkout feel misleading, and the task only requires finding the price.

## Generated output assessment
*Artifact:* Nine-page personalized children's storybook preview

> This does not feel like my family's memory: Grandpa Joe and the sandcastles are missing, while an invented uncle and threatening woods take over. The visible placeholders, “Adventrue,” “Samn,” repeated text, and unfinished final sentence make the preview look broken. I would not want to give this to Sam or pay for it in its current form.

| Criterion | Score (1-5) | Evidence |
|---|---|---|
| fidelity | 1 | The output correctly uses Sam, age 5, she/her, the beach, and mentions a yellow bucket. However, Grandpa Joe never appears, sandcastle building is never described, the yellow bucket is not shown, the special shared memor |
| coherence | 2 | There is a nominal opening, middle, and ending, but the plot jumps from a beach to evening introspection, rain, Bartholomew, threatening woods, and then back to the beach. The exact opening sentence is repeated, Sam's ag |
| age fit | 1 | The prose includes “ephemeral luminescence,” “crepuscular firmament,” “ineffable wonder,” and “existential trepidation,” and later describes shadows growing teeth and suggesting Sam may never be found. The measured FK gr |
| language | 1 | There is the title typo “Adventrue,” the name typo “Samn,” the grammatical phrase “in the beach,” unresolved placeholders, awkward pronoun logic, a repeated opening, a duplicated “The End,” and a sentence ending abruptly |
| text image fit | 2 | Some broad settings match, such as the evening sky and nighttime woods, but the rain page has a bright sun, the bucket and Grandpa Joe are missing, Bartholomew's winding path is absent, the threatening shadows are not sh |
| character consistency | 3 | Sam is represented as a small child throughout, but her hair and clothing drift: the cover and most pages show a brown-haired child in dark green, page 6 shows a bald child in teal beside Bartholomew, and page 7 returns  |
| visual quality | 2 | The illustrations are extremely sparse, use repeated geometric template scenes, and do not match the selected Watercolour style. The output labels itself “Pop-art comic,” while the cover and several interior pages are al |
| emotional resonance | 1 | The central memory is Grandpa Joe and Sam building a special sandcastle together, yet Grandpa Joe is absent and the replacement story features existential melancholy, dangerous woods, and threatening shadows. The unresol |

- **used correctly:** Sam's first name; Sam's age of 5; Sam's she/her pronouns; The beach setting in the opening text; A yellow bucket mentioned in the text
- **missing:** Grandpa Joe; Building sandcastles together; The special sandcastle as a shared memory; Sam's favourite yellow bucket as the central keepsake detail; Any meaningful evidence of the premium gift wrap; A Watercolour-style presentation matching the selected option
- **changed:** The warm shared beach memory became an unrelated fantasy and mild peril story; The setting shifted repeatedly among the beach, evening sky, rain, and woods; The special yellow bucket became an incidental prop; The intended personal ending became an incomplete thought about looking at the sky
- **invented:** Uncle Bartholomew; A lantern; A winding path; Deep woods; Shadows that grow teeth and whisper; A shiny red balloon; An unexplained evening melancholy; A storm and hood

### Part by part
#### Cover
![I1](artifacts/capture_01/img_00.jpg)
> A StoryHearth original Illustration style: Pop-art comic
- *Picture:* A very simple flat-colour illustration of a small, brown-haired child labelled Sam, standing between blue water, green land, a yellow star, and a large sun. It does not look like watercolour artwork.
- *Reaction:* The cover immediately feels unfinished because the title says “Adventrue,” and the image is basic rather than the Watercolour style I selected. It also does not establish the beach, Grandpa Joe, the sandcastles, or the yellow bucket.
  - [language, sev 3] The title visibly reads “The Magical Adventrue of Sam”; “Adventrue” is misspelled.
  - [visual_quality, sev 3] The selected style was Watercolour, but the cover says “Illustration style: Pop-art comic” and uses plain geometric shapes.
  - [fidelity, sev 2] The cover shows neither Grandpa Joe nor a sandcastle or yellow bucket.
  - [text_image_fit, sev 2] The cover title calls the story “The Magical Adventrue of Sam,” while the image is a static child beside generic water and land with no visible magic or beach activity.
- **Change I'd make:** Regenerate the cover in the selected Watercolour style with a corrected, personal title such as “Sam and Grandpa Joe's Sandcastle Day,” showing them building a sandcastle with the yellow bucket at the beach.
- **Suggested rewrite:** Sam and Grandpa Joe's Sandcastle Day A StoryHearth story

#### Dedication page
![I2](artifacts/capture_03/view_00.jpg)
> For {{recipient_name}}, with love from {{sender_name}}
- *Picture:* No illustration is visible. The white book page contains the unresolved dedication in the middle of the website preview.
- *Reaction:* Leaving raw template placeholders on a finished gift is a clear production failure. This page looks broken rather than personal.
  - [language, sev 4] The page displays the unrendered placeholders “{{recipient_name}}” and “{{sender_name}}.”
  - [visual_quality, sev 3] The page is empty apart from placeholder text and appears as an unformatted white rectangle.
  - [emotional_resonance, sev 3] A raw template message does not function as a personal dedication.
- **Change I'd make:** Either ask for the recipient and sender before generating the book or replace the unresolved line with a valid dedication using the available information.
- **Suggested rewrite:** For Sam, with love

#### Page 1
![I3](artifacts/capture_04/img_00.jpg)
> Once upon a time, in the beach, there lived a curious child named Sam. Sam was 5 years old and loved nothing more than a yellow bucket.
- *Picture:* Sam is shown standing front-facing in a generic landscape with blue water, green land, a sun, and a yellow star. There is no visible sandcastle, Grandpa Joe, or yellow bucket.
- *Reaction:* This at least names Sam, gives her age, uses the beach, and mentions the yellow bucket. However, “in the beach” is awkward, and the illustration omits almost every specific detail named in the sentence.
  - [language, sev 2] “Once upon a time, in the beach, there lived” is grammatically incorrect; the natural wording is “at the beach.”
  - [text_image_fit, sev 2] The text and alt description mention Sam at the beach, but the picture shows a generic shore-like scene and no bucket.
  - [visual_quality, sev 2] The picture is a sparse template-like arrangement rather than a Watercolour beach scene.
- **Change I'd make:** Replace the generic introduction with a concrete memory involving Sam and Grandpa Joe, and illustrate the yellow bucket and sandcastle clearly.
- **Suggested rewrite:** Sam was five years old, and she loved the beach. One sunny day, she went there with Grandpa Joe to build a special sandcastle with her favourite yellow bucket.

#### Page 2
![I4](artifacts/capture_05/img_00.jpg)
> One evening Sam gazed upward. The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.
- *Picture:* Sam stands under a purple evening sky with scattered white stars, but there is no Grandpa Joe, bucket, sandcastle, or beach activity.
- *Reaction:* The evening-sky picture is broadly connected to the text, but the sentence is far too advanced for a five-year-old. Words such as “ephemeral” and “existential trepidation” make the story feel clinical and depressing.
  - [age_fit, sev 4] “The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy, juxtaposing ineffable wonder with existential trepidation.”
  - [emotional_resonance, sev 3] The unexplained melancholy and existential language are not warm or child-friendly.
  - [fidelity, sev 3] The requested shared sandcastle memory is replaced by an evening sky observation, with no Grandpa Joe.
  - [text_image_fit, sev 1] The starry evening sky supports the idea of gazing upward, but the character is standing in the same generic setting rather than on a beach.
- **Change I'd make:** Replace this page with simple dialogue between Sam and Grandpa Joe while they build the sandcastle.
- **Suggested rewrite:** Sam dug a deep hole in the warm, wet sand. Grandpa Joe helped her fill her favourite yellow bucket, and they laughed when the sand spilled over the edge.

#### Page 3
![I5](artifacts/capture_06/img_00.jpg)
> Then the rain began to pour. Big grey drops splashed into the puddles as Samn pulled up her hood and ran for shelter, holding a yellow bucket tight.
- *Picture:* The picture is almost identical to the cover: Sam stands under a bright sun with a yellow star, blue water, and green ground. There is no rain, puddles, hood, path, shelter, or visible yellow bucket.
- *Reaction:* This is a direct picture-text contradiction: the story says pouring rain, while the illustration has a bright sun. “Samn” is another obvious error, and the invented storm distracts from the family memory.
  - [language, sev 3] Sam's name is misspelled as “Samn” in “as Samn pulled up her hood.”
  - [text_image_fit, sev 4] The text says “the rain began to pour,” but the image shows a bright sun and no rain, puddles, hood, shelter, or yellow bucket.
  - [fidelity, sev 3] The requested sandcastle-building memory is replaced by an unrequested rainstorm.
  - [character_consistency, sev 2] Sam's clothing and scene are simply copied from the cover rather than updated to show her running in rain.
- **Change I'd make:** Remove the invented storm, correct Sam's name, and show a continuous beach scene of her and Grandpa Joe packing sand into the yellow bucket.
- **Suggested rewrite:** Sam filled her yellow bucket with wet sand and scooped it out beside Grandpa Joe. Together, they shaped the sand into tall towers and wide walls.

#### Page 4
![I6](artifacts/capture_07/img_00.jpg)
> Uncle Bartholomew Suddenly, Uncle Bartholomew appeared with a lantern. "Sam, follow me!" he called, and he followed him along the winding path.
- *Picture:* Two simplified figures labelled “Uncle Bartholomew” and “Sam” stand on green land beside blue water. Bartholomew is much taller and has a small yellow rectangle that may represent a lantern; no winding path is shown.
- *Reaction:* Grandpa Joe has inexplicably been replaced by Uncle Bartholomew, which is a major betrayal of the family detail. The pronouns also become nonsensical: after Bartholomew tells Sam to follow, the sentence says “he followed him.”
  - [fidelity, sev 4] The requested relationship was “Grandpa Joe,” but the page twice substitutes “Uncle Bartholomew.”
  - [language, sev 3] After “Sam, follow me!” the text says “and he followed him,” which is grammatically possible in isolation but ambiguous and contextually wrong because it appears to make Sam the follower without identifying who followed whom.
  - [character_consistency, sev 3] Sam's head and outfit change from the brown-haired, dark-green-shirt figure on the cover to a bald, teal-shirt figure beside Bartholomew.
  - [text_image_fit, sev 2] The two figures support the introduction of Bartholomew, but there is no visible winding path, and the yellow rectangle is not clearly a lantern.
- **Change I'd make:** Delete Uncle Bartholomew and replace the entire episode with Grandpa Joe helping Sam make the special sandcastle.
- **Suggested rewrite:** Grandpa Joe carefully shaped the top of the castle. “What shall we call it?” he asked. Sam smiled and said, “The Sunny Tower!”

#### Page 5
![I7](artifacts/capture_08/img_00.jpg)
> Deep in the woods, the shadows grew teeth and whispered that no one would ever find Sam again. Sam clutched a shiny red balloon and trembled in the dark.
- *Picture:* Sam stands at night near three simple trees, a crescent moon, stars, and a red balloon. The image does not show threatening shadows, teeth, whispering, or Grandpa Joe.
- *Reaction:* This feels suddenly dark and threatening rather than like a treasured beach memory. The sentence about shadows growing teeth and no one finding Sam is likely to unsettle a five-year-old, and Grandpa Joe is still absent.
  - [age_fit, sev 3] “The shadows grew teeth and whispered that no one would ever find Sam again” introduces fear and a serious threat without reassuring resolution.
  - [fidelity, sev 4] The beach, sandcastles, Grandpa Joe, and shared memory are all displaced by an invented nighttime journey in the woods.
  - [emotional_resonance, sev 3] Sam is trembling, the shadows have teeth, and the text suggests she may never be found; this is not warm or reassuring.
  - [text_image_fit, sev 2] The picture includes a night setting, trees, and a red balloon, but not the anthropomorphic shadows or their teeth described in the text.
  - [text_image_fit, sev 2] No yellow bucket is visible despite its central importance in the requested memory.
- **Change I'd make:** Remove the threatening woods and use a warm scene of Sam and Grandpa Joe admiring or finishing their sandcastle.
- **Suggested rewrite:** They added a tiny castle on top and decorated the wide walls with smooth shells. Grandpa Joe said it was the finest sandcastle he had ever seen.

#### Page 6
![I8](artifacts/capture_09/img_00.jpg)
> Once upon a time, in the beach, there lived a curious child named Sam. At last the sun came out, and Sam skipped all the way home, happier than ever.
- *Picture:* Sam stands still in another bright generic beach-like scene with blue water, green land, a sun, and a yellow star. She is not visibly skipping, going home, or accompanied by Grandpa Joe.
- *Reaction:* The exact opening sentence is repeated just as the story supposedly ends, and it contains the same “in the beach” error. The cheerful conclusion is undermined by the fact that Sam is alone and the special sandcastle has disappeared.
  - [language, sev 3] “Once upon a time, in the beach, there lived a curious child named Sam” repeats the opening almost verbatim and retains the grammatical error “in the beach.”
  - [coherence, sev 3] The page abruptly restarts with the opening sentence instead of resolving the nighttime danger or the beach episode.
  - [fidelity, sev 3] The sentence says Sam goes home “happier than ever,” but there is no shared activity with Grandpa Joe, no sandcastle, and no yellow bucket.
  - [text_image_fit, sev 3] The text says Sam “skipped all the way home,” while the picture shows her standing still in the same generic landscape with no home or destination.
- **Change I'd make:** Replace the repeated opening with a clear conclusion to the sandcastle day and show Sam leaving the beach with Grandpa Joe.
- **Suggested rewrite:** When it was time to go home, Sam gave Grandpa Joe one last look at their sandcastle. He waved, and Sam waved back, already planning their next beach day.

#### Page 7 / End page
![I9](artifacts/capture_10/img_00.jpg)
> The End And from that day on, whenever Sam looked up at the sky, she would always remember The End
- *Picture:* An orange background displays “The End” above the same small front-facing Sam figure standing on the generic green-and-blue landscape.
- *Reaction:* The final thought is unfinished, “The End” appears twice, and it remembers looking at the sky rather than the sandcastles she made with Grandpa Joe. This loses the personal detail that should make the book worth keeping.
  - [language, sev 4] The sentence ends at “she would always remember” without a final punctuation mark or completing thought.
  - [language, sev 3] “The End” is printed twice on the same page.
  - [fidelity, sev 4] The intended memory was building sandcastles with Grandpa Joe using Sam's favourite yellow bucket, but the closing memory is only looking up at the sky.
  - [text_image_fit, sev 3] The text says Sam looks up at the sky, while the picture shows her facing forward against an orange background with no visible sky or remembered beach scene.
  - [visual_quality, sev 2] The end page repeats a generic character template rather than providing a meaningful final family illustration.
- **Change I'd make:** Remove the duplicate ending, complete the sentence, and close on the actual memory of Sam and Grandpa Joe's special sandcastle and yellow bucket.
- **Suggested rewrite:** The End From then on, whenever Sam saw her yellow bucket, she remembered the special sandcastle she had built with Grandpa Joe at the beach.

**Top changes to the output:** 1. Rebuild the entire story around Sam and Grandpa Joe making a special sandcastle with her favourite yellow bucket at the beach. | 2. Remove every unresolved placeholder, fix “Adventrue” and “Samn,” correct “in the beach,” eliminate repeated text, and complete the final sentence. | 3. Regenerate all illustrations in the selected Watercolour style and make each one specifically match its page, including Grandpa Joe, the yellow bucket, the sandcastles, and Sam's consistent brown-haired appearance. | 4. Replace the frightening existential language and shadowy peril with warm, concrete, age-five-appropriate language and shared family moments. | 5. Show the premium gift-wrap choice accurately or explain that it is not represented in the digital preview.

## Recommendations (participant's priorities)
- **[high] Make the generated story faithfully centre on the submitted family memory, including Grandpa Joe, the sandcastles, the yellow bucket, and the supplied relationships, without replacing them with invented characters or events.** (Generated storybook preview) - Personalisation is the entire purpose of the product, and this was the main reason I did not consider the book worth keeping.
- **[high] Apply the selected Watercolour style consistently and generate images that actually match each page's events and characters.** (Generated storybook preview) - I explicitly selected Watercolour but received a Pop-art comic, making the book look wrong and unreliable.
- **[high] Remove unresolved placeholders, fix “Adventrue” and “Samn,” correct grammar, eliminate repeated text, and complete the final sentence before showing the preview.** (Generated storybook preview) - These visible mistakes make the story look broken and make it unsuitable as a keepsake.
- **[high] Rewrite the story with warm, concrete, age-five-appropriate vocabulary and remove threatening shadows, existential distress, and confusing pronoun errors.** (Generated storybook preview) - The prose was too advanced and frightening for a five-year-old and weakened the emotional purpose of the story.
- **[high] Ensure Sam has a consistent brown-haired appearance and that Grandpa Joe, the bucket, and the sandcastles are visibly represented in the relevant illustrations.** (Generated storybook preview) - A personalised book should be recognisably about the child and the actual family memory on every relevant page.
- **[high] Do not preselect premium gift wrap, and show the basic delivered hardcover price and total before any extras are added.** (Hardcover checkout) - I had to investigate checkout to discover the real price, and a default extra feels misleading rather than helpful.
- **[high] Replace the technical sync error with a plain-language explanation and provide a clear recovery action or support route.** (My books dashboard) - The error made me worry that my family details had not loaded, but it gave me no way to fix or understand the problem.
- **[medium] Add a proper label and clear privacy reassurance beside the optional child-photo upload.** (Optional photo upload) - A parent should understand what the upload is for and how the child's image will be handled before uploading it.
- **[medium] Replace technical homepage and reading-level jargon with ordinary language, and provide meaningful alternative text or an accessible description for the main image.** (StoryHearth homepage and reading-level options) - The wording sounds aimed at specialists rather than families and makes the product harder to understand.
- **[medium] Use proper accessible labels for login and upload controls, improve footer contrast, and fix the logout link if it incorrectly returns to the dashboard.** (Log in, optional photo upload, and My books dashboard) - These details affect usability, accessibility, and confidence in basic account functions.
- **[low] Clearly explain which fields are optional and what happens after each form step.** (Create your book) - I had to infer that the special object field was optional and that the memory would be asked for on the next screen.

## Interview
- **In one or two sentences, what is this website for, and who is it for?** This is meant to turn a child's name, characteristics, and a family memory into a personalised storybook, apparently with an optional printed hardcover. It is aimed at parents or relatives wanting a keepsake featuring a child.
- **What was the most frustrating or confusing moment, and why?** The worst moment was opening the completed book: “Adventrue” was misspelled, the illustrations were labelled Pop-art after I selected Watercolour, and the story about Grandpa Joe and the sandcastles had been replaced with invented characters, threatening woods, and existential language.
- **What was the best moment?** The best part was entering the family memory about building sandcastles with Grandpa Joe using the yellow bucket, because the setup questions were clear and made me hopeful about the final result.
- **Was there any point where, in real life, you would have given up? Where and why?** I nearly gave up when the generated preview appeared obviously broken, and I definitely would not have continued to payment. I did look at checkout only to find out the real delivered cost.
- **What did you expect to find or be able to do that wasn't there?** I expected the finished story to centre on Sam and Grandpa Joe building sandcastles at the beach, with consistent characters, the yellow bucket, and Watercolour illustrations. I also expected a clear explanation of the sync error, proper labels and privacy information around child-photo upload, and the basic delivered hardcover price before checkout extras.
- **Did you trust this website with your information (and your family's)? Why or why not?** I was cautious about uploading a child's photo because there was no nearby privacy reassurance or clear upload label. I also trusted the generated result less because it ignored important family details, changed the requested visual style, and contained obvious errors.
- **Would you pay for this? How much would feel fair, and what would make you pay more?** I would not pay for this output. After correcting the story, illustrations, and text, roughly £25-£30 would feel fair for a digital keepsake, or around £35 for a decent printed hardcover; I might pay more for a polished, faithful book with a genuinely personalised narrative and reliable quality checks.
- **If the site produced something for you, how do you feel about it overall?** I do not feel that this reflects my family's memory. Grandpa Joe and the sandcastles were missing, the selected style was wrong, the story contained frightening and age-inappropriate material, and the visible typos, placeholders, repetition, and incomplete ending made it look unfinished. I would not give it to Sam or keep it as a family keepsake.

## Session log
| Step | Screen | Emotion | Think-aloud | Actions |
|---|---|---|---|---|
| 1 | StoryHearth – Personalised storybooks st | curious (1) | This looks relevant to me. The wording “multimodal generative narrative engine” and “lived-experience corpus” sounds far too technical for a normal family, but the three-step explanation underneath is clear enough. I cam | click |
| 2 | Log in – StoryHearth | reassured (1) | This looks straightforward. I can see the Email and Password boxes, so I will use my account details and click Log in. The lack of visible field labels is a small accessibility concern, but the placeholders make the purp | type; type; click |
| 3 | My books – StoryHearth | confused (-1) | I can see where I need to go, but that error message is alarming and technical. I’m not sure whether it means my family details have not loaded properly, although I can still try creating a book. | click |
| 4 | Create your book – StoryHearth | neutral (1) | This is straightforward enough. I will enter Sam, choose age 5 and she/her, add brown hair, and include Grandpa Joe. The form does not yet ask what the family memory is, so I expect that on the next screen. | type; select; select; type; type; click |
| 5 | Create your book – StoryHearth | reassured (2) | This is clear and easy to follow. I’ll say it was at the beach, include the yellow bucket, and describe building sandcastles with Grandpa Joe so the story is about our family memory. | type; type; type; click |
| 6 | Create your book – StoryHearth | reassured (1) | The reading level choices sound technical, but I can see that the middle range is already selected and that should suit Sam at age five. I’ll keep the soft watercolour look and click Next. | click |
| 7 | Create your book – StoryHearth | reassured (1) | This is a clear final step. I do not have a photo available here, so I will leave it empty and click “Create my book” because the wording clearly says the upload is optional. | click; wait_for_change |
| 8 | Your storybook – StoryHearth | frustrated (-1) | The book appeared, so the last action did work, but I’m disappointed by two obvious mistakes: “Adventrue” is misspelled, and this is a Pop-art comic when I chose Watercolour. I need to read all nine pages carefully befor | flip_through |
| 9 | Your storybook – StoryHearth | frustrated (-1) | I’ve finished the whole preview, but the ending feels weak: Sam is “looking up at the sky” even though our memory was about sandcastles at the beach. Now I’ll check the real hardcover cost, but I will not pay or enter an | click |
| 10 | Checkout – StoryHearth | annoyed (-1) |  | click; read_page |
| 11 | Checkout – StoryHearth | reassured (1) | That confirms removing the gift wrap worked and brought the real total down to £37.98. I have found out what the hardcover costs, including delivery, and I will not enter any payment details or pay. | done |
